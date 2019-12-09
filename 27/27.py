import math

def is_prime(potential_prime):
    if potential_prime == 0:
        return False
    elif potential_prime == 1:
        return False
    else:

        for x in range(2, int(math.sqrt(abs(potential_prime)) + 1)):
            if potential_prime % x == 0:
                return False

        return True

def count_largest_product():

    largest = 0
    product = 0

    for a in range(3, 1000):
        for b in range(3, 1000):

            if is_prime(a) and is_prime(b):

                i = 0
                while True:
                    quadratic = i ** 2 + a * i + b

                    if not is_prime(quadratic):
                        if i - 1 >= largest:
                            largest = i - 1
                            product = a * b
                        break

                    i += 1
                i = 0
                while True:
                    quadratic = i ** 2 - a * i + b

                    if not is_prime(quadratic):
                        if i - 1 > largest:
                            largest = i - 1
                            product = a * b * -1
                        break

                    i += 1
    return product

print(str(count_largest_product()))

