import smtplib
while(1):
    readMe=open('file.txt','r')
    str=readMe.read(1)
    print(str)
    if(str=='1'):
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login("science.reactor85@gmail.com", "c@rrot007")
            
            msg = "yashveer kuch nahi yr jo hota hai theek hota hai"
            server.sendmail("your email adresss", "adrash2601singh@gmail.com", msg)
            server.quit()
            print ('email sending succesfull!')
        except:
             print ('email not send')
             


                    
readMe.close()
