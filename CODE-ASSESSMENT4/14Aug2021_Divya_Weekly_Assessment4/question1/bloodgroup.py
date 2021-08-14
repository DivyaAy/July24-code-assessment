import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pymongo
import pytz
from datetime import datetime
from validation import vali as va

client = pymongo.MongoClient("mongodb+srv://chediv_1998:Basketball9@cluster0.8vz0p.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
mydata = client["BloodBankManagementDB"]
Collection_name = mydata["BloodBank"]
logging.basicConfig(filename = "BloodBankDB.log" ,level=logging.DEBUG)
donor_list = [ ]

class donor_details:
    def add_details(self,name,address,pincode,mobile_no,email_id):
        self.name   = name
        self.address = address
        self.pincode = pincode
        self.mobile_no = mobile_no
        self.email_id = email_id

class blodd_details(donor_details):
    def b_details(self,blood_group,last_donated_date,place):
        self.blood_group = blood_group
        self.last_donated_date = last_donated_date
        self.place = place
        details = {"Name":name,"Address":address,"Pincode":pincode,"Mobile_no":mobile_no,"Email_id":email_id,
                    "Blood_group":blood_group,"Last_donated_date":last_donated_date,"Place":place,"Date&TIme":TD,"delete_status":0}
        donor_list.append(details)

    def timeDate(time_zone,td):
        time_zone = pytz.timezone("Asia/kolkata")
        td = datetime.now(time_zone).strftime("%d-%h-%y %H:%M:%S")
        return td

BD = blodd_details()

while(True):
    print("1.ADD DONOR")
    print("2.SEARCH DONOR BASED ON BLOOD GROUP")
    print("3.SEARCH DONOR BASED ON BLOOD GROUP AND PLACE")
    print("4.UPDATE ALL DONOR DETAILS WITH MOBILE NUMBER")
    print("5.DELETE DONOR USING MOBILE NUMBER")
    print("6.DISPLAY TOTAL NO OF DONOR BASED ON BLOOD GROUP")
    print("7.NOTIFICATION TO ALL VIA EMAIL")
    print("8.EXIT")
    choice = int(input("Select your choice: "))

    if choice == 1:
        print("Add donor details")
        name = input ("Enter Donor Name: ")
        address = input("Enter Donor address: ")
        pincode = input("Enter pincode: ")                              #validation is happening in validation module
        val = va.pin(pincode)
        mobile_no = input("Enter Donor Mobile No: ")
        val1=va.m_num(mobile_no)
        email_id = input("Enter Donor Email ID: ")
        val2= va.email(email_id)
        blood_group = input("Enter Donor Blood group: ")
        val3= va.b_val(blood_group)
        last_donated_date = input("Enter last donated date: ")
        place = input("Enter donated palce: ")
        TD = BD.timeDate('td')
        BD.add_details(name,address,pincode,mobile_no,email_id)
        BD.b_details(blood_group,last_donated_date,place)
        result = Collection_name.insert_many(donor_list)
        #print(donor_list)
    
    if choice == 2:
        print("Search Donor details based on blood group")
        b_g = input("Enter Blood group: ")
        result = Collection_name.find({"Blood_group":b_g,"delete_status":0},{"_id":0})
        new_list = []
        for i in result:
            new_list.append(i)
            print(new_list)
    
    if choice == 3:
        print("Search donor based on blood group and place")
        b_g = input("Enter blood group: ")
        p = input("Enter a place: ")
        result = Collection_name.find({"Blood_group":b_g,"Place":p},{"_id":0})
        new_list = [ ]
        for i in result:
            new_list.append(i)
            print(i)
    
    if choice == 4:
        print("Update details using mobile number")
        mob = input("Enter donor mobile no: ")

        name1 = input ("Enter Donor Name: ")
        address1 = input("Enter Donor address: ")
        pincode1 = input("Enter pincode: ")
        mobile_no1 = input("Enter Donor Mobile No: ")
        email_id1 = input("Enter Donor Email ID: ")
        blood_group1 = input("Enter Donor Blood group: ")
        last_donated_date1 = input("Enter last donated date: ")
        place1 = input("Enter donated palce: ")
        result = Collection_name.update_many({"Mobile_no":mob},{"$set":{"Name":name1,"Address":address1,"Pincode":pincode1,"Mobile_no":mobile_no1,"Email_id":email_id1,
        "Blood_group":blood_group1,"Last_donated_date":last_donated_date1,"Place":place1}})
        print(result)
    
    if choice == 5:
        print("Delete Donor details using mobile no ")
        mob1 = input("Enter donor mobile no: ")
        result = Collection_name.update_many({"Mobile_no":mob1},{"$set":{"delete_status":1}})
        
    
    if choice == 6:
        print("Display total no of donor based on blood group")
        result = Collection_name.aggregate([{"$group":{"_id":"$Blood_group","Count":{"$sum":1}}}])
        for j in result:
            print(j)
    
    if choice == 7:
        print("Notification to all donors")
        try:
            result = Collection_name.find({},{"Email_id":1,"_id":0})
            new_list = [ ]
            for i in result:
                new_list.append(i)
            print(new_list)
            id = [d['Email_id'] for d in new_list if 'Email_id' in d]
            print(id)
        
            with open ('Donor.txt','a+') as FD:
                message = str(input("write a message:"))
                FD.write(message +"\n")
            #mail_content = '''Urgent in Need of A+ve blood group in Thanjavur GH hospital'''
            mail_content = message

            sender_address = 'Chedivya1998@gmail.com'
            sender_pass = 'Welcome@2169'
            receiver_address = "," .join(id)

            message = MIMEMultipart()
            message['From'] = sender_address
            message['To'] = receiver_address
            message['Subject'] = 'Urgent Need of Blood '

            message.attach(MIMEText(mail_content, 'plain'))
            attach_file_name = 'Donor.txt'
            attach_file = open(attach_file_name, 'rb')
            # payload = MIMEBase('application', 'octate-stream')
            payload = MIMEBase('application', 'txt',Name=attach_file_name)
            payload.set_payload((attach_file).read())
            encoders.encode_base64(payload) 

            payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
            message.attach(payload)

            session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
            session.starttls() #enable security
            session.login(sender_address, sender_pass) #login with mail_id and password
            text = message.as_string()
            session.sendmail(sender_address, receiver_address, text)
            session.quit()
            print('Mail Sent')
        except:
            print("Value Error")
            logging.debug("value error")
        finally:
            logging.info("Program run successfully")
    if choice == 8:
        print("Exit")
        print("Thank you for your valuable time")
        break




        