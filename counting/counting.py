def calculate_diff(s):
    n = len(s)
    differences = []

    for i in range(n):
        if s[i] == 'L':
            differences.append(n - 1 - 2*i)
        else:  # s[i] == 'R'
            differences.append(-n + 1 + 2*i)

    return differences

def max_row_values(s):
    n = len(s)
    initial_val = get_row_val(s)    #get initial row value
    differences = calculate_diff(s)
    
    # Sort the differences in descending order.
    sorted_diffs = sorted(differences, reverse=True)
    results = [initial_val]
    
    for k in range(1, n+1):  # Change this line to run up to n-1
        #check if negative value -> keep the prev max
        if sorted_diffs[k-1] >= 0:
            results.append(results[-1] + sorted_diffs[k-1])
        else:
            results.append(results[-1])

    return results

#calculates the row value
def get_row_val(s):
    n = len(s)
    value = 0
    
    for i in range(n):
        if s[i] == 'R':
            value += n - i - 1
        else:
            value += i
    return value

# Read input.txt
with open('input.txt', 'r') as f:
    length = int(f.readline().strip())
    test_case = f.readline().strip()

results = max_row_values(test_case)

# Write the results to output.txt
with open('output.txt', 'w') as output_file:
    output_file.write(' '.join(map(str, results[1:])))
