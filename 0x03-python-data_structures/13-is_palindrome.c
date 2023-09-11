#include"lists.h"

intis_palindrome(listint_t **head)
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
