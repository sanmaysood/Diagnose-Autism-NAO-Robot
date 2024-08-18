from gtts import gTTS
import subprocess
import ftplib
import paramiko
import os
import time
import sys 

from googletrans import Translator


def save_and_send(text, filename):

    # Translating the text
    translated = t.translate(text, dest="hi")
    language = "hi"
    text_val = translated.text

    # Creating audio file using google text to speech
    obj = gTTS(text=text_val, lang=language, slow=True)  
    obj.save(filename + ".mp3")

    # Uploading to ssh
    path = filename + ".mp3"
    file = open(path, "rb")
    str = "STOR " + path
    server.storbinary(str, file)
    file.close()
    command = "python2 /home/nao/Desktop/ftp_recv.py " + path + (" /home/nao/Desktop/audio/" + path) 
    stdin, stdout, stderr = ssh.exec_command(command)

def load(name, leftObject, rightObject, specialEducator):
    #connecting to the server
    HOSTNAME = "ftpupload.net"
    USERNAME = "epiz_33045168"
    
    PASSWORD = "J7RzvhjFoSIrD"
    server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)
    server.encoding = "utf-8"
    host = "192.168.26.16"
    _username = "nao"
    _password = "NAO@hmi"
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username = _username, password = _password)


    # Intro
    save_and_send("Hello. Mera naam Chintu hai. Mai triple aai tee dee ke ech em aai lab mein rehta hoon.", "namaste")
    save_and_send("Mai theek hoon. " + specialEducator + " aap kese ho?", "ashwini")
    save_and_send("Mujhe sunke accha laga", "counter").
    save_and_send("Hello " + name + " mera naam chintu hai. Aap kese ho?", "childAsk")
    save_and_send(name + " aapko pata hai mujhe frog jumps, rolly polly jesi bohut saari exercises aati hai.", "taskList")
    save_and_send("Aaj hum activities karenge!", "intro_ques")
    save_and_send("Kya mai aapko kuch aur krke dikhau?", "repeat_ques")


    # Cards
    save_and_send(specialEducator + " mujhe card dena.", "giveCard")
    save_and_send(name + " cards match karke dikhao", "cardsMatch")


    # Dance
    save_and_send('chalo ' + name + ' mere saath dance karo!', "dance")


    # Pointing
    save_and_send(text = 'Arrey ye dekho Ye Kya pada hua hai? Ye ' + leftObject + " hai ya " + rightObject + "?", "pleft")
    save_and_send(text = 'Aur idhar kya rakha hua hai? Ye ' + leftObject + " hai ya " + rightObject + "?", "pright")
    save_and_send(text = "Haan ye " + leftObject + " hai!", "leftfinal")
    save_and_send(text = "Haan ye " + rightObject + " hai!", "rightfinal")
    save_and_send(text = "ye " + leftObject + " hai. Chalo ab hum aage badte hain", "pleftNegative")
    save_and_send(text = "Ye " + rightObject + " hai. Chalo ab hum aage badte hain", "prightNegative")


    # Frog
    save_and_send(text = name + " aap hath se frog jumps kar sakte ho?", "frog")
    save_and_send(text = "ye dekho mere sath karo!", "frog2")


    # Body parts
    save_and_send(text = "chalo ab hum apne shareer ke baare mein seekhte hain", "body_intro")
    save_and_send(text = "This is my head.", "head")
    save_and_send(text = "Can you touch your head?", "headAsk")
    save_and_send(text = "These are my eyes.", "eyes")
    save_and_send(text = "Can you touch your eyes?", "eyesAsk")
    save_and_send(text = "This is my chest.", "chest")
    save_and_send(text = "Can you touch your chest?", "chestAsk")
    save_and_send(text = "These are my hands.", "hands")
    save_and_send(text = "Can you raise your hands?", "handsAsk")
    save_and_send(text = "Haan, ye aapka sir hai!", "headPositive")
    save_and_send(text = "Yes. These are your eyes.", "eyesPositive")
    save_and_send(text = "Yes. These are your hands.", "handsPositive")
    save_and_send(text = "Yes. This is your chest.", "chestPositive")



    # Reinforcements
    save_and_send(text = "Bohut badiya. Chalo ek high five do.", "high5")
    save_and_send(text = "Let's try again.", "tryAgain1")
    save_and_send(text = name + " meri taraf dekho.", "reinforce1")
    save_and_send(text = "very good!", "good")
    save_and_send(text = "Chalo aage badte hain", "bad")
    save_and_send(text = "Chalo koi baat nahi, Hum aage badte hain.", "bodyNegative")

    # Peekaboo
    save_and_send(text = name + " kya aap mujhe dekh sakte ho?", "peekaboo")
    save_and_send(text = "Booo", "peekaboo2")
    save_and_send(text = "Bohut Acche, ab aage badte hain.", "positive1")
    save_and_send(text = "Waah, Bohut acha!", "positive3")




if __name__ == "__main__":
    print("Loading files!!")
    load(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    print("Files loaded successfully!!")