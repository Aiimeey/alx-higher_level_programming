#include "main.h"
/**
 * _puts - prints a string
 * @str: string
 */

void _puts(char *str)
{
	int l = 0, i;

	while (*str != '\0')
	{
		str++;
		l++;

	}
	str = str - l;

	for (i = 0; i < l; i++)
	{
		_putchar (*str);
		str++;
	}
	_putchar('\n');
}