from PIL import Image, ImageOps
import sys


try:
    input = sys.argv[1]
    output = sys.argv[2]
except IndexError:
    sys.exit("Too few arguments.")


# Check the command line arguments
if len(sys.argv) > 3:
    sys.exit("Too many arguments")

# Check file extentions
else:
    name_1, file_1 = input.split(".")
    name_2, file_2 = output.split(".")
    extentions = ["jpeg", "jpg", "png"]

    if file_1.lower() not in extentions or file_2.lower() not in extentions:
        sys.exit("Invalid input")

    elif file_1 != file_2:
        sys.exit("Input and output have different extensions")

    try:

        shirt = Image.open("shirt.png")
        photo = Image.open(input)

        size = shirt.size
        photo = ImageOps.fit(photo, size)

        photo.paste(shirt, shirt)
        photo.save(output)

    except FileNotFoundError:
        sys.exit("File does not exist")
