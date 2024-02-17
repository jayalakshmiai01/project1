#include <stdio.h>
int main()
{
    int a,b,c;
    scanf("%d",&a);
    scanf("%d",&b);

     additionprogram(a,b);
     subtractionprogram(a,b);
     multiplicationprogram(a,b);
     divisionprogram(a,b);
     modulasprogram(a,b);
     incrementprogram(a,b);
     decrementprogram(a,b);
     logicalprogram(a,b);
     comparisonprogram(a,b);
     assignmentprogram(a,b);
     return 0;
}

     int additionprogram(int a,int b)
    {
      int c= a+b;
      printf("\n Added value is......%d\n",c);
    }
    int subtractionprogram(int a,int b)
    {

    int c = a-b;
    printf("\n subtracted value is.......%d\n",c);
    }
    int multiplicationprogram(int a,int b)
    {

        int c= a*b;
        printf("\n multiplied value is.......%d\n",c);
    }
    int divisionprogram(int a, int b)
    {
        float c= (float)a/b;
        printf("\n divided value is..........%f\n",c);
    }
    int modulasprogram(int a,int b)
    {
        int c = a%b;
        printf("\n modules value is......... %d\n",c);
    }
    int incrementprogram(int a)
    {
       while(a<20)
    {
        printf(" \n a value is.....%d\n",a);
        a++;
    }
    }
    int decrementprogram(int b)
    {
     while(b>5)
    {
        printf(" \n a value is.....%d\n",b);
        b--;
    }
    }
    int logicalprogram(int a,int b)

    {
        if(!(a<10 && b<20))
           {
               additionprogram(a,b);
           }
            else if(a<10 || b<20)
            {
                subtractionprogram(a,b);
            }
            else
            {

            printf("a and b value is .....%d\n",(a<10 && b<20));

           }
    }
    int comparisonprogram(int a,int b)
        {
            printf("\t\n*****comparison values*****");
            printf("\n %d",a == b);
            printf("\n %d",a!= b);
            printf("\n %d",a > b);
            printf("\n %d",a < b);
            printf("\n %d",a >= b);
            printf("\n %d",a <= b);

        }
        int assignmentprogram(int a,int b)
        {
            printf("\t\n******assining values*******");
            printf("\n %d",a = 5);
            printf("\n %d",a += b);
            printf("\n %d",a -= b);
            printf("\n %d",a *= b);
            printf("\n %d",a /= b);
            printf("\n %d",a &= b);
            printf("\n %d",a |= b);
            printf("\n %d",a ^= b);
            printf("\n %d",a >>= b);
            printf("\n %d",a <<= b);



        }
