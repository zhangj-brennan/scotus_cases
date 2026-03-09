import csv

input_file = "case_origin.csv"
output_file = "case_origin_with_type.csv"

unique_courts = set()

def classify(court_name):
    name = court_name.lower()

    if "court of appeals" in name:
        return "Court of Appeals"
    elif "u.s. district court" in name:
        return "U.S. District Court"
    else:
        unique_courts.add(court_name)
        return court_name


with open(input_file, newline='', encoding="utf-8") as infile, \
     open(output_file, "w", newline='', encoding="utf-8") as outfile:

    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    header = next(reader)
    writer.writerow(header + ["court_type"])

    for row in reader:
        code = row[0]
        court_name = row[1]

        court_type = classify(court_name)

        writer.writerow([code, court_name, court_type])


print("\nUnique courts detected:\n")

for court in sorted(unique_courts):
    print(court)

print("\nCSV written to:", output_file)