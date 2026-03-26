#include <iostream>
#include <string>
using namespace std;


//  1 - CAR

class Car {
private:
    string model;
    int year;

public:
    Car(string m, int y) {
        model = m;
        set_year(y);
    }

    string get_model() {
        return model;
    }

    void set_model(string m) {
        model = m;
    }

    int get_year() {
        return year;
    }

    void set_year(int y) {
        if (y >= 1886 && y <= 2026) {
            year = y;
        }
        else {
            cout << "Year must be between 1886 and 2026" << endl;
        }
    }

    int age() {
        return 2026 - get_year();
    }
};

//  2 - PRODUCT


class Product {
private:
    string name;
    double price;

public:
    Product(string n, double p) {
        name = n;
        set_price(p);
    }

    string get_name() {
        return name;
    }

    void set_name(string n) {
        name = n;
    }

    double get_price() {
        return price;
    }

    void set_price(double p) {
        if (p >= 0) {
            price = p;
        }
        else {
            cout << "Price cannot be negative" << endl;
        }
    }
};


//  3 - DATE


class Date {
private:
    int day, month, year;

public:
    Date(int d, int m, int y) {
        set_day(d);
        set_month(m);
        set_year(y);
    }

    int get_day() {
        return day;
    }

    void set_day(int d) {
        day = d;
    }

    int get_month() {
        return month;
    }

    void set_month(int m) {
        if (m >= 1 && m <= 12) {
            month = m;
        }
        else {
            cout << "Month must be between 1 and 12" << endl;
        }
    }

    int get_year() {
        return year;
    }

    void set_year(int y) {
        year = y;
    }

    bool is_valid() {
        if (month < 1 || month > 12) return false;

        int days_in_month;
        if (month == 2) {
            if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
                days_in_month = 29;
            }
            else {
                days_in_month = 28;
            }
        }
        else if (month == 4 || month == 6 || month == 9 || month == 11) {
            days_in_month = 30;
        }
        else {
            days_in_month = 31;
        }

        return (day >= 1 && day <= days_in_month);
    }
};

//  4 - EMPLOYEE


class Employee {
private:
    string name;
    int salary;

public:
    Employee(string n, int s) {
        name = n;
        set_salary(s);
    }

    string get_name() {
        return name;
    }

    void set_name(string n) {
        name = n;
    }

    int get_salary() {
        return salary;
    }

    void set_salary(int s) {
        if (s >= 10000) {
            salary = s;
        }
        else {
            cout << "Salary cannot be less than 10000" << endl;
        }
    }
};

// MAIN

int main() {
    int choice;

    cout << "Select task (1-4): ";
    cin >> choice;

    if (choice == 1) {

        Car c("Toyota", 2010);
        cout << c.get_model() << " " << c.age() << " years old" << endl;

        c.set_year(2000);
        cout << c.age() << endl;

        c.set_year(1800);
        cout << c.age() << endl;

    }
    else if (choice == 2) {

        Product p("Bread", 50);
        cout << p.get_name() << " " << p.get_price() << endl;

        p.set_price(60);
        cout << p.get_price() << endl;

        p.set_price(-10);
        cout << p.get_price() << endl;

    }
    else if (choice == 3) {

        Date d1(15, 5, 2023);
        cout << "Date 15/5/2023 is valid: " << d1.is_valid() << endl;

        Date d2(31, 2, 2023);
        cout << "Date 31/2/2023 is valid: " << d2.is_valid() << endl;

    }
    else if (choice == 4) {

        Employee e("Petrov", 25000);
        cout << e.get_name() << " " << e.get_salary() << endl;

        e.set_salary(30000);
        cout << e.get_salary() << endl;

        e.set_salary(5000);
        cout << e.get_salary() << endl;

    }
    else {
        cout << "Invalid choice" << endl;
    }

    return 0;
}