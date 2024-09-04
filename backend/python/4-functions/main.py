# def  =>  define 

# def test_function(fruit:str) -> str:
#     """This is test function for some checks"""
#     print(f"This is a {fruit}.")
#     return fruit

# fruit1 = test_function('banana')
# fruit2 = test_function("apple")
# fruit3 = test_function("orange")

# print("Return value 1: ", fruit1)
# print("Return value 2: ", fruit2)
# print("Return value 3: ", fruit3)
# ==========================================================
# ==========================================================
# ==========================================================
# ARGS  => Arguments  (but you can use any other word too)

# def blender(fruit:str='***', *args) -> None:
#     print("Arguments: ", args)
#     print(f"Blending {fruit}...")


# blender("banana")
# blender("apple")
# blender("orange", "mango", '...')
# blender()

# ==========================================================
# ==========================================================
# ==========================================================
# KWARGS  => Keyword Arguments (but you can use any other word too)

# def sum_up(a:int, b:int=10, c:int=15, **kwargs) -> int:
#     print(f"Keyword Arguments: {kwargs}")
#     return a + b + c

# res1 = sum_up(2, 2, 5)
# res2 = sum_up(2)
# res3 = sum_up(3, c=2, w=10, t='...', g='...')

# print("Result 1: ", res1)
# print("Result 2: ", res2)
# print("Result 3: ", res3)
# ==========================================================
# ==========================================================
# ==========================================================
# def must_have_function(*args, **kwargs) -> ...: pass

#     # pass  ==  ...

# print("Hello World!")

# ==========================================================
# ==========================================================
# ==========================================================
# LAMBDA  function

# def def_lmb_fn(x):
#     return x**2

# lmb_fn = lambda x, z: x+2+z

# print(lmb_fn(5, 5))
# ==========================================================
# ==========================================================
# ==========================================================
# RECURSION
# if 2==2:
#     print("Hello World!")
#     # end recursive function
# else: 
#     # call itself
#     ...


# ==========================================================
# ==========================================================
# ==========================================================
# def max_of_three_numbers(a:int, b:int, c:int) -> int:
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     else:
#         return c

# r1 = max_of_three_numbers(22, 5, 10)
# r2 = max_of_three_numbers(10, 3, 55)
# r3 = max_of_three_numbers(9, 99, 1)

# print("Result 1: ", r1)
# print("Result 2: ", r2)
# print("Result 3: ", r3)
# ==========================================================
# ==========================================================
# ==========================================================
def sum_up(*args):
    total = 0
    for x in args:
        total += x
    return total

result = sum_up(1, 2, 3, 4, 5, 6, 7, 8, 9)
print("Sum: ", result)