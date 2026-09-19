

import java.util.Scanner; 

public class OOPR_LAB_ASSIGNMENT_1_ACT_1 { 
    public static void main(String[] args) { 
        
        double jvscore, cscore, dbscore;
        
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("Input"); 
        
        System.out.println("Java Score: "); 
        jvscore = scanner.nextDouble();
        
        System.out.println("C Score: "); 
        cscore = scanner.nextDouble();
        
        System.out.println("Database Handling score: "); 
        dbscore = scanner.nextDouble();
        
        double avg = (jvscore + cscore + dbscore) / 3.0;
        char grade;
        
        if (avg >= 90) {
            grade = 'A';              
        } else if (avg >= 80) {
            grade = 'B';
        } else if (avg >= 70) {
            grade = 'C';
        } else if (avg >= 60) {
            grade = 'D';
        } else {
            grade = 'F';
        }
        
        System.out.println("Output:");
        System.out.println(grade);
        System.out.println("Explaination:");
        System.out.printf("The average of the students is %.3f, so the student's grade is %c.%n", avg, grade);
        
        System.out.println("Do you want to continue : YES / NO");
        String choice = scanner.next();
        if (choice.equalsIgnoreCase("YES")) {
            main(args);
        } else {
            System.out.println("TERMINATED.");
        }
    
        scanner.close();
        }
    }
}
