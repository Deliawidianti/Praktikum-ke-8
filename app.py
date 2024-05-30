import pandas as pd
#variabel yang berulang menggunakan list/matriks
list_nim=[]
list_nama=[]
list_uts=[]
list_uas=[]
list_total=[]

ulang=5
for i in range(ulang) :
    print("Data ke -" + str(i+1))
    list_nim.append(input('Nim :'))
    list_nama.append(input("Nama :"))
    list_uts.append(input("Nilai UTS : "))
    list_uas.append(input("Nilai UAS :"))
#PROSES
for i in range(ulang) :
    list_total.append((list_uas[i] + list_uts[i])/ 2)

tamu= {
    "Nim" :list_nim,
    "Nama Lengkap" : list_nama,
    "Nilai UTS" : list_uts,
    "Nilai UAS" : list_uas,
    "Rata-rata" : list_total
}
data_tamu = pd.DataFrame(tamu)
#cetak
print("============================ Daftar Nilai ============================ ")
print(data_tamu)
print("====================================================================== ")