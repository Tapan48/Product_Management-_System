from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

import database_models
from database import session,engine
from sqlalchemy.orm import Session
from models import Product



database_models.Base.metadata.create_all(bind=engine)   

app = FastAPI() 

# CORS for React dev server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def greet():
    return "welcome to fastapidev"

products = [
    Product(id=1, name="Product 1", description="Description 1", price=100, quantity=10),
    Product(id=2, name="Product 2", description="Description 2", price=200, quantity=20),
    Product(id=3, name="Product 3", description="Description 3", price=300, quantity=30),

    Product(id=6, name="Product 6", description="Description 6", price=600, quantity=60),
]

def get_db():
    db=session()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db=session()
    
    count = db.query(database_models.Product).count
  

    if count==0 :
        for product in products:
            db.add(database_models.Product(**product.model_dump()))
        db.commit()
init_db()   


# In-memory version (old approach) 
# @app.get("/products")
# def get_products_memory():
#     return products

@app.get("/products")
def get_products(db: Session = Depends(get_db)):

   db_products = db.query(database_models.Product).all()
   return db_products 


# In-memory version (old approach)
# @app.get("/product/{id}")
# def get_product_by_id_memory(id: int):
#     for product in products:
#         if product.id == id:
#             return product
#     return {"message": "Product not found"}

@app.get("/product/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        return db_product
    return { "Product not found"}
   

# In-memory version (old approach)
# @app.post("/product")
# def add_product_memory(product: Product):
#     products.append(product)
#     return product

@app.post("/products")
def add_product(product: Product, db: Session = Depends(get_db)):
    db_product = database_models.Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    
    return product



# In-memory version (old approach)
# @app.put("/product/{id}")
# def update_product(id: int, product: Product):
#     for i in range(len(products)):
#         if products[i].id == id:
#             products[i] = product
#             return { "product updated successfully"}

#     return "No product found to update"  

@app.put("/products/{id}")
def update_product(id: int, product: Product, db: Session = Depends(get_db)):

    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db_product.name = product.name  
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
      
        return { "product updated successfully"}
    else:
        return "No product found to update"    


# in memory version (old approach)
# @app.delete("/product/{id}")    
# # def delete_product(id: int):
# #     for i in range(len(products)):
# #         if products[i].id == id:    
# #             products.pop(i)
# #             return { "product deleted successfully"}
# #     return "No product found to delete"

@app.delete("/products/{id}")    
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return { "product deleted successfully"}
    else:
        return "No product found to delete"



