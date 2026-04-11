import pandas as pd
from clean import clean_df
import matplotlib.pyplot as plt
import pandas as pd

df = clean_df()
print(df["Order Date"].min())
plt.plot(df["Amount"], df["Order Date"])
plt.tight_layout()
plt.savefig("analysis.png")
