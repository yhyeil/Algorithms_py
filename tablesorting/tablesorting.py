# Read input from input.txt
with open('input.txt', 'r') as f:
    lines = f.readlines()

column_names = lines[0].strip().split()
rules_str = lines[1].strip().split(', ')
rules = [(rule.split()[0], rule.split()[1]) for rule in rules_str]

table = [line.strip().split() for line in lines[2:]]

# Define a custom sorting function based on the rules
def custom_sort(row):
    key = []
    for rule in rules:
        column_name, sort_order = rule
        index = column_names.index(column_name)
        value = row[index]
        
        if value.isdigit():
            key.append(int(value) if sort_order == 'ASC' else -int(value))
        else:
            # If it's DESC for a string, we negate the ordinal value of each character
            if sort_order == 'DESC':
                key.append(tuple(-ord(char) for char in value))
            else:
                key.append(value)
    return tuple(key)  # Convert key list to a tuple

# Sort the table based on the custom sorting function
table.sort(key=custom_sort)

# Write the sorted table to output.txt
with open('output.txt', 'w') as f:

    # Then, write the sorted data rows
    for row in table:
        f.write(' '.join(row) + '\n')
