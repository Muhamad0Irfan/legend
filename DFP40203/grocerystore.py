
class store:

    def __init__(self,keahlian,jumlahbayaran):
         self.keahlian = keahlian
         self.jumlahbayaran = jumlahbayaran

    def discount(self):
         if self.keahlian == "vip":
              print(self.jumlahbayaran-(self.jumlahbayaran*0.06))
         elif self.keahlian == "biasa":
              print(self.jumlahbayaran-(self.jumlahbayaran*0.04))
         else :
              print(self.jumlahbayaran)

a = input("Masukkan keahlian anda(VIP/biasa/Tiada):")
b = float(input("Masukkan jumlah bayaran bayaran:"))


customer = store(a,b)

customer.discount()

         



