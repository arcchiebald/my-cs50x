import cs50


def main():
    text = cs50.get_string("Enter a text: ")

    grade = coleman(text)

    if grade < 1:
        print("Before Grade 1")
    elif grade > 16:
        print("Grade 16+")
    else:
        print(f"Grade {round(grade)}")


def coleman(text):
    # Letters count
    letterCount = 0
    for char in text:
        if char.isalpha():
            letterCount += 1
    # Words count
    words = len(text.split())
    # Sentences count
    sentences = 0
    for letter in text:
        if letter == "." or letter == "?" or letter == "!":
            sentences += 1
    # Average variables
    avg100letters = letterCount / words * 100
    avg100sentences = sentences / words * 100
    # Coleman index
    colemanIndex = 0.0588 * avg100letters - 0.296 * avg100sentences - 15.8
    return colemanIndex


if __name__ == "__main__":
    main()