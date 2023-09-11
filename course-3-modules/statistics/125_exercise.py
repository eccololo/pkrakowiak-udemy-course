from statistics import NormalDist

mean = 170
stddev = 15

dist = NormalDist(mean, stddev)

probability = dist.cdf(180) - dist.cdf(170)

print(f"Probability: {round(probability * 100, 2)}%")