import os, string , math

class PRNG:
    """
    standard java.util.Random implemented with python
    """
    M = 2**48 # modulus
    A = 25214903917 # multiplier
    C = 11 # increment
    def __init__(self , seed):
        self.s = (seed ^ PRNG.A) % PRNG.M
    def random_number(self):
        self.s = (PRNG.A * self.s + PRNG.C) % PRNG.M
        return self.s >> 16
    def random_bytes(self , n):
        return b"".join(
            self.random_number().to_bytes(4, "little")
            for _ in range(math.ceil(n / 4)))[:n]
    
FILE = "random.png"
seed = int.from_bytes(os.urandom(6), "little")
prng = PRNG(seed)
with open(FILE , "rb") as f:
    b = f.read()
otp = prng.random_bytes(len(b))
c = bytes(b[i] ^ otp[i] for i in range(len(b)))
with open(FILE + ".enc", "wb") as f:
    f.write(c)