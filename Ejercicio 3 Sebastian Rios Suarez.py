import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from scipy.integrate import simpson

# =====================================================
# DEFINICIÓN DE LA FUNCIÓN Y SUS DERIVADAS
# =====================================================

t = sp.symbols('t')
A = 1

x = A * sp.exp(-t/3) * sp.cos(2*sp.pi*t + sp.pi/4)

# Derivadas simbólicas
v = sp.diff(x, t)
a = sp.diff(v, t)

# Conversión a funciones numéricas
x_fun = sp.lambdify(t, x, 'numpy')
v_fun = sp.lambdify(t, v, 'numpy')
a_fun = sp.lambdify(t, a, 'numpy')

# =====================================================
# INTERVALO DE TIEMPO
# =====================================================

t_total = np.linspace(0, 6, 2000)

v_total = v_fun(t_total)
a_total = a_fun(t_total)

# =====================================================
# FIGURA
# =====================================================

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
plt.subplots_adjust(bottom=0.25)

# Valor inicial del deslizador
t0 = 3

# Datos iniciales
mask = t_total <= t0

# =====================================================
# GRÁFICA DE VELOCIDAD
# =====================================================

line_v, = ax1.plot(t_total, v_total,
                   color='blue',
                   label='v(t)')

fill_v = ax1.fill_between(
    t_total[mask],
    v_total[mask],
    alpha=0.3
)

ax1.set_title('Integral de la velocidad')
ax1.set_xlabel('Tiempo (s)')
ax1.set_ylabel('v(t) [m/s]')
ax1.grid(True)

# =====================================================
# GRÁFICA DE ACELERACIÓN
# =====================================================

line_a, = ax2.plot(t_total, a_total,
                   color='green',
                   label='a(t)')

fill_a = ax2.fill_between(
    t_total[mask],
    a_total[mask],
    alpha=0.3
)

ax2.set_title('Integral de la aceleración')
ax2.set_xlabel('Tiempo (s)')
ax2.set_ylabel('a(t) [m/s²]')
ax2.grid(True)

# =====================================================
# CÁLCULO INICIAL DE INTEGRALES
# =====================================================

t_sel = t_total[mask]

trap_v = np.trapz(v_total[mask], t_sel)
simp_v = simpson(v_total[mask], t_sel)

trap_a = np.trapz(a_total[mask], t_sel)
simp_a = simpson(a_total[mask], t_sel)

texto = fig.text(
    0.05,
    0.02,
    f'Velocidad → Trapecio = {trap_v:.6f} | Simpson = {simp_v:.6f}\n'
    f'Aceleración → Trapecio = {trap_a:.6f} | Simpson = {simp_a:.6f}',
    fontsize=10
)

# =====================================================
# SLIDER
# =====================================================

slider_ax = plt.axes([0.15, 0.1, 0.7, 0.03])

slider = Slider(
    ax=slider_ax,
    label='Tiempo final t (s)',
    valmin=0.1,
    valmax=6.0,
    valinit=t0,
    valstep=0.1
)

# =====================================================
# FUNCIÓN DE ACTUALIZACIÓN
# =====================================================

def actualizar(val):

    global fill_v, fill_a

    tiempo = slider.val

    mask = t_total <= tiempo

    t_sel = t_total[mask]

    # Eliminar áreas anteriores
    fill_v.remove()
    fill_a.remove()

    # Dibujar nuevas áreas
    fill_v = ax1.fill_between(
        t_total[mask],
        v_total[mask],
        alpha=0.3
    )

    fill_a = ax2.fill_between(
        t_total[mask],
        a_total[mask],
        alpha=0.3
    )

    # Integración por Trapecio
    trap_v = np.trapz(v_total[mask], t_sel)
    trap_a = np.trapz(a_total[mask], t_sel)

    # Integración por Simpson
    simp_v = simpson(v_total[mask], t_sel)
    simp_a = simpson(a_total[mask], t_sel)

    texto.set_text(
        f'Velocidad → Trapecio = {trap_v:.6f} | Simpson = {simp_v:.6f}\n'
        f'Aceleración → Trapecio = {trap_a:.6f} | Simpson = {simp_a:.6f}'
    )

    fig.canvas.draw_idle()

slider.on_changed(actualizar)

plt.show()
