from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

# daugiausiai taškų pelnęs žaidėjas LKL ir MLKL
df = pd.read_csv('LKL_points.csv')
df1 = pd.read_csv('MLKL_points.csv')

LKL_avg_point_per_games = df['Player'].['Sum'].max()
print(LKL_avg_point_per_games)
