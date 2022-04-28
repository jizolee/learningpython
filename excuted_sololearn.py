
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

tlip2=pd.read_csv(r'C:\Users\userlap\Desktop\TLIP2.csv')
plt.scatter(tlip2['X'],tlip2['Y'],c=tlip2['Z'],s=1.25)
plt.figure(figsize=(100,100))
plt.savefig('poo.jpg')
plt.show() 
plt.close()