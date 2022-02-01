# 20CE075 PARTH PARMAR
# Practical 5 Swap Case
# https://github.com/Morningstar000/Python-Practical-5

string = input()
str1 = ''
for i in string:
    if i.isalpha():
        str1 += i.swapcase()
    else:
        str1 += i
print(str1)
