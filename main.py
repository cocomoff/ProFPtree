# -*- coding: utf-8 -*-

from ProFPtree import ProFPtree
from database import Database


def main():
    tdb = Database.toy()
    profptree = ProFPtree(tdb)
    print(profptree)

if __name__ == '__main__':
    main()
