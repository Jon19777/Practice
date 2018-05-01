# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 20:52:51 2018

@author: Matthew
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 50)
sinus = np.sin(x)


#%%

plt.plot(x, sinus)
plt.show()

#%%

''' Use plt.plot to get colour/marker abreviations'''

plt.plot(x, sinus, 'o')
plt.show()

#%%
'''Rapid multiplot'''

cosinus = np.cos(x)
plt.plot(x, sinus, "-b",  x, sinus, "-ob",  x, cosinus, "-r",  x, cosinus, "-or")
plt.xlabel('this is x!')
plt.ylabel('this is y!')
plt.title('My First Plot')
plt.show()

#%%

''' step by step'''

plt.plot(x, sinus, label='sinus', color='blue', linestyle='--', linewidth=2)
plt.plot(x, cosinus, label='cosinus', color='red', linestyle='-', linewidth=2)
plt.legend()
plt.show()
























