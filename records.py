from collections import defaultdict

class Record:
    def __init__(self):
        self.record = defaultdict(list)
        # record contains the mapping on the hash of a user's pin to their bank accounts
        # for simplicity, a user has exactly 1 bank account

    def hash_exists(self, h):
        if h in self.record:
            return True
        else:
            return False

    def add_account(self, h, account):
        self.record[h].append(account)

    def delete_account(self, h, idx):
        self.record[h].pop(idx)

    def view_accounts(self, h):
        return self.record[h]

    def get_record(self):
        return self.record



