
#初版:輸入建物資料可還原該土地每地坪價格。

class House_price :

    
    def __init__(self ) :
        self._input()
        self.the_age()
        self.formula()
        
        

    def _input(self , *args) :

        self.price = float(input('交易價格 :'))
        self.land = float(input('地坪:'))
        self.space = float(input('建坪:'))
        self.reset = float(input('重置成本 :'))
        

    def the_age (self , *args) :

        total_age = float(input('總年限:'))
        used_age = float(input('屋齡:'))
        self.age =(total_age - used_age) /total_age

        
    def formula (self) :

        formula = (self.price - (self.space * self.age * self.reset)) / self.land

        print('還原土地價格是 :'  , abs(round(formula,2)) , '萬/每地坪')
        return formula


House_price()





