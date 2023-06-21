def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x-1)

def is_odd(x):
    return not is_even(x)


print(is_odd(3))
print(is_even(3))

"""
print(is odd(3))

ret not(is even(3))

#masuk ke kondisi else
ret not(is odd(3-1))
ret not(is odd(2))
ret not(ret not(is even(2)))
ret not(ret not(is odd(2-1)))
ret not(ret not(is odd(1)))
ret not(ret not(ret not(is even(1))))
ret not(ret not(ret not(is odd(1-1))))
ret not(ret not(ret not(is odd(0))))
ret not(ret not(ret not(ret not(is even(0)))))

# masuk ke kondisi x == 0
ret not(ret not(ret not(ret not(true))))
ret not(ret not(ret not(false)))
ret not(ret not(true))
ret not(false)
(true)


print(is_even(3))

#masuk ke kondisi else
is_odd(3-1)
is_odd(2)
ret not(is even(2))
ret not(is odd(2-1))
ret not(is odd(1))
ret not(ret not(is even(1)))
ret not(ret not(is odd(1-1))) 
ret not(ret not(is odd(0)))
ret not(ret not(ret not(is even(0))))

#masuk ke kondisi x == 0
ret not(ret not(ret not(true)))
ret not(ret not(false))
ret not(true)
(false)
"""