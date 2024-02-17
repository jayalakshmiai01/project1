#include <iostream>

using namespace std;

int main()
{
    int m;

    cout << "enter the months (1-5)"<< endl;
    cin >> m;
    switch(m)
    {
    case 1:
        cout << "january" << endl;
        break;
    case 2:
        cout << "february" << endl;
        break;
    case 3:
        cout << "march" << endl;
        break;
    case 4:
        cout << "april" << endl;
        break;
    case 5:
        cout << "may" << endl;
        break;
    default:
        cout << "invalid month" << endl;

    }
    return 0;
}
