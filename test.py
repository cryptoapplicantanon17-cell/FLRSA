from src.keygen import generate_flrsa_keys
from src.cipher import encrypt
from src.decipher import decrypt_flrsa
import time

def run_test():
   
    print("--- FLRSA keys generator (1024 bits) ---")
    start = time.time()
    pub, priv = generate_flrsa_keys(1024)
   
    print(f"Keys generated at {time.time() - start:.2f}s")
    
    message = 123456789
   
    print(f"\nOriginal message : {message}")
    
    # Cypher
    c = encrypt(message, pub)
   
    print(f"cyphertext (begin) : {str(c)[:50]}...")
    
    # FLRSA decypher
    start_dec = time.time()
    m_decoded = decrypt_flrsa(c, priv)
    end_dec = time.time()
    
    print(f"\nDecyphered message : {m_decoded}")
    print(f"FLRSA decypher time: {end_dec - start_dec:.6f}s")
    
    if message == m_decoded:
      
        print("\nSUCCES : binomial decypher works !")
    else:
       
        print("\n FAILED : Error in computation.")

if __name__ == "__main__":
    run_test()
