class Student :  public Person{
	private:
		vector<int> testScores;
	public:
  		// Write your constructor
        Student (
            string firstName_,
            string lastName_,
            int identification_,
            vector<int> testScores_
        ) :
            Person(firstName_, lastName_, identification_),
            testScores(testScores_)
        {

        }

  		// Write char calculate()
        char
        calculate (
            void
        ) {
            char letterGrade = '?';
            float average = 0.0;

            // Calculate average
            for (auto & score : testScores) {
                average += score;
            }
            average /= testScores.size();

            // Assign letter grade
            if (average >= 90.0) {
                letterGrade = 'O';
            } else if (average >= 80.0) {
                letterGrade = 'E';
            } else if (average >= 70.0) {
                letterGrade = 'A';
            } else if (average >= 55.0) {
                letterGrade = 'P';
            } else if (average >= 40.0) {
                letterGrade = 'D';
            } else {
                letterGrade = 'T';
            }

            return letterGrade;
        }
};
