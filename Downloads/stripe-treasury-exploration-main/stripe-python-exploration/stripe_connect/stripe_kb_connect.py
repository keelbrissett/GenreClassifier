# Testing the creation of a connected account using the API
# Building on stripe_demo.py by Tanatswa Manyakara
# Desc:INSERT FUNCTIONALITY HERE
# Author(s): 

import os
import stripe
stripe.api_key = os.environ.get("STRIPE_API_KEY_WITH_WRITE_PERMISSIONS")

def create_custom_account():
    """ Create a new custom connected account.

    Returns:
        Account: a new custom account
    """
    return stripe.Account.create(
        country="US",
        type="custom",
        capabilities={"card_payments": {"requested": True},
                      "transfers": {"requested": True}},
    )


def get_all_connected_accounts():
    """ Gets the list of all connected accounts
    Returns:
        list: a list of all the connected accounts
    """
    custom_accounts = stripe.Account.list(limit=100)
    return custom_accounts


def get_connected_account(account_id):
    """ Gets an account by its id

    Returns:
        Account: a custom connected account
    """
    return stripe.Account.retrieve(account_id)


def update_connected_account(account_id):
    """ Gets an account by its id, and updates the specified information
    Returns:
        Account: an updated connected account
    """
    stripe.Account.modify(
        "acct_1FWOJSJAcKD3e91Z",
        metadata={"order_id": "6735"},
    )
    return stripe.Account.retrieve(account_id) 


def delete_connected_account(account_id):
    """ Deletes an account by its id
    Returns:
        void
    """
    stripe.Account.delete("acct_1FWOJSJAcKD3e91Z")


if __name__ == "__main__":
    # accounts = get_all_connected_accounts()
    # for account in accounts:
    #     print(account.id + "\n")
    #     print(account.type)
    print(get_connected_account("acct_1NGfEEQtR95WdtNQ"))

