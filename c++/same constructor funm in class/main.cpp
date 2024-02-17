#include <iostream>

using namespace std;
class accessspecifier
{
private:
    int b=10;
protected:
    int pc=250;
public:
    int a,c;
    void sumb()
    {
        c=b;
        cout << c;
        c=pc;
        cout << c;
    }
};
int main()
{
    accessspecifier as;
    as.a=25;
    cout << as.a;
    as.sumb();
    return 0;
}
