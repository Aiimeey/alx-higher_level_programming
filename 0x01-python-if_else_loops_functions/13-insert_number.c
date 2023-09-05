#include "lists.h"
#include <stddef.h>
#include <stdlib.h>
#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new, *current, *prev;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = number;
    new->next = NULL;

    current = *head;
    prev = NULL;

    while (current && number > current->n)
    {
        prev = current;
        current = current->next;
    }

    if (prev == NULL)
    {
        new->next = *head;
        *head = new;
    }
    else
    {
        prev->next = new;
        new->next = current;
    }

    return (new);
}
