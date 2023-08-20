# Generating a multiplication table using nested loops

# Outer loop for rows (multiplicands)
for i in range(1, 11):
    # Inner loop for columns (multipliers)
    for j in range(1, 11):
        # Calculate the product
        product = i * j
        
        # Formatting the output
        print(f"{i} * {j} = {product}\t", end="")
    
    # Move to the next line after each row is complete
    print()
