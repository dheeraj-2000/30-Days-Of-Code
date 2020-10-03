#include<iostream>
#include<algorithm>
#include<list>
#include<queue>

using namespace std;
queue <int> q;
struct graph
{
  list<int>adj;
};
list<int>::iterator it;
int main()
{
  int V,e,v,u;
  cout<<"enter no. of vertices in graph"<<endl;
  cin>>V;
  graph g[V];
  cout<<"no. ofedges"<<endl;
  cin>>e;
  for(int i=0;i<e;i++)
        {
            cout<<"enter edges from parent u to v"<<endl;
            cin>>u>>v;
            g[u].adj.push_back(v);
        }
  int s,t;
  cout<<"enter start vertex"<<endl;
  cin>>s;
  bool visited[V];
  q.push(s);
  visited[s]=true;
  while(!q.empty())
  {
    t=q.front();
    cout<<t<<"\t";
    q.pop();
    for(it=g[t].adj.begin();it!=g[t].adj.end();it++)
    {
        if(!visited[*it])
        {
          visited[*it]=true;
          q.push(*it);
        }
    }
  }
}
/*print adjacency list;
for(int i=0;i<V;i++)
{
cout<<i<<"\t";
for(it=g[i].adj.begin();it!=g[i].adj.end();it++)
{
cout<<*it<<"\t";
}
cout<<"\n";
}
*/
