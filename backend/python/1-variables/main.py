# sep  =>  separator   =>  разделитель
# end  =>  end of line =>  конец строки
# print("Hello", "world!", "Again", "it", "is ...", sep="+")
# ----------------------------------------------------------
# x = "qwe"
# z = 5

# print(type(x)) # <class 'str'>
# print(type(z)) # <class 'int'>

# # print(isinstance(x, str))  # True
# print(type(x) == str)    # True

# # print(isinstance(z, int))  # True
# print(type(z) == int)    # True
# ----------------------------------------------------------
# x = "2"  # 2
## int(x)  ==  parseInt(x)

# print("Before: ", type(x))
# x = int(x)
# print("After: ", type(x))
# print("-----------------------------------")
## str(x)  ==  String(x)
# x = 10
# print("Before: ", type(x))
# x = str(x)
# print("After: ", type(x))
# ----------------------------------------------------------
# NUMBER = 12
# print(NUMBER)
# NUMBER = 15
# print(NUMBER)
# ----------------------------------------------------------
# %  ->  Modulus
# number = 5
# print(number % 2)
# number = 11
# print(number % 3)
# ----------------------------------------------------------
# **  =>  power  =>  степень
# number = 3
# print(number ** 3)
# number = 2
# print(number ** 4)
# ----------------------------------------------------------
# //  =>  floor division  =>  целочисленное деление
# int(3.123)  #  3
# print(11 // 2) #  5
# print(13 // 3) #  4
# print(14 // 4) #  3
# ----------------------------------------------------------
# print(2 > 3)     # False
# print(3 <= 5)    # True
# print(3 == 3)    # True
# print(9/3 == 3)  # True
# print(2**2 != 5) # True
# print(9//4 >= 2) # True
# print(15%6 < 5)  # True
# ----------------------------------------------------------
# ||   ==    or
# &&   ==    and
# !    ==    not

# print(2 == 2 or 3 == 4 or 5 == 6 or 7 == 10)  # True
# print(2 == 5 or 3 == 4 or 5 == 6 or 7 == 10)  # False

# print(2 == 2 and 3 == 3 and 4 == 4 and 5 == 5)  # True
# print(2 == 2 and 3 == 3 and 4 == 4 and 5 == 6)  # False

# print(not 2 == 2)  # False
# print(not 3 == 2)  # True
# ----------------------------------------------------------
# Банковый баланс
bank_balance = 0

# Депозит
deposit = 10000

# Процентная ставка
interestRate = 0.1

# Задание:
# Рассчитываем доход по депозиту
# bank_balance = bank_balance + deposit
bank_balance += deposit
print("Our balance: $", bank_balance)

# когда мы хотим узнать 17% от  $67
# 1.  (67 / 100) * 17   => 17% от 67
# 2.  67 * 0.17         => 17% от 67

income_after_1_year = bank_balance * interestRate
print("After 1 year: $", bank_balance + income_after_1_year)

print("Monthly: $", income_after_1_year/12)
