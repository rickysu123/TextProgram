import smtplib

fromaddr = input("Enter a valid gmail email address. It can be fake!\n")

# Credentials
username = input("Enter username of email provided.")
password = input("Enter password of email provided.")

number = input("Phone number to send to?\n")

carrier = input("Phone carrier? (att, verizon, sprint, metro)\n")

msg = input("Message?\n")

if carrier == "att":
    number += "@txt.att.net"
elif carrier == "verizon":
    number += "@vtxt.com"
elif carrier == "sprint":
    number += "@messaging.sprintpcs.com"
elif carrier == "metro":
    number += "@mymetropcs.com"

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)

times = eval(input("Number of times to send message?"))

count = 0

while count < times:
             server.sendmail(fromaddr, number, msg)
             # uncomment to show number of messages sent
             #print("Sent = " + str(count+1))
             # uncomment to show number of messages sent
             count += 1
             
server.quit()

# att = @att.txt.net
# verizon = @vtxt.com
# sprint = @messaging.sprintpcs.com
