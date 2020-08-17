class Car:
    def __init__(self, tyres=4, liters=1250, total_km=0, disagree=0, piece=''):
        self.tyres = tyres
        self.liters = liters
        self.total_km = total_km
        self.disagree = disagree
        self.piece = piece

    '''Viagem'''
    def travel(self):
        if self.total_km <= 10000 and self.disagree <= 282:
            return f'Liters: {self.liters}, Tyres: {self.tyres}'
        elif self.total_km <= 10000 and self.disagree >= 290:
            return f'Liters: {self.liters}, Tyres: {self.tyres}'

    '''Reabastecer'''
    def refuel(self):
        if self.liters < 625 or self.liters > 1250:
            refuel = 1250 - self.liters
            self.liters += refuel
        return f'{self.liters}%'

    '''Manutenção'''
    def maintenance(self):
        if self.piece == 'liters':
            liters = self.refuel()
        if self.piece == 'tyres':
            if self.disagree ==  282:
                tyres = 4
        return f'Liters: 1250, Tyres: 4'

    '''Cria um novo carro'''
    def create_car(self):
        return f'Liters: {self.liters}, Tyres: {self.tyres}'

    '''Verifica o status do carro'''
    def get_car_stauts(self):
        return f'Liters: {self.liters}, Tyres: {self.tyres}'

    '''Cria pneus'''
    def create_tyres(self):
        if self.disagree > 285:
            return 'Pneu criado'
        return 'Pneu não criado'