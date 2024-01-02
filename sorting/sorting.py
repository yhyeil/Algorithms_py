def can_sort(n, arr):
    # Separate the numbers at even and odd indices
    even_indices = [arr[i] for i in range(0, n, 2)]
    odd_indices = [arr[i] for i in range(1, n, 2)]

    # Sort them
    even_indices.sort()
    odd_indices.sort()

    # Combine the two sorted lists
    merged = [0] * n
    merged[::2] = even_indices
    merged[1::2] = odd_indices

    # Check if the combined list is sorted
    return merged == sorted(arr)

with open('input.txt', 'r') as file:
    n = int(file.readline().strip())
    line = list(map(int, file.readline().split()))

if can_sort(n, line):
    with open('output.txt', 'w') as output_file:
        output_file.write("YES")
else:
    with open('output.txt', 'w') as output_file:
        output_file.write("NO")
