#include "main.h"
/**
 * _isdigit - checks for a digit (0 through 9).
 * @c: The character to be checked
 * Return: 1  if c is a digit and 0 otherwise
 */
int _isdigit(int c)
{
	if (c >= 48 && c < 58)
		return (1);
	else
		return (0);

}