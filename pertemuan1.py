import random
import time

angka_random = random.randint(1, 100)
jml_tebakan = 0
game = True

tebakan_angka = []
print("Selamat datang di permainan tebak angka!")
print("Silahkan tebak angka antara 1 hingga 100, kesempatan anda hanya 5 kali")

while game:
    
    tebakan = int(input("\nTebak angka anda: "))
    tebakan_angka.append(tebakan)
    time.sleep(0.5)


            
    if jml_tebakan == 4 and tebakan != angka_random:
        print(f"Kesempatan anda habis. Angka yang dicari adalah {angka_random}")
        print(f"Terimakasih telah bermain!")

        mainlagi = input("Apakah anda ingin bermain lagi? (y/n): ")  
        if mainlagi.lower() == 'y':
            print("\nMemulai permainan baru...")
            time.sleep(1)
            angka_random = random.randint(1, 100)
            print("Angka telah diacak kembali!")
            jml_tebakan = 0
            tebakan_angka = []
            game = True


        elif mainlagi.lower() == 'n':
            game = False
        
    elif tebakan < 1 or tebakan > 100:
        print("Tebakan harus antara 1 hingga 100, coba lagi!\n")
    

    elif tebakan < angka_random:
        print("Tebakan terlalu rendah, coba lagi!")
        jml_tebakan += 1
        
        print(f"Kesempatan tersisa: {5 - jml_tebakan}\n")
        print("Angka yang sudah anda coba: ")
        for angka in tebakan_angka:
            print(angka, end=" ")

        
        

    elif tebakan > angka_random:
        print("Tebakan terlalu tinggi, coba lagi!")
        jml_tebakan += 1
        
        print(f"Kesempatan tersisa: {5 - jml_tebakan}\n")
        print("Angka yang sudah anda coba: ", end=" ")
        for angka in tebakan_angka:
            print(angka, end=" ")

            
        
    elif tebakan == angka_random:
        print(f"Selamat! terbakan anda benar, angka yang dicari adalah {angka_random}")  
        print(f"Anda berhasil menebak dalam {jml_tebakan+1} tebakan")
        mainlagi = input("Apakah anda ingin bermain lagi? (y/n): \n")  
        if mainlagi.lower() == 'y':

            print("\nMemulai permainan baru...")
            time.sleep(1)
            angka_random = random.randint(1, 100)
            print("Angka telah diacak kembali!")
            jml_tebakan = 0
            tebakan_angka = []
            game = True
        
        elif mainlagi.lower() == 'n':
            game = False


