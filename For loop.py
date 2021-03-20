# List sebagai iterable
gorengan = ['bakwan','cireng','tahu isi','tempe goreng','ubi goreng']

for g in gorengan:
    print(g)
    print(len(g))

# string sebagai iterable

bakwan = 'bakwan'

for i in bakwan:
    print(i)

# for di dalam for
gorengan = ['bakwan', 'cireng', 'tahu isi', 'tempe goreng', 'ubi goreng']
buah = ['semangka','jeruk','apel','anggur']
sayur = ['kangkung','woretel','tomat','kentang']

Daftar_belanja = [gorengan,buah,sayur]

for subDaftarBelanja in Daftar_belanja:
    print(subDaftarBelanja)
    for kompomen in subDaftarBelanja:
        print(kompomen)