#include "main.h"
/**
 * _atoi - convert a string to an integer.
 * @s: string
 * Return: int
 */
int _atoi(char *s)
{
	int sign = 1;
	int num = 0;

	while (*s != '\0')
	{
		if (*s == '-')
		{
			sign = sign * -1;
		}
		if (*s >= '0' && *s <= '9')
		{
			num = num * 10 + (*s - '0');
		}
		else if (*s < '0' || *s > '9')
		{
			if (num != 0)
			{
				break;
			}
		}

		s++;
	}

	return (sign * num);
}