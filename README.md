# HW_PBO
# Functionality
* *Capability*: The system should support different user roles (students, professors, admin, operator, parents) with role-specific functionalities. For students, this might include viewing grades and course materials. Professors would need to post grades and course materials, admins oversee system operations, operators handle technical issues, and parents access student progress.

* *Reusability*: Components like user authentication, data retrieval, and notification services should be designed for reuse across different modules.

* *Security*: User authentication, data encryption, and access control are essential. Sensitive data like student records and grades must be securely managed.

*Usability*
* *Human Factors*: The interface should be intuitive for all user types, accommodating varied tech proficiency. It should have a responsive design for different devices.

* *Consistency*: The system should maintain a consistent look and feel across all modules and user roles.

# Reliability
* *Documentation*: Comprehensive user guides for each user role, FAQs, and system manuals are necessary.
Reliability

* *Availability*: The system should be available 24/7, with minimal downtime.
Failure Rate & Duration: It should have a low failure rate. Any system failures should be resolved quickly.

* *Predictability*: System behavior in response to user actions should be predictable and consistent.

# Performance
Speed: Fast response times for user queries and actions.
Efficiency: Optimized for minimal resource consumption without compromising functionality.
Resource Consumption: Should be optimized to work smoothly on standard institutional hardware.
Scalability: Capable of handling an increasing number of users and data volume.

*Supportability*
Testability: The system should be easily testable to find and fix bugs.
Extensibility: It should be designed to allow easy updates and additions of new features.
Serviceability: Problems within the system should be easy to diagnose and fix.
Configurability: Allow easy configuration of features like user roles, permissions, and system settings.

# Use Case and User Stories
Use Case diagram will represent the interactions between various user roles and the system

*User Roles (Actor)*
* Student (mahasiswa)
* Professor(Dosen)
* Operator(Tata Usaha)
* Admin (PTI)

*User Stories (Functionalities)*
* student
 * enroll course
 * view grade
 * access course material
 * view schedule
 * you named it

* Professor
 * upload course
 * view course member
 * add grade
 * you named it

* Admin
 * User management
 * systm monitoring
 * you named it

* Operator
 * Technical support
 * support dosen
 * support mahasiswa
 * daily operation
 * you named it

# Class Diagram
* Main Classes: User, Course, Grade, Material, Notification, SystemSettings.

* User Class: Subclasses for Student, Professor, Admin, Operator, Parent.

* Relationships:
  * Users to Courses (enrollment, teaching).
  * Users to Grades (viewing, uploading).
  * Users to Materials (access, management).

* Attributes: Specific to each class, like user ID, course details, grade records.

* Methods: Functions like registerCourse(), uploadGrades(), generateReport().

# User (Abstract Class)
*Attributes: UserID, Name, Email, Password*
* Methods: login(), logout()
* Student (Inherits User)
* Attributes: EnrollmentID, Courses (List), Grades (List), Absences
* Methods: enrollInCourse(), viewGrades(), recordAbsence(), viewCourses()
*Professor (Inherits User)*
* Attributes: FacultyID, CoursesTaught (List)
* Methods: uploadGrades(), manageCourseMaterials(), monitorAttendance()
*Admin (Inherits User)*
* Attributes: AdminID
* Methods: manageUserAccounts(), generateReports(), overseeSystemOperations()
*Operator (Inherits User)*
* Attributes: OperatorID
* Methods: provideTechnicalSupport(), maintainSystem()
*Course*
* Attributes: CourseID, Name, Description, StudentsEnrolled (List), CourseMaterials
* Methods: addStudent(), removeStudent(), updateCourseMaterial()
*Grade*
* Attributes: StudentID, CourseID, LetterGrade, NumericScore
* Methods: updateGrade()
*Attendance*
* Attributes: StudentID, CourseID, DatesAbsent
* Methods: recordAbsence(), calculateAttendanceRate()
*Association:*
`Students have an association with Courses and Grades.`
`Professors have an association with Courses (they teach) and the Grades (they assign).`
`Parents have an association with their children's academic records.`
*Aggregation:*
Course aggregates Students (as it contains a list of enrolled students) and CourseMaterials.
![usecase](./Screenshot%202024-04-23%20233815.png)

# mermaid
    classDiagram 
    class User {
    <<abstract>>
    +UserID
    +Password
    +Login()
    +Logout()
}

# class Student {
    +EnrollmentID
    +CoursesList
    +GradesList
    +Absences
    +EnrollInCourse()
    +ViewGrades()
    +RecordAbsence()
    +ViewSchedule()
    +ViewPaymentBills()
}

# class Professor {
    +FacultyID
    +CoursesTaught: List
    +UploadGrades()
    +MonitorAttendance()
    +UpdateSchedule()
}

# class Operator {
    +OperatorID
    +ProvideTechnicalSupport()
    +MaintainSystem()
    +ConfirmPayment()
}

# class Course {
    +CourseID
    +Name
    +Description
    +StudentsEnrolled: List
    +CourseMaterials: List
    +AddStudent()
    +RemoveStudent()
    +UpdateCourseMaterial()
}

# class Announcement {
    +AnnouncementID
    +Title
    +Content
    +PostedBy
    +DatePosted
    +CreateAnnouncement()
    +DeleteAnnouncement()
    +EditAnnouncement()
}

# class Payment {
    -PaymentID
    -Amount
    -Date
    +processPayment()
    +generateReceipt()
    +cancelPayment()
}

# class Grade {
    +StudentID
    +CourseID
    +LetterGrade
    +NumericScore
    +UpdateGrade()
}

# class Attendance {
    +StudentID
    +CourseID
    +DatesAbsent
    +RecordAbsence()
    +CalculateAttendanceRate()
}

`User <|-- Student`
`User <|-- Professor`
`User <|-- Operator`

`Student "n" -- "n" Course : enrolls in >`
`Course "1" -- "n" Grade : has > `
`Course "1" -- "n" Attendance : has >`
`Professor "1" -- "1" Course : teaches >`

`Student "n" -- "n" Payment : makes >`
`Course "n" -- "n" Announcement : has >`
