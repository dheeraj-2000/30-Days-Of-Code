#include <iostream>
#include <queue>
#include <stack>

using namespace std;

class Solution {
  public:
    //Write your code here
    void pushCharacter(const char c_) { _s.push(c_); }
    void enqueueCharacter(const char c_) { _q.push(c_); }
    char popCharacter() {
        char c = _s.top();
        _s.pop();
        return c;
    }
    char dequeueCharacter() {
        char c = _q.front();
        _q.pop();
        return c;
    }
  private:
    queue<char> _q;
    stack<char> _s;
};
