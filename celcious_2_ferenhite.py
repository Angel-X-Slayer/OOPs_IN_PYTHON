class select:
    def __init__(self,choose):
        self.choose=choose

    def calc(self):
        if(self.choose==0):
            c=int(input("enter the celcious value: "))
            f=((9*c)/5)
            print(f"celcious={c};ferenhite={f}")

        else:
            f=int(input("enter the ferenhite value: "))
            c=((5*f)/9)
            print(f"celcious={c};ferenhite={f}")

choose=int(input("enter 0 for cel to fer Or enter 1 for fer to cel: "))
a=select(choose)
a.calc()

