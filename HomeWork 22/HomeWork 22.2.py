import json


def filter_json_by_attribute(input_file, output_file, attribute, value):
    input_file = open(input_file, 'r')
    data = json.load(input_file)
    input_file.close()

    filtered_data = [
        entry for entry in data
        if value in entry.get(attribute, [])]

    output_file = open(output_file, 'w')
    json.dump(filtered_data, output_file, indent=4)
    output_file.close()

    print(f"Filtered data has been written to {output_file}")


input_file = "person.json"
output_file = "filtered_person.json"

filter_json_by_attribute(input_file, output_file, 'languages', 'English')
