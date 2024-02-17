#include<stdio.h>
struct myvalue
 {
     int s1,s2,s3;

 };
int main()
{
    int a,b;
    a=2;
    b=4;
    printf("The value of a is%d\n",a);
    printf("The value of b is%d\n",b);
    //addition(a,b);
    //subtraction(a,b);
    //multiplication(a,b);
    //divition(a,b);
    //modulas(a,b);
    //increment();
    //decrement();
    //assaingment(a,b);
    //relational(a,b);
    //forloopprogram();
    //switchprogram();
    //ifprogram();
    //nestedloopprogram();
    structureprogram();




}

int addition(int a,int b)
  {

    int c;
    printf("\n...ADDITION...\n");
    c=a+b;
    printf("\naddition value is:\n",c);
    return 0;
  }

  int subtraction(int a,int b)
{

    int c;
    printf("\n...SUBTRACTION...\n");
    c=a-b;
    printf("\nThe subtraction value is%d\n",c);
    return 0;

}

int multiplication(int a,int b)
{
    int c;
    printf("\n...multiplication...\n");
    c=a*b;
    printf("\nThe multiply value is%d\n",c);
    return 0;
    }

int divition(int a,int b)
{
    float c;
    printf("\n...........divition...........\n");
    c=(float)a/b;
    printf("\nThe divition value is%d\n",c);
    return 0;

}
int modulas(int a,int b)
{


    int c;
    printf("\n...........Modulas............\n");
    c=a%b;
    printf("\nThe modulas value is%d\n",c);
    return 0;

}

int increment()
{
    int i=1;
    while(i<5)
        {
    printf("\n.........INCREMENT..........\n");
    printf("\nThe increment value is%d\n",i);
    ++i;}

}

int decrement()
{
    int i=7;
    do
        {
         printf("\n.............DECREMENT............\n");
         printf("\nThe decrement value is%d\n",i);
         i--;
         }
         while(i>5);
        return 0;
}
int assaingment(int a, int b)
          {
printf("..........assaignment...........");
              a+=b;
              printf("A:%d",a);
              a-=b;
              printf("B:%d",a);

              return 0;

          }
 int relational(int a,int b)
{
    printf(".........relational.........");
    printf("greater value is %d",a>b);
    printf("\n less than value is %d",a<b);
    printf("\n greater than or equal is %d",a>=b);
    printf("\n lessthan or equal is %d",a<=b);
    printf("\n equal value is %d",a==b);
    printf("\n notequal value is %d",a!=b);
    return 0;
}
int forloopprogram()
{

    int i,n;
    printf("\n enter the limit:");
    scanf("%d",&n);
    for(i=1;i<=n;i+=2)
    {
        printf("\n%d",i);
            }
            return 0;

    }

    int switchprogram()
{
    int ch;
    printf("\n enter the value:");
    scanf("%d",&ch);
    switch(ch)
    {
    case 1:
        printf("\n one");
        break;
    case 2:
        printf("\n two");
        break;
    case 3:
        printf("\n three");
        break;
    default:
        printf("\n invalid number");
        break;
    }
    return 0;
    }

int ifprogram()
{
    int mark;
    printf("\n Enter the marks:");
    scanf("%d",&mark);
    if("mark>=35")
    {
        printf("\n you are pass for the exam");
    }
    return 0;
}

int elseifprogram()
{
    int mark;
    printf("\n Enter the marks:");
    scanf("%d",&mark);
    if(mark>=35)
    {
        printf("\n you are pass for the exam");
    }
    else
    {
        printf("you are not pass for exam");
    }
    return 0;

}

int nestedloopprogram()
{
    int i,j;
    for(i=0;i<5;i++)
    {
        for(j=0;j<5;j++)
        {
            printf("*");
        }
        printf("\n");
    }
    return 0;
}
int structureprogram()
{
    struct myvalue
    s1,s2,s3;
    scanf("%d",&s1.a);
    scanf("%d",&s2.a);
    s3.a=s1.a+s2.a;
    printf("\n added value is:\n");
    return 0;
}


