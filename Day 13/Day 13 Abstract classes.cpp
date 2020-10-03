class MyBook : Book{
    private:
    int price;
    public:
    MyBook(string t,string a,int price):Book(t,a){
        this->price = price;
    }
    void display(){
        cout << "Title: " << title << endl << "Author: " << author << endl << "Price: " << price << endl;
    }
};
