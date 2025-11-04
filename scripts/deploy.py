import os
from brownie import accounts, USDC, MAVUSD, Defibank
from dotenv import load_dotenv
load_dotenv()

def main():
    account = accounts.add(os.getenv("PRIVATE_KEY"))
    usdc_addr = USDC.deploy({"from": account})
    mavusd_addr = MAVUSD.deploy({"from": account})
    Defibank.deploy(usdc_addr, mavusd_addr, {"from": account})