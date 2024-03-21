from functools import cache


'''
        0
      1   2
    3   4   5
  6   7   8   9
10 11  12   13  14
'''

def stringifyState(state: int):
    str_rep = ""
    for i in range(5):
        str_rep += " " * (4 - i)
        for j in range(i + 1):
            str_rep += f"{int(state & (1 << (i * (i + 1) // 2 + j)) > 0)} "
        str_rep += "\n"
    return str_rep


jumpables = {
    0: [(1, 3), (2, 5)],
    1: [(3, 6), (4, 8)],
    2: [(4, 7), (5, 9)],
    3: [(1, 0), (4, 5), (6, 10), (7, 12)],
    4: [(7, 11), (8, 13)],
    5: [(2, 0), (4, 3), (8, 12), (9, 14)],
    6: [(3, 1), (7, 8)],
    7: [(4, 2), (8, 9)],
    8: [(4, 1), (7, 6)],
    9: [(5, 2), (8, 7)],
    10: [(6, 3), (11, 12)],
    11: [(7, 4), (12, 13)],
    12: [(7, 3), (8, 5), (11, 10), (13, 14)],
    13: [(8, 4), (12, 11)],
    14: [(9, 5), (13, 12)]
}


def numPegs(state: int) -> int:
    return sum([int(state & (1 << i) > 0) for i in range(15)])


@cache
def solve(state: int) -> bool:
    if numPegs(state) < 8:
        return False

    if numPegs(state) == 8:
        for i in range(15):
            if state & (1 << i) == 0:
                for j, k in jumpables[i]:
                    if state & (1 << j) > 0 and state & (1 << k) > 0:
                        return False
        print(stringifyState(state))
        return True

    for i in range(15):
        if state & (1 << i) == 0:
            for j, k in jumpables[i]:
                if state & (1 << j) > 0 and state & (1 << k) > 0:
                    if solve(state ^ (1 << i) ^ (1 << j) ^ (1 << k)):
                        print(stringifyState(state))
                        return True
    return False

if __name__ == "__main__":
    for i in range(15):
        if solve(0b111111111111111 ^ (1 << i)):
            break
