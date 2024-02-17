#include <iostream>

using namespace std;
class room
{
private:
    int length;
    int breath;
public:
    void setlengthbreath(int l,int b)
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
    room r;
    r.setlengthbreath(10,5);
    cout << "length of r" << r.getlength() << endl;
    cout << "breath of r" << r.getbreath() << endl;
    cout << "area is" << r.calculatearea() << endl;
    return 0;
}

