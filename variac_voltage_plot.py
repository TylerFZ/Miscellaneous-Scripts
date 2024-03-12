import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("G:/Shared drives/Fleetzero Engineering/11 - Testing/Thermal Propagation Testing/TR Test 18  Single Cell TR Initiated Via Heating, Revisited/variac_voltage.csv")
x = df["Time (min)"]
y = df["Variac Voltage (V)"]

fig, ax1 = plt.subplots()
plt.step(x, y, where='post')
ax1.set_xlabel("Time (min)")
ax1.set_ylabel("Variac Voltage (V)")

plt.grid(axis='x', color='0.95')
plt.title('Variac Voltage')
plt.show()