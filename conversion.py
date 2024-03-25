# U+1F47B,U+1F480,U+1F47E,U+1F5A4 funny imoji list
import csv, cv2

with open('emojis.csv', 'r') as FILE:
    reader = csv.reader(FILE)
    emojis = list(reader)

image = cv2.imread("input.png", cv2.IMREAD_GRAYSCALE)
image_height, image_width = image.shape[:2]

block_size = 4

output = []

for x in range(0, image_height, 4):

    output_row = []

    for y in range(0, image_width, 4):

        #obtain the grey value
        total_grey_value = 0
        if x + block_size <= image_height and y + block_size <= image_width:
            for block_x in range(block_size):
                for block_y in range(block_size):
                    total_grey_value += image[x + block_x, y + block_y]
        total_grey_value = total_grey_value / (block_size**2)

        output_row.append(total_grey_value)
    output.append(output_row)

print(output)


