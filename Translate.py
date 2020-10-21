#Google Translate Python Türkçe ve detaylı anlatım-Alperen T.
import googletrans #Google translate kütüphanemizi ekliyoruz.
from googletrans import Translator #İçinden çeviriciyi(translator) çekiyoruz.
import time
from colorama import init #Renk kütüphanesi
from colorama import Fore, Back, Style #Renk kütüphanesinin içindeki modüller
init()
#Kullanıcağımız komutları tanımamız lazım;
#İşte bazı kullanıcığımız Komutlar;

"""
src: Kaynak dil 
dest: İngilizce (en) olarak ayarlanmış hedef dil
origin: Orijinal metin
text: Çevrilmiş metin,
pronunciation: Çevrilen metnin telaffuzu
"""

çevirici = Translator() #Translatorı daha kolay kullanmak için çevirici değişkenine atıyoruz.
yazı = input("Çevirmek istediğiniz yazıyı giriniz---->") #Kullanıcın çevirmek istediği yazıyı istiyoruz.
print(Fore.GREEN) #Yeşil Renk
print("DOĞRULANDI ÇEVİRMEK İSTEDİĞİNİZ YAZI :"+yazı) #Kullanıcıya bir dönüt veriyoruz ve doğrulamak için verdiği değeri ona gösteriyoruz.
print(Fore.WHITE) #Beyaz renk

yazıdili = input("Yazdığınız yazının dilini belirtin-ÖRN : tr--->") #Kullanıcıdan yazdığı metni çevirmek için bir değer istiyoruz
SonucDili = input("Hangi dile dönüştürmek istediğinizi belirtin-ÖRN : en--->")#Kullanıcıdan yazdığı metni neye çevirmek istediğini soruyoruz.
SonucYazı = çevirici.translate(yazı,dest=SonucDili,src=yazıdili)#Sonunda sonucu ona göstermek için bir değer atıyoruz.

print("Yazınız çeviriliyor lütfen bekleyiniz...") #Dönüt veriyoruz.
time.sleep(0.5) #Okuması için süre

print(Fore.CYAN) #CYAN RENGİ
print("Orjinal metin :"+SonucYazı.origin) #orjinal metni gösteriyoruz.
print("Sonuç :"+SonucYazı.text) #Sonucu gösteriyoruz.
input("Kapatmak için enter a basınız....") #Ve sistemden çıkması için bir değer veriyoruz
#import Asistan-Kase
exit()