#include<iostream>
#include<vector>
using namespace std;

int main()
{

    vector<int> a;
    int i;
    for(i=0;i<=10;i++)
    {
        a.push_back(i);
    }
    cout<<"vector size is="<<a.size();
    for(i=0;i<=10;i++)
    {
        cout<<"value of vector is="<<a[i]<<endl;
    }
    vector<int>::iterator b;
    for(b=a.begin();b<a.end();b++)
    {
        cout<<*a;
    }
    a.clear();
    cout<<"vector size is="<<a.size();
}
