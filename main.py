import smtplib, ssl
import time
from datetime import datetime
from credentials import sleepTimer

from credentials import smtp_server, port, password, sender
from config import receiver_email, messageA, totalLoopNum

def infoRead():
    file = open("info.txt","r")
    print(file.readlines(0))

    

mainloop = True
loopnum = 0

# Create a secure SSL context
context = ssl.create_default_context()



send = True



print("Started")
print("")
if send == True:
    try:
        server = smtplib.SMTP(smtp_server,port)
        #server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        #server.ehlo() # Can be omitted
        server.login(sender, password)

        print("Connection Complete\n")

        averagetimeA = []
        while mainloop == True:


            startTime = time.perf_counter()
            x = 0
            for z in receiver_email:
                receiver = receiver_email[x]
                message = ""
                y = 0
                for z in messageA:
                    message = messageA[y]
                    server.sendmail(sender, receiver, message)
                    print(f"sent message {y + 1} to {receiver}")
                    y += 1

                x += 1


            endTime = time.perf_counter()
            
            timeStarted = endTime - startTime
            now = 0
            now = datetime.now()
            dt = now.strftime("%d/%m/%Y %H:%M:%S")
            print(f"message sent {dt}, session lasted {round(timeStarted, 2)} secs")
            averagetimeA.append(round(timeStarted, 2))
            print("")
            sleepTimer()
            loopnum += 1
            if loopnum >= totalLoopNum:
                mainloop = False


    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()

    averagetime = 0
    for x in averagetimeA:
        averagetime += x

    averagetime = averagetime / len(averagetimeA)

    print("Session Finished")
    print(f"Average Time = {round(averagetime, 2)}")