#ifndef LISTS_H
#define LISTS_H

/* Structure for a singly linked list node */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

/* Function prototypes */
int is_palindrome(listint_t **head);
void reverse_list(listint_t **head);

#endif
