print("==================== KASIR ====================")
total = 0

while True :
    harga = int(input('Harga Barang :'))
    b = input("Apakah anda membeli barang lagi? [yes/no] : ")
    total += harga
    if b == 'no':
        print("TOTAL BELANJA :", total)
        break
    elif b == 'tidak': 
        print("INVALID")
        break
