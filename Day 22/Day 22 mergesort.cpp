#include<iostream>
using namespace std;
int merge(int L[],int R[],int A[],int l,int r)
{

//cout<<"l is"<<l<<endl;

  int i=0,j=0,k=0;
  while(i<l&&j<r)
  {
    if(L[i]<=R[j])
            {
              A[k]=L[i];
              i++;
            }
    else
            {
              A[k]=R[j];
              j++;
            }
    k++;
  }
    while(i<l)
     {
        A[k]=L[i];
        i++;k++;
     }
      while(j<r)
      {
        A[k]=R[j];
        j++;k++;
      }
}
int mergesort(int A[],int n)
{
  //cout<<"n is "<<n<<endl;
  if(n>=2){


  int i;
  int mid=n/2;
  int L[mid];
  int R[n-mid];

  for(i=0;i<mid;i++)
          L[i]=A[i];
  for(i=mid;i<n;i++)
          R[i-mid]=A[i];
  int l= sizeof(L)/sizeof(L[0]);
  int r= sizeof(R)/sizeof(R[0]);
  mergesort(L,l);
  mergesort(R,r);
  merge(L,R,A,l,r);
}
}

int main()
{
  int m,i;
  cin>>m;
  int A[m];
  for(i=0;i<m;i++)
{

    cin>>A[i];

}
mergesort(A,m);
for(i=0;i<m;i++)
{
  cout<<A[i]<<"\t"<<endl;
}
}
