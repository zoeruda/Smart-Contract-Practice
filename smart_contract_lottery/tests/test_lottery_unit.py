## Unit Tests:
# Testing the smallest piece of code in an isolated instance, typically done in a development network

from brownie import Lottery, accounts, config, network
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.deploy_lottery import deploy_lottery
from web3 import Web3
import pytest


def test_get_entrance_fee():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    # Arrange
    lottery = deploy_lottery()
    # Act
    # 2,000 eth / usd
    # usdEntryFee is 50
    # 2000/1 == 50/x == 0.025
    expected_entrance_fee = Web3.toWei(0.025, "ether")
    entrance_fee = lottery.getEntranceFee()
    # Assert
    assert expected_entrance_fee == entrance_fee
