# account open


def open_account(name):
    print("=" * 135)
    print(f"Hey '{name}' Account opened successfully!".center(135))
    print("=" * 135)


# account deposit


def deposit(balance, amount):
    print(f"Depositing {amount:,} ".center(135))
    balance += amount
    print("=" * 135)
    print(f"New balance is {balance:,}".center(135))
    print("=" * 135)
    return balance


# account withdraw


def withdraw(balance, amount):
    if balance >= amount:
        print("=" * 135)
        print(f"Withdrawing {amount:,} ".center(135))
        print("=" * 135)
        balance -= amount
    else:
        print("Insufficient funds".center(135))
    print("=" * 135)
    print(f"New balance is {balance:,}".center(135))
    print("=" * 135)
    return balance


# show balance
def show_balance(balance):
    print("=" * 135)
    print(f"Your Current balance is {balance:,}".center(135))
    print("=" * 135)


# main function
def main():
    print(
        r"""
 _    _      _                            _                            ________  ___ _   _  ______             _    
| |  | |    | |                          | |                          /  ___|  \/  || | | | | ___ \           | |   
| |  | | ___| | ___ ___  _ __ ___   ___  | |_ ___    _ __ ___  _   _  \ `--.| .  . || |_| | | |_/ / __ _ _ __ | | __
| |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | '_ ` _ \| | | |  `--. \ |\/| ||  _  | | ___ \/ _` | '_ \| |/ /
\  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | | | | | | | |_| | /\__/ / |  | || | | | | |_/ / (_| | | | |   < 
 \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  |_| |_| |_|\__, | \____/\_|  |_/\_| |_/ \____/ \__,_|_| |_|_|\_\
                                                                __/ |                                               
                                                               |___/                                                
""".center(
            135
        )
    )

    name = input("Enter your name to open an account:")
    balance = 0
    open_account(name)
    while True:
        action = input(
            """Choose actions :
            press 1:deposit\n
            press 2:withdraw\n
            press 3:show balance\n
            press 4:exit\n
            |
            |
            xxx:(withdraw all amount)\n              
            Your choice: """
        )
        if action == "1":
            amount = float(input("Enter amount to deposit: "))
            balance = deposit(balance, amount)
        elif action == "2":
            amount = float(input("Enter amount to withdraw: "))
            balance = withdraw(balance, amount)
        elif action == "3":
            show_balance(balance)
        elif action == "4":
            print("=" * 135)
            print(
                r"""Ｔｈａｎｋ ｙｏｕ ｆｏｒ ｂａｎｋｉｎｇ ｗｉｔｈ ｕｓ.Ｂｙｅ!👋""".center(
                    125
                )
            )
            print("=" * 135)
            break

        elif action == "xxx":
            print("=" * 135)
            print("Withdrawing all amount".center(135))
            balance = withdraw(balance, balance)

        else:
            print("Invalid choice. Please try again.".center(135))


try:
    main()
except Exception as e:
    print(f"The error has come-->: {e}")
# end of the code
