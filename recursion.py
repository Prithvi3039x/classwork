# def fact(n):
#     if n == 0 or n== 1:
#         return 1
#     return n * fact(n-1)


# a = fact(5)
# print(a)


# square = lambda n : n * n
# print(square(5))

# add = lambda a,b : a+b
# print(add(10,20))


def fun(n):
    if n == 0:
        return
    fun(n-1)
    print(n)
fun(3)