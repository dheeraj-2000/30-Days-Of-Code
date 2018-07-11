class Calculator : public AdvancedArithmetic {
public:
    int divisorSum(int n) {
        int total=0,i;
        for(i=1; i<=n; i++)
        {
            if(n%i == 0)
            {
            total+=i;
            }
        }
        return total;
    }
};
