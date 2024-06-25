#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;

    // Checking if height is between 1 and 8, otherwise question repeats.
    do
    {
        height = get_int("Enter a height: ");
    }
    while (((height < 1) || (height > 8)));

    // For every row, do following
    for (int row = 1; row <= height; row++)
    {
        // Add blank spaces
        for (int blank = 1; blank <= (height - row); blank++)
        {
            printf(" ");
        }
        // Add first part of the pyramid
        for (int hash1 = 1; hash1 <= row ; hash1++)
        {
            printf("#");
        }
        // Add two blank spaces to move second part of the pyramid further.
        printf(" ");
        printf(" ");

        // Add the second part of the row
        for (int hash2 = 1; hash2 <= row; hash2++)
        {
            printf("#");
        }

        // After the row is finished, go to the newline.
        printf("\n");
    }
}