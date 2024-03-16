**In this repository, some practical questions of the applied cryptography course are placed with their code.**

**Question1:**

Byte-based Vigenère cipher encryption is used to secure the HTTP protocol. The key used in this type of encryption is an arbitrary byte string XORed with each word of the desired text. In this question, suppose the key used is smaller than the size of the text. The hex representation of a request and its response is provided to you in encrypted form. Decrypt them.

> *request=* 3cc6ed9d907b0dfdaa829948a6901986e9b454a875951dd21a9958a8625c53cfe197dafa94c1be76a14d02fe1934c1cf157a5d10e1315ee8db77bba806b8d15c90838c774cba86c4ba596be7be8e8509ae9318dea4aa15f1368662be78ef07f83f1e29aadb9c94cff1a6b26eeb613afe182ed08e027a
>
> *response=*
> 24ddea999f654fa3edd8c754efad1886b1d550a860c7588c0da619ed29032ae8e599c7e9db80ba64b51e0cfe6657f48404336b72841958e3953298b34490d857a492973e05e6d0f4ca2255e0f48dcf08ad8a4491f4ad14f162dd3ab72ba246fb7d0565e5d999dde693cee621fc5b09ea1938aaeb7d14  

---------------------------------------------------------------------------------------------------

**Question2:**

A file in PNG format encrypted with the Pseudo One-Time Pad method and named random.png.enc is attached to the exercise. Below is the code to encrypt the file, including the PRG used. Decrypt the file.

-------------------------------------------

**Question3:**

Implementation of Lamport Signatures in python and checking the correctness of 5 given signatures

--------------------------

**Question4:**

In this question, we are going to use one of the famous elliptical bends called *secp192r1*. To solve this exercise, you can use the *tinyec* library. Elliptic curves can be defined with different forms, one of the most famous of which is the *Weierstrass normal form*.

**1.** For the above curve, write the values of $a$ and $b$​ in the *Weierstrass form* and write the equation of the curve.

**2.** Find a point like $G=(x,y)$ on this curve that starts with your student number (if your student number is not there, you can add new low-value digits; for example, instead of $studentno$, put the value of $10 ∗ studentno$ and check if there is a point With this $x$ can be on the curve or not and continue this process until you find a point on the curve where the decimal display starts with your student number.

**3.** Find the value of $2G$ and $s.G$ on the curve where $s$ is your student number.

**4.** Encrypt the $sG$ point using the $kG$ point as the public key and a random $r$ using the [ElGamal encryption](https://en.wikipedia.org/wiki/ElGamal_encryption). Note that $k$ here means the private key and it must be randomly generated.

**5.** Decrypt the encrypted message in the previous part using the private key $k$.

----------------------------------------------------

**Question5:**

Paillier cryptosystem is one of the asymmetric encryption algorithms which is famous for its additive (partial) homomorphic feature. In this system, it is possible to calculate the sum of two numbers only by having their encrypted value. In the following, the algorithms of this design are defined:

*Key generation:* Similar to RSA, first, two numbers, p and q, are generated. Then consider $n = pq$ , $g = 1 + n$ , $\lambda = ϕ(n)$ and $\lambda = \lambda^{-1}\mod n$. the public key and private key is $(n,g)$ and $(\lambda,\mu)$ respectively.

*Encryption:* To encrypt $0 ≤ m < n$  , first a random number $0 < r < n$ is generated and the encrypted text is queal to $c = g^{m}r^{n} \mod n^{2}  $​

*Decryption*: The message is calculated as $m = ⌊(c^{λ} \mod n^{2})/n⌋\mu \mod n$ .

**1.** $c_0$ and $c_1$ are the encrypted values of two messages $m_0$, $m_1$ with the public key $(n,g)$. Find the encrypted value of $m_0 + m_1$ using the additive homomorphic feature in Paillier cryptosystem.

> $c_0$ = 1431135290069325008583005767760440194352250669868642015637284664827863096526854295290213163196780672778228721128052234092877469782343204440819088345226674  
>
> $c_1$ = 766502765098026355380112715536128541917607723218993231191798626637402444561652254317663096357141828249072007319292850196436742539757315839907222753619573  
>
> n = 61186929436230855420766379500946377903931541699202551225466267001310907409761  

**2.** In this scheme, if the value of r used is revealed, it is possible to decrypt without having the private key. Decrypt the message $c$ with the given public key and the random value $r$.

> c = 1857855433435253966261472405564630068207257435599367652422302291177346557860873816680098602083496236349568385254262863758166153798362744023058732538696778
>
> r = 14935127747067141332266439078227426312235659727377265398012065621101840712218
>
> n = 70700063534546514342061240350548864227722633715593560476868914510092441292783  

--------------------------------------------

**Question6:**

