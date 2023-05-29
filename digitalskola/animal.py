class Hewan:
  nama_latin = 'animalia'

  def __init__(self, nama, umur):
    self.nama = nama
    self.umur = umur

  def bangun(self):
    return f'{self.nama} sudah bangun.'

  @classmethod
  def change_nama_latin(cls, nama_latin):
    cls.nama_latin = nama_latin



class Kucing(Hewan):
    
  def bangun(self):
    return f'{self.nama} sudah bangun lagi.'

  def lari(self, kecepatan):
    if kecepatan > 10:
      print(f'{self.nama} berlari cepat sekali')
    else:
      print(f'{self.nama} berlari lambat')


# Membuat instance object untuk Kucing Persia dan Kucing Turkish Angora
kucing_persia = Kucing(nama='Kucing Persia', umur=8)
kucing_turkish_angora = Kucing(nama='Kucing Turkish Angora', umur=10)


kucing_turkish_angora.change_nama_latin('felis catus turkishina') # contoh nama latin
# Informaasi masing-masing kucing
print(f"""
nama            : {kucing_turkish_angora.nama}
umur            : {kucing_turkish_angora.umur}
nama latin      : {kucing_turkish_angora.nama_latin}
method 'bangun' : {kucing_turkish_angora.bangun()}
""")
kucing_turkish_angora.lari(8)
