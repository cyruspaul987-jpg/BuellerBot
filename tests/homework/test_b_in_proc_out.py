import os
import sys

sys.path.append(os.getcwd())

from src.homework.b_in_proc_out.output import multiply_numbers


def test_multiply_sevens() -> None:
    assert multiply_numbers(7, 7) == 49


def test_multiply_fives() -> None:
    assert multiply_numbers(5, 5) == 25
