# Short script to oranize csv files form scraper
# Calculating price/kg
# Formatting

# Improvemnts:
# Include user input to open and create files.


import csv
import re # RegEx operations

# Opens file and writes inital data.
new_file = open("nonRaw.csv", "w")
csv_writer = csv.writer(new_file)
csv_writer.writerow(["Produkt", "Mengde", "Pris", "Per KG"])

with open("sp_scrape.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    # Skips first line.
    csv_file.readline()

    for line in csv_reader:

        ## Removes non-ASCII and clutter text.
        line[0] = line[0].replace("Microgreens-frÃ¸", "")
        line[0] = line[0].replace("microgreens-frø", "")
        line[0] = line[0].replace("for Microgreen", "")
        line[0] = line[0].replace("Ã¸", "ø")
        line[0] = line[0].replace("Ã¥", "å")
        line[0] = line[0].replace("Ã", "ø")
        line[0] = line[0].replace("Â´", "´")
        line[0] = line[0].replace(",", "")
        line[0] = line[0].replace("-", "")
        line[0] = line[0].replace("(50 gram)", "")
        line[0] = line[0].replace("(250 gram)", "")
        line[0] = line[0].replace("(1kg)", "")

        # Finds the product amount, used to calculate price/kg
        mengde = re.findall("\(.*?\)", line[0])
        mengde = str(mengde)
        mengde = mengde[3:]
        mengde = mengde[:-3]

        line[1] = line[1][:-3]
        line[1] = int(line[1])

        perKG = 0
        pris = line[1]
        if "1kg" in mengde:
            perKG = pris

        elif "2" in mengde:
            perKG = pris/250*1000

        else:
            perKG = pris/50*1000

        pris = line[1]

        # Writes data to file.
        csv_writer.writerow([line[0], mengde, line[1], perKG])
