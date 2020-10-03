#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
         float mealcost,tippercent,taxpercent,totalcost;
    int tip,tax,l,m;
    scanf("%f\n%d\n%d",&mealcost,&tip,&tax);
    tippercent=mealcost*tip/100;
    taxpercent=mealcost*tax/100;
    totalcost=mealcost+tippercent+taxpercent;
    l=totalcost;
    m=(totalcost*100)-(l*100);
    l=(m>=50)?l+1:l;
    printf("The total meal cost is %d dollars.",l);
    return 0;
}
