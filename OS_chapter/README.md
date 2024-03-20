## CPU의 구성요소 ALU, CU, Register 의 역할
 ### ALU (Arithmetic and logical unit)
   > 산술연산과 논리연산을 수행하는 역할
 ### CU (Control unit)
   > CPU에 일을 시키기 위해 실행파일에 저장되어 있는 명령어들을 해석해주는 역할
 ### Register
 - Register 는 CPU 내에 존재하는 아주 작은 메모리 공간
    ALU 가 일을 하고 있는동안 다른 명령들을 처리할 수 없기에 Register 에 저장
    - 프로그램 카운터 (Program Counter): 
        메모리에서 가져다가 실행할 다음영역의 주소를 일시적으로 저장하는 레지스터
        (지금 ALU 에서 작업 1 실행중 다음에 실행할 작업의 메모리 주소를 일시적으로 저장하는 역할)
    - 인스트럭션 레지스터 (Instruction Register): 
        방금전에 메모리에서 가져와서 이제 해석해야되는 명령어를 저장하는 레지스터
        (프로그램 카운터가 가리키는 메모리 주소에 있는 데이터(명령어)를 저장하는 역할)
    - 어드레스 레지스터:
        메모리의 주소를 저장하는 레지스터, CPU 가 읽어 들이고자 하는 주소값을 어드레스 버스에 보낼때 거치는 레지스터
    - 버퍼 레지스터:
        메모리에 읽거나 쓰려는 데이터나 명령어를 일시적으로 저장하는 레지스터
        (데이터를 읽고 쓴다 = 데이터를 주고받는다 이때 데이터를 바로 전달 되는게 아니고 전달하기 위해 대기하는 상태가 있다
        이때 버퍼링이라는 과정이 필요한데 이 버퍼링을 위해 사용되는 레지스터)
    - 플래그 레지스터:
        연산겨로가 또는 CPU 상태에 대한 부가적인 정보를 저장하는 레지스터
    - 스택 포인터:
        스택의 꼭대기를 가리키는 레지스터 
        <스택 : 지역변수나 매개변수를 저장하기위한 메모리 영역의 공간>
        (이 스택에서 다음 꺼내 써야 할 것이 어느 곳에 있는지 가리키는 것)

## 메인 메모리와 보조기억장치의 차이
### 메인 메모리
  - 보통 주기억 장치 또는 RAM (Random Access Memory) 이 메인 메모리에 포함되고 처리 속도가 빠르며 프로그램 및 데이터를 일시적으로 저장할 수 있는 공간이다
    하지만 휘발성이여서 전원이 꺼지면 데이터가 날아가버린다.
### 보조 기억장치
  - 보통 하드 디스크(HDD), SSD 등 이 포함되고 메인 메모리에 비해 용량이 크면서 속도가 느리다.
    프로그램 및 데이터를 장기적으로 저장할 수 있는 공간이며 비휘발성이라 전원이 꺼져도 데이터가 날아가지 않는다.


### 버스 시스템은 데이터를 주고받기위한 경로로, 데이터 종류에 따른 세가지 버스시스템
 - 데이터 버스: 데이터 이동을 위해 필요한 버스
    일반적으로 CPU 와 메인메모리 사이에서 데이터를 주고받을 때 사용된다.
 - 컨트롤 버스: CPU 가 원하는 바를 메모리에 전달하기위한 버스
    CPU 와 다른 하드웨어 장치들이 서로 제어 신호를 주고 받을 때 사용된다.
 - 어드레스 버스: 주소값을 참조하기 위해 주소값 이동을 위해 필요한 버스
    일반적으로 CPU 가 메인 메모리나 입출력 장치와 같은 외부 장치로의 주소 정보를 주고 받을 떄 사용된다.

## 식사하는 철학자
>다섯 명의 철학자가 하나의 원탁에 앉아 식사를 한다. 각각의 철학자들 사이에는 포크가 하나씩 있고, 앞에는 접시가 있다. 접시 안에 든 요리는 포크를 두개 사용하여 먹어야만 하는 스파게티 이다. 그리고 각각의 철학자는 다른 철학자에게 말을 할 수 없으며, 번갈아가며 각자 식사하거나 생각하는 것만 가능하다. 따라서 식사를 하기 위해서는 왼쪽과 오른쪽의 인접한 철학자가 모두 식사를 하지 않고 생각하고 있어야만 한다. 또한 식사를 마치고 나면, 왼손과 오른손에 든 포크를 다른 철학자가 쓸 수 있도록 내려놓아야 한다. 이 때, 어떤 철학자도 굶지 않고 식사할 수 있도록 하는 방법은 무엇인가?

위의 조건으로 보면 식사중 교착 상태(데드락)이 발생할 가능성이 있다.
스파게티를 먹기위한 자원이 포크라고 할 때, 철학자들은 프로세스(스레드) 가 되고 이 프로세스들을 실행하기 위해 필요한 자원의 수는 2개 이다.

각 프로세스마다 1개의 자원을 점유하고 대기하게 되면 서로 꼬리에 꼬리를 물고 누구도 실행되지 못하고 무기한 대기 하게 된다.
이렇게 되면 이러지도 저러지도 못하는 상황이 오게 된다.

이 상황을 해결 하는 방법은 애초에 자원을 2개 사용할 수 있는 상황이 아니라면 자원을 하나도 점유하지 않는 방법도 있다.
이렇게 되면 자원이 5개, 프로세스가 5개라 할때, 5개의 프로세스중 2개의 프로세스가 실행되고 나머지 프로세스는 기다렸다가
이전 프로세스들이 실행 종료되면 실행할 수 있다.


