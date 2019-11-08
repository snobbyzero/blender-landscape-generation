import random
import time

import numpy as np

NOISE_WIDTH = 200
NOISE_HEIGHT = 200
AMP = 5.0


def noise(x, y, seed):
    n = x + y * 57
    n = (n << 13) ^ n
    random.seed(n + seed)
    # для окружения острова водой
    #if x < NOISE_HEIGHT / 80 or x > 15 or y < NOISE_WIDTH / 80 or y > 15:
    #    return 0.1
    return random.uniform(0.0, +1.0)


# косинусная интерполяция
def cosine_interpolation(a, b, x):
    ft = x * np.pi
    f = (1 - np.cos(ft)) * 0.5
    return a * (1 - f) + b * f


def linear_interpolation(a, b, x):
    return a + (b - a) * x


def interpolated_noise(x, y, interpolation, seed):
    interpolation = interpolation
    point_x = int(x)
    point_y = int(y)
    fractional_x = x - point_x
    fractional_y = y - point_y
    v1 = noise(point_x, point_y, seed)
    v2 = noise(point_x + 1, point_y, seed)
    v3 = noise(point_x, point_y + 1, seed)
    v4 = noise(point_x + 1, point_y + 1, seed)
    i1 = interpolation(v1, v2, fractional_x)
    i2 = interpolation(v3, v4, fractional_x)
    return interpolation(i1, i2, fractional_y)


# матрица с обработанными значениями
def get_noise_arr(seed):
    start_time = time.time()
    zz = [[] for i in range(NOISE_HEIGHT)]
    for i in range(NOISE_WIDTH):
        for j in range(NOISE_HEIGHT):
            temp = 0
            for n in range(1, 5):
                #zz[i].append(
                #    (interpolated_noise(i * AMP / NOISE_WIDTH, j * AMP / NOISE_HEIGHT, cosine_interpolation, seed)))
                temp += (interpolated_noise(i * 2 * n * AMP / NOISE_WIDTH, j * 2 * n * AMP / NOISE_HEIGHT, cosine_interpolation, seed)) * 0.25 * (5 - n)
            zz[i].append(np.power(temp, 4))
    max_val = np.amax(zz)
    min_val = np.amin(zz)
    print("noise time %s" % (time.time() - start_time))
    return zz, max_val, min_val
