#include <iostream>

using namespace std;
class birds
{
private:
    string color;
string weight;
public:
    void eat()
    {
        cout << "i can eat" << endl;

    }
     string birdname()
    {

        string name = "rose";
        return name;

    }
    /*string mycolor()
    {
        string color = "red";
        return color;
    }*/



    void setcolor()
    {
        cout << "setcolor is:" << endl;
        cin >> color;
    }
    string getcolor()
    {
      return color;
    }
    void setweight()
    {
        cout << "setweight is" << endl;
        cin >> weight;
    }
    int getweight()
    {
        return weight;
    }
};
    class dog : public birds{
    };

int main()
{
   /* birds bs;
    bs.eat();
    cout << bs.birdname() << endl;
    //cout << bs.mycolor() << endl;
    cout << bs.myweight() << endl;
    bs.myweight1();
    bs.setcolor();
    cout << "color is:" << bs.getcolor() << endl;

    if(bs.myweight()==25)
    {
    cout << "return type is equal to 25" << endl;
    }*/
dog dg;
dg.setcolor();
dg.getweight();
dg.eat();
    cout << "color is:" << dg.getcolor() << endl;
    cout << "weight is:" << dg.getweight() << endl;
    return 0;
}
