from brownie import FundMe
from scripts.helpful_scripts import get_account, deploy_mocks


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEnteranceFee()
    print(f"the current entry fee is {entrance_fee}")
    print("Funding")
    amount = entrance_fee * 10 ** 10
    fund_me.fund({"from": account, "value": amount})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
