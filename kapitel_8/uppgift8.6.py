def ref_demo(a, x):
    l = [e for e in a if e >= x]
    return sum(l)


v = [2, 5, 3]
print(ref_demo(v, 3))
