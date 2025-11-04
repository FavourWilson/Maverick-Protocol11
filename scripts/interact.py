import os
from brownie import Contract, accounts
from dotenv  import load_dotenv
load_dotenv()

def main ():
    account = accounts.add(os.getenv("PRIVATE_KEY"))
    


    usdc_contract = Contract('0x64BEcE3F88dE30D38d9B1C395Df6Ed3A9C9931b7')
    defi_contract = Contract ('0xe3f96ABB6760bAbD410A590CcbEdA89f0a68B8bA')  
    print(f" Before function callcurrent usdc token deposit balance is {defi_contract.depositBalance(account)}")  

    usdc_contract.approve(defi_contract,10000,{"from": account}) 
    defi_contract.depositToken(10000, {"from": account})   

    print(f"After function call current usdc token deposit balance is {defi_contract.depositBalance(account)}")         

    defi_contract.withdraw(100, {"from": account})   

    print(f"After withdrawal current usdc token deposit balance is {defi_contract.depositBalance(account)}")             