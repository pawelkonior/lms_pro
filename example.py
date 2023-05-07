# from _decimal import Decimal
#
# import pytest
#
#
# def divide(a, b):
#     if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
#         raise ValueError(f'Something is no yes!')
#     return a / b
#
#
# # test correct dividing
# def test_correct_dividing():
#     assert divide(2, 1) == 2
#
#
# # test incorrect dividing
# def test_incorrect_dividing():
#     assert divide(2, 1) != 4
#
#
# # test non int or float division
# def test_non_int_or_float_division():
#     with pytest.raises(ValueError) as ctx:
#         divide(Decimal(4), 2)
#     assert 'Something is no yes!' in str(ctx)
#
#
# # test invalid zero division;
# def test_invalid_zero_division():
#     with pytest.raises(ZeroDivisionError) as ctx:
#         divide(2, 0)
#     assert 'division by zero' in str(ctx)
#

# def g():
#     print(1)
#     yield 1
#     print(2)
#     yield 2
#     print(3)


# g1 = g()
# print(next(g1))
# print(next(g1))
# print(next(g1))
# for i in g():
#     print(i)

def g():
    idx = 0
    while True:
        yield idx
        idx += 1
        if idx > 3:
            return


# g1 = g()
# print(next(g1))
# print(next(g1))
# print(next(g1))
# print(next(g1))
# print(next(g1))
# print(next(g1))

# for i in g():
#     print(i)