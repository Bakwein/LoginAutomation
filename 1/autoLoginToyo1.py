from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep
import sys

# SOL ÜST BUTON



'''
!!!! ÇALIŞTIRILMASI İÇİN YAPILMASI GEREKENLER !!!!
-python derlemek için python'ın bir sürümünün bilgisayarda bulunması gereklidir -> https://www.python.org/downloads/

!!! SANAL ÇALIŞTIRMA ORTAMI OLUŞTURMA
python'u yükleme çeşidine göre aşağıdaki gibi venv(sanal ortam) oluşturulabilir.
py.exe -m venv myenv
python3.12 -m venv myenv
-sonucta myenv klasoru olusur. Olusması birkac dakika surmektedir.

!!! myenv içine girme
win -> myenc\Scripts\activate
macos -> source myenv\bin\activate

!!! myenv içine girdikten sonra gerekli bağımlılıkları yükelemek için
a) requirements.txt kullanma
pip install -r requirements.txt

b) derleyip teker teker görme :D -> bu garip tercih :D. ->
py.exe veya python3 kullanarak;
py.exe autoLoginToyo1.py
python3.12 autoLoginToyo1.py şeklinde derleyip çıkan hata mesajlarına göre pip install yapılabilir. Örneğin;
xxxx module required -> hatası 
ÇÖZÜM -> pip install xxxx(olmaz ise google üzerinden pypi xxxx yazarak gerekli siteden kopyalama yapılarak indirilebilir.)

!!! TÜM MODULLER TAMAM SIRA DERLEMEDE - TEST
py.exe veya python3 kullanarak;
py.exe autoLoginToyo1.py
python3.12 autoLoginToyo1.py 
BU ŞEKİLDE PROGRAM ÇALIŞTIIRLABİLİR.

!!!! python programı .exe haline çevirmek için !!!!
pip install pyinstaller 
.ico dosyasının da dizinde olması gereklidir (ikon eklemek için)
pyinstaller --onefile --noconsole --icon=ico.ico autoLoginToyo1.py

BUILD -> .exe oluştururken geçiçi build etme dosyaları burada depolanır - Gereksiz Dosyalar
DIST -> .exe'nin bulunduğu klasör. .exe ile tüm dosyalardan bağımsız programı istediğiniz bilgisayarda ek yükleme gerekmeden kullanabilirsiniz.

'''


'''  HATA DURUMLARI


!!!!! BAZI YERLERE EXCEPTIONLAR EKLEDİM KOD OLARAK ÇALIŞTIRIP EXCEPTION YARATAN YERİ BULABİLMENİZE YARDIMCI OLABİLİR

HATA NEDENLERİ BUNLAR OLABİLİR;

1- İtem'ları almak için kullandığım özellikler değiştiyse veya unique özellik olarak aldığım özelliklerin sayısının 1'den fazla olması! (Timeout hatası ile karşılaşılır!)

2- SPP 1 İSİMLİ BUTON KALDIRILMIŞ OLABİLİR. O ZAMAN BEKLEME WHILE'INA GİRMEZ.

'''

def wait_for_clickable(driver, selector, unique_val):
    #print("clickable", unique_val)
    try:
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((selector, unique_val))
        )
        return element
    except TimeoutException:
        return None
    
def wait_for_pre(driver, selector, unique_val):
    #print("pre", unique_val)
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((selector, unique_val))
        )
        return element
    except TimeoutException:
        return None


