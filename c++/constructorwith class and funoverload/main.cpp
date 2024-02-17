#include<iostream>
using namespace std;
class student
{
    int rno;
    char name[50];
    double fees;
    public:
    student()
    {
        cout<<"Enter the RollNo:";
        cin>>rno;
        cout<<"Enter the Name:";
        cin>>name;
        cout<<"Enter the Fees:";
        cin>>fees;
    }



    void display()
    {
        cout<<endl<<rno<<"\t"<<name<<"\t"<<fees;
    }
};

int main()
{
    student s;
    s.display();
    return 0;

}


/*#include <iostream>
using namespace std;

class constructor {
public:
    int a, b;


    constructor()
    {
        a = 10;
        b = 20;
    }
};

int main()
{
     constructor c;

    cout << "a: " << c.a << endl << "b: " << c.b;
    return 0;
} */


/*#include<iostream>
using namespace std;
class function
{

function()
{
    int a;
    cin >> a;
    cout << "enter the value" <<a << endl;
}
function()
{
    int a,b;
    cin >> a,b;
    cout << "enter the value" << a,b << endl;
}
};
 int main()
 function fun;*/



