using namespace std;


int main(){
    int64_t n;
    string S;
    cin >> S;
    try {
        n = stoi(S);
        cout << n;
    } catch (...) {
        cout << "Bad String";
    }
    return 0;
