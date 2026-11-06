
# Program: University Scholarship Eligibility System
# Topic: Conditional Statements (if, elif, else)

print("=" * 50)
print("       UNIVERSITY SCHOLARSHIP SYSTEM")
print("=" * 50)

# STEP 1: Collect Student Information

student_name = input("\nEnter Student Name: ")

if student_name.strip() == "":
    print("\nError: Student name cannot be empty!")

else:
    try:
        marks = float(input("Enter Academic Marks (%): "))
        attendance = float(input("Enter Attendance Percentage (%): "))
        family_income = float(input("Enter Monthly Family Income (Rs.): "))

        # STEP 2: Validate Student Information

        if marks < 0 or marks > 100:
            print("\nError: Marks must be between 0 and 100.")

        elif attendance < 0 or attendance > 100:
            print("\nError: Attendance must be between 0 and 100.")

        elif family_income < 0:
            print("\nError: Family income cannot be negative.")

        else:
            # STEP 3: Evaluate Scholarship Eligibility

            reasons = []

            if marks < 80:
                reasons.append("Academic marks are below 80%.")

            if attendance < 85:
                reasons.append("Attendance is below 85%.")

            if family_income > 50000:
                reasons.append("Family income exceeds Rs. 50,000.")

            # STEP 4: Display Student Evaluation Report

            print("\n" + "=" * 50)
            print("          SCHOLARSHIP EVALUATION REPORT")
            print("=" * 50)

            print("\nSTUDENT INFORMATION")
            print("-" * 50)
            print(f"Student Name       : {student_name}")
            print(f"Academic Marks     : {marks:.2f}%")
            print(f"Attendance         : {attendance:.2f}%")
            print(f"Monthly Family Income: Rs. {family_income:,.2f}")

            print("\nELIGIBILITY CRITERIA")
            print("-" * 50)
            print("Minimum Academic Marks : 80%")
            print("Minimum Attendance     : 85%")
            print("Maximum Family Income  : Rs. 50,000")

            print("\nSCHOLARSHIP DECISION")
            print("-" * 50)

            if len(reasons) == 0:

                if marks >= 90:
                    print("Eligibility Status : ELIGIBLE")
                    print("Scholarship Award  : FULL SCHOLARSHIP")

                elif marks >= 80:
                    print("Eligibility Status : ELIGIBLE")
                    print("Scholarship Award  : PARTIAL SCHOLARSHIP")

            else:
                print("Eligibility Status : NOT ELIGIBLE")
                print("Reasons for Ineligibility:")

                for reason in reasons:
                    print(f"- {reason}")

            print("\n" + "=" * 50)
            print("       END OF SCHOLARSHIP REPORT")
            print("=" * 50)

    except ValueError:
        print("\nError: Please enter valid numeric values for marks, attendance, and income.")
