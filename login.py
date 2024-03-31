import requests

# Form bilgileri
url = "https://wifi.gsb.gov.tr/j_spring_security_check"
tc_kimlik_numarasi = "TC_KİMLİK_NUMARASI"
sifre = "PAROLANIZ"

# Form verileri
form_data = {
    "j_username": tc_kimlik_numarasi,
    "j_password": sifre
}

# Formu gönderme
response = requests.post(url, data=form_data)

# Yanıtı kontrol etme
if response.status_code == 200:
    print("Başarıyla giriş yapıldı!")
else:
    print("Giriş yapılamadı. Hata kodu:", response.status_code)
