import random

from PIL import Image, ImageDraw
import time

from noise import get_noise_arr, NOISE_WIDTH, NOISE_HEIGHT

SEED = random.randint(0, 1000)
noise_arr, max_val, min_val = get_noise_arr(SEED)
image = Image.new("RGB", (NOISE_WIDTH, NOISE_HEIGHT))

color_image = Image.new("RGB", (NOISE_WIDTH, NOISE_HEIGHT))


def color(height):
    print(height)
    if height <= 0.03:
        return (12, 129, 166)
    elif height <= 0.05:
        return (235, 232, 143)
    elif height <= 0.2:
        return (115, 190, 131)
    else:
        return (143, 144, 144)


start_time = time.time()
for x in range(NOISE_WIDTH):
    for y in range(NOISE_HEIGHT):
        t = (noise_arr[x][y] - min_val) / (max_val - min_val)
        ImageDraw.Draw(color_image).point((x, y), color(t))
        ImageDraw.Draw(image).point((x, y),
            (int(255 - t * 255), int(255 - t * 255), int(255 - t * 255)))
image.save("C:/Users/user/PycharmProjects/blender_test/test.png", "PNG")
color_image.save("C:/Users/user/PycharmProjects/blender_test/color.png", "PNG")
print("Draw time: %s" % (time.time() - start_time))
