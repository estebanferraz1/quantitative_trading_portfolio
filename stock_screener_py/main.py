# -*- coding: utf-8 -*-
"""main.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YC8WVQw4FVgjGqdyI7Kb5P6q51fDYZ1I
"""

from nsepy import get_history
from datetime import date
import pandas as pd

stocks = ['AAOI', 'ACDC', 'ACIC', 'ACMR', 'ACXP', 'ALPN', 'ALXO', 'AMRK', 'AMXC', 'AMTX', 'ARHS', 'ASLE', 'AVGR', 'AXLA', 'BFRG', 'BIVI', 'BJDX', 'BLDE', 'BTAI', 'CDIO', 'CLRB', 'COCO', 'CRGX', 'CRSR', 'CSWC', 'DAKT', 'DCTH', 'DH', 'DRCT', 'DSGN', 'EMLD', 'EVER', 'EXFY', 'FLWS', 'FWRG', 'GCT', 'GRPN', 'HOWL', 'HSDT', 'HTLD', 'IDEX', 'INOD', 'INZY', 'KNSA', 'KNTE', 'LFMD', 'LIFW', 'LUNR', 'LVOX', 'LYRA', 'MAMA', 'MDAI', 'METC', 'MGTX', 'MNMD', 'MNTS', 'MOND', 'NDLS', 'NMRA', 'NN', 'NRDS', 'PDSB', 'PHAT', 'PIXY', 'PLL', 'PRME', 'PUBM', 'RILY', 'RMNI', 'RUM', 'RVPH', 'RYZB', 'SASI', 'SATS', 'SAVA', 'SBGI', 'SEAT', 'SGHT', 'SHOT', 'SIGA', 'SKWD', 'SLNO', 'SPRY', 'SWBI', 'SWIM', 'TASK', 'TAST', 'TH', 'THRX', 'TPST', 'TRIN', 'TTOO', 'ULCC', 'VERI', 'VICR', 'VTGN', 'VYNE', 'WAVD', 'WISH', 'ZYXI', 'AESI', 'AGTI', 'AHT', 'AMPX', 'AMPY', 'ARR', 'ATMU', 'BKE', 'BRDG', 'DTC', 'ENFN', 'FF', 'FNA', 'FPI', 'GNK', 'GNRD', 'HLLY', 'HRTG', 'HTH', 'IVR', 'KGS', 'LL', 'LMND', 'LXU', 'MBI', 'NAPA', 'NINE', 'OUST', 'SBOW', 'SCU', 'SJT', 'SKLZ', 'SRG', 'SWI', 'TGLS', 'WEAV', 'WOW', 'WSR']
start_date=date(2021,1,1)
end_date=date.today()

def Importdata():
    for stock in stocks:
        rawdata = get_history(symbol=stock,start=start_date,end=end_date)
        file_name = 'Data/{}.cvs'.format(stock)
        df = pd.DataFrame(rawdata)
        df.to_csv(file_name,encoding='utf-8')
        print(stock)

def Loaddata():
    for stock in stocks:
        try:
            rawdata =pd.read_csv('Data/{}.csv'.format(stock))
            print(stock)
            print(rawdata)
        except:
            pass

importdata()