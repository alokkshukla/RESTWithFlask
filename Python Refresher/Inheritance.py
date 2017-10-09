class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    def friend1(self, friend_name):
        return Student(friend_name, self.school)

    @classmethod
    def friend(cls, origin, friend_name, *args, **kwargs):
        return cls(friend_name, origin.school, args, kwargs)


# class WorkingStudent(Student):
#     pass
#
# anna = WorkingStudent("anna","MIT")
# print(anna.__dict__)

class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary


# anna = WorkingStudent("anna","MIT",20)
# greg = anna.friend1("greg")
# Greg = anna.friend(anna,"Greg",34)
# #print(greg.salary)
# print(Greg.salary)


def my_method(arg1, arg2):
    return arg1 + arg2


def my_long_method(arg1, arg2, arg3):
    return arg1 + arg2 + arg3


def my_list_method(data):
    return sum(data)


print(my_list_method([1, 2, 3]))


def addition_simplified(*args):
    return sum(args)


print(addition_simplified(1, 2, 3))


def named_args(name, location):
    print(name)
    print(location)


named_args(name='jose', location='us')


def what_are_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)


what_are_kwargs(1, 2, 3)
what_are_kwargs(1, 2, 3, name='Jose', location='US')
what_are_kwargs(1, 2, 3, location='US', name='jose')


def methodception(another):
    return another()


def add_two_numbers():
    return 34 + 45


print(methodception(add_two_numbers))
print(methodception(lambda: 23 + 45))

my_list = [13, 23, 45, 34, 45]
my_list.remove(23)

print(list(filter(lambda x: x != 13, my_list)))

print((lambda x: x * 3)(4))

print([x for x in my_list if x != 13])

# Decorators

import functools


def my_decorator(func):
    @functools.wraps(func)
    def func_that_runs_func():
        print("In the decorator - before func")
        func()
        print("In the decorator - after func")

    return func_that_runs_func


@my_decorator
def my_func():
    print("In the func")


my_func()


def dec_with_arg(num):
    def my_decorator(func):
        @functools.wraps(func)
        def func_that_runs_func(*args, **kwargs):
            print("In the decorator - before func")
            if (num != 56):
                print("Cant run")
            else:
                func(*args, **kwargs)
            print("In the decorator - after func")

        return func_that_runs_func

    return my_decorator


@dec_with_arg(6)
def my_func2(a, b):
    print(a + b)


my_func2(1, 2)
