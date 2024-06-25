# TODO

while True:
    try:
        height = int(input("Enter a height: "))
    except ValueError:
        print("That's not an integer.")
    else:
        if height > 0 and height < 9:
            break

# For every row
for row in range(1, height + 1):
    # Add blank spaces
    for blank in range(height-row):
        print(" ", end="")
    # Print first part of pyramid
    for prt1 in range(row):
        print("#", end="")
    # Print two blank spaces
    print("  ", end="")
    # Print second part of pyramid
    for prt1 in range(row):
        print("#", end="")
    # After row is finished, go to newline
    print("")
