#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <strings.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    char *name;
    int votes;
}
candidate;


// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(char *name);
void print_winner(void);

int main(int argc, char *argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }
    

    int voter_count = 0;
    printf("Number of voters: ");
    scanf("%d", &voter_count);

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        char *name;
        printf("Vote: ");
        scanf("%s", name);

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
bool vote(char *name)
{
    // For every element of 'candidates' array:
    for (int i = 0; i < candidate_count; i++)
    {
        // If typed name matches names of the candidates:
        if (strcmp(name, candidates[i].name) == 0)
        {
            candidates[i].votes++;
            return true;
        }
    }
    return false;
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    // Declaring a variable to store highest votes.
    int highest_votes = 0;
    // For every candidate:
    for (int i = 0; i < candidate_count; i++)
    {
        // If candidate's vote count exceeds 'highest_votes':
        if (candidates[i].votes > highest_votes)
        {
            // Update 'highest_votes' variable.
            highest_votes = candidates[i].votes;
        }
    }
    // Lastly, print the winner(s) whose votes amount is equal to 'highest_votes'
    for (int j = 0; j < candidate_count; j++)
    {
        if (candidates[j].votes == highest_votes)
        {
            printf("%s\n", candidates[j].name);
        }
    }
    return;
}