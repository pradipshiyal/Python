# 23) WAP to convert integer into binary
n = 11
bi = 0
i = n
power = 1

while n > 0:
    rem = n % 2
    bi = bi + rem * power
    power *= 10
    n //= 2

print(bi) 