#include <stdio.h>

int main()
{
    int n=6,a[6][6];
    for(int i=0;i<n;i++){
      for(int j=0;j<n;j++)
        {scanf("%d",&a[i][j]);}}
    int max=-64;
    int cur=0;

    for(int i=0;i<n-2;i++){
      for(int j=0;j<n-2;j++){
         int x=a[i][j];
         int b=a[i][j+1];
         int c=a[i][j+2];
         int d=a[i+1][j+1];
         int e=a[i+2][j];
         int f=a[i+2][j+1];
         int g=a[i+2][j+2];
    cur=x+b+c+d+e+f+g;
    if(cur>max){
      max=cur;
    }}}
    printf("%d",max);
return 0;
}
