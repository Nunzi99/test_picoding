#!/usr/bin/env python3
"""Simple in-memory CLI banking application with 4 basic operations."""

import sys
from dataclasses import dataclass, field


@dataclass
class Account:
    """Represents a bank account."""
    account_number: str
    holder_name: str
    balance: float = 0.0


# In-memory storage
accounts: dict[str, Account] = {}


def generate_account_number() -> str:
    """Generate a unique 8-digit account number."""
    num = len(accounts) + 10000000
    return str(num)


# ----- Operations -----

def create_account(holder_name: str) -> None:
    """Operation 1: Create a new bank account."""
    if holder_name in [a.holder_name for a in accounts.values()]:
        print(f"\nError: An account for '{holder_name}' already exists.")
        return

    acnt_num = generate_account_number()
    accounts[acnt_num] = Account(account_number=acnt_num, holder_name=holder_name)
    print(f"\n✓ Account created successfully!")
    print(f"  Account Number: {acnt_num}")
    print(f"  Holder Name:    {holder_name}")
    print(f"  Initial Balance: ${0.00:.2f}")


def deposit(account_number: str, amount: float) -> None:
    """Operation 2: Deposit money into an account."""
    if amount <= 0:
        print("\nError: Deposit amount must be greater than zero.")
        return

    acnt = accounts.get(account_number)
    if not acnt:
        print(f"\nError: Account '{account_number}' not found.")
        return

    acnt.balance += amount
    print(f"\n✓ Deposit successful!")
    print(f"  Amount:      ${amount:.2f}")
    print(f"  New Balance: ${acnt.balance:.2f}")


def withdraw(account_number: str, amount: float) -> None:
    """Operation 3: Withdraw money from an account."""
    if amount <= 0:
        print("\nError: Withdrawal amount must be greater than zero.")
        return

    acnt = accounts.get(account_number)
    if not acnt:
        print(f"\nError: Account '{account_number}' not found.")
        return

    if amount > acnt.balance:
        print(f"\nError: Insufficient funds. Available balance: ${acnt.balance:.2f}")
        return

    acnt.balance -= amount
    print(f"\n✓ Withdrawal successful!")
    print(f"  Amount:      ${amount:.2f}")
    print(f"  New Balance: ${acnt.balance:.2f}")


def view_balance(account_number: str) -> None:
    """Operation 4: View account balance."""
    acnt = accounts.get(account_number)
    if not acnt:
        print(f"\nError: Account '{account_number}' not found.")
        return

    print(f"\n─────── Account Details ─────━━")
    print(f"  Account Number: {acnt.account_number}")
    print(f"  Holder Name:    {acnt.holder_name}")
    print(f"  Balance:        ${acnt.balance:.2f}")
    print(f"─────────────────────────────────")


# ----- Input helpers -----

def get_positive_float(prompt: str) -> float:
    """Prompt for a positive float value."""
    while True:
        value = input(prompt).strip()
        try:
            result = float(value)
            if result > 0:
                return result
            print("   Please enter a value greater than zero.")
        except ValueError:
            print("   Invalid number. Please try again.")


def get_account_number(prompt: str) -> str:
    """Prompt and validate an existing account number."""
    while True:
        acct = input(prompt).strip()
        if acct in accounts:
            return acct
        print(f"   Account '{acct}' not found. Please try again.")


# ----- CLI menu -----

MENU = """
╔══════════════════════════════════╗
║       BANKING APPLICATION        ║
╠══════════════════════════════════╣
║  [1] Create Account              ║
║  [2] Deposit Money               ║
║  [3] Withdraw Money              ║
║  [4] View Balance                ║
║  [5] List All Accounts           ║
║  [0] Exit                        ║
╚══════════════════════════════════╝"""


def run_menu() -> None:
    """Display and handle the main menu loop."""
    while True:
        print(MENU)
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            holder = input("\n  Enter account holder name: ").strip()
            if not holder:
                print("\n  Error: Name cannot be empty.")
            else:
                create_account(holder)
        elif choice == "2":
            acct = get_account_number("  Enter account number: ")
            amt = get_positive_float("  Enter amount to deposit: $")
            deposit(acct, amt)
        elif choice == "3":
            acct = get_account_number("  Enter account number: ")
            amt = get_positive_float("  Enter amount to withdraw: $")
            withdraw(acct, amt)
        elif choice == "4":
            acct = get_account_number("  Enter account number: ")
            view_balance(acct)
        elif choice == "5":
            if not accounts:
                print("\n  No accounts exist yet.\n")
            else:
                print(f"\n{'─'*38}")
                print(f"  {'Account #':<12}{'Holder Name':<18}{'Balance':>14}")
                print(f"  {'─'*12}{'─'*18}{'─'*14}")
                for acnt in accounts.values():
                    print(
                        f"  {acnt.account_number:<12}"
                        f"{acnt.holder_name:<18}"
                        f"${acnt.balance:>13.2f}"
                    )
                print(f"{'─'*38}\n")
        elif choice == "0":
            print("\nGoodbye! Thank you for banking with us.\n")
            sys.exit()
        else:
            print("\n  Invalid choice. Please try again.\n")


if __name__ == "__main__":
    run_menu()
