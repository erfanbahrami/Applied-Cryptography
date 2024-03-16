import os, string, math

class PRNG:
    """
    standard java.util.Random implemented with python
    """
    M = 2**48  # modulus
    A = 25214903917  # multiplier
    C = 11  # increment

    def __init__(self, seed):
        self.s = (seed ^ PRNG.A) % PRNG.M

    def random_number(self):
        self.s = (PRNG.A * self.s + PRNG.C) % PRNG.M
        return self.s >> 16

    def random_bytes(self, n):
        return b"".join(
            self.random_number().to_bytes(4, "little") for _ in range(math.ceil(n / 4))
        )[:n]

M = 2**48  # modulus
A = 25214903917  # multiplier
C = 11  # increment

def decryptor(current):
        next = (A * current + C) % M
        return next 

file_encrypted = "C:\\Users\\ErF\\Desktop\\random.png.enc"
signiture = b"\x89\x50\x4e\x47\x0d\x0a\x1a\x0a"

with open( file_encrypted , "rb") as f:
    b = f.read()

s1_prim = bytes(b[i] ^ signiture[i] for i in range(4))
s2_prim = bytes(b[i+4] ^ signiture[i+4] for i in range(4))

reversed_data = s1_prim[::-1]
s1_prim = reversed_data

reversed_data = s2_prim[::-1]
s2_prim = reversed_data

for i in range (2 ** 16):
    s1 = b"0"
    s1 = s1_prim + (i.to_bytes(2, "little"))
    s2 =(A * int.from_bytes(s1,"big") + C ) % M
    s2_prim_t = s2 >> 16
    s2_prim_t = s2_prim_t.to_bytes(4,"big")
    if s2_prim == s2_prim_t :
        plaintext = b"\x89\x50\x4e\x47\x0d\x0a\x1a\x0a"
        current = s2
        for i in range(math.ceil(len(b) / 4)-2):
            next = decryptor(current)
            next_copy = next
            next = (next >> 16).to_bytes(4,"little")
            plaintext += bytes(b[4*i+8+j] ^ next[j] for j in range(4) if 4*i+8+j < len(b))
            current = next_copy

file_decrypted = "C:\\Users\\ErF\\Desktop\\aa.png"
with open(file_decrypted , "wb") as f:
    f.write(plaintext)




