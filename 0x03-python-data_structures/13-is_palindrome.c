#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to the head of the linked list.
 * Return: 0 if not a palindrome, 1 if a palindrome.
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow, *fast, *prev_slow, *mid;
    int is_palindrome = 1;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    /* Find the middle of the linked list */
    slow = *head;
    fast = *head;
    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev_slow = slow;
        slow = slow->next;
    }

    /* Reverse the second half of the linked list */
    mid = slow;
    if (fast != NULL)
        slow = slow->next;
    prev_slow->next = NULL;
    reverse_list(&slow);

    /* Compare the first half and reversed second half */
    while (*head != NULL && slow != NULL)
    {
        if ((*head)->n != slow->n)
        {
            is_palindrome = 0;
            break;
        }
        *head = (*head)->next;
        slow = slow->next;
    }

    /* Restore the original linked list */
    reverse_list(&mid);
    prev_slow->next = mid;

    return is_palindrome;
}

/**
 * reverse_list - Reverses a linked list.
 * @head: Pointer to the head of the linked list.
 */
void reverse_list(listint_t **head)
{
    listint_t *prev = NULL;
    listint_t *current = *head;
    listint_t *next = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head = prev;
}
