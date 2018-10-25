import sys
sys.path.insert(0, '../lib')
from productos import getProductos

def listarProductos() :
    productos = getProductos()

    print('Producto  <><><>  Stock')
    print()

    for k in productos :
        if productos[k]["stock"] > 0:
            print('~~>' + productos[k]["nombre"] + ' ' + str(productos[k]["stock"]))

    return None
