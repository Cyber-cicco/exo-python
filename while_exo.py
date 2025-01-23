from numpy.random import randint

for i in range(1500, 2701):
    if i % 5 == 0 and i % 7 == 0:
        print(i)

i = randint(0, 11)
while i > 2 :
    print(i)
    i = randint(0, 11)
print(i)
