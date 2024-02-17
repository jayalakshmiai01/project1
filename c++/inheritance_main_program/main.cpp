#include <iostream>

using namespace std;
class parentbird
{
private:
    string color;
int weight;
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
        cout << "setcolor is:" ;
        cin >> color;
    }
    string getcolor()
    {
      return color;
    }
    void setweight()
    {
        cout << "setweight is :" << endl;
        cin >> weight;
    }
    int getweight()
    {
        return weight;
    }
};
    class childbird : public parentbird{

        public:

        void birdsound()
        {
            cout << "i can sing" << endl;
        }

    };
class grandchildbird : public childbird{

};
class parrot : public parentbird{
  public:

        void birdsound()
        {
            cout << "i can mow" << endl;
        }

};
int main()
{

    /*cout << "parentbird output:" << endl;
   parentbird pb;
    pb.setcolor();
    pb.myweight();
    pb.eat();

    cout << "color is:" << pb.getcolor() << endl;
    cout << pb.birdname() << endl;
    //cout << bs.mycolor() << endl;
    cout << pb.myweight() << endl;



   /* if(bs.myweight()==25)
    {
    cout << "return type is equal to 25" << endl;
    }*/

    cout << "this output is childbird class" << endl;

childbird cb;

cb.setcolor();
cb.getweight();
cb.eat();
cb.birdsound();
    cout << "color is:" << cb.getcolor() << endl;
    cout << "weight is:" << cb.getweight() << endl;
    return 0;

cout << "this output is grandchilbird class" << endl;



grandchildbird gb;

gb.setcolor();
gb.getweight();
gb.eat();
gb.birdsound();
    cout << "color is:" << gb.getcolor() << endl;
    cout << "weight is:" << gb.getweight() << endl;
    return 0;



parrot p;

p.setcolor();
p.getweight();
p.eat();
p.birdsound();
    cout << "color is:" << p.getcolor() << endl;
    cout << "weight is:" << p.getweight() << endl;
    return 0;
}
