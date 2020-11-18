import numpy as np  # I'll use the numpy random functionalities
from random import randrange


def nextmove(x, y):
    dir = randrange(1, 5)
    if dir == 1:
        x += 1
    elif dir == 2:
        y += 1
    elif dir == 3:
        x -= 1
    elif dir == 4:
        y -= 1
    return x, y


x, y = 0, 0


for i in range(10):
    x, y = nextmove(x, y)
    print(x, y)


# integrating the weird function with hit-or-miss ----------------------------|
# Re-do here in class


def f(x): return np.sin(1/((x-a)*(b-x)))**2  # the function to integrate


N = 10000
k = 0
a = 0.
b = 2.

for i in range(N):
    x_sampl = a + (b-a)*np.random.random()
    y_sampl = np.random.random()
    if y_sampl <= f(x_sampl):
        k += 1

A = (b-a)*1.
I = A*k/N
print("I = {0:.6e}".format(I))

# error
sigma_HM = np.sqrt(I*(A-I)/N)  # HM stands for hit-or-miss
print('error for hit-or-miss = {0:.6e}'.format(sigma_HM))


# integrating the weird function with mean value -----------------------------|
# Re-do here in class
k = 0  # will contain average of f
k2 = 0  # will contain average of f**2
for i in range(N):
    x = a + (b-a)*np.random.random()
    k += f(x)
    k2 += f(x)**2

I = k * (b-a)/N
print("I = {0:.6e}".format(I))

# error
var = k2/N - (k/N)**2  # variance <f**2> - <f>**2
sigma_MV = (b-a)*(var/N)**0.5  # MV stands for Mean Value
print('error for mean value = {0:.6e}'.format(sigma_MV))
print('Recall error for hit-or-miss = {0:.6e}'.format(sigma_HM))
