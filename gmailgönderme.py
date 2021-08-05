import smtplib


def GmailSender(user,mesaj,konu):
    sender_email = "Gönderen Mail" #Mesaj Gönderecek Olan Mail
    rec_email = "Gönderilen Mail veya Mailler" #Birden fazla mail eklenicekse liste şeklinde eklenmelidir.
    password = "Gönderen şifre" #Mesaj Gönderen Mailin Şifresi

    subject = konu
    content = "Siteismi'nden,\n{} kullanıcısının,\nSize bir mesajı var!\n\n{}".format(user,mesaj) #Mesajın içeriği

    message = "Subject : {}\n\n{}".format(subject,content) # mesajın gönderilmeye hazır son hali
    realmessage = message.encode("utf-8")

    mail = smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login(sender_email,password)
    mail.sendmail(sender_email,rec_email,realmessage)


GmailSender() #Bu fonksiyon kullanılacak olan view'a import edilmeli ve (kullanıcıadı,mesaj,konu) şeklinde değerler atanmalıdır.








