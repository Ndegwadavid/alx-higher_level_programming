#include <stdlib.h>

/**
 * struct listint_s - singlry linked ltists
 * @n: integer
 * @next: defines that it will point to the next node 
 *
 * Description: singly linked list node structure
 * for alc holberton project.
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer to the head of the list
 * @number: number to stat whtih
 *
 * Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node, *current_node, *prev_node;

    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return (NULL);

    new_node->n = number;
    new_node->next = NULL;

    if (*head == NULL)
    {
        *head = new_node;
        return (new_node);
    }

    current_node = *head;
    prev_node = NULL;

    while (current_node != NULL && current_node->n < number)
    {
        prev_node = current_node;
        current_node = current_node->next;
    }

    if (prev_node == NULL)
    {
        new_node->next = current_node;
        *head = new_node;
    }
    else
    {
        new_node->next = current_node;
        prev_node->next = new_node;
    }

    return (new_node);
}