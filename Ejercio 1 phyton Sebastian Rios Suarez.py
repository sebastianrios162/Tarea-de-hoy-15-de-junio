import numpy as np
import matplotlib.pyplot as plt

# Parámetro
A = 1  # Amplitud (puedes cambiarla)

# Intervalo de tiempo
t = np.linspace(0, 6, 1000)

# Función de posición
x = A * np.exp(-t/3) * np.cos(2*np.pi*t + np.pi/4)

# Primera derivada (velocidad)
v = A * np.exp(-t/3) * (
    -(1/3)*np.cos(2*np.pi*t + np.pi/4)
    - 2*np.pi*np.sin(2*np.pi*t + np.pi/4)
)

# Segunda derivada (aceleración)
a = A * np.exp(-t/3) * (
    (1/9 - 4*np.pi**2)*np.cos(2*np.pi*t + np.pi/4)
    + (4*np.pi/3)*np.sin(2*np.pi*t + np.pi/4)
)

# Gráficas
plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.plot(t, x)
plt.title('Posición x(t)')
plt.ylabel('x (m)')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t, v)
plt.title('Velocidad x\'(t)')
plt.ylabel('v (m/s)')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t, a)
plt.title('Aceleración x\'\'(t)')
plt.xlabel('Tiempo (s)')
plt.ylabel('a (m/s²)')
plt.grid(True)

plt.tight_layout()
plt.show()
