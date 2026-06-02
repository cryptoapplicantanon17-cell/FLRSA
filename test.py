from src.keygen import generate_flrsa_keys
from src.cipher import encrypt
from src.decipher import decrypt_flrsa
import time
def standarddecrypt(cyphertext, private_key):
    d = private_key['d']
    n = private_key['n']
    # Standard RSA decipher
    return pow(cyphertext, d, n)
def run_test():
   
    print("--- FLRSA keys generator (1024 bits) ---")
    
    pub, priv = generate_flrsa_keys(1024)
   
    #print(f"Keys generated at {time.time() - start:.2f}s")
    
    message = 123456789
   
    print(f"\nOriginal message : {message}")
    
    # Cypher
    c = encrypt(message, pub)
   
    print(f"cyphertext (begin) : {str(c)[:50]}...")
    
    # FLRSA decypher
    start_dec = time.perf_counter_ns()
    m_decoded = decrypt_flrsa(c, priv)
    end_dec = time.perf_counter_ns()
    start_dec1 = time.perf_counter_ns()
    m_decoded1 = standarddecrypt(c,priv)
    end_dec1 = time.perf_counter_ns()
    ratiodec = (end_dec1-start_dec1)/(end_dec-start_dec)
    
    
    print(f"\nDecyphered message with FLRSA : {m_decoded}")
    print(f"FLRSA decypher time: {end_dec - start_dec:.6f}")
    print(f"\nStandard Decyphered message : {m_decoded1}")
    print(f"Standard decypher time: {end_dec1 - start_dec1:.6f}")
    print("ratio:",ratiodec)
    if message == m_decoded:
      
        print("\nSUCCES : binomial decypher works !")
    else:
       
        print("\n FAILED : Error in computation.")

if __name__ == "__main__":
    run_test()
