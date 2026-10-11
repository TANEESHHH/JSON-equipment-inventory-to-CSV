def parse_equipment_line(line):
    cleanedline = line.strip().strip(",").strip("{}").strip()
    partsofcleaned = cleanedline.split(",")
    record = {}
    for part in partsofcleaned:
        key, value = part.split(":")
        key = key.strip().strip('"')
        value = value.strip().strip('"')

        if key == "working":
            record[key] = (value == "true")
        else:
            record[key] = value 
    return record


def read_equipment(filename):
    records = []
    with open(filename, "r") as source:
        for line in source:
            line_str = line.strip()
            if line_str == "[" or line_str == "]":
                continue                   
            record = parse_equipment_line(line_str)
            records.append(record)
    return records  


def csv_row(record):
    id = record["id"]
    room = record["room"]
    kind = record["kind"]
    if record["working"] == "true":
        state = "READY"
    else:
        state = "REPAIR"
    return f"{id},{room},{kind},{state}"


def write_csv(records, filename):
    with open(filename, "w") as file:
        file.write("id,room,kind,state\n")

        for record in records:
            file.write(csv_row(record) + "\n")

def main():
    records = read_equipment("equipments.json")
    write_csv(records, "equipments.csv")
    print(f"Wrote  {len(records)}  equipment records")

if __name__ == "__main__":
    main()