## 스래싱 (thrashing)
동시에 실행되는 프로세스의 수가 늘어나게 되면 어느 순간부터 page fault 가 자주 발생하게 되고
page fault 가 진행 될때는 cpu 가 아무것도 하지 않아서 cpu 사용률이 떨어지게 된다.

이 때, 운영체제는 cpu 사용률이 떨어진것만 보고 cpu 가 놀고 있다고 판단하여 더 많은 프로세스들을 메모리에 올리려하고
이렇게 되면 page fault 가 더 자주 발생하게 되고 다시 또 cpu 사용률이 떨어지고 더 많은 프로세스들을 메모리에 올리려하고 하는 
악순환이 발생된다.

이러한 현상을 스래싱이라 한다.

## 워킹셋 (Working Set)
운영체제가 메모리를 관리 할 때 지역성을 활용하는 것을 말한다. 운영체제는 프로세스가 필요한 전체 메모리를 할당하는 것이 아니고 일부만 할당하는데, 지역성을 잘 고려해서 가장 많이 사용하는 페이지를 미리 working set 으로 구별하고 그 working set 을 메모리에 할당한다.

이 때 working set 의 구간을 working set window 라 한다. working set window 의 값은 working set 을 이루는 페이지의 갯수에 따라 달라진다. 페이지 갯수가 3개 이면 working set window 는 3이 된다

전체 메모리 참조가 아니라 지정한 구간만큼의 내용만을 working set window 로 정의하고 이를 계속 이동해가면서 working set 내용을 변경시키는 구조이다.
이렇게 하면 working set 에는 현재 프로세스가 실행될 때 필요한 지역성에 해당하는 페아자들만 들어있기 때문에 page fault 를 최소화 할 수 있다.

page fault 는 working set window 가 이동할때만 발생한다.

## 연결리스트 (Linked List)
연결리스트는 여러 요소들이 서로 연결되어 있는 데이터 구조를 말한다. 
각 요소는 데이터를 저장하는 노드로 구성되어있고, 노드는 데이터 필드와 다음 노드를 가리키는 링크(포인터)로 이루어져 있다.

- 장점 삽입과 삭제가 빠르다
  특히 단일 연결리스트에서는 리스트의 중간에 삽입 이나 삭제 할때 삽입될 노드가 가리키는 노드를 앞의 노드로, 뒤의 노드가 가리키는 노드를 삽입될 노드로 주소 변경해 주면 끝이다.
  동적으로 크기가 조절될 수 있다. 즉, 실행 시간에 요소를 추가하거나 제거할 수 있다.

- 임의에 요소에 접근하는 것이 오래걸린다.
  인덱스처럼 바로 접근하는 것이아니라 맨 처음 요소부터 주소를 찾아가기 때문에 오래걸린다.
  포인터를 저장하는 메모리 공간을 추가로 할당해야 하기 때문에 기존의 배열같은 자료구조 보다 더 많은 공간을 차지한다.

* 단일 연결리스트
```
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
```

* 이중 연결 리스트
```
// 이중 연결 리스트
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 노드 구조체 정의
typedef struct Node {
    char *data;
    struct Node *prev;
    struct Node *next;
} node;

// 새로운 노드 생성
struct Node* createNode(node **head_ref, char *str_data) {
    // 노드 생성
    node* newNode = (node*)malloc(sizeof(node));
    newNode->data = strdup(str_data);
    newNode->next = *head_ref;

    // 이전 노드를 NULL로 설정
    newNode->prev = NULL;

    // 현재 헤드가 NULL이 아니면, 현재 헤드의 이전 노드를 새로운 노드로 설정
    if (*head_ref != NULL)
        (*head_ref)->prev = newNode;

    // 헤드를 새로운 노드로 업데이트
    *head_ref = newNode;
}

int main() {
    // 연결 리스트 생성 및 초기화
    node *head = NULL;

    createNode(&head, "Head");
    createNode(&head, "Apple");
    createNode(&head, "Banana");

    // 연결 리스트 출력
    printf("이중 연결 리스트: ");
    while (head != NULL) {
        printf("%s ", head->data);
        head = head->next;
    }
    printf("\n");

    return 0;
}
```

* 원형 연결 리스트
```
// 원형 연결 리스트
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 노드 구조체 정의
typedef struct Node {
    char *data;
    struct Node *next;
} node;

// 새로운 노드 생성
node* createNode(node **head_ref, char *str_data) {
    // 노드 생성
    node* newNode = (node*)malloc(sizeof(node));
    newNode->data = strdup(str_data);
    newNode->next = NULL;

    // 헤드가 NULL인 경우, 새로운 노드를 가리키게 함
    if (*head_ref == NULL) {
        newNode->next = newNode;
        *head_ref = newNode;
    } else {
        // 헤드가 NULL이 아닌 경우, 새로운 노드를 헤드의 다음 노드로 삽입
        newNode->next = (*head_ref)->next;
        (*head_ref)->next = newNode;
    }
}

int main() {
    // 연결 리스트 생성 및 초기화
    node *head = NULL;

    createNode(&head, "Head");
    createNode(&head, "Apple");
    createNode(&head, "Banana");

    // 연결 리스트 출력
    printf("원형 연결 리스트: ");
    node* temp = head;
    if (head != NULL) {
        do {
            printf("%s ", temp->data);
            temp = temp->next;
        } while (temp != head);
    }
    printf("\n");ß

    return 0;
}
```