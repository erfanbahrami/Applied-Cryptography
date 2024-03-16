import os, hashlib

hash_fnc=lambda x:hashlib.sha3_224(x).digest()

class LamportSignature:
    K=len(hash_fnc(b''))*8 # digest length
    def sign(sign_key, m):
        h = hash_fnc(m)
        K = len(h) * 8
        assert len(sign_key) == 2 * K, "private key and message digest length mismatch"
        # convert to binary and add leading zeros if needed
        h = bin(int.from_bytes(h, "big"))[2:].zfill(K)
        # create signature
        signature = []
        for i in range(K):
            signature.append(sign_key[2 * i + int(h[i])])
        return signature

    def verify(verify_key, m, signature):
        flag = True
        h = hash_fnc(m)
        K = len(h) * 8
        assert len(verify_key) == 2 * K, "public key and message digest length mismatch"
        assert len(signature) == K, "signature and message digest length mismatch"
        h = bin(int.from_bytes(h, "big"))[2:].zfill(K)
        for i in range( K ):
            check = hash_fnc( signature[i] )
            if verify_key[ 2 * i + int(h[i]) ] != check :
                flag = False   
        return flag


if __name__ == "__main__":
    K = LamportSignature.K  # digest length
    verify_key = [bytes.fromhex(x) for x in open("C:\\Users\\ErF\\Desktop\\vk.txt").read().split()]

    print("************************************** message 1 **************************************")
    msg = open("C:\\Users\\ErF\\Desktop\\msg1.txt", "rb").read()
    sig = [bytes.fromhex(x) for x in open("C:\\Users\\ErF\\Desktop\\sig1.txt").read().split()]
    print("verify msg.txt:", LamportSignature.verify(verify_key, msg, sig))

    print("************************************** message 2 **************************************")
    msg = open("C:\\Users\\ErF\\Desktop\\msg2.txt", "rb").read()
    sig = [bytes.fromhex(x) for x in open("C:\\Users\\ErF\\Desktop\\sig2.txt").read().split()]
    print("verify msg.txt:", LamportSignature.verify(verify_key, msg, sig))

    print("************************************** message 3 **************************************")
    msg = open("C:\\Users\\ErF\\Desktop\\msg3.txt", "rb").read()
    sig = [bytes.fromhex(x) for x in open("C:\\Users\\ErF\\Desktop\\sig3.txt").read().split()]
    print("verify msg.txt:", LamportSignature.verify(verify_key, msg, sig))

    print("************************************** message 4 **************************************")
    msg = open("C:\\Users\\ErF\\Desktop\\msg4.txt", "rb").read()
    sig = [bytes.fromhex(x) for x in open("C:\\Users\\ErF\\Desktop\\sig4.txt").read().split()]
    print("verify msg.txt:", LamportSignature.verify(verify_key, msg, sig))

    print("************************************** message 5 **************************************")
    msg = open("C:\\Users\\ErF\\Desktop\\msg5.txt", "rb").read()
    sig = [bytes.fromhex(x) for x in open("C:\\Users\\ErF\\Desktop\\sig5.txt").read().split()]
    print("verify msg.txt:", LamportSignature.verify(verify_key, msg, sig))
