#include <math.h>
#include "helpers.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // Declaring a variable to store average color
    int avgColor;
    // For every row of pixels (i):
    for (int i = 0; i < height; i++)
    {
        // For every pixel (j):
        for (int j = 0; j < width; j++)
        {
            avgColor = (int) round((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0);
            image[i][j].rgbtBlue = avgColor;
            image[i][j].rgbtGreen = avgColor;
            image[i][j].rgbtRed = avgColor;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    int originalRed, originalGreen, originalBlue;
    int sepiaRGB[3];
    // For each row of pixels (i):
    for (int i = 0; i < height; i++)
    {
        // For each pixel (j):
        for (int j = 0; j < width; j++)
        {
            originalRed = image[i][j].rgbtRed;
            originalGreen = image[i][j].rgbtGreen;
            originalBlue = image[i][j].rgbtBlue;

            // Calculate the sepia-pixel color
            sepiaRGB[0] = round(.393 * originalRed + .769 * originalGreen + .189 * originalBlue);
            sepiaRGB[1] = round(.349 * originalRed + .686 * originalGreen + .168 * originalBlue);
            sepiaRGB[2] = round(.272 * originalRed + .534 * originalGreen + .131 * originalBlue);

            // For each sepia-color:
            for (int s = 0; s < 3; s++)
            {
                // If one of the RGB parameters exceed 255:
                if (sepiaRGB[s] > 255)
                {
                    sepiaRGB[s] = 255;
                }
            }

            // Apply the filter to each pixel
            image[i][j].rgbtRed = sepiaRGB[0];
            image[i][j].rgbtGreen = sepiaRGB[1];
            image[i][j].rgbtBlue = sepiaRGB[2];
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // Declaring a rgbtriple variable to temporarily store pixel
    RGBTRIPLE tempPix[width];
    // For every row of pixels (i):
    for (int i = 0; i < height; i++)
    {
        // Implementing a for loop in order to temporarily store the original row of pixels.
        for (int k = 0; k < width; k++)
        {
            tempPix[k] = image[i][k];
        }
        // For every pixel (j):
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed = tempPix[(width - 1) - j].rgbtRed;
            image[i][j].rgbtGreen = tempPix[(width - 1) - j].rgbtGreen;
            image[i][j].rgbtBlue = tempPix[(width - 1) - j].rgbtBlue;

        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Declare a variable to store original image:
    RGBTRIPLE tempImg[height][width];
    // Implementing for loop to copy image to temporary variable:
    for (int m = 0; m < height; m++)
    {
        for (int l = 0; l < width; l++)
        {
            tempImg[m][l] = image[m][l];
        }
    }
    // For every row of pixels (i):
    for (int i = 0; i < height; i++)
    {
        // For every pixel (j):
        for (int j = 0; j < width; j++)
        {
            // Reset all variables for the new pixel:
            int countedPixels = 0;
            float sumofRed = 0;
            float sumofGreen = 0;
            float sumofBlue = 0;

            // Creating for loop in order to access all the adjacent pixels:
            for (int ic = -1; ic < 2; ic++)
            {
                for (int jc = -1; jc < 2; jc++)
                {
                    // If pixel is not on the border of the image:
                    if (i + ic < 0 || i + ic >= height)
                    {
                        continue;
                    }
                    if (j + jc < 0 || j + jc >= width)
                    {
                        continue;
                    }
                    // Calculate sum of every color
                    sumofRed += tempImg[i + ic][j + jc].rgbtRed;
                    sumofBlue += tempImg[i + ic][j + jc].rgbtBlue;
                    sumofGreen += tempImg[i + ic][j + jc].rgbtGreen;
                    countedPixels++;
                }
            }

            image[i][j].rgbtRed = (int) round(sumofRed / countedPixels);
            image[i][j].rgbtGreen = (int) round(sumofGreen / countedPixels);
            image[i][j].rgbtBlue = (int) round(sumofBlue / countedPixels);
        }
    }
    return;
}
