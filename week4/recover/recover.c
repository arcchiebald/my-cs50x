#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        printf("Usage ./recover [file]\n");
        return 1;
    }
    FILE *src = fopen(argv[1], "r");
    unsigned char *buffer = malloc(512);
    int photoNum = 0;
    char *fName = malloc(3 * sizeof(int));

    if (buffer == NULL)
    {
        return 1;
    }

    while (fread(buffer, sizeof(unsigned char), 512, src) == 512)
    {
        // If fread sees a header of JPG file:
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            sprintf(fName, "%03i.jpg", photoNum);
            FILE *image = fopen(fName, "w");
            fwrite(buffer, 1, 512, image);
            fclose(image);
            photoNum++;
        }
        else if (photoNum != 0)
        {
            FILE *image = fopen(fName, "a");
            fwrite(buffer, 1, 512, image);
            fclose(image);
        }
    }
    fclose(src);
    free(buffer);
    free(fName);
    exit(0);
}
