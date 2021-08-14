import re
class vali:
    def pin(pincode):
        pin = re.search("^6\d{5}$",pincode)
        if pin:
            print("valid pincode")
        else:
            print("error")
    def m_num(mobile_no):
        no = re.search("^\+91?[6-9]\d{9}$",mobile_no)
        if no:
            print("valid phn no")
        else:
            print("error")
    def b_val(blood_group):
        b =re.search("^(A|B|AB|O)[+-]+ve$",blood_group)
        if b :
            print("valid blood group")
        else:
            print("Error")
    def email(email_id):
        regex = "^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$"
        if (re.match(regex,email_id)):
            print("valid email id")
        else:
            print("Error")
    if __name__ == '__main__':
        email_id = 'divyabbplayer@gmail.com'
        email(email_id)

