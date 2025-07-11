import re  

def cek_password(password):
    if len(password) < 8 : 
        return "Lemah : Panjang harus lebih dari 8 bro/sis"
    elif not re.search("[a-z]",password):
        return "Lemah : Tidak ada huruf kecil bro/sis"
    elif not re.search("[A-Z]", password):
        return "Lemah : Tidak ada huruf besar bro/sis"
    elif not re.search("[0-9]", password):
        return "Lemah : Tidak ada angka di dalam nya bro/sis"
    elif not re.search("[_@$]", password):
        return "Lemah : Tidak ada simbol beuhh kecewa berat bro/sis"
    else :
        return "Terlalu OP bro/sis hati hati lupa loh :>" 

password = input("Masukan password : ")
print(cek_password(password))  