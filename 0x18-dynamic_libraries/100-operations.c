#include <stdio.h>
/**
* add - function that returns the sum of a and b
* @a: integer number
* @b: integer number
* Return: sum of a and b
*/
int add(int a, int b)
{
	return (a + b);
}
/**
* sub - function that returns the difference of a and b
* @a: integer number
* @b: integer number
* Return: difference of a and b
*/
int sub(int a, int b)
{
	return (a - b);
}
/**
* mul - function that returns the product of a and b
* @a: integer number
* @b: integer number
* Return: product of a and b
*/
int mul(int a, int b)
{
	return (a * b);
}
/**
* div - function that returns the result of the division of a by b
* @a: integer number
* @b: integer number
* Return: division of a by b
*/
int div(int a, int b)
{
	if (b != 0)
		return (a / b);
	else
		return (0);
}

/**
* mod - function that returns the remainder of the division of a by b
* @a: integer number
* @b: integer number
* Return: remainder of division of a by b
*/
int mod(int a, int b)
{
	if (b != 0)
		return (a % b);
	else
		return (0);
}
