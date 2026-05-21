// Test file for cloe-test-repo — feel free to read, edit, or delete this.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node {
    int value;
    struct Node *next;
} Node;

typedef struct {
    Node *head;
    int size;
} LinkedList;

LinkedList *list_create() {
    LinkedList *list = malloc(sizeof(LinkedList));
    list->head = NULL;
    list->size = 0;
    return list;
}

void list_push_front(LinkedList *list, int value) {
    Node *node = malloc(sizeof(Node));
    node->value = value;
    node->next = list->head;
    list->head = node;
    list->size++;
}

void list_push_back(LinkedList *list, int value) {
    Node *node = malloc(sizeof(Node));
    node->value = value;
    node->next = NULL;
    if (!list->head) {
        list->head = node;
    } else {
        Node *cur = list->head;
        while (cur->next) cur = cur->next;
        cur->next = node;
    }
    list->size++;
}

int list_pop_front(LinkedList *list) {
    if (!list->head) return -1;
    Node *tmp = list->head;
    int val = tmp->value;
    list->head = tmp->next;
    free(tmp);
    list->size--;
    return val;
}

void list_reverse(LinkedList *list) {
    Node *prev = NULL, *cur = list->head, *next = NULL;
    while (cur) {
        next = cur->next;
        cur->next = prev;
        prev = cur;
        cur = next;
    }
    list->head = prev;
}

void list_print(LinkedList *list) {
    Node *cur = list->head;
    printf("[");
    while (cur) {
        printf("%d", cur->value);
        if (cur->next) printf(", ");
        cur = cur->next;
    }
    printf("] (size: %d)\n", list->size);
}

void list_free(LinkedList *list) {
    Node *cur = list->head;
    while (cur) {
        Node *next = cur->next;
        free(cur);
        cur = next;
    }
    free(list);
}

int main() {
    LinkedList *list = list_create();

    for (int i = 1; i <= 5; i++) list_push_back(list, i * 10);
    list_push_front(list, 5);
    list_print(list);

    list_reverse(list);
    list_print(list);

    printf("Popped: %d\n", list_pop_front(list));
    list_print(list);

    list_free(list);
    return 0;
}
