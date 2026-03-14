import random
tinggi_daun = 28
tinggi_batang = 10

# warna
merah = "\033[31m"
coklat = "\033[38;2;139;69;19m"
hijau = "\033[32m"
kuning = "\033[33m"
biru = "\033[34m"
tutup = "\033[0m"

pola_daun = ["^", "^", "^", "🔴", "🔵", "🟡"]

for i in range(tinggi_daun):
    spasi = " " * (tinggi_daun - i)

    if i == 0:
        print(spasi + "⭐")
    else:
        baris_daun = []
        sebelumnya = None

        for k in range(2 * i + 2):
            baris_sekarang = random.choice(pola_daun)

            # agar bola tidak berdempetan
            if sebelumnya in ["🔴","🔵","🟡"] and baris_sekarang in ["🔴","🔵","🟡"]:
                baris_sekarang = "^"

            if baris_sekarang == "^":
                baris_daun.append(hijau + "^" + tutup)

            elif baris_sekarang == "🔴":
                baris_daun.append(merah + "●" + tutup)

            elif baris_sekarang == "🔵":
                baris_daun.append(biru + "●" + tutup)

            elif baris_sekarang == "🟡":
                baris_daun.append(kuning + "●" + tutup)

            sebelumnya = baris_sekarang

        print(spasi + "".join(baris_daun))

for j in range(tinggi_batang):
    spasi = " " * tinggi_daun
    batang = coklat + "|" * 3 + tutup
    print(spasi + batang)