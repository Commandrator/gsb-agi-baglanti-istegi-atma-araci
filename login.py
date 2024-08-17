from bs4 import BeautifulSoup
from getpass import getpass
import requests
url = "https://wifi.gsb.gov.tr"
path=["/j_spring_security_check", "/maksimumCihazHakkiDolu.html"]
data = {"j_username": "","j_password": ""} #Varsayılan bilgileri buraya girebilirsin. username, kimlik numarası; password, şifreniz.
service = ["mainPanel:kota:j_idt101","mainPanel:kota:j_idt103","mainPanel:kota:j_idt104:0:j_idt105","servisUpdateForm:j_idt137","mainPanel:kota:j_idt93","mainPanel:kota:j_idt95","mainPanel:kota:j_idt96:0:j_idt97","servisUpdateForm:j_idt128","j_idt20:0:j_idt28"]
serviceName = {"mainPanel:kota:j_idt101":"Oturum Saati","mainPanel:kota:j_idt103":"Giriş Saati","mainPanel:kota:j_idt104:0:j_idt105":"Kota","servisUpdateForm:j_idt137":"Sağlayıcı","mainPanel:kota:j_idt93":"Oturum Saati","mainPanel:kota:j_idt95":"Giriş Saati","mainPanel:kota:j_idt96:0:j_idt97":"Kota","servisUpdateForm:j_idt128":"Sağlayıcı","j_idt20:0:j_idt28":"aktif_oturum","mainPanel:kota":"kapali_oturum"}

if (data.get("j_username") == ""):
    text = input("Kullanıcı adı:")
    data["j_username"]=text
if (data.get("j_password") == ""):
    text = getpass("Parola:")
    data["j_password"]=text
try:
    response = requests.post(url + path[0], data=data,)
    if response.status_code == 200:    
        soup = BeautifulSoup(response.content, 'html.parser')
        for form in soup.select('form[id]'):
            if (serviceName.get(form.attrs["id"]) == "aktif_oturum"):
                print("Maksimum Cihaz Sayısı: https://wifi.gsb.gov.tr" + path[1])
            elif(serviceName.get(form.attrs["id"]) == "kapali_oturum") :
                for label in form.select('label[id]'):
                    for service_id in service:
                        if(label.attrs['id'] == service_id):
                            print(f"{serviceName.get(label.attrs['id'], 'Bilinmeyen Hizmet')}: {(label.getText())}")
                print("\nDiğer işlemleri için: " + url)
    else:
        print("Hata kodu:", response.status_code)
except:
    print("Bağlantınızı Kontrol Edin")
