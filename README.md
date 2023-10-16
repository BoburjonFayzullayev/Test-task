# Appoinment 

Bu proyekt tibbiy ko'rik va davolanishdagi bemorlarni uchrashuvga tayinlash uchun ishlab chiqildi. Uchrashuv shifokor tomonidan yaratiladi va tegishli hujjatlarni o'z ichiga oladi.
Ushbu hujjat bemor, shifokor, tashxis hamda bemor murojaat qilishi kerak b'lgan muassasa haqida ma'lumotlar bo`ladi.


## O'rnating

Proyektni o'rnating:

1. Bu proyektni o'zingizning kompyuteringizda yoki serverda yuklab oling.
2. Proyekt katalogiga o'ting `cd proyekt_nomi`.
3. Virtual muhitni yaratish uchun `python -m venv venv` komandasi orqali o'zingiz uchun yangi virtual muhit yarating.
4. Virtual muhitni faollashtirish uchun (Windows uchun) `venv\Scripts\activate`, (Mac/Linux uchun) `source venv/bin/activate` komandalarini ishga tushiring.
5. Proyektning talqinlarini o'rnatish uchun `pip install -r requirements.txt` komandasini bajarib chiqing.

## Sozlashlar

Proyekt sozlashlari:

1. `settings.py` faylini oching va proyekt sozlashlarini sozlang.
2. Ma'lumotlar bazasini o'rnatish va migroatsiyalarni bajarish uchun `python manage.py migrate` komandasini ishga tushiring.

## Ishga tushirish

Proyektni ishga tushirish:

1. `python manage.py runserver` komandasi orqali loyihani ishga tushiring.
2. Brauzeringizda [http://http://127.0.0.1:8000/api/](http://localhost:8000/api/) manzilini oching va API ga kirishingiz mumkin.


# Appoinment API

API yordamida yangi nomzodlarni qo'shish, mavjud nomzodlarni ko'rish, bitta nomzodni olish va nomzod identifikatorlari saqlash mumkin.

## Endpointlar

- `POST /api/`: Yangi nomzod qo'shish uchun
- `GET /list/`: Barcha nomzodlarni ko'rish uchun
- `GET /api/<id>/`: Bitta nomzodni ko'rish uchun (nomzod ID sifatida)

## Ma'lumotlar Modeli

### Nomzod (Appointment)

- `id`: Nomzodning unikal ID si (integer)
- `identifier`: Nomzod identifikatori (tibbiy tashkilot yoki tibbiy xizmat turi) uchun o'zgaruvchi
  - `system`: Identifikator tizimi uchun URL manzil (string)
  - `value`: Identifikator qiymati (string)
- `patient`: Nomzodning identifikatori (tibbiy tashkilot yoki tibbiy xizmat turi) uchun o'zgaruvchi (string)
- `practitioner`: Nomzodning davolovchi identifikatori (tibbiy tashkilot yoki tibbiy xizmat turi) uchun o'zgaruvchi (string)
- `organization`: Nomzodning tashkilot identifikatori (tibbiy tashkilot yoki tibbiy xizmat turi) uchun o'zgaruvchi (string)


 ## Qo'llanmalar
Bu proyekt yaratishda quyidagi qo'llanmalardan foydalanildi:

Django Framework
Django REST framework