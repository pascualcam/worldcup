import pandas as pd
import numpy as np
import matplotlib as plt

def getTournamentsData():
    df = pd.read_csv('data-csv/tournaments.csv')
    return df

def main():
    tournaments_data = getTournamentsData()
    x = 0