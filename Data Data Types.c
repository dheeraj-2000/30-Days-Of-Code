#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int i = 4,j;
    double d = 4.0,dd;
    char s[] = "HackerRank ";
    char str[100],*p,a[100];
    scanf("%d",&j);
    scanf("%lf",&dd);
    scanf(" %[^\n]",str);
    p=strcpy(a,s);
    printf("%d\n",i+j);
    printf("%.1lf\n",d+dd);
    // Print the sum of the double variables on a new line.
    p=strcat(a,str);
    printf("%s\n",p);
    // Concatenate and print the String variables on a new line
}
