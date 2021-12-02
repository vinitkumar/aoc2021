from __future__ import annotations

import argparse
import os.path

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    positions = [line for line in s.splitlines()]
    hor = 0
    depth = 0

    for position in positions:
        pos_type, value = position.split(" ")
        if pos_type == "forward":
            hor += int(value)
        if pos_type == "down":
            depth = depth + int(value)
        if pos_type == "up":
            depth = depth - int(value)
        print(aim, depth)
    return hor * depth


INPUT_S = '''\
forward 5
down 5
forward 8
up 3
down 8
forward 2
'''


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, 150),
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
