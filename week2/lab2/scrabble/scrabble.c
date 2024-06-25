#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // Combination of several if statements to decide the winner.
    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score1 < score2)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

// Function to compute the score:
int compute_score(string word)
{
    // Declaring a variable to store the score:
    int score = 0;
    // For every character in the given string:
    for (int i = 0; i < strlen(word); i++)
    {
        // If character is LOWERCASE letter:
        if (islower(word[i]))
        {
            // Creating for loop to identify letter.
            for (int j = 97; j < 123; j++)
            {
                if ((int)word[i] == j)
                {
                    score += POINTS[j - 97];
                }
            }
        }
        // If character is UPPERCASE letter:
        else if (isupper(word[i]))
        {
            // Creating for loop to identify letter.
            for (int k = 65; k < 90; k++)
            {
                if ((int)word[i] == k)
                {
                    score += POINTS[k - 65];
                }
            }
        }
    }
    return score;
}
