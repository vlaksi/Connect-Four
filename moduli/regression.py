"""
Modul u kome se nalaze implementacije za nase regresije 
i crtanje regresije nad nasim podacima.
"""
import matplotlib
from matplotlib.pylab import rcParams
from sklearn.datasets import load_boston
#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
import matplotlib.pyplot as plt

from .load import *


rcParams['figure.figsize'] = 8, 6
matplotlib.rcParams.update({'font.size': 12})

def lasso_regression(data, predictors, alpha, models_to_plot={}):
    #Fit the model
    lassoreg = Lasso(alpha=alpha,normalize=True, max_iter=1e5)
    lassoreg.fit(data[predictors],data['y'])
    y_pred = lassoreg.predict(data[predictors])
    #print("Predikcija poteza", y_pred)
  
    #Return the result in pre-defined format
    rss = sum((y_pred-data['y'])**2)
    ret = [rss]
    ret.extend([lassoreg.intercept_])
    ret.extend(lassoreg.coef_)
    return ret

def ridge_regression(data, predictors, alpha):

    #Fit the model
    ridgereg = Ridge(alpha=alpha,normalize=True)
    ridgereg.fit(data[predictors],data['y'])
    y_pred = ridgereg.predict(data[predictors])
    #print("Predikcija poteza", y_pred)
    #print("PREDIKCIJA ZA PRVI POTEZ", y_pred[1])
   
    for p in y_pred:
        if p not in pom_y:
            pom_y.append(p)
    
    #for x in range(len(pom_y)):
    #    print("Predikcija za potez ", x+1 , round(abs(pom_y[x])))

    #Return the result in pre-defined format
    rss = sum((y_pred-data['y'])**2)
    ret = [rss]
    ret.extend([ridgereg.intercept_])
    ret.extend(ridgereg.coef_)
    return ret

def ridge_regression_PLOTOVANJE(data, predictors, alpha, models_to_plot={}):
    #Fit the model
    ridgereg = Ridge(alpha=alpha,normalize=True)
    ridgereg.fit(data[predictors],data['y'])
    y_pred = ridgereg.predict(data[predictors])

    #print("Predikcija poteza", y_pred)
    
    #Check if a plot is to be made for the entered alpha
    if alpha in models_to_plot:
        plt.subplot(models_to_plot[alpha])
        plt.tight_layout()
        plt.plot(data['x'],y_pred)
        plt.plot(data['x'],data['y'],'.')
        plt.title('Plot for alpha: %.3g'%alpha)
        plt.draw()
        plt.pause(1)

    #Return the result in pre-defined format
    rss = sum((y_pred-data['y'])**2)
    ret = [rss]
    ret.extend([ridgereg.intercept_])
    ret.extend(ridgereg.coef_)
    return ret