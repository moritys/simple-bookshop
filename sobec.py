# from dataclasses import dataclass


# @dataclass
# class Person:
#     name: str
#     age: int

#     def __post_init__(self, *args):
#         if not isinstance(self.age, int):
#             raise TypeError('age is str!')


# constantin = Person('constantin', '28')
# print(constantin)

# class Test:
#     def __init__(self, par) -> None:
#         ...

#     @staticmethod
#     def execute_test(func, *args):
#         print(f'started {func.__name__} test')
#         try:
#             func(*args)
#             print(f'{func.__name__} test COMPLETED')
#         except Exception:
#             print(f'{func.__name__} test FAILED')


# def div(x, y):
#     return x / y


# Test.execute_test(div, 2, 5)
# Test.execute_test(div, 2, 0)
