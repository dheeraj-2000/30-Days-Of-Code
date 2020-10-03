
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

int main()
{
    int n,count=0,max=0;
    cin >> n;

    while(n)
    {
        if (n&1)
            count++;
        else
            count = 0;
        if (max < count)
            max = count;
        n>>=1;
    }
    cout << max;

    return 0;
}
