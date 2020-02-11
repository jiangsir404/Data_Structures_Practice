[TOC]
Referer:
- 线性结构-栈和队列 https://www.shiyanlou.com/courses/20/labs/104/document/

## 基础

定义
: 首先我们来讲讲栈，栈是只能在表尾进行插入或删除操作的线性表，通常我们称表尾端为`栈顶`，表头端为`栈底`，它是一种`先进后出`的线性表，既只能在表尾端插入元素，称为`入栈`，也只能在表尾端删除元素，称为`退栈`

## 栈的存储结构

栈既可以用数组来实现，也可以用链表来实现。用数组实现的栈，我们叫作顺序栈，用链表实现的栈，我们叫作链式栈

> 栈需要关注入栈push的栈满条件和出栈pop时的栈空条件。

### java
java版本的顺序栈:
```

// 基于数组实现的顺序栈
public class ArrayStack {
  private String[] items;  // 数组
  private int count;       // 栈中元素个数
  private int n;           //栈的大小

  // 初始化数组，申请一个大小为n的数组空间
  public ArrayStack(int n) {
    this.items = new String[n];
    this.n = n;
    this.count = 0;
  }

  // 入栈操作
  public boolean push(String item) {
    // 数组空间不够了，直接返回false，入栈失败。
    if (count == n) return false;
    // 将item放到下标为count的位置，并且count加一
    items[count] = item;
    ++count;
    return true;
  }
  
  // 出栈操作
  public String pop() {
    // 栈为空，则直接返回null
    if (count == 0) return null;
    // 返回下标为count-1的数组元素，并且栈中元素个数count减一
    String tmp = items[count-1];
    --count;
    return tmp;
  }
}
```


### c/c++
2. c版本实现的链式栈，使用两个栈指针分别指向栈尾和栈顶来实现。这块复杂，栈满时该程序还会申请一个更大的空间，实现动态扩容。

```
typedef int SElemType;
typedef int Status;

typedef struct
{
	SElemType *base;//栈尾指针 
	SElemType*top;//栈顶指针
	int size; //栈的大小 
}SqStack;

Status InitStack(SqStack*S)
{
	S->base=(SElemType*)malloc(INIT_SIZE*sizeof(SElemType));
	if(!S->base)
	{
		exit(OVERFLOW);
	}
	S->top=S->base;
	S->size=INIT_SIZE;
	return OK;
}
//压栈，插入元素e为新的栈顶元素 

Status Push(SqStack *S,SElemType e)
{
    //栈满条件
	if((S->top-S->base)/sizeof(SElemType)>=S->size)
	{
		S->base=(SElemType*)realloc(S->base,(S->size+INCREMENT_SIZE)*sizeof(SElemType));//不用malloc，因为malloc是创建新的空间，而relloc是追加空间 
		if(!S->base)//分配失败 
		{
			exit(OVERFLOW);
		}
		S->top=S->base+S->size;//让top指针指向栈顶 
		S->size+=INCREMENT_SIZE;
	}
	*S->top=e;
	S->top++;//添加元素后栈顶指针就要指向下一个位置 
	return OK;
}

//退栈:若栈不为空，则删除S的栈顶元素，用e返回其值，并返回OK，否则返回ERROR; 
Status Pop(SqStack *S,SElemType*e)
{
    //栈空条件
	if(S->top==S->base)
	{
		return ERROR;
	}
	S->top--;//让top指针指向栈顶元素 
	*e=*S->top;//取出栈顶元素 
	return OK;
}
```

### python


时间复杂度分析:
不管是顺序栈还是链式栈，入栈、出栈只涉及栈顶个别数据的操作，所以时间复杂度都是 O(1)。

## 栈的应用
### 函数调用栈
系统的函数调用栈时物理存在的结构，数据结构的栈只是一种抽象的数据结构，但都满足先进后出的特点，再x86的机器上，栈时从高地址往低地址增长的。

如下demo: 
```

int main() {
   int a = 1; 
   int ret = 0;
   int res = 0;
   ret = add(3, 5);
   res = a + ret;
   printf("%d", res);
   reuturn 0;
}

int add(int x, int y) {
   int sum = 0;
   sum = x + y;
   return sum;
}
```
函数调用栈如下图(下面是高地址)
![image](8DD3FF84DEC8439CA73760449A6963FD)
大致过程:
```
参数入栈：将参数从右向左依次压入系统栈中
返回地址入栈：将当前代码区调用指令的下一条指令地址压入栈中，供函数返回时继续执行
代码区跳转：处理器从当前代码区跳转到被调用函数的入口处
栈帧调整：
    具体包括保存当前栈帧状态值，已备后面恢复本栈帧时使用（EBP入栈）
    将当前栈帧切换到新栈帧。（将ESP值装入EBP，更新栈帧底部）
    局部变量入栈,esp减小

恢复的过程就是现弹出栈帧(pop ebp),这样就可以恢复出调用函数的栈帧了，此时栈顶会指向返回地址,再将返回地址弹出(pop eip),并保存到eip中，之后就会回到原来调用函数的下一条地址继续运行了。
```

