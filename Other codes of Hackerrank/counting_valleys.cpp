/* 
 * https://www.hackerrank.com/challenges/counting-valleys/problem
*/

#include <bits/stdc++.h>

using namespace std;

// Complete the countingValleys function below.
int countingValleys(int n, string s) {
int current=0,ans=0;
    for(int i=0;i<n;){
        if(s[i]=='U')
            current++;
        else
            current--;
        //cout<<current<<" ";
        if(current<0){
          ans++;i++;
            while(current<0){
                if(s[i]=='U')
                    current++;
                else
                    current--;
                i++;
                if(i>=n)
                    break;
            }
        }else{
            i++;
        }
    }
    return ans;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string s;
    getline(cin, s);

    int result = countingValleys(n, s);

    fout << result << "\n";

    fout.close();

    return 0;
}

