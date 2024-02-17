
#include<iostream>
using namespace std;
class funoverloading
{
public:
    void addition()
    {
    int a=10,b=20c;
    c=a+b;
    cout << c;
}

     void additionf()
     {
    float a=10.5f,b=20.5f,c;
    c=a+b;
    cout << c;
     }

};
int main()
{
    funoverloading ad;
    ad.addition();
    ad.additionf();
    return 0;

}
