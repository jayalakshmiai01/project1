#include <iostream>

using namespace std;
class cars
{
public:
    string brand = "nissan";
    void messageprint()
    {

        cout<<"welcome to nissan:" << endl;
            }
};
class cartype
{
public:
    string cartypename="nissansuv";
    void messageprintfor()
    {
        cout << " welcome to nissansuv"<< endl;

    }
};
class nissansuv : public cars, public cartype
{

};

int main()
{
nissansuv ns;
ns. messageprint();
ns.messageprintfor();

    return 0;
}
