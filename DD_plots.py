import numpy as np
from plotly import express as px
import pandas as pd

def liftpolar(filename):
    df = pd.read_csv(filename)
    fig = px.line(df, x='α / °', y='c_l', title='Lift Polar')
    fig.show()


def dragpolar(filename):
    df = pd.read_csv(filename)
    fig = px.line(df, x='c_l', y='c_d', title='Drag Polar')


def momentpolar(filename):
    df = pd.read_csv(filename)
    fig = px.line(df, x='α / °', y='c_m', title='Pitching Moment Polar')


def readfile(filename):
    data = []
    with open(filename, 'r') as f:
        f = f.readlines()
        for line in f:
            dataline = []
            line = line.split('\t')
            for item in line:
                item = item.strip(' \n')
                dataline.append(item)
            data.append(dataline)

