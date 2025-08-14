import os
import shutil
import re
import argparse
from zenpy import Zenpy
from zenpy.lib.exception import APIException

pattern = re.compile(r'^\d{5}$')

def is_case_solved(case_id, zenpy_client, debug=False):
    """Check if a Zendesk case is marked as 'Solved' or 'Closed'."""
    if debug:
        print(f"[Debug] is_case_solved: Case {case_id} ", end="")
    try:
        ticket = zenpy_client.tickets(id=case_id)
        if debug:
            print(f"is " + ticket.status.lower())
        return ticket.status.lower() in ['solved', 'closed']
    except APIException as e:
        print(f"Error fetching case {case_id}: {e}")
        return False

def delete_solved_case_dirs(downloads_dir, zenpy_client, debug=False, dry_run=False):
    """Iterate through subdirectories and delete (or list) those with 'Solved' status cases."""
    for subdir in os.listdir(downloads_dir):
        subdir_path = os.path.join(downloads_dir, subdir)
        if os.path.isdir(subdir_path) and pattern.match(subdir):
            if debug:
                print(f"[Debug] Evaluating directory: {subdir}")
            case_id = int(subdir)
            if is_case_solved(case_id, zenpy_client, debug):
                if dry_run:
                    print(f"[Dry Run] Would delete directory for solved case: {case_id}")
                else:
                    try:
                        shutil.rmtree(subdir_path)
                        print(f"Deleted directory for solved case: {case_id}")
                    except Exception as e:
                        print(f"Failed to delete {subdir_path}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Delete Zendesk case folders marked as 'Solved'")
    parser.add_argument('--debug', action='store_true', help='Enable debug output')
    parser.add_argument('--dry-run', action='store_true', help='List actions without performing them')
    parser.add_argument('--dir', type=str, default=os.path.expanduser('/home/yourusername/cases'),
                        help='Directory to scan for case folders')
    parser.add_argument('--subdomain', type=str, default='knime', help='Zendesk subdomain')
    parser.add_argument('--email', type=str, default='your.name@knime.com', help='Zendesk email')
    parser.add_argument('--token', type=str, default='xxxyourtokenxxx', help='Zendesk API token')

    args = parser.parse_args()

    creds = {
        'subdomain': args.subdomain,
        'email': args.email,
        'token': args.token
    }
    zenpy_client = Zenpy(**creds)

    delete_solved_case_dirs(args.dir, zenpy_client, debug=args.debug, dry_run=args.dry_run)
