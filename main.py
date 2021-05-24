print("Sayı Tahmin oyununa hoşgeldiniz!")

number = 69

playerNumbers = int(input("0 ile 70 arasında bir sayı tahmin ediniz:"))

change = 2

while True:
    if change !=0:
        if playerNumbers > number:
            change -=1
            print(change, "hakkınız kaldı")
            playerNumbers = int(input("Daha küçük bir sayı giriniz:"))
        elif playerNumbers < number:
             change -=1
             print(change, "hakkınız kaldı")
             playerNumbers = int(input("Daha büyük bir sayı giriniz:"))
        
        if playerNumbers == number:
            print("Tebrikler oyunu kazandın!")
            break


    if change == 0:
        print("Üzgünüm oyunu kaybettiniz ötede ağlayabilirsiniz.")
        break
