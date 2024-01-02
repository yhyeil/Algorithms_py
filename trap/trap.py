def minimum_damage(n, k, traps):
    # Compute the net saving for each trap if jumped over
    potential_savings = [(a_i - (n - i - 1), i) for i, a_i in enumerate(traps)]
    
    # Sort potential savings in descending order
    potential_savings.sort(reverse=True)

    # Indices of the traps we'll jump over
    jump_indices = set([idx for _, idx in potential_savings[:k]])

    # Compute the total damage
    total_damage = 0
    bonus_damage = 0  # Accumulated bonus damage due to jumps
    
    for i, a_i in enumerate(traps):
        if i in jump_indices:
            bonus_damage += 1  # Jumping over the trap increases bonus damage
        else:
            total_damage += a_i + bonus_damage  # Base damage + bonus damage

    return total_damage

# Read input from file
with open("input.txt", "r") as f:
    n, k = map(int, f.readline().strip().split())
    traps = list(map(int, f.readline().strip().split()))
    damage = minimum_damage(n, k, traps)

    # Write output to file
    with open("output.txt", "w") as out:
        out.write(str(damage))
