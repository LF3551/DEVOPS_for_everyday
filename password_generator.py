import random

lower = "abcdefghijklmnoprstuvwxyz"
upper = "ABCDEFGHIJKLMNOPRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*:;/,._-"

all_data = lower+upper+numbers+symbols
length = 16
password = "".join(random.sample(all_data,length))
print(password)
