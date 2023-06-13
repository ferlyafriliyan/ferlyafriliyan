# --- [ RECODE TERUS SAMPE MAMPUS ] --- #
try:
    import os
    from Crypto.Cipher import AES
    from Crypto.Random import get_random_bytes
    import marshal
    import zlib
    import base64
    from pathlib import Path

    def encrypt_hyperion(input_file, output_file, key):
        chunk_size = 64 * 1024
        iv = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_CBC, iv)

        with open(input_file, 'rb') as file_in:
            with open(output_file, 'wb') as file_out:
                file_out.write(iv)
                while True:
                    chunk = file_in.read(chunk_size)
                    if len(chunk) == 0:
                        break
                    elif len(chunk) % 16 != 0:
                        chunk += b' ' * (16 - (len(chunk) % 16))
                    encrypted_chunk = cipher.encrypt(chunk)
                    file_out.write(encrypted_chunk)

    def decrypt_marshal(input_file, output_file, key):
        with open(input_file, 'rb') as file_in:
            data = file_in.read()
            decrypted_data = marshal.loads(data)
        
        with open(output_file, 'wb') as file_out:
            file_out.write(decrypted_data)

    def decrypt_lambda(input_file, output_file, key):
        with open(input_file, 'rb') as file_in:
            data = file_in.read()
            decrypted_data = eval(lambda data: zlib.decompress(base64.b64decode(data)).decode())(data)
        
        with open(output_file, 'w') as file_out:
            file_out.write(decrypted_data)

    def main():
        logo = '''
        .___.   .__        __         .__    .__        ___.          .__        ___.                 
        |   | __|__| _____/  |_  ____ |  |__ |__| ____  \_ |__   ____ |__| ______\_ |__   ___________ 
        |   |/ __ |\__  \\   __\/ __ \|  |  \|  |/ ___\  | __ \_/ __ \|  |/  ___/ | __ \_/ __ \_  __ \
        |   / /_/ | / __ \|  | \  ___/|   Y  \  \  \___  | \_\ \  ___/|  |\___ \  | \_\ \  ___/|  | \/
        |___\____ |(____  /__|  \___  >___|  /__|\___  > |___  /\___  >__/____  > |___  /\___  >__|   
                \/     \/          \/     \/        \/      \/     \/        \/      \/     \/       
        '''
        print(logo)

        print("Menu:")
        print("1. Encrypt File")
        print("2. Decrypt Marshal")
        print("3. Decrypt Lambda Marshal Zlib Base64")
        print("4. Encrypt Hyperion")
        choice = input("Select an option (1/2/3/4): ")
    
        if choice == '1':
            input_file = input("Masukkan jalur file input: ")
            output_file = input("Masukkan jalur file output: ")
            key = b'0123456789ABCDEF'
            
            # Mendapatkan jalur absolut dari input_file dan output_file
            input_path = Path(input_file).resolve()
            output_path = Path(output_file).resolve()
            
            encrypt_file(str(input_path), str(output_path), key)
            print("File successfully encrypted.")
        elif choice == '2':
            input_file = input("Masukkan jalur file input: ")
            output_file = input("Masukkan jalur file output: ")
            key = b'0123456789ABCDEF' 
            
            # Mendapatkan jalur absolut dari input_file dan output_file
            input_path = Path(input_file).resolve()
            output_path = Path(output_file).resolve()
            
            decrypt_marshal(str(input_path), str(output_path), key)
            print("File successfully decrypted using marshal.")
        elif choice == '3':
            input_file = input("Masukkan jalur file input: ")
            output_file = input("Masukkan jalur file output: ")
            key = b'0123456789ABCDEF' 
            
            # Mendapatkan jalur absolut dari input_file dan output_file
            input_path = Path(input_file).resolve()
            output_path = Path(output_file).resolve()
            
            decrypt_lambda(str(input_path), str(output_path), key)
            print("File successfully decrypted using lambda marshal zlib base64.")
        elif choice == '4':
            input_file = input("Masukkan jalur file input: ")
            output_file = input("Masukkan jalur file output: ")
            key = b'0123456789ABCDEF' 
            
            # Mendapatkan jalur absolut dari input_file dan output_file
            input_path = Path(input_file).resolve()
            output_path = Path(output_file).resolve()
            
            encrypt_hyperion(str(input_path), str(output_path), key)
            print("File successfully encrypted using Hyperion.")
        else:
            print("The option you selected is invalid.")

    if __name__ == '__main__':
        main()

except ImportError:
    print("The pycryptodome module is not installed. Please install the module by running the command: [pip install pycryptodome].")
except Exception as e:
    print("An error occurred while executing file encryption:", str(e))
