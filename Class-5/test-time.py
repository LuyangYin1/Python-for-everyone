import timeit
import math as Math
t = [n ** 2 for n in range(1000)]
print(timeit.timeit('sum(t)', globals=globals(), number=1000))
t = (Math.sqrt(n) for n in range(1000))
print(timeit.timeit('sum(t)', globals=globals(), number=1000))