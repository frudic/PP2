def m(l):
    r = 1
    for i in l:
        r *= i
    return r

def c(s):
    u = sum(1 for i in s if 'A' <= i <= 'Z')
    l = sum(1 for i in s if 'a' <= i <= 'z')
    return u, l

def p(s):
    return s == s[::-1]

def s(n, t):
    x = n ** 0.5
    print("Square root of", n, "after", t, "milliseconds is", x)

def a(t):
    return all(t)

print(m([1, 2, 3, 4]))
print(c("HelloWorld"))
print(p("madam"))
s(25100, 2123)
print(a((True, True, True)))