try:
#
    service = ChromeService(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions() #Chrome'a ek özellikler eklemek için options'u aldık
    options.add_argument("--start-fullscreen") #tam ekran başlatmasını sağlayan özellik
    options.add_argument("--force-device-scale-factor=0.9")
    options.add_experimental_option("detach", True) # hep görünür şekilde açık kalmasını sağlayan özellik

#chrome test bloğunu kaldırmak için gerekli özellikler
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches",["enable-automation"])

#Giriş yaptıktan sonra google'un şifreyi kaydetme pop-up'ını otomatik olarak kaldırır.
    prefs = {"credentials_enable_service": False,
        "profile.password_manager_enabled": False}
    options.add_experimental_option("prefs",prefs)

#belirlenen servis ve ayarlar ile webserver'ı başlatma
    driver = webdriver.Chrome(service=service, options=options)

# URL'ye git - webserver ile url'yi açma
    driver.get("xxx")
    #driver.execute_script("document.body.style.zoom='90%'")

#driver.save_screenshot("img.png")

# KULLANICI ADI input bloğunu almak için
    try:
        while True:
            username_field = wait_for_pre(driver, By.CSS_SELECTOR, "xxx")
            if username_field:
                #print("kirdi")
                break
    except:
        print("username elementi alinamadi")
        sys.exit()

#ŞİFRE input bloğunu almak için
    try:
        
        while True:
            password_field = wait_for_pre(driver, By.CSS_SELECTOR, "xxx")
            if password_field:
                #print("kirdi")
                break
        
    except:
        print("password elementi alinamadi")
        sys.exit()

#BURADA X KULLANICI ADI GİRİLMELİDİR
    for char in "xxx":
        username_field.send_keys(char) #harfleri teker teker input value'suna gönderir.
        sleep(0.1) #insan taklidi için :D

#BURADA X YERİNE ŞİFRE GİRİLMELİDİR
    for char in "xxx":
        password_field.send_keys(char) #harfleri teker teker input value'suna gönderir.
        sleep(0.1) #insan taklidi için :D

# GİRİŞ BUTONUNU alma
    try:
        while True:
            login_button = wait_for_clickable(driver,By.CSS_SELECTOR, "xxx")
            if login_button:
                #print("kirdi")
                login_button.click()
                break
    except :
        print("buton alinamadi")
        sys.exit()

     # butonu aldıktan sonra butona basma işlemi.

    
#Doküman readyState durumuna yani tüm yüklemeler oluncaya kadar while içinde döner. Yüklemeler bitince while'dan çıkıp alttan devam eder.
    #print("iki")
    '''
    element_load_control1 = False
    while not element_load_control1:
        try:
            elem = driver.find_element((By.CSS_SELECTOR, ".xxx"))  
            element_load_control1 = True
        except:
            pass'''

    #print("uc")

# ANASAYFADA MENÜ GRİDİNİ AÇMAK İÇİNN GEREKLİ OLAN BUTON
    try:
        
        while True:
            menu_but = wait_for_clickable(driver, By.CSS_SELECTOR, ".xxx")
            if menu_but:
                #print("kirdi")
                menu_but.click()
                break
    except:
        print("menu butonu alinamadi")
        sys.exit()

#print(menu_but, "*")
    #menu_but.click() #grid menü butonuna basar

#gerekli tabloların bulunduğu 6'lı buton olan sayfaya geçiş için tıklanması gereken menü elemanı
    try:
        
        while True:
            to_ges = wait_for_clickable(driver, By.CSS_SELECTOR, "xxx")
            if to_ges:
                #print("kirdi")
                to_ges.click()
                break

    except:
        print("ges'e basilamadi")
        sys.exit()
#print(to_ges, "*")
    #to_ges.click() #menü elemanı bulunduysa içine girer böylece 6'lı butonlu sayfaya yönlendirilmiş olur.
    '''
print("WHILE ÖNCESİ")
while driver.execute_script("return document.readyState") != "complete":
    pass

print("YÜKLENDİ, UYUYORUM")
sleep(1)
print("UYANDIM")
    '''
# BU 6'LI BUTONLU SAYFADA 2 BUTON HARİCİ DİNAMİK OLARAK SAYFAYA GELMEKTE VE BU BUTONLARIN GELİŞİ BİRAZCIK VAKİT ALMAKTA. ALTTAKİ WHILE ILE TÜM BUTONLAR GELENE KADAR BEKLENİR.

#4 BUTONDAN BİRİ OLAN SPP 1 İSİMLİ BUTON GELENE KADAR ALTTAKİ WHILE DÖNMEYE DEVAM EDER.  
# !! EĞER SPP İSİMLİ BUTON KALDIRILDIĞI VB. DURUMLARDA BU HATAYA SEBEP OLUR!!!!!!!!!!
    #("kontroldeyim")
    element_load_control = False
    while not element_load_control:
        try:
            elem = driver.find_element(By.XPATH, "xxx")  
            element_load_control = True
        except:
            sleep(1)
    #print("ciktim")

# TIKLANACAK BUTONU ALMA
    try:
        
        while True:
            trytoclick = wait_for_clickable(driver,By.XPATH,  "xxx")
            if trytoclick:
                #print("kirdi")
                trytoclick.click()
                break

    except:
        print("ssp butonu bulunamadi")
        sys.exit()

#print(trytoclick, "butonu buldum")
    #trytoclick.click() # TIKLANACAK BUTONA TIKLAMA 
    
    #driver.execute_script("document.body.style.transform='scale(0.8)'")

    while True:
        try:
            yo = wait_for_pre(driver, By.ID, "xxx")
            if yo:
                if yo.text.strip():
                    print("aha!")
                    driver.refresh()
                    element_load_control = False
                    while not element_load_control:
                        try:
                            elem = driver.find_element(By.XPATH, "xxx")
                            element_load_control = True
                        except:
                            print("??")
                            sleep(5)
                            try:
                                elem = driver.find_element(By.XPATH, "xxx")
                                element_load_control = True
                                continue
                            except:
                                pass
                            driver.refresh()

                    while True:
                        try:
                            trytoclick = wait_for_clickable(driver,By.XPATH,  "xxx" )
                            if trytoclick:
                                trytoclick.click()
                                break
                        except:
                            print("ssp butonu bulunamadi")
                            #sys.exit()

        except:
            #print("exp detection!")
            pass

except Exception as ex:
    print("Exception bulundu!", ex)