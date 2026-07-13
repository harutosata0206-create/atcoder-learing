def f(x):
    result = (x**2) + (2 * x) + 3 
    return result


t = int(input())

ans = f(f(f(t) + t) + f(f(t)))
print(ans)