class Shirt: 
    def __init__(self, name="not mentioned", ID="not mentioned",price=0,type="notmentioned",size=0): 
        self.name = name 
        self.ID = ID 
        self.price = price 
        self.type = type 
        self.size = size 
        print("Constructor get called") 
        
    def show_shirt(self): 
        print("Shirt Details....") 
        print("Name of shirt: ",self.name) 
        print("Shirt ID number: ",self.ID) 
        print("Price of Shirt: ",self.price) 
        print("Type of shirt: ",self.type) 
        print("Size of shirt: ",self.size) 
   def __del__(self): 
        print("Destructor called")
        
st = Shirt('LV',123,20000,"casual",30) 
st.show_shirt()
