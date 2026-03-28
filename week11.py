import seaborn as sns
import matplotlib.pyplot as plt

titanic=sns.load_dataset('titanic')
print(titanic.head())

plt.figure(figsize=(8,6))
sns.histplot(titanic['fare'],kde=True,bins = 30,color='blue')
plt.title('Distribution of Fare Prices', fontsize = 16)
plt.xlabel("Fare Price", fontsize = 10)
plt.ylabel('Frequency', fontsize = 14)
plt.show()
