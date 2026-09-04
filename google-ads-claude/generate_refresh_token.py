#!/usr/bin/env python3
"""
Generate a Google Ads API OAuth2 refresh token from a "Desktop app"
client secret JSON file (downloaded from Google Cloud Console).

Usage:
    python generate_refresh_token.py /path/to/client_secret.json

Opens a browser for the Google consent screen, then prints the
refresh token to use in google-ads.yaml or your app's config.
"""
import sys

from google_auth_oauthlib.flow import InstalledAppFlow

# Required scope for the Google Ads API
SCOPES = ["https://www.googleapis.com/auth/adwords"]


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} /path/to/client_secret.json")
        sys.exit(1)

    client_secrets_path = sys.argv[1]

    flow = InstalledAppFlow.from_client_secrets_file(client_secrets_path, scopes=SCOPES)
    # Runs a local loopback server and opens your default browser.
    # access_type=offline + prompt=consent ensures a refresh_token is returned.
    credentials = flow.run_local_server(
        access_type="offline",
        prompt="consent",
    )

    print("\nAccess token:\n", credentials.token)
    print("\nRefresh token:\n", credentials.refresh_token)
    print(
        "\nSave the refresh token above — put it in your google-ads.yaml as "
        "`refresh_token:` (or your app's secret store). Do not commit it to git."
    )


if __name__ == "__main__":
    main()
