#include <iostream>

using namespace std;
class room
{
public:
    int length;
    int breath;

    int calculatearea()
    {
        return length * breath;
    }

};
int main()
{
room r;
r.length = 10;
r.breath = 20;
cout << "area is" << r.calculatearea() << endl;
    return 0;
}
