from account import *
from input import *
from records import *
import time

class System:
    def __init__(self):
        print("ATM Initialized...")
        self.records = Record()
        self.input_checker = InputChecker(True)

    def cardhandler(self):
        # Can modify function to enable security check on a given card
        pass

    def pinhandler(self, pin):
        hp = hash(pin)
        return [self.records.hash_exists(hp), hp]

    def check_input(self, s):
        self.input_checker.check(s)
        return True

    def access_ic(self):
        return self.input_checker

    def access_records(self):
        return self.records

    def shutdown(self):
        self.access_records().get_record().clear()
        print("\nShutting down...")


def banking(acc, input_checker):
    ret = 0
    while True:
        choice = input("Select: ")
        options = ['1', '2', '3', '4']
        if choice not in options:
            print('Please select from the given four options.')
            continue
        if choice == '1':
            is_num = False
            while True:
                if is_num:
                    break
                try:
                    amt = input("Enter deposit amount:  ")
                    input_checker.check(amt)
                    acc.deposit(int(amt))
                    is_num = True
                except Exception:
                    print("Failed to deposit. Deposit amount must be an integer.")
        elif choice == '2':
            is_num = False
            while True:
                if is_num:
                    break
                try:
                    amt = input("Enter withdrawal amount:  ")
                    input_checker.check(amt)
                    acc.withdraw(int(amt))
                    is_num = True
                except Exception:
                    print("Failed to withdraw. Withdrawal amount must be an integer.")
        elif choice == '3':
            acc.read_balance()
        elif choice == '4':
            ret = 1
            break
    return ret


def start(s):
    try:
        while True:
            time.sleep(1)
            print("Please enter your card into the ATM.", end='')
            time.sleep(1)
            print("   *inserts card!*")
            s.cardhandler()
            done = False
            time.sleep(1)
            while True:
                if done:
                    break
                pin = input("Please enter your 4 digit PIN:  ")

                if len(pin) != 4:
                    print("PIN must be exactly 4 digits.")
                    continue
                if s.check_input(pin):
                    veri = s.pinhandler(pin)
                    if veri[0]:
                        acc = s.access_records().view_accounts(veri[1])[0]
                        print("Successfully authenticated user.")
                        print("What would you like to do?")
                        print("Options:")
                        print("[1] Deposit")
                        print("[2] Withdraw")
                        print("[3] Get Balance")
                        print("[4] Quit")
                        while True:
                            result = banking(acc, s.access_ic())
                            if result:
                                done = True
                                ret = 1
                                time.sleep(1)
                                print(".")
                                time.sleep(1)
                                print(".")
                                time.sleep(1)
                                print(".")
                                time.sleep(1)
                                print("===================")
                                print("Session Terminated.")
                                print("===================\n")
                                time.sleep(2)
                                break
                    else:
                        print("Incorrect PIN. Please try again.")

    except KeyboardInterrupt:
        ret = 1
    except EOFError:
        ret = 1
    except Exception as err:
        print("ERROR: " + repr(err).split("'")[1])
        ret = 0
    if not ret:
        print("Returning to Main Menu...")
    return ret


if __name__ == "__main__":
    sys = System()
    time.sleep(1)
    # Add sample bank account with PIN #9056
    sample_acc = Account(1200, 500)
    sys.access_records().add_account(hash('9056'), sample_acc)

    # Start main procedure
    print("**Press CTRL-C at anytime to shutdown ATM**")
    time.sleep(1)
    while True:
        if start(sys):
            break
    # Delete sample bank account before terminating
    sys.shutdown()

