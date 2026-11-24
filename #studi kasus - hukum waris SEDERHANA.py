 #studi kasus - hukum waris SEDERHANA


 #aturan hukum waris sederhana menggunakan pemograman python
 #1. jika ahli waris adalah anak laki - laki, mendapat 2 bagian
 #2. jika asli waris adalah anak prempuan, mendapat 1 bagian
 #3. pemograman meminta jumlah anak laki -laki dan jumlah anak prempuan
 #4. progam menghitung bagian masing - masing ahli waris
 
print("===progam pembagian waris sederhana ===")
warisan = int(input("masukan jumlah harta warisan : Rp "))
lk = int(input("jumlah anak - laki : "))
pr = int(input("jumlah anak prempuan : "))

#menghitung jumlah bagian
bagian_lk = lk * 2
bagian_pr = pr * 1
total_bagian = bagian_lk + bagian_pr

#percabangan waris
if total_bagian > 0:
    nilai_bagian = warisan / total_bagian
    
    print("\n== HASIL PEMBAGIAN")
if lk > 0:
    print("setiap anak laki - laki mendapat Rp",int(nilai_bagian*2))

if pr > 0:
    print("setiap anak prempuan mendapat Rp",int(nilai_bagian))

else:
    print("tidak ada ahli waris")
    