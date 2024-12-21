"""Functions that simulate dice rolls.

A dice function takes no arguments and returns a number from 1 to n
(inclusive), where n is the number of sides on the dice.

Types of dice:

 -  Dice can be fair, meaning that they produce each possible outcome with equal
    probability. Examples: four_sided, six_sided

 -  For testing functions that use dice, deterministic test dice always cycle
    through a fixed sequence of values that are passed as arguments to the
    make_test_dice function.
"""

from random import randint


#这个函数返回一个公平的骰子函数，该骰子能随机生成从 1 到 sides（包含 sides）的一个整数，且每个数字的概率相等
def make_fair_dice(sides):
    """Return a die that returns 1 to SIDES with equal chance."""
    assert type(sides) == int and sides >= 1, 'Illegal value for sides'
    def dice():
        return randint(1,sides)
    return dice

four_sided = make_fair_dice(4)#会返回 1 到 4 之间的随机整数
six_sided = make_fair_dice(6)#会返回 1 到 6 之间的随机整数


#make_test_dice(*outcomes)：这个函数返回一个确定性的骰子，它会按顺序返回你提供的 outcomes 参数中的值，且每次调用时返回的值会在这些值之间循环
def make_test_dice(*outcomes):
    """Return a die that cycles deterministically through OUTCOMES.

    >>> dice = make_test_dice(1, 2, 3)
    >>> dice()
    1
    >>> dice()
    2
    >>> dice()
    3
    >>> dice()
    1
    >>> dice()
    2

    This function uses Python syntax/techniques not yet covered in this course.
    The best way to understand it is by reading the documentation and examples.
    """
    assert len(outcomes) > 0, 'You must supply outcomes to make_test_dice'
    for o in outcomes:
        assert type(o) == int and o >= 1, 'Outcome is not a positive integer'
    index = len(outcomes) - 1
    def dice():#nonlocal index: 关键字 nonlocal 用来声明 index 变量不是局部的，而是引用外部作用域中的变量（index）。这使得 index 在每次调用时都能被更新
        nonlocal index
        index = (index + 1) % len(outcomes)
        return outcomes[index]
    return dice