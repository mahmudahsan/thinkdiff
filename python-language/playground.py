import statistics

data = [10, 8, 5, 3, 1, 2, 1, 9, 10, 5]
print(f'{statistics.fmean(data)=}')

print(f'{statistics.geometric_mean(data)=}')

print(f'{statistics.multimode(data)=}')

print(f'{statistics.quantiles(data, n=3)=}')