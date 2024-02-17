/*
#include <iostream>

using namespace std;

int main()
{
    int a,b;
    cout << "\n enter the values A and B:" << endl;
    cin >> a >> b;
    if(a>b)
    {
        cout << a << "greater number:" << endl;
    }
     if(b>a)
    {
        cout << b << "greater number:" << endl;
    }
     if(a==b)
    {
        cout << a <<"and"<< b<< "equal number:" << endl;
    }

    return 0;
}
*/

/*#include<iostream>
using namespace std;
int main()
{
    char c;
    cout << "enter the character:"<< endl;
    cin >>c;
    if(c=='a' || c=='e' || c=='i' || c=='o' || c=='u')
    {
       cout <<" is a vowel" << endl;
    }
    else

        {
       cout <<" is not a vowel" << endl;
    }
    return 0;
}*/

#include<iostream>
using namespace std;
int main()
{
    int h,w;
    float b;
    cout << "enter the vlaues height,weight,breath:" <<endl;
    cin>>h>>w>>b;

    if(h>50 & w<1.7 & b>1500)
    {
        cout <<"grade 10"<<endl;
    }
    else
        if(h>50,w<1.7)
    {
        cout << "grade 9"<<endl;
    }
    else if(h>50,b>1500)
    {
        cout << "grade 8"<<endl;
    }
    else
    {
        cout <<"none of the above"<< endl;
    }
    return 0;
}
