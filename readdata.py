import pandas as pd

df = pd.read_csv("output.csv")
print(df.head())

print(df.isnull().count())

import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# Create figure
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

ax1.active(df['active'], df['State'])
ax1.set(title='active cases')
ax1.grid()

