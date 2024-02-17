#include <iostream>

using namespace std;

int main()
{
    int a=10, b=20;
    printf("value of                         : %d \t \n",a);
    printf("address of a                     :%d\t\n",&a);
    printf("\n***********************************************************\n");

    printf("value of                         : %d\t\n",b);
    printf("address of b                     : %d\t\n",b);
    printf("\n***********************************************************\n");

    int *p=&a;
    printf("value of p                       :%d\t\n",p);
    printf("address of p                     :%d\t\n",&p);
    printf("value stored in the address of p : %d \t\n",*p);

    int **q=&p;
     printf("value of p                      :%d\t\n",q);
    printf("address of p                     :%d\t\n",&q);
    printf("value stored in the address of p : %d \t\n",**q);

    int ***r=&q;
    printf("value of p                       :%d\t\n",r);
    printf("address of p                     :%d\t\n",&r);
    printf("value stored in the address of p : %d \t\n",***r);

    int *s=&a;
    printf("value of p                       :%d\t\n",s);
    printf("address of p                     :%d\t\n",&s);
    printf("value stored in the address of p : %d \t\n",*(int*)s);

    return 0;
}
