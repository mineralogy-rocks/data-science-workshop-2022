import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import pyrolite.plot
from pyrolite.util.classification import TAS


initial_data = pd.read_csv('./data/mafic_dykes.csv', encoding='UTF-8')


# Task 1. Replace ',' to '.'.
initial_data.loc[:, ['SiO2', 'Al2O3', 'Fe2O3', 'MgO', 'CaO', 'Na2O', 'K2O', 'TiO2',
                     'P2O5', 'MnO', 'Cr2O3', 'Ba', 'Ni', 'Sc', 'LOI', 'Sum', 'Be', 'Co',
                     'Cs', 'Ga', 'Hf', 'Nb', 'Rb', 'Sn', 'Sr', 'Ta', 'Th', 'U', 'V', 'W',
                     'Zr', 'Y', 'La', 'Ce', 'Pr', 'Nd', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho',
                     'Er', 'Tm', 'Yb', 'Lu', 'TOT/C', 'TOT/S', 'Mo', 'Cu', 'Pb', 'Zn',
                     'Ni.1', 'As', 'Cd', 'Sb', 'Bi', 'Ag', 'Au', 'Hg', 'Tl', 'Se']] = initial_data.loc[:, ['SiO2', 'Al2O3',
                       'Fe2O3', 'MgO', 'CaO', 'Na2O', 'K2O', 'TiO2',
                       'P2O5', 'MnO', 'Cr2O3', 'Ba', 'Ni', 'Sc', 'LOI', 'Sum', 'Be', 'Co',
                       'Cs', 'Ga', 'Hf', 'Nb', 'Rb', 'Sn', 'Sr', 'Ta', 'Th', 'U', 'V', 'W',
                       'Zr', 'Y', 'La', 'Ce', 'Pr', 'Nd', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho',
                       'Er', 'Tm', 'Yb', 'Lu', 'TOT/C', 'TOT/S', 'Mo', 'Cu', 'Pb', 'Zn',
                       'Ni.1', 'As', 'Cd', 'Sb', 'Bi', 'Ag', 'Au', 'Hg', 'Tl', 'Se']].replace(r'\,', '.', regex=True)

initial_data.loc[:, ~initial_data.columns.isin(['Specimen', 'Location', 'Country rocks', 'Analysis type', 'Rock Type',
                                                'Notes'])] = \
    initial_data.loc[:, ~initial_data.columns.isin(['Specimen', 'Location', 'Country rocks', 'Analysis type', 'Rock Type',
                                               'Notes'])].replace(r'\,', '.', regex=True)


# Task 2. Replace '<' with '' (empty).
initial_data.replace(r'\<', '', regex=True, inplace=True)


# Task 3. Convert analyses columns from strings to numeric data types.
initial_data.loc[:, ~initial_data.columns.isin(['Specimen', 'Location', 'Country rocks', 'Analysis type', 'Rock Type',
                                                'Notes'])] = \
    initial_data.loc[:, ~initial_data.columns.isin(['Specimen', 'Location', 'Country rocks', 'Analysis type', 'Rock Type',
                                                'Notes'])].astype('float64')


# Task 4. Build a TAS diagram using the pyrolite package.
df = initial_data.copy()

df["Na2O + K2O"] = df["Na2O"] + df["K2O"]
cm = TAS()
fig, ax = plt.subplots(1)
cm.add_to_axes(ax, alpha=0.5, linewidth=0.5, add_labels=True)

for category in df['Rock Type'].drop_duplicates():
    df.loc[df['Rock Type'] == category].pyroplot.scatter(ax=ax, components=['SiO2', 'Na2O + K2O'], alpha=1, marker='o',
                                                         label=category)

ax.legend()
ax.set_ylabel("Na$_2$O + K$_2$O")
ax.set_xlabel("SiO$_2$")

plt.tight_layout()
plt.savefig(f"python/figures/TAS.jpeg", dpi=300, format='jpeg')
plt.close()


# Task 5. Customize it a bit: change the color of points depending on the 'Rock Type' category.
