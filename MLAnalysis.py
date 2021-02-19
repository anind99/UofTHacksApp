
# Statistical and ML Analysis on Data
import numpy as np
import pandas as pd
df=pd.read_csv('responses.csv', sep=',')

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
data = df.values[:,:70]
Sum_of_squared_distances = []
K = range(1,15)
for k in K:
    km = KMeans(n_clusters=k)
    km = km.fit(data)
    Sum_of_squared_distances.append(km.inertia_)