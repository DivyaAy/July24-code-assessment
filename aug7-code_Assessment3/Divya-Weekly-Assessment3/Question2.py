import re,json
import smtplib
import logging
logging.basicConfig(filename = "Student_Details_code.log" ,level=logging.DEBUG)
std_list=[ ]
class Student:
    def std_details(self,name,roll_no,adm_no,college,parent_name,mobile_no,email_id):
        self.name = name
        self.roll_no = roll_no
        self.adm_no = adm_no
        self.college = college
        self.parent_name = parent_name
        self.mobile_no = mobile_no
        self.email_id = email_id
        
class Sem1Result(Student):
    def mark_details(self,machines_mark,Oops_mark,Power_sys_analysis_mark,control_sys_mark,power_electronics_mark,total,percentage):
        self.machines_mark= machines_mark
        self.Oops_mark = Oops_mark
        self.Power_sys_analysis_mark=Power_sys_analysis_mark
        self.control_sys = control_sys_mark
        self.Power_electronics_mark = power_electronics_mark
        self.total = total
        self.percentage = percentage
        details = {"Name":name,"Roll_no":roll_no,"Admin_No":adm_no,"College":college,"Parent_Name":parent_name,
                    "Mobile_No":mobile_no,"Email_Id":email_id,"Machines":machines_mark,"OOps":Oops_mark,
                    "PSA":Power_sys_analysis_mark,"CS":control_sys_mark,"PE":power_electronics_mark,"total":total,"percentage":percentage}
        std_list.append(details)
    def validation(self,mobile_no):
        val = re.match("^\+91?[6-9]\d{9}$",mobile_no)
        if val:
            return True
        
    def vali(self,email_id):
        val1 = re.search("r^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",email_id)
        if val1:
            pass 
        
SR = Sem1Result()

while(True):
    print("1.Add_STUDENT_DETAILS")
    print("2.GENERATE JSON FILE AND DISPLAY IN API TO VIEW STUDENTS DETAILS WITH MARKS")
    print("3.GENERATE JSON FILE AND DISPLAY IN API TO VIEW STUDENTS DETAILS WITH RANKING BASE")
    print("4.SEND A MAIL TO PARENTS IF PERCENTAGE IS LESS THAN 50%")
    choice = int(input("enter your choice : "))

    if choice == 1:
        print("you selected to add_student_details")
        name = input("Enter a name: ")
        roll_no = int(input("Enter a roll_no : "))
        adm_no = int(input("Enter a admission no: "))
        college = input("Enter college name: ")
        parent_name = input("enter a Parent name: ")
        mobile_no = int(input("Enter a phn no with country code: "))
        SR.validation('mobile_no')        
        email_id = input("Enter Email id: ")
        SR.vali('email_id')
        print("!! Give marks for out of 40 only !!")
        machines_mark = int(input("Enter a Machines Mark: "))
        Oops_mark = int(input("Enter a Oops Mark: "))
        Power_sys_analysis_mark = int(input("Enter a PSA Mark: "))
        control_sys_mark=int(input("Enter a CS Mark: "))
        power_electronics_mark = int(input("Enter a PE Mark: "))
        total = machines_mark+Oops_mark+Power_sys_analysis_mark+control_sys_mark+power_electronics_mark
        percentage = (total/200)*100
        SR.std_details(name,roll_no,adm_no,college,parent_name,mobile_no,email_id)
        SR.mark_details(machines_mark,Oops_mark,Power_sys_analysis_mark,control_sys_mark,power_electronics_mark,total,percentage)

    if choice == 2:
        try:
            mydata = json.dumps(std_list)
            with open ('student Details with Mark.json','w+',encoding='UTF8',newline='') as j:
                j.write(mydata+"\n")
                j.close
        except TypeError:
            print("something went wrong")
    
    if choice == 3:
        mydata = json.dumps(std_list)
        with open ('student Details Ranking Base.json','w+',encoding='UTF8',newline='') as m:
            l =str(sorted(std_list,key = lambda i:i["total"],reverse=True))
            m.write(l)
            m.close

    if choice == 4:
        message =(list(filter(lambda k : k["percentage"] < 50,std_list)))
        break
    else:
        print("Choose next !")
        logging.info("Code Run sucessfully")

try:
    e_id=input("Enter parent's valid email id: ")
    va = "r^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if va :
        print("valid email id")
    else:
        print("invalid id")
except:
    print("error in validation")

y =str(message)
w = f''' Your son / Daughter scored below avg ,
                 {y} '''
connection = smtplib.SMTP ("smtp.gmail.com",587)
connection.starttls()
connection.login("chedivya1998@gmail.com","Welcome@2169")
connection.sendmail("chedviya1998@gmail.com",e_id,w)
print("Email sent successfully")
connection.quit()
    



    
    















