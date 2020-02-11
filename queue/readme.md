[TOC]
# 队列

## 基础
1. 特点:
- 一种`先进先出`的`线性表`，只能在一端插入元素，在另一端删除元素，
- 允许插入元素的一端称为`队尾`，允许删除元素的一端称为`队头`。

2. 顺序队列和链式队列

用数组实现的队列叫作顺序队列，用链表实现的队列叫作链式队列。


java实现的顺序队列:
```

// 用数组实现的队列
public class ArrayQueue {
  // 数组：items，数组大小：n
  private String[] items;
  private int n = 0;
  // head表示队头下标，tail表示队尾下标
  private int head = 0;
  private int tail = 0;

  // 申请一个大小为capacity的数组
  public ArrayQueue(int capacity) {
    items = new String[capacity];
    n = capacity;
  }

  // 入队
  public boolean enqueue(String item) {
    // 如果tail == n 表示队列已经满了
    if (tail == n) return false;
    items[tail] = item;
    ++tail;
    return true;
  }

  // 出队
  public String dequeue() {
    // 如果head == tail 表示队列为空
    if (head == tail) return null;
    // 为了让其他语言的同学看的更加明确，把--操作放到单独一行来写了
    String ret = items[head];
    ++head;
    return ret;
  }
}
```

和顺序栈相比，顺序队列实现稍微复杂一些，顺序栈只需要一个数组下标count表示栈的大小即可，指向栈顶。而顺序队列需要两个下标分别指向队头和队尾。

3. 队满和队空的判断

队满
: 入队操作enqueue()判断队满的条件是队尾下标等于数组大小，

队空
: 出队操作dequeue()的队空的条件是队头下标等于队尾下标。

## 队列操作
### 数据搬移
![image](1963965C01DD4F18A3AF31374886EC8D)
![image](DB7A1545456E4CEFB4C858AA4BF419CE)

随着入队和出队的操作，head和tail都会持续往后移动，当 tail 移动到最右边，即使数组中还有空闲空间，也无法继续往队列中添加数据了。这时候就需要我们做数据搬移了。

出队函数dequeue()保存不变，我们只需要再入队enqueue()的时候，但tail==n的时候进行一次数据搬移操作即可。
```

   // 入队操作，将item放入队尾
  public boolean enqueue(String item) {
    // tail == n表示队列末尾没有空间了
    if (tail == n) {
      // tail ==n && head==0，表示整个队列都占满了
      if (head == 0) return false;
      // 数据搬移
      for (int i = head; i < tail; ++i) {
        items[i-head] = items[i];
      }
      // 搬移完之后重新更新head和tail
      tail -= head;
      head = 0;
    }
    
    items[tail] = item;
    ++tail;
    return true;
  }
```

### 循环队列
![image](DD7D17BFA4914B1593018D54F4643171)
![image](A34F281EF4224F868867F05193263095)

用数组实现的队列，但tail=n的是时候，会有数据搬移操作，这样入队操作性能就会收到影响，循环队列就可以解决这样的问题。

1. 特点:
- tail指向下一个元素的位置。
- 当队满时，最后一个tail是无法存储数据的，所以循环队列会浪费一个数组的存储空间。

2. 队满和队空的判断条件

队空
: tail == head 即可认为是队空

队满
: 当队满时，(tail+1)%n=head。

![image](2207D6B8CC284253AB5A5A0EF9A3147D)

## 队列应用
队列主要再多线程，线程池里面用的非常多。常见的有阻塞队列和并发队列。

### 阻塞队列
阻塞队列
: 其实就是在队列基础上增加了阻塞操作。简单来说，就是在队列为空的时候，从队头取数据会被阻塞。因为此时还没有数据可取，直到队列中有了数据才能返回；如果队列已经满了，那么插入数据的操作就会被阻塞，直到队列中有空闲位置后再插入数据，然后再返回。

阻塞队列的经典应用就是消费者-生产者模型

![image](CD05E6588D1242C881CCBA45FAD24467)

