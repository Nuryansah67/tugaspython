def hitung_diskon(harga, persen_diskon):
    return harga - (harga * persen_diskon / 100)

def info_produk(nama, harga):
    if harga > 200000:
        harga_diskon = hitung_diskon(harga, 20)
    elif harga >= 100000:
        harga_diskon = hitung_diskon(harga, 10)
    else:
        harga_diskon = hitung_diskon(harga, 5)
    print(f"{nama} | harga asli: {harga} | setelah diskon: {harga_diskon}")

info_produk("jaket", 250000)    
info_produk("kemeja", 120000)
info_produk("kaos", 80000)
info_produk("sepatu", 200000)

        
    
