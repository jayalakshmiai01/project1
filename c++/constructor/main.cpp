/*#include <iostream>

using namespace std;
class subject
{
private:
    int a,b,c;
    string name;
public:
    void integer()
    {
       a=1;
       b=4;
       cout << "enter the integer number:" << endl;
    }
    string name()
    {
       string name = abi
        cout << "enter the name:" << endl;
    }
};
int main()
{
    subject s;
    s.integer();
    s.name();
    return 0;
}
*/
#include <iostream>

using namespace std;
class room
{
private:
    int length;
    int breath;
public:
     room(int l,int b)
    {
        length = l;
        breath = b;
    }
    int getlength()
    {
        return length;
    }
    int getbreath()
    {
        return breath;
    }
    int calculatearea()
    {
        return length * breath;
    }
};
int main()
{
    room r(10,15);

   // cout << "length of r" << r.getlength() << endl;
   // cout << "breath of r" << r.getbreath() << endl;
    cout << "area is" << r.calculatearea() << endl;
    return 0;
}

