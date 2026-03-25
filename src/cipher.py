def encrypt(message, public_key):
    e = public_key['e']
    n = public_key['n']
    # Standard RSA cipher
    return pow(message, e, n)
