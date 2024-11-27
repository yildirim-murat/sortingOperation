import random
import time
from threading import Thread

def rastgele_sayilar_uret():
    return [random.randint(1, 10000) for _ in range(1000000)]

def bubble_sort(sayilar):
    n = len(sayilar)
    for i in range(n):
        for j in range(0, n-i-1):
            if sayilar[j] > sayilar[j+1]:
                sayilar[j], sayilar[j+1] = sayilar[j+1], sayilar[j]
    return "OK"

def selection_sort(sayilar):
    n = len(sayilar)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if sayilar[j] < sayilar[min_idx]:
                min_idx = j
        sayilar[i], sayilar[min_idx] = sayilar[min_idx], sayilar[i]
    return "OK"

def insertion_sort(sayilar):
    n = len(sayilar)
    for i in range(1, n):
        key = sayilar[i]
        j = i - 1
        while j >= 0 and sayilar[j] > key:
            sayilar[j + 1] = sayilar[j]
            j -= 1
        sayilar[j + 1] = key
    return "OK"

def quick_sort(sayilar):
    if len(sayilar) <= 1:
        return sayilar
    pivot = sayilar[len(sayilar) // 2]
    left = [x for x in sayilar if x < pivot]
    middle = [x for x in sayilar if x == pivot]
    right = [x for x in sayilar if x > pivot]
    # return quick_sort(left) + middle + quick_sort(right)
    return "OK"

def zaman_hesapla_siralama(isim, siralama_fonksiyonu, sayilar):
    baslangic_zamani = time.time()
    sirali_sayilar = siralama_fonksiyonu(sayilar[:])
    bitis_zamani = time.time()
    gecen_sure_ms = (bitis_zamani - baslangic_zamani) * 1000
    print(f"{isim}: {sirali_sayilar} - {gecen_sure_ms:.3f} ms")

sayilar = rastgele_sayilar_uret()
print("Rastgele sayılar:", sayilar)

siralamalar = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Quick Sort": quick_sort
}

threadler = []
for isim, fonksiyon in siralamalar.items():
    thread = Thread(target=zaman_hesapla_siralama, args=(isim, fonksiyon, sayilar))
    threadler.append(thread)

for thread in threadler:
    thread.start()

for thread in threadler:
    thread.join()