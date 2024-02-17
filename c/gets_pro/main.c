#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
    int x;
    char str[20];

    printf("enter the x value :\n");
    scanf("%d");
    printf("enter the string:");
    gets(str);
    printf("%s",str);

    return 0;
}
