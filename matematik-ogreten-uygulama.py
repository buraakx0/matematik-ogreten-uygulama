girdi = int(input("Lütfen bir seçenek belirtiniz:\n\n1 - Toplama İşlemleri\n2 - Çıkarma İşlemleri\n3 - Çarpma İşlemleri\n\nSeçeneğinizi giriniz: "))

# toplama
soru1 = "10 + 22"
soru2 = "9 + 18"
soru3 = "98 + 56"
soru4 = "13 + 49"
soru5 = "52 + 63"
cevap1 = 32
cevap2 = 27
cevap3 = 156
cevap4 = 62
cevap5 = 115
# cikarma 
sorucikart = "20 - 8"
sorucikart1 = "215 - 29"
sorucikart2 = "89 - 52"
sorucikart3 = "8 - 51"
sorucikart4 = "287 - 96"
cevapc1 = 12
cevapc2 = 186
cevapc3 = 37 
cevapc4 = -43
cevapc5 = 191

if girdi == 1:
    toplama1 = int(input("{} işleminin sonucu nedir? ".format(soru1)))
    toplama1 == cevap1 and print("Cevap Doğru!")
    toplama1 != cevap1 and print("Cevabınız yanlış! Doğru cevap: {}".format(cevap1))

    toplama2 = int(input("{} işleminin sonucu nedir? ".format(soru2)))
    toplama2 == cevap2 and print("Cevap Doğru!")
    toplama2 != cevap2 and print("Cevabınız yanlış! Doğru cevap: {}".format(cevap2))

    toplama3 = int(input("{} işleminin sonucu nedir? ".format(soru3)))
    toplama3 == cevap3 and print("Cevap Doğru!")
    toplama3 != cevap3 and print("Cevabınız yanlış! Doğru cevap: {}".format(cevap3))

    toplama4 = int(input("{} işleminin sonucu nedir? ".format(soru4)))
    toplama4 == cevap4 and print("Cevap Doğru!")
    toplama4 != cevap4 and print("Cevabınız yanlış! Doğru cevap: {}".format(cevap4))

    toplama5 = int(input("{} işleminin sonucu nedir? ".format(soru5)))
    toplama5 == cevap5 and print("Cevap Doğru!")
    toplama5 != cevap5 and print("Cevabınız yanlış! Doğru cevap: {}".format(cevap5))

if girdi == 2:
    cikarma1 = int(input("{} işleminin sonucu nedir? ".format(sorucikart)))
    cikarma1 == cevapc1 and print("Cevap Doğru!") 
    cikarma1 != cevapc1 and print("Cevabınız yanlış! Doğru cevap: {}".format(cevapc1))

    cikarma2 = int(input("{} işleminin sonucu nedir? ".format(sorucikart1)))
    cikarma2 == cevapc2 and print("Cevap Doğru!") 
    cikarma2 != cevapc2 and print("Cevabınız yanlış! Doğru cevap: {}".format(cevapc2))

    cikarma3 = int(input("{} işleminin sonucu nedir? ".format(sorucikart2)))
    cikarma3 == cevapc3 and print("Cevap Doğru!") 
    cikarma3 != cevapc3 and print("Cevabınız yanlış! Doğru cevap: {}".format(cevapc3))

    cikarma4 = int(input("{} işleminin sonucu nedir? ".format(sorucikart3)))
    cikarma4 == cevapc4 and print("Cevap Doğru!") 
    cikarma4 != cevapc4 and print("Cevabınız yanlış! Doğru cevap: {}".format(cevapc4))

    cikarma5 = int(input("{} işleminin sonucu nedir? ".format(sorucikart4)))
    cikarma5 == cevapc5 and print("Cevap Doğru!")
    cikarma5 != cevapc5 and print("Cevabınız yanlış! Doğru cevap: {}".format(cevapc5))

if girdi == 3:
    print("yakında eklenecek :)")

# python matematik-ögreten-uygulama.py buraak <3
