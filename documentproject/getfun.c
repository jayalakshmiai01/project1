#include<stdio.h>

int fun()
 {

add(getA(),getB());
sub(getA(),getB());
return 0;
 }
 int getA()
    {
      int a;
    printf("Enter the value : \n");
     scanf("%d",&a);
     return a;
     }
     int getB()
    {
      int b;
    printf("Enter the value : \n");
     scanf("%d",&b);
     return b;}

 int add(int y,int x)
 {
     int z=x+y;
     printf("The value of  Z is :%d\n",z);
 }
  int sub(int y,int x)
 {
     int z=x-y;
     printf("The value of  Z is : %d\n",z);
     return 0;
 }


