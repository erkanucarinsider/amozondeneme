import random
import sys

a = "abcdefghıjklmnoprstuvyz"
b = "ABCDEFGHIJKLMNOPRSTUVYZ"
t = b[random.randint(0, len(a))] + a[random.randint(0, len(b))] + b[random.randint(0, len(a))]
for i in range(int(sys.argv[1])):
    print(f"Coupon:{t}:Number:{i}" + sys.argv[2])
