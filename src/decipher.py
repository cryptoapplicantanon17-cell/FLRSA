def decrypt_flrsa(ciphertext, priv):
   """
    Optimized FLRSA Decryption (Version 1.1.0)
    Removal of inv2 by expanding consecutive terms (c^3 - c).
    """
    # Private key parameters extraction
   n = priv['n']
   B2 = priv['B2']
   inv6 = priv['inv6']
   delta = priv['delta']

   c = ciphertext

    # 1. Cubic term calculation: (c^3 - c) MOD n
    # The product of three consecutive integers (c-1)c(c+1) becomes c^3 - c
    # This value is mathematically always divisible by 6
   c_cube_minus_c = (pow(c, 3, n) - c) % n

    # 2. Applying the simplified formula without inv2
    # m_d0 = c + B2 * [(c^3 - c) / 6]
   term_optimized = (B2 * c_cube_minus_c * inv6) % n
   m_d0 = (c + term_optimized) % n

    # 3. Final delta correction application
    # m = m_d0 * c^delta MOD n
   m = (m_d0 * pow(c, delta, n)) % n
   
   return m

