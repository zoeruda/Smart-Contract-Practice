from brownie import network, config, accounts, SimpleStorage


def deploy_simple_storage():
    account = get_account()
    ## Spin a test account using ganache-cli:
    # account = accounts[0]
    # print(account)
    ## Load account already added to brownie:
    # account = accounts.load("sample-account")
    # print(account)
    ## Add account from env variable
    # account = accounts.add(config["wallets"]["from_key"])
    # print(account)
    simple_storage = SimpleStorage.deploy({"from": account})  # Transact
    print(simple_storage)  # Call
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
