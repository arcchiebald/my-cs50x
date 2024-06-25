#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <string.h>
#include <stdio.h>

// Function declarations.
int count_letters(string sample_text);
int count_words(string sample_text);
int count_sentences(string sample_text);

int main(void)
{
    // Prompting an user for a text input.
    string text = get_string("Enter a text: ");

    // Counting average letters and sentences per 100 words(L/W and S/W both multiplied by 100)
    float average100_letters = (count_letters(text) / (float) count_words(text)) * 100;
    float average100_sentences = count_sentences(text) / (float) count_words(text) * 100;


    // Declaring 'index' variable in order to store grade number.
    float index = 0.0588 * average100_letters - 0.296 * average100_sentences - 15.8;

    // If index is less than 1
    if (index < 1)
    {
        // Print following:
        printf("Before Grade 1\n");
    }
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", (int) round(index));
    }
}




// Function for counting letters in a sentence.
int count_letters(string sample_text)
{
    // Declaring a variable to store letters sum.
    int letters_count = 0;

    // Introducing a for loop to check every character of given text.
    for (int i = 0; i < strlen(sample_text); i++)
    {
        // If character is a letter(upper- or lowercase):
        if (islower(sample_text[i]) || isupper(sample_text[i]))
        {
            // Increase 'letters_count' variable by 1.
            letters_count++;
        }
    }
    // Finally, returning amount of letters in a variable after checking the text with for loop.
    return letters_count;
}




// Function for counting words in a sentence.
int count_words(string sample_text)
{
    // Declaring a variable in order to store words count.
    int words_count = 1;

    // Introducing a for loop to go through every character of text.
    for (int j = 0; j < strlen(sample_text); j++)
    {
        // If there is a space character in text and it is surrounded with non-blank characters:
        if (sample_text[j] == ' ' && sample_text[j - 1] != ' ' && sample_text[j - 1] != ' ')
        {
            // Increase 'words_count' by 1.
            words_count++;
        }
    }
    // Lastly, returning amount of words to a variable.
    return words_count;
}




// Function for counting words in a sentence.
int count_sentences(string sample_text)
{
    // Declaring a variable in order to store words count.
    int sentences_count = 0;

    // Introducing a for loop to go through every character of text.
    for (int k = 0; k < strlen(sample_text); k++)
    {
        // If there is a dot character in the text:
        if (sample_text[k] == '.' || sample_text[k] == '?' || sample_text[k] == '!')
        {
            // Increase 'sentences_count' by 1.
            sentences_count++;
        }
    }
    // Lastly, returning amount of sentences to a variable.
    return sentences_count;
}