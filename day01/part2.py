from __future__ import annotations

import argparse
import os.path

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    numbers = [int(line) for line in s.splitlines()]
    prev_sum = 0
    sum_num = 0
    cnt = 0
    total = len(numbers)
    for i, n in enumerate(numbers):
        print(i, i+3)
        if i < total - 3:
            sum_num = sum(numbers[i:i+3])
            if sum_num > prev_sum: 
                cnt += 1
            prev_sum = sum_num
    return cnt


INPUT_S = '''\
199
200
208
210
200
207
240
269
260
263
'''


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, 5),
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
