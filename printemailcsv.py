print("email,name,surname")
import random
import sys

a = "abcdefghijklmnoprstuvzx123456789"
t = a[random.randint(0, 23)] + a[random.randint(0, 23)] + a[random.randint(0, 23)]
for i in range(int(sys.argv[1])):
    print(f"{t}deneme{i}@deneme.com,test{i},user{i}")
