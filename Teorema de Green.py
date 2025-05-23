import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parâmetros
R = 4  # Raio da circunferência maior
r = 1  # Raio da circunferência menor
t = np.linspace(0, 2 * np.pi, 1000)
k = (R + r) / r  # Fator de multiplicação angular

# Equações da epicicloide
x = (R + r) * np.cos(t) - r * np.cos(k * t)
y = (R + r) * np.sin(t) - r * np.sin(k * t)

# Circunferência maior 
theta = np.linspace(0, 2 * np.pi, 500)
xc = R * np.cos(theta)
yc = R * np.sin(theta)

# Figura
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')
ax.grid(True)
ax.set_title("Curva Epicicloide")

# Plot da circunferência maior
ax.plot(xc, yc, color='black', linestyle='--', label='Circunferência maior (raio 4)')

# Curva da epicicloide
linha, = ax.plot([], [], color='purple', lw=2, label='Epicicloide')
ponto, = ax.plot([], [], 'ro', label='Ponto P')  # Vermelho
circ_menor, = ax.plot([], [], color='purple', alpha=0.5, label='Circunferência menor')
centro, = ax.plot([], [], 'o', color='purple', markersize=4, label='Centro da menor')

# Inicialização
def init():
    linha.set_data([], [])
    ponto.set_data([], [])
    circ_menor.set_data([], [])
    centro.set_data([], [])
    return linha, ponto, circ_menor, centro

# Atualização da animação
def update(frame):
    # Atualiza curva
    linha.set_data(x[:frame], y[:frame])
    ponto.set_data(x[frame], y[frame])

    # Centro da circunferência menor 
    t_val = t[frame]
    cx = (R + r) * np.cos(t_val)
    cy = (R + r) * np.sin(t_val)
    centro.set_data(cx, cy)

    # Ângulo de rotação da menor (gira enquanto se move)
    theta2 = np.linspace(0, 2 * np.pi, 100)
    rot_angle = -k * t_val  # rotação da menor enquanto gira

    # Circunferência menor rotacionada corretamente
    xm = cx + r * np.cos(theta2 + rot_angle)
    ym = cy + r * np.sin(theta2 + rot_angle)
    circ_menor.set_data(xm, ym)

    return linha, ponto, circ_menor, centro

# Criação da animação
ani = animation.FuncAnimation(
    fig, update, frames=len(t),
    init_func=init, interval=10, blit=True
)

plt.legend()
plt.show()
