#include "main.h"
/**
 * _strncat - concatenate two strings
 * using at most n bytes from src
 * @dest: input value
 * @src: input value
 * @n: input value
 *
 * Return: dest
 */

char *_strncat(char *dest, char *src, int n)
{
	int  i = 0, j = 0;

	while (*(dest + i) != '\0')
	{
		i++;
	}


	while (*(src + j) != '\0' && n > j)
	{
		*(dest + i + j) = *(src + j);
		j++;
	}


	*(dest + i + j) = '\0';

	return (dest);
}