# -*- coding: utf-8 -*-

from item import Trans

class Database(object):
    def __init__(self, transactions):
        self.transactions = transactions

    def __len__(self):
        return len(self.transactions)

    def __iter__(self):
        return iter(self.transactions)

    def dump(self):
        print("--------------")
        for trans in self.transactions:
            print(trans)
        print("--------------\n")


    @staticmethod
    def toy():
        toylist = [
            [("A", 1.0), ("B", 0.2), ("C", 0.5)],
            [("A", 0.1), ("D", 1.0)],
            [("A", 1.0), ("B", 1.0), ("C", 1.0), ("D", 0.4)],
            [("A", 1.0), ("B", 1.0), ("D", 0.5)],
            [("B", 0.1), ("C", 1.0)],
            [("C", 0.1), ("D", 0.5)],
            [("A", 1.0), ("B", 1.0), ("C", 1.0)],
            [("A", 0.5), ("B", 1.0)]
        ]
        ans = []
        for tlist in toylist:
            ans.append(Trans.build_from_list(tlist))
        return Database(ans)