### 并发队列
线程安全的队列我们叫作并发队列。最简单直接的实现方式是直接在 enqueue()、dequeue() 方法上加锁，但是锁粒度大并发度会比较低，同一时刻仅允许一个存或者取操作。实际上，基于数组的循环队列，利用 CAS 原子操作，可以实现非常高效的并发队列。这也是循环队列比链式队列应用更加广泛的原因

## 完整代码实现

```
#include <stdio.h>
#include <stdlib.h>

#define TRUE 1
#define FALSE 0
#define OK 1
#define ERROR 0
#define OVERFLOW -2

typedef int QElemType;
typedef int Status;

/*
 * 存储结构
 */
typedef struct QNode
{
    QElemType data;
    struct QNode *next;
}QNode, *QueuePtr;

typedef struct
{
    QueuePtr front;    //队头指针
    QueuePtr rear;    //队尾指针
}LinkQueue;

/*
 * 初始化队列
 */
Status InitQueue(LinkQueue *Q)
{
    Q->front = Q->rear = (QueuePtr) malloc(sizeof(QNode));
    if (!Q->front)
    {
        exit(OVERFLOW);
    }
    Q->front->next = NULL;
    return OK;
}

/*
 * 销毁队列
 */
Status DestroyQueue(LinkQueue *Q)
{
    while (Q->front)
    {
        Q->rear = Q->front->next;
        free(Q->front);
        Q->front = Q->rear;
    }
    return OK;
}

/*
 * 清空队列
 */
Status ClearQueue(LinkQueue *Q)
{
    DestroyQueue(Q);
    InitQueue(Q);
}

/*
 * 判断队列是否为空
 */
Status IsEmpty(LinkQueue Q)
{
    if (Q.front->next == NULL)
    {
        return TRUE;
    }
    else
    {
        return FALSE;
    }
}

/*
 * 获取队列的长度
 */
int GetLength(LinkQueue Q)
{
    int i = 0;
    QueuePtr p = Q.front;
    while (Q.rear != p)
    {
        i++;
        p = p->next;
    }
    return i;
}

/*
 * 获取队头元素
 */
Status GetHead(LinkQueue Q, QElemType *e)
{
    QueuePtr p;
    if (Q.front == Q.rear)
    {
        return ERROR;
    }
    p = Q.front->next;
    *e = p->data;
    return OK;
}

/*
 * 入队
 */
Status EnQueue(LinkQueue *Q, QElemType e)
{
    QueuePtr p = (QueuePtr) malloc(sizeof(QNode));
    if (!p)
    {
        exit(OVERFLOW);
    }
    p->data = e;
    p->next = NULL;
    Q->rear->next = p;
    Q->rear = p;
    return OK;
}

/*
 * 出队
 */
Status DeQueue(LinkQueue *Q, QElemType *e)
{
    QueuePtr p;
    if (Q->front == Q->rear)
    {
        return ERROR;
    }
    p = Q->front->next;
    *e = p->data;
    Q->front->next = p->next;
    if (Q->rear == p)
    {
        Q->rear = Q->front;
    }
    free(p);
    return OK;
}

/*
 * 访问元素
 */
void visit(QElemType e)
{
    printf("%d ", e);
}

/*
 * 遍历队列
 */
Status TraverseQueue(LinkQueue Q, void (*visit)(QElemType))
{
    QueuePtr p = Q.front->next;
    while (p)
    {
        visit(p->data);
        p = p->next;
    }
    return OK;
}

int main()
{
    LinkQueue Q;
    if (InitQueue(&Q))
    {
        QElemType e;
        int i;

        printf("init_success\n");

        if (IsEmpty(Q))
        {
            printf("queue is empty\n");
        }

        for (i = 0; i < 10; i++)
        {
            EnQueue(&Q, i);
        }

        GetHead(Q, &e);
        printf("The first element is %d\n", e);

        printf("length is %d\n", GetLength(Q));

        DeQueue(&Q, &e);
        printf("delete element is %d\n", e);

        TraverseQueue(Q, *visit);

        if (DestroyQueue(&Q))
        {
            printf("\ndestroy_success\n");
        }
    }
}
```
