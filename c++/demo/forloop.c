#include<stdio.h>
void forloop()
{
    int i,n;
    printf("\n enter the limit:");
    scanf("%d",&n);
    for(i=1;i<=n;i+=2)
    {
        printf("\n%d",i);
    }
}
    