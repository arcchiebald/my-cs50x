// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 676;
unsigned int wrdCount = 0;
unsigned int hashNum = 0;
// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    hashNum = hash(word);
    node *current = table[hashNum];
    while (current != NULL)
    {
        if (strcasecmp(current->word, word) == 0)
        {
            return true;
        }
        current = current->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    if (word[1] != '\0')
    {
        return ((toupper(word[0]) - 65) * 26) + (toupper(word[1]) - 65);
    }
    else
    {
        return ((toupper(word[0]) - 65) * 26);
    }
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *dict = fopen(dictionary, "r");
    char wrd[LENGTH + 1];
    unsigned int index = 0;
    if (dict == NULL)
    {
        fclose(dict);
        return false;
    }
    else if (dict != NULL)
    {
        while (fscanf(dict, "%s", wrd) != EOF)
        {
            node *newWord = malloc(sizeof(node));
            index = hash(wrd);
            strcpy(newWord->word, wrd);
            newWord->next = table[index];
            table[index] = newWord;
            wrdCount++;
        }
        fclose(dict);
        return true;
    }
    fclose(dict);
    return false;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return wrdCount;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < 676; i++)
    {
        node *row = table[i];

        while (row != NULL)
        {
            node *temp = row;
            row = row->next;
            free(temp);
        }
    }
    return true;
}
