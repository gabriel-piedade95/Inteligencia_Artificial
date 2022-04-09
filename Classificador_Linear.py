import random as rand
import numpy as np

class Perceptron:
    
    def __init__(self, eta = 0.1, epochs = 50, seed = 1):
        
        self._eta = eta
        self._epochs = epochs
        self._seed = seed 





    def fit(self, X, Y):
            
        SEED = self._seed
        self.W  = np.array([rand.random() * 10 for x in range(X.shape[1])])
        self.b = np.array([rand.random()*10])
        
        for epoch in range(self._epochs):
                
            erros_lista = [0] * Y.shape[0]
            k = 0
                
            for x_i, y_i in zip(X, Y):
                    
                y_hat = int(np.where((sum(self.W*x_i) + self.b) >= 0, 1, -1))
                    
                    
                erro_y = int(y_hat!= y_i)
                erros_lista[k] = erro_y
                    
                if erro_y != 0:
                        
                    D_y = (y_i - y_hat) * self._eta
                    self.W = self.W + (x_i*D_y)
                    self.b = self.b + D_y
                        
                    k += 1
                    
            if sum(erros_lista) == 0:
                    
                break
                
        return self