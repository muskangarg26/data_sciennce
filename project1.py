import datetime

class attendancemanagementsystem:
    def _init_(self):
        self.users={
            "muskan":"muskan123"
            #replace  with actual username #  and password for authentication
        }
        self.students={}
        self.attendance={}
    
    def login(self):
        while True:
                username=input("Username:")
                password=input("password:")
                if username in self.users and self.users[username]==password:
                    print("login successful.")
                    break
                else:
                   print("invalid credentials .please try again.")
            #---to add the student----
    def add_student(self,student_id,student_name):
                self.students[student_id]=student_name
                #to mark the attendence
    def mark_attendance(self,date,student_id,is_present):
                if date not in self.attendance:
                 self.attendance[date]={} 
                 self.attendance[date][student_id]=is_present  
                        #to view the student attendance report
    def view_student_attendance(self,student_id):
                  print(f"attendance for student {self.students.get(student_id,'N/A')}:")
                  for date,is_present in self.attendance.items():
                   if student_id in is_present:
                       print(f"{date}:{'present'if is_present[student_id]else'absent'}")
                                    #to generate attendance report----
    def generate_report(self, report_type, start_date=None, end_date=None):
                 if report_type not in ["daily","weekly","monthly"]:
                              
                     print("invalid report type.available options :daily,weekly,monthly")
                     return
                 
                 if start_date is None:
                  start_date=min(self.attendance.keys())
                 if end_date is None:
                   end_date=datetime.date.today()
                   
                 current_date=start_date
                 while current_date <=end_date:
                   if current_date in self.attendance:
                     present_count = sum(1 for is_present in self.attendance [current_date].values()if is_present )          
                     total_count = len(self.attendance[current_date])
                     print(f"{current_date} - {present_count}/{total_count}students present")
                                                   
                   if report_type == "daily":
                      break
                    
                   if report_type == "weekly":
                     current_date += datetime.timedelta(days=7)
                   elif report_type=="monthly":
                       next_month=current_date.month % 12 + 1
                       next_year=current_date.year + 1 if next_month==1 else current_date.year
                       current_date=current_date.replace(year=next_year,month=next_month,day=1)

    def main():
                     attendance_system=attendancemanagementsystem()
                     attendance_system.login()

                     while True:
                            print("\n attendance management system menu:")
                            print("1.add student")
                            print("2.mark attendance")
                            print("3.view student attendance")
                            print("4.generate attendance report")
                            print("5.exit")

                            choice=int(input("enter your choice(1-5):"))
                            if choice ==1:
                               student_id=input("enter  the student ID:")
                               student_name=input("enter the student name:")
                               attendance_system.add_student(student_id,student_name)
                               print(f"student choice '{student_name}'with ID'{student_id}'added successfully.")
                            
                            elif choice ==2:
                               date_str=input("enter the date(YYY-MM-DD)for attendance marking:")
                               date=datetime.datetime.strptime(date_str,'%Y-%m-%D').date()
                               student_id=input("enter the student ID:")
                               is_present=input("IS the student present ?(yes/no):").lower()=='Yes'
                               attendance_system.mark_attendance(date,student_id,is_present)
                            elif choice==3:
                                    student_id=input("enter the student ID:")
                                    attendance_system.view_student_attendance(student_id)

                            elif choice==4:
                                report_type=input("enter the report type(daily?weekly/monnthly):").lower()
                                start_date_str=input("enter the start date(YYYY-MM-DD):")
                                start_date=datetime.datetime.strptime(start_date_str,'%Y-%M-&D').date()
                                end_date_str=input("enter the end date(YYYY-MM-DD):")
                                end_date=datetime.datetiime.strptome(end_date_str,'%Y-%M-%D').Date()
                                attendance_system.generate_report(report_type,start_date,end_date)

                            elif choice==5:
                                print("exiting attendance management system.")
                                break
                            else:
                                print("invalid choice.please try again.")
    if __name__== "_main_":
       main()
 
                                                
                                                   

                            
                        
        

      
