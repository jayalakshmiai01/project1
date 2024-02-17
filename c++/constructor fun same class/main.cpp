#include <iostream>

using namespace std;

class student
{
    public:
        student()
        {
        string name;
        int m1,m2,m3;
        float avg;

        cout << "enter the name:" << endl;
        cin >> name;
        cout <<"enter the marks:"<< endl;
        cin >> m1>>m2>>m3;
        avg=(m1+m2+m3)/3;
        cout << "enter the avg :" << avg << endl;
        }
        };

class display
{
public:
    void getdata()
    {
        int a, b;
        cin >> a;
        cin >> b;
        cout << "total:" << a+b<< endl;
    }
    int sum(int a, int b, int c)
    {
    cout << "total:" << a+b+c << endl;
    }
    float sum(float a, float b)
    {
    cout << "total:"<< a+b << endl;
    }

    };

int main()
{
    student o;
    display d;
    d.getdata();
    return 0;
}
