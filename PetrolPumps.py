def truckTour(petrolpumps):
    n = len(petrolpumps)
    start = 0  # Menyimpan indeks titik awal tur yang memenuhi persyaratan
    petrol = 0  # Menyimpan jumlah bensin di tangki truk
    for i in range(n):
        petrol += petrolpumps[i][0] - petrolpumps[i][1]
        if petrol < 0:  # Jika bensin di tangki truk menjadi negatif
            start = i + 1  # Cobalah titik berikutnya sebagai titik awal tur
            petrol = 0  # Reset jumlah bensin di tangki truk
    return start
petrolpumps = [[1,5],[10,3],[3,4]]
print(truckTour(petrolpumps))