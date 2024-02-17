#include <iostream>

using namespace std;

int main()
{

    int value1,value2,total,op;
    cout<<"enter value :";
    cin>>value1;
    cout<<"enter value :";
    cin>>value2;
    cout<<"enter operator";
    cin>>(op);
    switch(op)
    {
case 1:
    total=value1+value2;
    cout<<"\n added value of a and b \n "<<total;
    break;
case 2:
    total=value1-value2;
    cout<<"\n subtracted value of a and b \n "<<total;
    break;
case 3:
    total=value1*value2;
    cout<<"\n multiplied value of a and b \n "<<total;
    break;
case 4:
    total=value1/value2;
    cout<<"\n divided value of a and b \n "<<total;
    break;
case 5:
    total=value1%value2;
    cout<<"\n modulus value of a and b \n "<<total;
    break;
    case 6:
    value1++;
    cout<<"\n postincrement value of  \n "<<value1;
    break;
    case 7:
     ++value1;
    cout<<"\n preincrement value of \n "<<value1;
    break;
    }
    return 0;
}











