class Product: 
    def __init__(self, name="not mentioned", ID="not mentioned",price=0,quantity=0): 
        self.name = name 
        self.ID = ID 
        self.price = price 
        self.quantity = quantity 
        print("Constructor get called") 
        
    def show_product(self): 
        print("Product info....") 
        print("Name of product: ",self.name) 
        print("Product ID number: ",self.ID) 
        print("Price of product: ",self.price) 
        print("Quantity of product: ",self.quantity) 
 
    def __del__(self): 
        print("Destructor called") 
             
pd = Product('Coffee machine',123,20000,2) 
pd.show_product() 
