import smtplib  
import time  
from email.mime.text import MIMEText
from threading import Timer

class Email:
        def sendEmail(self,address,sub,content):  
                self.smtp_host = 'smtp.mailgun.org'
                self.account = 'postmaster@sandbox015d597a6fde4e39a8e6e6b0e7c815ef.mailgun.org'  
                self.password='5b29a87d451c4b4c11ebdb64d3603740'  
                self.msg = MIMEText(content,'html','utf-8')  
                self.msg["Accept-Language"]="zh-CN"  
                self.msg["Accept-Charset"]="ISO-8859-1,utf-8"  
                self.msg['Subject']=sub  
                self.msg['From'] = 'postmaster@sandbox015d597a6fde4e39a8e6e6b0e7c815ef.mailgun.org'
                self.msg['To']=address 
                self.smtp = smtplib.SMTP(self.smtp_host)  
                self.smtp.login(self.account,self.password)  
                self.smtp.sendmail(self.account, address, self.msg.as_string())
                self.smtp.quit()  
                print ("发送成功").decode('utf-8').encode('mbcs')  

def run():
        t = Timer(3600, run)
        t.start()
        a = Email()
        a.sendEmail("jacky@holy-hi.com", "testEmail", "can you receive?")

def main():
        pass

if __name__ == '__main__':
        run()
