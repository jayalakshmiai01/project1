#include <iostream>

using namespace std;
class MyFirstClass
{

public:
    void division();
    void modulus();

    int addition()
    {
        int a,b;
        cout<<"\n addition";
        cout<<"\n enter the value a:";
        cin>>a;
        cout<<"enter the value b:";
        cin>>b;
        cout<< "addition is :";
        cout<< (a+b);

    }
    int subtraction()
    {
        int a,b;
        cout<<"\n subtraction";
        cout<<"\n enter the value a:";
        cout<<a;
        cout<<"\n enter the value b:";
        cout<<b;
        cout<<"subtracted is";
        cout<< (a-b);

    }
    int multiplication()
    {
        int a,b;
        cout<<"\n multiplication";
        cout<<"\n enter the value a:";
        cout<<a;
        cout<<"\n enter the value b:";
        cout<<b;
        cout<<"multiplied is";
        cout<< (a*b);

    }
};
    void MyFirstClass::division()

      {

        int a,b;
        cout<<"\n division";
        cout<<"\n enter the value a:";
        cout<<a;
        cout<<"\n enter the value b:";
        cout<<b;
        cout<<"divided is";
        cout<< (a/b);

    }
    void MyFirstClass::modulus()

     {

       int a,b;
        cout<<"\n modulus";
        cout<<"\n enter the value a:";
        cout<<a;
        cout<<"\n enter the value b:";
        cout<<b;
        cout<<"modulus is";
        cout<< (a%b);

}
int main()
{

    MyFirstClass MFC;

    MFC.addition();
    MFC.subtraction();
    MFC.multiplication();
    MFC.division();
    MFC.modulus ();
    return 0;
}


