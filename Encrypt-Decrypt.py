#!/usr/bin/env python3
"""
Enhanced Encryption/Decryption Utility
Author: Kumar
Supports multiple encryption algorithms and enhanced security
"""

import base64
import hashlib
import os
import json
import time
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import secrets

class EnhancedCrypto:
    def __init__(self):
        self.algorithm = "AES-256-GCM"
        self.key_size = 32
        self.iv_size = 16
        
    def generate_key(self, password=None):
        """Generate encryption key with optional password"""
        if password:
            salt = os.urandom(16)
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=salt,
                iterations=100000,
            )
            key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
            return key, salt
        else:
            key = Fernet.generate_key()
            return key, None
    
    def encrypt_data(self, data, key, salt=None):
        """Encrypt data using the specified algorithm"""
        try:
            if isinstance(data, str):
                data = data.encode('utf-8')
            
            if isinstance(key, str):
                key = key.encode('utf-8')
            
            iv = os.urandom(self.iv_size)
            
            cipher = Cipher(
                algorithms.AES(key),
                modes.GCM(iv),
            )
            encryptor = cipher.encryptor()
            
            ciphertext = encryptor.update(data) + encryptor.finalize()
            tag = encryptor.tag
            
            encrypted_data = iv + tag + ciphertext
            
            return base64.b64encode(encrypted_data).decode('utf-8')
            
        except Exception as e:
            print(f"Encryption error: {e}")
            return None
    
    def decrypt_data(self, encrypted_data, key, salt=None):
        """Decrypt data using the specified algorithm"""
        try:
            if isinstance(key, str):
                key = key.encode('utf-8')
            
            encrypted_bytes = base64.b64decode(encrypted_data)
            
            iv = encrypted_bytes[:self.iv_size]
            tag = encrypted_bytes[self.iv_size:self.iv_size+16]
            ciphertext = encrypted_bytes[self.iv_size+16:]
            
            cipher = Cipher(
                algorithms.AES(key),
                modes.GCM(iv, tag),
            )
            decryptor = cipher.decryptor()
            
            decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
            
            return decrypted_data.decode('utf-8')
            
        except Exception as e:
            print(f"Decryption error: {e}")
            return None
    
    def encrypt_file(self, input_file, output_file, key, salt=None):
        """Encrypt a file"""
        try:
            with open(input_file, 'rb') as f:
                data = f.read()
            
            encrypted_data = self.encrypt_data(data, key, salt)
            
            if encrypted_data:
                with open(output_file, 'w') as f:
                    f.write(encrypted_data)
                print(f"[+] File encrypted successfully: {output_file}")
                return True
            else:
                print(f"[-] Failed to encrypt file: {input_file}")
                return False
                
        except Exception as e:
            print(f"[-] File encryption error: {e}")
            return False
    
    def decrypt_file(self, input_file, output_file, key, salt=None):
        """Decrypt a file"""
        try:
            with open(input_file, 'r') as f:
                encrypted_data = f.read()
            
            decrypted_data = self.decrypt_data(encrypted_data, key, salt)
            
            if decrypted_data:
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(decrypted_data)
                print(f"[+] File decrypted successfully: {output_file}")
                return True
            else:
                print(f"[-] Failed to decrypt file: {input_file}")
                return False
                
        except Exception as e:
            print(f"[-] File decryption error: {e}")
            return False

def main():
    """Main function for encryption/decryption operations"""
    crypto = EnhancedCrypto()
    
    print("🔐 Enhanced Encryption Utility")
    print("=" * 50)
    
    while True:
        print("\nOptions:")
        print("1. Encrypt file")
        print("2. Decrypt file")
        print("3. Generate new key")
        print("4. Exit")
        
        choice = input("\nSelect option (1-4): ").strip()
        
        if choice == "1":
            input_file = input("Enter input file path: ").strip()
            output_file = input("Enter output file path: ").strip()
            password = input("Enter encryption password (or press Enter for random key): ").strip()
            
            if password:
                key, salt = crypto.generate_key(password)
            else:
                key, salt = crypto.generate_key()
                print(f"Generated key: {key.decode()}")
                if salt:
                    print(f"Generated salt: {base64.b64encode(salt).decode()}")
            
            success = crypto.encrypt_file(input_file, output_file, key, salt)
            
        elif choice == "2":
            input_file = input("Enter encrypted file path: ").strip()
            output_file = input("Enter output file path: ").strip()
            key_input = input("Enter encryption key: ").strip()
            
            success = crypto.decrypt_file(input_file, output_file, key_input)
            
        elif choice == "3":
            password = input("Enter password for key derivation (or press Enter for random): ").strip()
            key, salt = crypto.generate_key(password if password else None)
            print(f"Generated key: {key.decode()}")
            if salt:
                print(f"Generated salt: {base64.b64encode(salt).decode()}")
                
        elif choice == "4":
            print("Goodbye!")
            break
            
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
