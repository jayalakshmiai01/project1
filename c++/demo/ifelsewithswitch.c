#include<stdio.h>
int ifswitchprogram()
{
    int a;
    int b;
    int c;
    int d;
    int e;
    printf("\tEnter the value :  \n\t");
    scanf("%d",&a);
    if(a==2)
    {
        printf("Enter the 1st value : \n");
        scanf("%d",&b);
         printf("Enter the 2nd value : \n");
        scanf("%d",&c);
        printf("Enter the operator: \n");
        scanf("%d",&e);
        switch(e)
        {
        case 1:
    printf("The added value : %d \n\t",b+c);
            break;
            case 2:
    printf("The added value : %d \n\t",b-c);
            break;
        }
    }
    else
    {
        printf("Enter the 1st value : \n");
        scanf("%d",&b);
         printf("Enter the 2nd value : \n");
        scanf("%d",&c);
         printf("Enter the 3nd value : \n");
        scanf("%d",&d);
        printf("Enter the operator: \n");
        scanf("%d",&e);
        switch(e)
        {
        case 1:
    printf("The added value : %d \n\t",b+c+d);
            break;
        case 2:
    printf("The added value : %d \n\t",b*c*d);
            break;
        }
    }
    }