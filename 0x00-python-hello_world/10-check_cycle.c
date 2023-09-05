#include "lists.h"
/**
 * check_cycle - Checks if a linked list has a cycle
 * @list: A pointer to the head of the linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *ptr1 = list;
	listint_t *ptr2 = list;

	if (!list)
		return (0);

	while (ptr2 && ptr2->next)
	{
		ptr1 = ptr1->next;
		ptr2 = ptr2->next->next;

		if (ptr1 == ptr2)
			return (1);
	}

	return (0);
}
