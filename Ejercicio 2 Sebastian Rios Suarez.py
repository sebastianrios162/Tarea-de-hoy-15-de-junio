import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Variables simbólicas
t = sp.symbols('t')
A = 1  # Amplitud

# Función de posición
x = A * sp.exp(-t/3) * sp.cos(2*sp.pi*t + sp.pi/4)

# Primera derivada (velocidad)
v = sp.diff(x, t)

# Segunda derivada (aceleración)
a = sp.diff(v, t)

# Mostrar derivadas en consola
print("Posición x(t):")
sp.pprint(x)

print("\nVelocidad v(t) = dx/dt:")
sp.pprint(v)

print("\nAceleración a(t) = d²x/dt²:")
sp.pprint(a)

# Convertir expresiones simbólicas a funciones numéricas
x_num = sp.lambdify(t, x, 'numpy')
v_num = sp.lambdify(t, v, 'numpy')
a_num = sp.lambdify(t, a, 'numpy')

# Intervalo de tiempo
t_val = np.linspace(0, 6, 1000)

# Evaluación numérica
x_val = x_num(t_val)
v_val = v_num(t_val)
a_val = a_num(t_val)

# Crear figura con subplots
plt.figure(figsize=(10, 8))

# Gráfica de posición
plt.subplot(3, 1, 1)
plt.plot(t_val, x_val, 'r', linewidth=2)
plt.title('Posición x(t)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Posición (m)')
plt.xlim(0, 6)
plt.grid(True)

# Gráfica de velocidad
plt.subplot(3, 1, 2)
plt.plot(t_val, v_val, 'b', linewidth=2)
plt.title('Velocidad v(t)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (m/s)')
plt.xlim(0, 6)
plt.grid(True)

# Gráfica de aceleración
plt.subplot(3, 1, 3)
plt.plot(t_val, a_val, 'g', linewidth=2)
plt.title('Aceleración a(t)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Aceleración (m/s²)')
plt.xlim(0, 6)
plt.grid(True)

# Ajustar espacios entre gráficas
plt.tight_layout()

# Mostrar figura
plt.show()
