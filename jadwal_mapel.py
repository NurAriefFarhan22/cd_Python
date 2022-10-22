print("Mencari jadwal harian")

print ("senin")
print ("selasa")
print ("rabu")
print ("kamis")
print ("jumat")
print("===========================")
hari = str(input("Pilih hari: "))
senin = ("senin")
selasa = ("selasa")
rabu = ("rabu")
kamis = ("kamis")
jumat = ("jumat")


if (hari == senin):
    print ("Indo, Sejarah, Inggris, Pkk, Paibp")
elif hari == selasa:
    print ("Prod, Pjok, Prod")
elif hari == rabu:
    print ("Indo, P5, Inggris")
elif hari == kamis:
    print ("Prod")
elif hari == jumat:
    print ("MTK, Prod, Pkn")
else:
    print ("Hari libur ^_^")