#include<iostream>
using namespace std;
//  Function Overloading
int sum(int a,int b)
{
    return a+b;
}
int sum(int a,int b,int c)
{
    return a+b+c;
}
float sum(float a,float b)
{
    return a+b;
}
int main()
{
    cout<<"Total : "<<sum(10,20)<<endl;
    cout<<"Total : "<<sum(10,20,30)<<endl;
    cout<<"Total : "<<sum(10.25f,25.10f)<<endl;
    return 0;
}
