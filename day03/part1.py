from __future__ import annotations

import argparse
import os.path

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    """
    Considering only the first bit of each number, there are five 0 bits and seven 1 bits. Since the most common bit is 1, the first bit of the gamma rate is 1.

    The most common second bit of the numbers in the diagnostic report is 0, so the second bit of the gamma rate is 0.

    The most common value of the third, fourth, and fifth bits are 1, 1, and 0, respectively, and so the final three bits of the gamma rate are 110.

    So, the gamma rate is the binary number 10110, or 22 in decimal.

    The epsilon rate is calculated in a similar way; rather than use the most common bit, the least common bit from each position is used. So, the epsilon rate is 01001, or 9 in decimal. Multiplying the gamma rate (22) by the epsilon rate (9) produces the power consumption, 198.
    """
    lines = s.splitlines() 
    lenlines = len(lines)
    count = [0] * len(lines[0])
    for line in lines:
        for i, n in enumerate(line):
            if n == "1":
                count[i] += 1
    print(count, lenlines)
    gamma = []
    elp = []
    for cnt in count:
        if lenlines - cnt < cnt:
            # 1 is the most significant bit
            gamma.append("1")
            elp.append("0")
        else:
            gamma.append("0")
            elp.append("1")
    print(gamma, elp)
    gamma = "".join(gamma)
    elp = "".join(elp)
    return int(gamma, 2) * int(elp, 2) 


INPUT_S = '''\
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
'''


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, 198),
    ),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, timing():
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
