username = "informatika"
password = "12345678"

for i in range(3):
    input_username = input("Masukkan username : ")
    input_password = input("Masukkan password : ")
    
    if input_username == username and input_password == password:
        print("Login berhasil!")
        break
    else:
        print("Username atau password salah coba lagi")
        
if i == 2:
    print("Akun diblokir.")
