#ketentuan

#1. istri mendapat 1/8 bagian
#2. sisa harta setelah bagian istri diberikan kepada anak 
#3. anak laki - laki dapat 2 bagian 
#4. anak perempuan dapat 1 bagian 
#program input jumlah anak laki - laki dan jumlah anak perempuan

print("=== PROGRAM PEMBAGIAN WARISAN ===")

#program input
warisan = int(input("Masukan jumlah harta Warisan: Rp"))
lk = int(input("jumlah anak Laki-laki: "))
pr = int(input("jumlah anak perempuan: "))

#menghitung jumlah pembagian
bagian|_istri = warisan * 1/8
bagian_lk = lk * 2
bagian_pr = pr * 1
total_bagian = bagian_lk + bagian_pr
sisa_warisan = warisan + bagian_istri

#percabangan waris
if total_bagian > 0:
    nilai_bagian = sisa_warisan / total_bagian
    
print("harta warisan bagian istri: Rp", int(bagian_istri))
print("sisa harta warisan: Rp", int(sisa_warisan))

print("\n=== HASIL PEMBAGIAN ===")
if bagian_istri > 0:
    print("bagian istri mendapat: Rp", int(bagian_istri))
if lk > 0:
    print("setiap anak laki-laki mendapat: Rp", int(nilai_bagian *2))
if pr >        
