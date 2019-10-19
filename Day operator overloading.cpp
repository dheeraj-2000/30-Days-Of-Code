#include<iostream>
using namespace std;

class complex
{
private:
	int real;
	int img;
public:
	complex(int r=0,int i=0)
	{
		real = r;
		img = i;
	}
	void print()
	{
		cout<<real<<"+i"<<img<<endl;
	}
	friend complex operator+(complex const&,complex const&);
};
complex operator+(complex const&c1,complex const&c2)
{
	return complex(c1.real+c2.real,c1.img+c2.img);
}
int main()
{
	complex c1(10,5),c2(2,4);
	complex c3=c1+c2;
	c3.print();
	return 0;
}