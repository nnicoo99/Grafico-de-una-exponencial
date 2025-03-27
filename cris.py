# Importamos las librerías necesarias
import matplotlib.pyplot as plt
import numpy as np

# Datos
x = np.linspace(0, 10, 100)  # Generamos 100 puntos entre 0 y 10
y = np.exp(x)  # Calculamos e^x para cada valor de x

# Creamos el gráfico
plt.plot(x, y, label='y = e^x', color='g')

# Añadimos título y etiquetas
plt.title('Gráfico Exponencial en Python')
plt.xlabel('x')
plt.ylabel('y = e^x')

# Añadimos una leyenda
plt.legend()

# Mostramos el gráfico
plt.show()
#edit desde github
