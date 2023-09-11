#include"lists.h"
/**
 * is_palindrome - Check if a singly linked list is a palindrome
 * @head: Pointer to a pointer to the head of the linked list
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	const listint_t *current;
	int n = 0, j, i = 0, a;
	int arr[1024];

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	current = *head;

	while (current != NULL)
	{
		arr[n] = current->n;
		current = current->next;
		n++;
	}
	n--;
	a = n / 2;
	for (j = n; i < a; i++, j--)
{
		if (arr[i] != arr[j])
		{
			return (0);
		}
	}
	return (1);
}
