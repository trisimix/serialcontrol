import subprocess
import os
import stat
dmi = subprocess.check_output('dmidecode', shell=True)
#print(variable)
#run program once as root then cron it as root
try :
    file = open("/var/log/serialcontrol/dmidecode.txt", "r")
    file.close()
except FileNotFoundError:
    script = '/var/tmp/serialcontrol.bash'
    with open(script, 'w') as file:
        file.write("#!/bin/bash/\nif [ ! -d /var/log/serialcontrol/ ]\nthen\n\tmkdir /var/log/serialcontrol/\nfi");
    #st = os.stat(script)

    #os.chmod(script, st.st_mode | stat.S_IEXEC)

    subprocess.call(["bash", script])
    subprocess.call(["rm", script])
#with open('/var/log/serialcontrol/dmidecode.txt' , 'w') as file:
#        file.write(dmi);
file = open("/var/log/serialcontrol/dmidecode.txt" , "w");
dmi = str(dmi)
dmi = dmi.replace('\\n', '\n')
dmi = dmi.replace('\\t', '\t')
file.write(dmi)
file.close()
script2 = '/var/log/serialcontrol/serialcontro1.bash'
#with open(script2, 'w') as file:
#	file.write('#!/bin/bash\nrecipients="archmachine9@gmail.com"\nsubject="...Subject..."\necho -e "to: $recipients\nsubject: $subject\n"| (cat - &&uuencode /var/log/serialcontrol/dmidecode.txt) | ssmtp archmachine9@gmail.com')
import smtplib
sender = 'archmachine9@gmail.com'
receivers = 'archmachine9@gmail.com'
message = "\r\n".join([
	"From: archmachine9@gmail.com",
	"To: archmachine9@gmail.com",
	"Subject: SerialControl",
	"",
	dmi
	])
username = 'archmachine9@gmail.com'
password = ''
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(sender, receivers, message)
server.quit()
#subprocess.call(["bash", script2])
#this sub is supposed to /n with actual /n's
#subprocess.run(["sed -i 's/\\n/\n/g' /var/log/serialcontrol/dmidecode.txt"], shell=True)
#except FileNotFoundError:
    #file = open('/var/tmp/serialcontrol.bash', 'w') 
    #file.write("#!/bin/bash/\nif [ ! -d /var/log/serialcontrol/]\nthen\n\tmkdir /var/log/serialcontrol/\nfi");
    #file.close()
    #st = os.stat("/var/tmp/serialcontrol.bash")
    #os.chmod("/var/tmp/serialcontrol.bash", st.st_mode | stat.S_IEXEC)
    #subprocess.call("/var/tmp/serialcontrol.bash")
    
