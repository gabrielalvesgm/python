import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
#import e invocar as bibliotecas.

dados_diabetes = pd.read_csv(r"C:\Users\Gabriel Alves\Desktop\Estudos\Python\csv\diabetes.csv")

print(dados_diabetes.head())

sns.histplot(dados_diabetes['Age'], kde=True)
plt.title('Idade')
plt.show()


# 'Outcome' é a coluna que diz se a pessoa tem diabetes (0 ou 1)
X = dados_diabetes.drop('Outcome', axis=1)
y = dados_diabetes['Outcome']



# Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



# Normalizar os dados (importante para modelos como Regressão Logística)
scaler = StandardScaler() 
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)



# 5. Treinando o modelo (exemplo com Regressão Logística)
model = LogisticRegression()
model.fit(X_train_scaled, y_train)


# 6. Fazer previsões
y_pred = model.predict(X_test_scaled)


# 7. Avaliar o modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Acurácia do modelo: {accuracy * 100:.2f}%')


# Matriz de Confusão
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Não Diabético', 'Diabético'], yticklabels=['Não Diabético', 'Diabético'])
plt.title('Matriz de Confusão')
plt.show()



# 8. Exibir previsões de algumas amostras
for i in range(5):
    print(f"Amostra {i+1} - Predição: {'Diabético' if y_pred[i] == 1 else 'Não Diabético'}")
    
    
#Boxplot para comparar glicose entre outros grupos de Outcome

sns.boxplot(x='Outcome', y='Glucose', data=dados_diabetes)
plt.title('Comparação de Glicose entre classes de resultado')
plt.xlabel('Resultado (0 = Não Diabético, 1 = Diabético)')
plt.ylabel('Nível de Glicose')
plt.show()



#Violin plot para comparar IMC entre os grupos de Outcome
sns.violinplot(x='Outcome', y='BMI', data=dados_diabetes, inner="quartile")
plt.title('Comparação de IMC entre classes de resultado')
plt.xlabel('Outcome (0 = Não Diabético, 1 = Diabético)')
plt.ylabel('IMC')
plt.show()



#Contagem de casos por número de gestantes e Outcome
sns.countplot(x='Pregnancies', hue='Outcome', data=dados_diabetes)
plt.title('Número de Gestações vs. Resultado')
plt.xlabel('Número de Gestações')
plt.ylabel('Contagem')
plt.legend(title='Resultado', labels=['Não Diabético', 'Diabético'])
plt.show()



#Scatterplot entre glicose e IMC, colorido por Outcome
sns.scatterplot(x='Glucose', y='BMI', hue='Outcome', data=dados_diabetes, palette='coolwarm')
plt.title('Relação entre Glicose e IMC')
plt.xlabel('Nível de Glicose')
plt.ylabel('IMC')
plt.legend(title='resultado', labels=['Não Diabético', 'Diabético'])
plt.show()


#Gráfico de dispersão ou Scatterplot, plano cartesiano
#Scatterplot entre idade e insulina, colorido por Outcome
sns.scatterplot(x='Age', y='Insulin', hue='Outcome', data=dados_diabetes, palette='viridis')
plt.title('Relação entre Idade e Insulina')
plt.xlabel('Idade')
plt.ylabel('Insulina')
plt.legend(title='Outcome', labels=['Não Diabético', 'Diabético'])
plt.show()