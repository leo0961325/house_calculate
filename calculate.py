
#版本1:輸入建物資料可還原該土地每地坪價格。
#版本2:輸入建材條件


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

        total_age = input('耐用年限，請輸入1.鋼筋混凝土造 2.加強磚造 3. 木材造 :  ')
        if total_age == '1' :
            total_age = 50
        elif total_age == '2' :
            total_age = 35
        elif total_age == '3' :
            total_age = 20
        else :
            print('invalid input')
            
        used_age = float(input('現在屋齡:'))
        self.age =(total_age - used_age) /total_age

        if used_age > total_age :
            self.age = 0

        
    def formula (self) :

        formula = (self.price - (self.space * self.age * self.reset)) / self.land

        print('還原土地價格是 :'  , abs(round(formula,2)) , '萬/每地坪')
        return formula


House_price()





