import matplotlib.pyplot as plt;
data=pd.read_csv("Iris - Iris.csv") ;
print(data);

data.plot(kind="scatter",
          x='SepalLengthCm',
          y='PetalLengthCm')
plt.grid()
data=data.dropna()
print(data.head(50))

y = pd.get_dummies(data.Species, prefix='Species')
print(y.head(50))
