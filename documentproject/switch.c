#include<stdio.h>
int switch1()
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

