import matplotlib.pyplot as plt
import pandas as pd


fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y, 'g--', linewidth=2)


ax.set_title('Normal Distribution - Right Tail Highlighted')
ax.set_xlabel('Value')
ax.set_ylabel('Probability Density')
ax.legend()
plt.tight_layout()
plt.show()