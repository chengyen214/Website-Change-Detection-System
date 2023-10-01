
# Website-Change-Detection-System
在網站輸入欲查詢變動之網頁，系統會呈現網頁更動或如未有詢問是否登記持續追蹤並由後台系統隔一段時間比對差異。

## Prerequisites

- python 
- MySQL
- Flask

# Flask
* 安裝套件 `pip install -r REQUIREMENT.txt`
* 啟動 `python index.py`
* http://localhost:5000/

## ER Model 

![image](./images/ERModel.png)

## Relational Schema

![image](./images/Relation1.png)
![image](./images/Relation2.png)

## Page

1. Read
    - /CourseSelectRecommendation
    - /Read/SelectCourse
    - /Read/Course
    - /Read/Student
    - /Read/Teacher
2. Create
    - /Create/DataSubmission
    - /Create/Course
    - /Create/Student
    - /Create/Teacher
3. Update
    - /PersonalData/Update
4. Delete
    - /Delete/SelectCourse
    - /Delete/Student
