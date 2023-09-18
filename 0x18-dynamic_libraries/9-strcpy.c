#include "main.h"
/**
 * *_strcpy - a function that copies the string pointed to by src
 * @dest: copy to
 * @src: copy from
 * Return: string
 */

char *_strcpy(char *dest, char *src)
{
	int i, l = 0;

	while (*src != '\0')
	{
		l++;
		src++;
	}
	src = src - l;

	for (i = 0; i <= l; i++)
	{

		*(dest + i) = *(src + i);

	}

	return (dest);
}