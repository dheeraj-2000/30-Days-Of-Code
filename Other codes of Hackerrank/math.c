#include <stdio.h>

int factorial(int a)
{
    if (a == 0 || a == 1)
    {
        return 1;
    }
    else
    {
        return a * factorial(a - 1);
    }
}

int main()
{
    // this programme is to find the factorial number
    int num;
    printf("Enter the number for which you want to check the factorial number\n");
    scanf("%d", &num);

    int value = factorial(num);
    printf("The value of the factorial is %d\n", value);
    return 0;
}
