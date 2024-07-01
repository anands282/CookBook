"""
you need to unpack N items from an iterable but the iterable may contain more elements leading to 'too many values to
unpack exception'
Solution:
use *expression to bulk unpack
"""


def unpack_grades(grades):
    first, *middle, last = grades
    return middle


if __name__ == "__main__":
    print(unpack_grades((100, 200, 300, 400, 500)))
