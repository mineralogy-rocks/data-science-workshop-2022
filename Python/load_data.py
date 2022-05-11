import pandas as pd
import numpy as np
import re

initial_data = pd.read_csv('../data/mafic_dykes.csv', encoding='UTF-8')

initial_data.loc[:, ['SiO2', 'Al2O3', 'Fe2O3', 'MgO', 'CaO', 'Na2O', 'K2O', 'TiO2',
                       'P2O5', 'MnO', 'Cr2O3', 'Ba', 'Ni', 'Sc', 'LOI', 'Sum', 'Be', 'Co',
                       'Cs', 'Ga', 'Hf', 'Nb', 'Rb', 'Sn', 'Sr', 'Ta', 'Th', 'U', 'V', 'W',
                       'Zr', 'Y', 'La', 'Ce', 'Pr', 'Nd', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho',
                       'Er', 'Tm', 'Yb', 'Lu', 'TOT/C', 'TOT/S', 'Mo', 'Cu', 'Pb', 'Zn',
                       'Ni.1', 'As', 'Cd', 'Sb', 'Bi', 'Ag', 'Au', 'Hg', 'Tl', 'Se']].replace(r'\,', '.', regex=True,
                                                                                              inplace=True)

initial_data.loc[:, initial_data.columns.isin(['Specimen', 'Location', 'Country rocks', 'Analysis type', 'Rock Type',
                                               'Notes'])].replace(r'\,', '.', regex=True, inplace=True)

initial_data.replace(r'\<', '', regex=True, inplace=True)