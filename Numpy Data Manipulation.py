from numpy.random import default_rng
rng = default_rng()
vals = rng.standard_normal(10)
more_vals = rng.standard_normal(10)


random_array = rng.integers(1000, size=(5, 5))
print(random_array)
print(random_array[1, 2])
print(random_array.sum())
print(random_array.mean(1))
print(random_array.max(axis=0))
