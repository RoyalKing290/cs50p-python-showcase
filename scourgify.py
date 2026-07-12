import csv
import sys

# Expects the user to provide two command-line arguments
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

else:
    old_file = sys.argv[1]
    new_file = sys.argv[2]

    try:
        with open(old_file, "r") as reader_file:

            reader = csv.DictReader(reader_file)
            clean_row = []

            for row in reader:
                last, first = row["name"].replace('"', '').split(",")
                last = last.strip()
                first = first.strip()
                new_students = {"first": first, "last": last, "house": row["house"]}
                clean_r

        with open(new_file, "w") as writer_file:

            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(writer_file, fieldnames=fieldnames)

            writer.writeheader(clean_row)
            writer.writerow(clean_row)

    except FileNotFoundError:
        sys.exit("File does not exist")
