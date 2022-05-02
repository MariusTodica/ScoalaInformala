class CatalogAuto:
    def __init__(self, marca , tip):
        self.marca = marca
        self.tip = tip

    def schimb_culoare(self, culoare):
        self.culoare = culoare

    def __str__(self):
        return f"Culoarea este :{self.culoare}"

class ScauneIncalzite(CatalogAuto):
    def __init__(self, scaune_incalzite, marca, tip):
        super().__init__(marca, tip)
        self.scaune_incalzite = scaune_incalzite
    def __str__(self):
        return f"Marca este :{self.marca},\n Tipul este:{self.tip},\n Scaune incalzite :{self.scaune_incalzite}"

class BlocuriOpticeLDED(CatalogAuto):
    def __init__(self, blocuri_optice_led, marca, tip):
        super().__init__(marca, tip)
        self.blocuri_optice_led = blocuri_optice_led


    def __str__(self):
         return f"Marca este :{self.marca},\n Tipul este:{self.tip},\n Blocuri optice:{self.blocuri_optice_led}"


obj = ScauneIncalzite(marca= "ARO" , tip= 461 , scaune_incalzite= "NU")
print(obj)
obj.schimb_culoare("rosu")
print(obj.culoare)