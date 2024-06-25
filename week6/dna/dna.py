import csv
import sys


def main():

    # TODO: Check for command-line usage
    if not len(sys.argv) == 3:
        exit("Usage: python dna.py [csv-file] [txt-file]")

    csvFile = sys.argv[1]
    txtFile = sys.argv[2]

    # TODO: Read database file into a variable
    dBase = []
    with open(f"{csvFile}", 'r') as file:
        reader = csv.DictReader(file)
        for name in reader:
            dBase.append(name)

    # TODO: Read DNA sequence file into a variable
    with open(f"{txtFile}", 'r') as txtFile:
        sequence = txtFile.readline()
    # TODO: Find longest match of each STR in DNA sequence
    strArray = list(dBase[0].keys())[1:]
    strRuns = {}
    for str in strArray:
        strRuns[str] = longest_match(sequence, strArray[strArray.index(str)])
    # TODO: Check database for matching profiles
    isMatch = False
    for person in dBase:
        count = 0
        for str in strArray:
            if int(person[str]) == int(strRuns[str]):
                count += 1
                if count == len(strArray):
                    break
        if count == len(strArray):
            print(f"{person['name']}")
            isMatch = True
            break
    if not isMatch:
        print("No Match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
