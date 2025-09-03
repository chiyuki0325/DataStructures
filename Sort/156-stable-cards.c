#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 结构体定义
typedef struct Card {
    char color; int value;
} Card;

typedef struct Stack {
    int cursor; char* values;
} Stack;

void inputCard(Card* card) {
    scanf(" %c%d", &card->color, &card->value);
}

void printCard(Card* card) {
    printf("%c%d ", card->color, card->value);
}


void swap(Card* a, Card* b) {
    Card tmp = *a;
    *a = *b;
    *b = tmp;
}

void bubbleSort(int len, Card* cards) {
    for (int i=0; i<len-1; i++) {
        for (int j=0; j<len-1-i; j++) {
            if (cards[j].value > cards[j+1].value) {
                swap(&cards[j], &cards[j+1]);
            }
        }
    }
}

void selectionSort(int len, Card* cards) {
    for (int i=0; i<len; i++) {
        int minIdx=i;
        for (int j=i; j<len; j++) {
            if (cards[j].value<cards[minIdx].value) minIdx=j;
        }
        if (minIdx!=i) swap(&cards[i], &cards[minIdx]);
    }
}

void pushStack(Stack* stack, char value) {
    stack->values[stack->cursor]=value;
    stack->cursor++;
}

char popStack(Stack* stack) {
    stack->cursor--;
    return stack->values[stack->cursor];
}

Stack* makeStacks(int len, Card* cards) {
    Stack* stacks = malloc(sizeof(Stack)*9);
    for (int i=0; i<9; i++) {
        stacks[i].cursor=0;
        stacks[i].values = malloc(sizeof(char)*len);
    }
    for (int i=0; i<len; i++) {
        pushStack(&stacks[cards[i].value-1], cards[i].color);
    }
    return stacks;
}

void compareCards(int len, Stack* oriStacks, Card* new) {
    Stack* newStacks = makeStacks(len, new);
    for (int i=0; i<9; i++) {
        if (oriStacks[i].cursor!=newStacks[i].cursor) {
            printf("Cursor mismatch\n");
            return;
        }
        while (oriStacks[i].cursor>0) {
            char a=popStack(&oriStacks[i]);
            char b=popStack(&newStacks[i]);
            if (a!=b) {
                printf("Not stable\n");
                return;
            }
        }
    }
    printf("Stable\n");
}

int main() {
    // 输入
    int len; scanf("%d", &len);
    Card* cards = malloc(sizeof(Card)*len);
    for (int i=0; i<len; i++) {
        inputCard(cards+i);
    }

    Card* ori = malloc(sizeof(Card)*len);
    memcpy(ori, cards, sizeof(Card)*len);
    Stack* oriStacks = makeStacks(len, ori);
    Stack* oriStacks2 = malloc(sizeof(Stack)*9);
    memcpy(oriStacks2, oriStacks, sizeof(Stack)*9);

    bubbleSort(len, cards);
    for (int i=0; i<len; i++) {
        printCard(cards+i);
    }
    printf("\n");
    compareCards(len, oriStacks, cards);

    memcpy(cards, ori, sizeof(Card)*len);

    selectionSort(len, cards);
    for (int i=0; i<len; i++) {
        printCard(cards+i);
    }
    printf("\n");
    compareCards(len, oriStacks2, cards);

    return 0;
}
