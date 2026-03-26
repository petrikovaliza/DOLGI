class Wallet:
    def __init__(self, rub=0, usd=0, eur=0):
        self.rub = rub
        self.usd = usd
        self.eur = eur
        self.usd_to_rub = 90
        self.eur_to_rub = 100
    
    def __str__(self):
        return f"Wallet: {self.rub} RUB, {self.usd} USD, {self.eur} EUR"
    
    def to_rub(self):
        return self.rub + (self.usd * self.usd_to_rub) + (self.eur * self.eur_to_rub)
    
    def __add__(self, other):
        total_rub = self.to_rub() + other.to_rub()
        rub_part = total_rub
        usd_part = 0
        eur_part = 0
        
        if rub_part >= self.eur_to_rub:
            eur_part = int(rub_part // self.eur_to_rub)
            rub_part = rub_part % self.eur_to_rub
        
        if rub_part >= self.usd_to_rub:
            usd_part = int(rub_part // self.usd_to_rub)
            rub_part = rub_part % self.usd_to_rub
        
        return Wallet(rub=int(rub_part), usd=usd_part, eur=eur_part)


wallet1 = Wallet(rub=1000, usd=50)
wallet2 = Wallet(eur=30, usd=20)
print(wallet1 + wallet2)
