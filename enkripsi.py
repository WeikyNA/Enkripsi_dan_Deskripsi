plaintext = ['ABCDEFGH IJKLMNOPQRSTUVWXYZ.,?!1234567890']
kata = input('Masukkan Teks: ').upper()
kunci = int(input('Masukkan Kunci: '))
ce = []
m = []
de = []
pj = len(kata)
x = 0

for i in range(pj):
    m.append(kata[i])
    ce.append(plaintext[0].find(kata[i]))
    de.append(plaintext[0].find(kata[i]))
    x = (ce[i] + kunci) % 41
    s = ce[i]
    st = plaintext[0][x]

awal = s
chiper = x
chiperText = st

import matplotlib.pyplot as plt

plt.plot(x)
plt.grid(True)
plt.show()