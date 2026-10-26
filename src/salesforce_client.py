"""Salesforce Client Helper Module.

Provides authenticated Salesforce connection handling using python-dotenv
and simple-salesforce.
"""

import os
from typing import Optional
from dotenv import load_dotenv
from simple_salesforce import Salesforce

# Load .env file automatically
load_dotenv()


def get_salesforce_connection() -> Salesforce:
    """Connect to Salesforce using credentials configured in environment variables.

    Supports Username/Password/Token auth and custom domain.
    """
    username = os.getenv("SALESFORCE_USERNAME")
    password = os.getenv("SALESFORCE_PASSWORD")
    security_token = os.getenv("SALESFORCE_SECURITY_TOKEN")
    domain = os.getenv("SALESFORCE_DOMAIN", "login")
    api_version = os.getenv("SALESFORCE_API_VERSION", "60.0")

    if not username or not password:
        raise ValueError(
            "Missing Salesforce credentials! "
            "Please copy '.env.example' to '.env' and set SALESFORCE_USERNAME and SALESFORCE_PASSWORD."
        )

    # Initialize connection
    sf = Salesforce(
        username=username,
        password=password,
        security_token=security_token or "",
        domain=domain,
        version=api_version,
    )
    return sf


if __name__ == "__main__":
    print("Connecting to Salesforce...")
    try:
        sf = get_salesforce_connection()
        print(f"Successfully authenticated! Connected to Salesforce instance: {sf.sf_instance}")

        # Example query: retrieve current org details or sample accounts
        results = sf.query("SELECT Id, Name FROM Organization")
        org_name = results["records"][0]["Name"]
        print(f"Connected Organization Name: {org_name}")
    except Exception as e:
        print(f"Connection failed: {e}")
