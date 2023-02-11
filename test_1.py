class Computer:
    def __init__(self,cpu,ram,name):
        self.prosesser=cpu
        self.RAM=ram
        self.com=name
    def printing_the_config(self):
        print(f"the config for {self.com} is {self.prosesser} and {self.RAM}")
com1=Computer("i7,9th gen","8Gb","Asus ROG")
com2=Computer("Ryzen 5,H pros","8Gb","MSI gf 63")
com1.printing_the_config()
com2.printing_the_config()
