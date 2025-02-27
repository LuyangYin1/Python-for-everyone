from collections import namedtuple
import sys
import os

def main():
    Rec = namedtuple('rec', ['name', 'age', 'score'])
    pat = Rec('pat', 23, 99)
    print(pat)
    print(pat.name, pat.age, pat.score)
    print(pat[0], pat[1], pat[2])
    print(pat._fields)
    print(pat._asdict())
    print(pat._replace(name='sam'))
    print(pat._replace(name='sam', age=33))
    print(pat._replace(name='sam', age=33, score=88))
    print(pat._replace(name='sam', age=33, score=88)._asdict())


if __name__ == '__main__':
    main()  