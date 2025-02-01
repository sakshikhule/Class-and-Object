class Book: 
    def __init__(self, name="not mentioned", ID="not 
mentioned",price=0,author="not mentioned"): 
        self.name = name 
        self.ID = ID 
        self.price = price 
        self.author = author 
        print("Constructor get called") 
        
    def show_book(self): 
        print("Book info....") 
        print("Name of book: ",self.name) 
        print("Book ID number: ",self.ID) 
        print("Price of book: ",self.price) 
        print("Author of book: ",self.author) 
 
    def __del__(self): 
        print("Destructor called") 
             
bk = Book('Marvel',123,200,"Mr. Stark") 
bk.show_book() 
