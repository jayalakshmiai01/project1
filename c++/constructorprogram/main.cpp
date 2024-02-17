#include <iostream>

using namespace std;
class person
{
private:
    int id;
    string name;
public:
    void set_details()
    {
        cout << "Enter the id:" << endl;
        cin >> id;
        cout << "Enters the name:" << endl;
        cin >> name;

    }
    string get_name()
    {
        return name;
    }
    id get_id()
    {
        return name;
    }
};
class people : public person
{
    char course[50];
    int fees;
public:
    void set_datas()
    {
        cout << "enter the course:" << endl;
        cin >> course
        cout << "enter the fees:" << endl;
        cin >> fees;
    }
     string get_course()
    {
        return course;
    }
     int get_fees;
     {
         return fees;
     }
};


int main()
{
    people p;
    p.set_details()
    p.set_datas()
    cout << "\n " << p.get_name << endl;
    cout <<"\n" << p.get_id << endl;
    cout << "\n" << p.get_course << endl;
    cout << "\n" << p.get_fees << endl;
    return 0;
}
