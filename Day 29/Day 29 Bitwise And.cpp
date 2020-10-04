#include<bits/stdc++.h>

using namespace std;
using ll = long long;

int main() {
    int t;
    cin >> t;
    while(t--) {
        ll n, k;
        cin >> n >> k;
        ll max_ans = 0;
        ll j = k-1;
        for(int i=n; i>=2; i--) {
            if((i&j) > max_ans && i != j) {
                max_ans = i&j;
            }
        }
        cout << max_ans << endl;
    }
}

