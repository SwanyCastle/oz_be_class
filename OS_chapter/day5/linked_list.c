// 단일 연결 리스트
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 노드 구조체 정의
typedef struct Node {
    char *data;
    struct Node *next;
} node;


// 새로운 노드 생성
struct Node* createNode(node **head_ref, char *str_data) {
    // 노드 생성
    node* newNode = (node*)malloc(sizeof(node));
    newNode->data = strdup(str_data);
    newNode->next = *head_ref;
    *head_ref = newNode;
}

int main() {
    // 연결 리스트 생성 및 초기화
    node *head = NULL;

    createNode(&head, "Head");
    createNode(&head, "Apple");
    createNode(&head, "Banana");

    // 연결 리스트 출력
    printf("단일 연결 리스트: ");
    while (head != NULL) {
        printf("%s ", head->data);
        head = head->next;
    }
    printf("\n");

    return 0;
}

// // 이중 연결 리스트
// #include <stdio.h>
// #include <stdlib.h>
// #include <string.h>

// // 노드 구조체 정의
// typedef struct Node {
//     char *data;
//     struct Node *prev;
//     struct Node *next;
// } node;

// // 새로운 노드 생성
// struct Node* createNode(node **head_ref, char *str_data) {
//     // 노드 생성
//     node* newNode = (node*)malloc(sizeof(node));
//     newNode->data = strdup(str_data);
//     newNode->next = *head_ref;

//     // 이전 노드를 NULL로 설정
//     newNode->prev = NULL;

//     // 현재 헤드가 NULL이 아니면, 현재 헤드의 이전 노드를 새로운 노드로 설정
//     if (*head_ref != NULL)
//         (*head_ref)->prev = newNode;

//     // 헤드를 새로운 노드로 업데이트
//     *head_ref = newNode;
// }

// int main() {
//     // 연결 리스트 생성 및 초기화
//     node *head = NULL;

//     createNode(&head, "Head");
//     createNode(&head, "Apple");
//     createNode(&head, "Banana");

//     // 연결 리스트 출력
//     printf("이중 연결 리스트: ");
//     while (head != NULL) {
//         printf("%s ", head->data);
//         head = head->next;
//     }
//     printf("\n");

//     return 0;
// }


// // 원형 연결 리스트
// #include <stdio.h>
// #include <stdlib.h>
// #include <string.h>

// // 노드 구조체 정의
// typedef struct Node {
//     char *data;
//     struct Node *next;
// } node;

// // 새로운 노드 생성
// node* createNode(node **head_ref, char *str_data) {
//     // 노드 생성
//     node* newNode = (node*)malloc(sizeof(node));
//     newNode->data = strdup(str_data);
//     newNode->next = NULL;

//     // 헤드가 NULL인 경우, 새로운 노드를 가리키게 함
//     if (*head_ref == NULL) {
//         newNode->next = newNode;
//         *head_ref = newNode;
//     } else {
//         // 헤드가 NULL이 아닌 경우, 새로운 노드를 헤드의 다음 노드로 삽입
//         newNode->next = (*head_ref)->next;
//         (*head_ref)->next = newNode;
//     }
// }

// int main() {
//     // 연결 리스트 생성 및 초기화
//     node *head = NULL;

//     createNode(&head, "Head");
//     createNode(&head, "Apple");
//     createNode(&head, "Banana");

//     // 연결 리스트 출력
//     printf("원형 연결 리스트: ");
//     node* temp = head;
//     if (head != NULL) {
//         do {
//             printf("%s ", temp->data);
//             temp = temp->next;
//         } while (temp != head);
//     }
//     printf("\n");ß

//     return 0;
// }