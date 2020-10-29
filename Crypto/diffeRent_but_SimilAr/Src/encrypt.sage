#!/usr/bin/env sage

from public_key import e, n
from secret import secret

from binascii import hexlify
from sage.all import GF, PolynomialRing
from Crypto.Util.number import long_to_bytes, bytes_to_long

P=PolynomialRing(GF(2),'x')
n_poly = P(n)
R.<a> = GF(2^2049)

ciphertext = b''

for idx in secret:
    idx_int = bytes_to_long(idx.encode())
    idx_poly = P(R.fetch_int(idx_int))
    c_idx_poly = pow(idx_poly, e, n_poly)
    c_idx_int = R(c_idx_poly).integer_representation()
    ciphertext += long_to_bytes(c_idx_int) + b'\n'*3

open('secret', 'wb').write(ciphertext)
