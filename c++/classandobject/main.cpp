#include <iostream>

using namespace std;
class myfirstclass
{
public:
    int a =10;
    void multiply()
    {
    int x,y;
    cin>>x>>y;
    cout<<(x*y);
    }
};
int addition ()

{
    int a,b;
    cin>>a>>b;
    a=a+b;
    cout<<a;

}
int main()
{
    addition();
    myfirstclass mfc;
    cout << mfc.a;
    mfc.multiply();
    return 0;
}

