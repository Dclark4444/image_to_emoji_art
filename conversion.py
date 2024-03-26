# U+1F47B,U+1F480,U+1F47E,U+1F5A4 funny imoji list
import csv, cv2, os, glob
def get_emojis():
    with open('emojis.csv', 'r') as FILE:
        reader = csv.reader(FILE)
        emojis = list(reader)[0]
    return emojis

def get_image(image_index):
    image = cv2.imread("input" + str(image_index) + ".png", cv2.IMREAD_GRAYSCALE)
    return image

def write_text_file(image_index, output):
    with open("output" + str(image_index) + ".txt", "w", encoding='utf-8') as FILE:
        FILE.write(output)

def get_emoji(grey_value, emojis):
    step_value = 255 / len(emojis)
    for char_index, char in enumerate(emojis):
        if grey_value <= (char_index * step_value) + step_value:
            return chr(int(char[2:], 16))


def create_output(image, imojis):
    image_height, image_width = image.shape[:2]
    block_size = (image_height + image_width) // 200
    output = ""

    for x in range(0, image_height, block_size):

        output_row = ""

        for y in range(0, image_width, block_size):

            #obtain the grey value
            total_grey_value = 0
            if x + block_size <= image_height and y + block_size <= image_width:
                for block_x in range(block_size):
                    for block_y in range(block_size):
                        total_grey_value += image[x + block_x, y + block_y]
            total_grey_value = total_grey_value / (block_size**2)

            output_row += get_emoji(total_grey_value, imojis)
        output += output_row
        output += "\n"

    return output

def main():
    EMOJIS = get_emojis()

    os.chdir("input_pngs")
    for image_index, image in enumerate(glob.glob('*.png')):
        current_image = get_image(image_index)
        current_output = create_output(current_image, EMOJIS)
        os.chdir("../output_txts")
        write_text_file(image_index, current_output)
        os.chdir("../input_pngs")
        print("File Completed: " + str(image_index + 1))

    input("Output has completed, please press enter to close the program ")

main()
