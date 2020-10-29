#!/usr/bin/env sage

from public_key import n,e

from sage.all import GF, PolynomialRing
from binascii import hexlify
from Crypto.Util.number import long_to_bytes

P=PolynomialRing(GF(2),'x')
n_poly = P(n)
R.<a> = GF(2**2049)

f_enc = [block for block in open('secret','rb').read().split(b'\n'*3) if block != b'']
c_int = [Integer(hexlify(ciphertext), 16) for ciphertext in f_enc]

plaintext = b''
(p,_), (q,_) = factor(n_poly)

for idx in c_int:
    c_poly = P(R.fetch_int(idx))
    phi = (2**p.degree() - 1) * (2**q.degree() - 1)
    d = ZZ(Mod(e,phi)**-1)
    f_poly = pow(c_poly, d, n_poly)
    plaintext += long_to_bytes(R(f_poly).integer_representation())

print(plaintext)
