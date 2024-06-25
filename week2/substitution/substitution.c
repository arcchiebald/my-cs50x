#include <cs50.h>
#include <ctype.h>
#include <string.h>
#include <stdio.h>

void substitute(string text, string key);

int main(int argc, string argv[])
{
    // Checking the case, if user types no input, to exit program and
    // avoid segmentation fault(which occurs when we are accessing argv[1] further,
    // which will be undefined, if user types no command-line argument)
    if (argc < 2)
    {
        return 1;
    }

    // Checking if key consists only of letters, otherwise execution stops.
    for (int i = 0; i < strlen(argv[1]); i++)
    {
        if ((int) isalpha(argv[1][i]) == 0)
        {
            printf("Usage: ./substitution key\n");
            return 1;
        }
        for (int u = i + 1; u <= strlen(argv[1]); u++)
        {
            if (argv[1][i] == argv[1][u])
            {
                printf("Usage: ./substitution key\n");
                return 1;
            }
        }
    }
    // If user types more than one command-line argument, or does not type any, then abort the program.
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    } // If key is does not consist of 26 letters, abort further execution of the program.
    else if (strlen(argv[1]) != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }
    // Prompting user to enter plain text, which will be eventually encrypted using the key above.
    string plain = get_string("plaintext: ");
    printf("ciphertext: ");
    substitute(plain, argv[1]);
    return 0;
}


void substitute(string text, string key)
{
    // For every character in the plain text:
    for (int k = 0; k < strlen(text); k++)
    {
        if (islower(text[k]))
        {
            // For every possible lowercase letter in this particular position:
            for (int j = 97; j <= 122; j++)
            {
                if ((int) text[k] == j)
                {
                    printf("%c", tolower(key[j - 97]));
                }
            }
        }
        else if (isupper(text[k]))
        {
            // For every possible uppercase letter in this particular position:
            for (int m = 65; m <= 90; m++)
            {
                if ((int) text[k] == m)
                {
                    printf("%c", toupper(key[m - 65]));
                }
            }
        }
        else // Non-letter characters will be ignored and printed untouched.
        {
            printf("%c", text[k]);
        }
    }
    printf("\n");
}