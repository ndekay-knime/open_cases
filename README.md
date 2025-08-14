# open_cases
Python script to remove unneeded case subdirectories

1. You will need a valid Zendesk account and Oauth/API token to use this script.

Note, Per Zendesk:
OAuth is a way of authenticating API requests, which involves an OAuth access token (a key) being created. Traditionally, Zendesk OAuth access tokens have not expired, nor had a mechanism to refresh. However, as part of our ongoing commitment to enhancing security and aligning with industry standards, there are now configurable options you can use to establish automated expiration and refreshes of OAuth tokens used in your application(s).

While this is currently an optional enhancement, on April 30, 2026, we’ll begin enforcing expiration for OAuth access tokens. This will enhance the security of your integrations by minimizing the risks associated with long-lived tokens, as well as allow your application(s) to refresh access tokens seamlessly without requiring your users to frequently reauthorize.

See [1] for more information on updating your token.

2. This script assumes that the subdirectories it is to check are a) subdirectories of the --dir parameter; b) five-digit numeric casenumbers. (See `pattern` regex in script code.)

In summary, as long as you properly configure `--dir`, `--email`, and `--token` (or provide them on the command line), you should be good to go.

[1] https://developer.zendesk.com/api-reference/ticketing/oauth/grant_type_tokens/?utm_source=marketo&utm_medium=transactional_email&utm_campaign=PROD_Expiration_tokens_WW_2025&mkt_tok=ODE5LVJSUS0wNjAAAAGa8_b9ch7Dm0-tPIWR1KPD7guiI7_tNS99STB5pJKjgmAN7mggPmFnsmXZ3HF2gwfK3wj1-nwO6sIS5Lk4DJ3EOT3J-O7J6-brUH5HGDDUSg
