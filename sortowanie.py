

## Przykładowe dane
#arr = [64, 34, 25, 12, 22, 11, 90]
#
#for i in range(len(arr) - 1):
#    for j in range(len(arr) - 1):
#        if arr[j] > arr[j + 1]:
#            temp = arr[j]
#            arr[j] = arr[j + 1]
#            arr[j + 1] = temp
#
#print("Przed sortowaniem:", arr)
#
## Sortowanie
#
#print("Po sortowaniu:", arr)
#print(" --------------------------------------------")
#
#def merge_sort(arr1):
#
#
#
#    if len(arr1) > 1:
#        mid = len(arr1) // 2
#        left = arr1[:mid]
#        right = arr1[mid:]
#
#
#
#
#        # Rekurencyjnie sortuj każdą połówkę
#        merge_sort(left)
#        merge_sort(right)
#
#        i = 0
#        j = 0
#        k = 0
#
#        while i < len(left) and j < len(right):
#            if left[i] < right[j]:
#                arr1[k] = left[i]
#                i += 1
#            else:
#                arr1[k] = right[j]
#                j += 1
#            k += 1
#
#        while i < len(left):
#            arr1[k] = left[i]
#            i += 1
#            k += 1
#        while j < len(right):
#            arr1[k] = right[j]
#            j += 1
#            k += 1
#
#
#arr1 = [64, 34, 25, 12, 22, 11, 90, 21]
#
#merge_sort(arr1)
#
#print(arr1)


def bebelkowe_sortowanie(lista):
    zamieniono = True
    while zamieniono:
        zamieniono = False
        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:

                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp

                zamieniono = True




def merge_sort(lista):

    if len(lista) > 1:
        left = lista[:len(lista)//2]
        right = lista[len(lista)//2:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lista[k] = left[i]
                i += 1
            else:
                lista[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lista[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            lista[k] = right[j]
            j += 1
            k += 1


def quick_sort(lista, left, right):
    if left < right:
        pivot = lista[right]
        i = left - 1

        for j in range(left, right):
            if lista[j] < pivot:
                i += 1

                # Zamiana elementów
                temp = lista[i]
                lista[i] = lista[j]
                lista[j] = temp

        # Umieszczamy pivota na odpowiedniej pozycji


        temp = lista[i+1]
        lista[i+1] = lista[right]
        lista[right] = temp
        pivot_index = i + 1  # Indeks pivota

        # Rekurencyjne wywołania dla lewych i prawych podtablic
        quick_sort(lista, left, pivot_index - 1)
        quick_sort(lista, pivot_index + 1, right)


def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        key = lista[i]  # Element do wstawienia
        j = i - 1

        # Przesuwanie elementów większych od key
        while j >= 0 and lista[j] > key:
            lista[j + 1] = lista[j]
            j -= 1

        # Wstawienie key w odpowiednie miejsce
        lista[j + 1] = key


def main():
    lista = [1, 65, 2, 98, 2, 5, 3, 6, 84, 25, 8, 0]
    #bebelkowe_sortowanie(lista)
    #merge_sort(lista)
    #quick_sort(lista, 0, len(lista) - 1)
    insertion_sort(lista)
    print(lista)
main()