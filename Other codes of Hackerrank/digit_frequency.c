// https://www.hackerrank.com/challenges/frequency-of-digits-1/problem
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <ctype.h>

int main(void)
{
    char s[1000];
    
    scanf("%s", s);
    
    int count[10];
    int number = 48;
    // char *var;
    // printf("length %d", strlen(s));
    int i =0;
    for(int k = 0; k < 10; k++)
    {
        count[k] = 0;
    }
        while(number < 58)
        {
            int sum = 0;

            for(int c = 0; c < strlen(s); c++)
            {
                // printf("%c ", s[c]);
                int n = (int)s[c];
                // printf("number %d ",n);
                 if(n < 58 && n > 47)
                 {
                    if(n == number)
                    {
                        // printf("inside\n");
                        count[number - 48] = count[number - 48] + 1;
                    }
                 }
                
                   
                // printf("%d", count[number]);
            
            }
            i++;
            number++;
        }

        for (int j = 0; j < 10; j++)
        {
            printf("%d ", count[j]);
        }
}
