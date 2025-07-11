import itertools 
import string 
import time  

def brute_force_password(target_password):
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits 

    start_time = time.time()
    
    for password_length in range (3, 4):    
        for guess in itertools.product(characters, repeat=password_length):
            guess_password = ''.join(guess)
            print(f"mencoba : {guess_password}") 
            
            if guess_password == target_password:
                end_time = time.time()
                print(f"password ditemukan : {guess_password}")
                print(f"password ditemukan dalam : {end_time-start_time:.2f}detik")
                return guess_password
            
        print(f"password tidak ditemukan dalam waktu yang ditentukan")
        return None
    
target_password = "Ac2" 
brute_force_password(target_password) 

