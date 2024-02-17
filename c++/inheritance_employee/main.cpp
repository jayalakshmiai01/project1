//constructor with parameter

/*#include <iostream>

using namespace std;
class employee
{
private:
    int empid;
    string name;
    double salary;
public:
    employee(int eid, string n, double s)
    {
    empid = eid;
    name = n;
    salary = s;
    }
    void print()
    {
        cout << "employee id is" << empid << endl;
        cout << "employee name is" << name << endl;
        cout << "employee salary is" << salary << endl;

    }
};
int main()
{
    employee e1(01,"jaya",1000);
    e1.print();
    return 0;
}
*****************************************************************************************
*/
//inheritance
/*#include <iostream>

using namespace std;
class employee
{
private:
    int empid;
    string name;
    double salary;
public:
    employee(int eid, string n, double s)
    {
    empid = eid;
    name = n;
    salary = s;
    }
    void print()
    {
        cout << "employee id is" << empid << endl;
        cout << "employee name is" << name << endl;
        cout << "employee salary is" << salary << endl;

    }
    void setempid(int eid)
    {
    empid=eid;
    }
    int getempid()
    {
        return empid;
    }
    void setname(string n)
    {
        name = n;
    }
    string getname()
    {
        return name;
    }
    void setsalary(double s)
    {
        salary = s;
    }
    int getsalary()
    {
        return salary;
    }
};
int main()
{
    employee e1(01,"jaya",1000);
    e1.print();
    e1.setempid(2);
    e1.setname ("kavi");
    e1.setsalary(25000);
    e1.print();
    cout << "name" << e1.getname() << endl;
    return 0;
}

*******************************************************************************************
*/

#include <iostream>

using namespace std;
class employee
{
private:
    int empid;
    string name;
    double salary;
public:
    employee(int eid, string n, double s)
    {
    empid = eid;
    name = n;
    salary = s;
    }
    void print()
    {
        cout << "employee id is" << empid << endl;
        cout << "employee name is" << name << endl;
        cout << "employee salary is" << salary << endl;

    }
    void setempid(int eid)
    {
    empid=eid;
    }
    int getempid()
    {
        return empid;
    }
    void setname(string n)
    {
        name = n;
    }
    string getname()
    {
        return name;
    }
    void setsalary(double s)
    {
        salary = s;
    }
    int getsalary()
    {
        return salary;
    }
};
int main()
{
    employee e1(01,"jaya",1000);
    e1.print();
    e1.setempid(2);
    e1.setname ("kavi");
    e1.setsalary(25000);
    e1.print();
    cout << "name" << e1.getname() << endl;
    return 0;
}
