from math import ceil, floor, pow


# Function to round - off the number
def Round_off(N, n):
    b = N
    c = floor(N)


    i = 0
    while (b >= 1):
        b = b / 10
        i = i + 1

    d = n - i
    b = N
    b = b * pow(10, d)
    e = b + 0.5
    if (float(e) == float(ceil(b))):
        f = (ceil(b))
        h = f - 2
        if (h % 2 != 0):
            e = e - 1
    j = floor(e)
    m = pow(10, d)
    j = j / m
    print("The number after rounding-off is", j)

if __name__ == '__main__':

    N = 139.01


    n = 5

    Round_off(N, n)