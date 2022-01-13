from PIL import Image

x1, x2, y1, y2 = -1.25, 1.25, -1.25, +1.25
max_iterations = 255
image_of_x = 512
image_of_y = 512
image = Image.new("RGB", (image_of_x, image_of_y))
for y in range(image_of_y):
    zy = y * (y2- y1) / (image_of_y - 1)  + y1
    for x in range(image_of_x):
        zx = x * (x2 - x1) / (image_of_x - 1)  + x1
        z = zx + zy * 1j
        c = z
        for i in range(max_iterations):
            if abs(z) > 2.0: break
            z = z * z + c
        image.putpixel((x, y), (i % 2 * 128, i % 8 * 16, i % 8 * 256))
image.show()