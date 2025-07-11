import hashlib 

def hash_file(filename):
    try :
        with open(filename, "rb") as f:
            file_hash =hashlib.md5()
            while chunk := f.read(8193):
                file_hash.update(chunk)
            return file_hash.hexdigest()
    except FileNotFoundError :
        return "File tidak ditemukan "

filename = input("masukan nama file : ")
print(hash_file(filename))  