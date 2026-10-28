import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Parameters
N = 1000      # population
I0 = 1        # initially infected
R0 = 0        # initially recovered
beta = 0.5    # infection rate
gamma = 0.1   # recovery rate
days = 160
dt = 0.1      # time step (days) for the numerical integration

S, I, R = N - I0 - R0, I0, R0
t_values, S_values, I_values, R_values = [0.0], [S], [I], [R]

steps_per_day = round(1 / dt)
for day in range(1, days + 1):
    for _ in range(steps_per_day):
        new_infections = beta * S * I / N * dt
        new_recoveries = gamma * I * dt
        S -= new_infections
        I += new_infections - new_recoveries
        R += new_recoveries
    t_values.append(day)
    S_values.append(S)
    I_values.append(I)
    R_values.append(R)

plt.figure(figsize=(8, 5))
plt.plot(t_values, S_values, label="Susceptible")
plt.plot(t_values, I_values, label="Infected")
plt.plot(t_values, R_values, label="Recovered")
plt.xlabel("Time (days)")
plt.ylabel("Number of people")
plt.title("SIR epidemic model")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("sir_plot.png", dpi=150)
