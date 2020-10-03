#include <stdio.h>

int main()
{
    int n;
    scanf("%d",&n);
    if(n > 0 && n < 101)
     { 
        if(n % 2 ==! 0)
            printf("Weird");
        
        else if(n % 2 == 0) {
           if(n > 1 && n < 6)
             printf("Not Weird");
           else if(n > 5 && n < 21)
             printf("Weird");
           else if(n > 20)
             printf("Not Weird"); 
        }
    }

    return 0;
}