### 括号匹配的检验
检验圆括号和方括号是否正确匹配。

我们用栈来保存未匹配的左括号，从左到右依次扫描字符串。当扫描到左括号时，则将其压入栈中；当扫描到右括号时，从栈顶取出一个左括号。如果能够匹配，比如“(”跟“)”匹配，“[”跟“]”匹配，“{”跟“}”匹配，则继续扫描剩下的字符串。如果扫描的过程中，遇到不能配对的右括号，或者栈中没有数据，则说明为非法格式。当所有的括号都扫描完成之后，如果栈为空，则说明字符串为合法格式；否则，说明有未匹配的左括号，为非法格式。

### 表达式求值
比如`34+13*9+44-12/3`,编译器只需要通过两个栈来实现，一个保存运算符的栈，另一个保存操作数的栈。从左到右遍历表达式，遇到操作数，就压入操作数栈，遇到运算符，就与运算符栈的栈顶元素进行比较:
1. 如何比运算符栈顶元素的优先级高，就将当前运算符压入栈
2. 如果比运算符栈顶元素的优先级低或者相同，从运算符栈中取栈顶运算符，从操作数栈顶取2个操作符，然后计算后把计算结果压入操作数栈，继续比较。

![image](438CDBF23BDF4F0CBF4495FC47F2042F)


## 完整应用程序

1. c语言版
```
#include<stdio.h>
#include<stdlib.h> 

#define TRUE 1
#define FALSE 0
#define OK 1
#define ERROR 0
#define OVERFLOW -2
#define INIT_SIZE 20
#define INCREMENT_SIZE 5

typedef int SElemType;
typedef int Status;

typedef struct
{
	SElemType *base;//栈尾指针 
	SElemType*top;//栈顶指针
	int size; //栈的大小 
}SqStack;

Status InitStack(SqStack*S)
{
	S->base=(SElemType*)malloc(INIT_SIZE*sizeof(SElemType));
	if(!S->base)
	{
		exit(OVERFLOW);
	}
	S->top=S->base;
	S->size=INIT_SIZE;
	return OK;
}

Status DestroyStack(SqStack*S)
{
	free(S->base);//只是释放掉S->base指向的空间 
	S->base=NULL; //base的值为空，则表明栈结构不存在 
	S->top=NULL; //初始化线性表是已将S-top=S-base，故不用再释放掉S-top的空间 
	S->size=0;
	return OK;
}

Status ClearStack(SqStack *S) 
{
	S->top=S->base; //让栈顶的指针指向栈尾，可作为栈空的标记 
	return OK;
}

Status IsEmpty(SqStack S)
{
	if(S.top==S.base)//top==base可作为栈空的标记 
	{
		return TRUE;
	}
	else return FALSE;
}

int GetLength(SqStack S){
	return (S.top-S.base);
}

Status GetTop(SqStack S,SElemType *e)
{
	if(S.top>S.base)//即栈不为空的意思 
	{
		*e=*(--S.top); //取栈顶元素,栈顶指针指向的是栈顶元素的下一个位置 
		return OK;
	}
	else
	{
		return ERROR;
	}
}

//压栈，插入元素e为新的栈顶元素 

Status Push(SqStack *S,SElemType e)
{
	if((S->top-S->base)/sizeof(SElemType)>=S->size)//栈满，追加 存储空间 
	{
		S->base=(SElemType*)realloc(S->base,(S->size+INCREMENT_SIZE)*sizeof(SElemType));//不用malloc，因为malloc是创建新的空间，而relloc是追加空间 
		if(!S->base)//分配失败 
		{
			exit(OVERFLOW);
		}
		S->top=S->base+S->size;//让top指针指向栈顶 
		S->size+=INCREMENT_SIZE;
	}
	*S->top=e;
	S->top++;//添加元素后栈顶指针就要指向下一个位置 
	return OK;
}

//退栈:若栈不为空，则删除S的栈顶元素，用e返回其值，并返回OK，否则返回ERROR; 
Status Pop(SqStack *S,SElemType*e)
{
	if(S->top==S->base)//如果栈为空 
	{
		return ERROR;
	}
	S->top--;//让top指针指向栈顶元素 
	*e=*S->top;//取出栈顶元素 
	return OK;
}

void visit(SElemType e)
{
	printf("%d ",e);
}

Status TraverseStack(SqStack S,void(*visit)(SElemType))
{
	while(S.top>S.base)//条件是栈不为空 
	{
		visit(*S.base);
		S.base++;
	}
	return OK;
}
int main(){
	SqStack S;
	if(InitStack(&S)) 
	{
		SElemType e;
		int i;
		printf("init_success\n");
		if(IsEmpty(S))
		{
			printf("Stack is empty\n");
		}
		for(i=0;i<10;i++){
			Push(&S,i);
		}
		GetTop(S,&e);
		printf("The first element is %d\n",e);
		printf("length is %d\n",GetLength(S));
		Pop(&S,&e);
		printf("Pop element is %d\n",e);
		TraverseStack(S,*visit);
		
		if(DestroyStack(&S))
		{
			printf("\ndestroy_success\n");
		 } 
	}
	return 0;
}

```