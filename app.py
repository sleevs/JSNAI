from flask import Flask 

from math import *
import pandas as pd
import numpy as np 
import matplotlib
import matplotlib.pyplot as plt
from pylab import *

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

    
@app.route("/")
def index():
    
    #datafreme
    np.random.seed(2)

    dataframe = pd.DataFrame(np.random.randn(5,4), index='COZINHA DELIVERY MARKET TRANSPORTE IMOBILIARIA'.split(),columns='SERVIÇOS PEDIDOS PRODUTOS FATURAMENTO'.split())
    print(dataframe)
    return dataframe.to_html()