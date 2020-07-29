from flask import Flask, jsonify, request
from products import products


app = Flask(__name__)

@app.route('/ping')
def ping():
  return jsonify({"message":"Pong!"})

@app.route('/products')
def getProducts():
  return jsonify({"products": products, "message": "Product's list"})

@app.route('/products/<string:product_name>')
def getProduct(product_name):
  productsFound = [product for product in products if product['name'] == product_name]
  if len(productsFound) > 0:
    return jsonify(productsFound)
  return jsonify('Product not found')

@app.route('/products', methods=['POST'])
def addProduct():
  new_product = {
    "name": request.json['name'],
    "price": request.json['price'],
    "quantity": request.json['quantity']
  }
  products.append(new_product)
  return jsonify({"message": "Product Added Successfully", "products": products})

@app.route('/products/<string:product_name>', methods=['PUT'])
def modifyProduct(product_name):
  productFound = [product for product in products if product['name'] == product_name ]
  if len(productFound) > 0:
    productFound[0]['name'] = request.json['name']
    productFound[0]['price'] = request.json['price']
    productFound[0]['quantity'] = request.json['quantity']
    return jsonify(
      {
        "message": "Product Updated",
        "product": productFound[0]
      }
    )
  return jsonify("Product Not Found")

@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
  productFound = [ product for product in products if product['name'] == product_name ]
  if len(productFound): 
    products.remove(productFound[0])
    return jsonify(
      {
        "message": "Product removed from products", 
        "products": products
      })
  return jsonify("Product not Found")

if __name__ == "__main__":
    app.run(debug = True, port = 4000)


