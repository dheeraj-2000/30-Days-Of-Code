 Difference(vector<int> a){
        elements = a;
        maximumDifference = 0;
    }
    void computeDifference(){
        int n = elements.size()-1;
        for(int i = 0; i < n; i++){
            for(int j = i; j < n; j++){
                if(maximumDifference < abs(elements[i]-elements[j+1])){
                    maximumDifference = abs(elements[i]-elements[j+1]);
                }}}}	// Add your code here
