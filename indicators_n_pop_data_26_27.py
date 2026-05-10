"""
@author: peter.saiu@nhs.net
Created: 2024
version: 0.1.3
Updated on 10/5/2026 with data for 2025/26 (which includes Indicators from 2024/25 and GP population for April 2026). 

Description: 
The code in this script imports the population and indicators data which 
are then imported and run in the strealit app ('eFIT')      # 

"""

import pandas as pd

# Indicator and GP population data is for the year: 
year_v3 = '2025-26_v3'  # delete after this version (used only for QRL HAMPSHIRE AND ISLE OF WIGHT ICB)
year_v2 = '2025-26_v2'
year = '2026-27'

# Import the indicators data
indicators_S1Y5D = pd.read_csv(f'input_data_ind/indicator_S1Y5D_{year}.csv')      # Central East ICB
indicators_D7T5G = pd.read_csv(f'input_data_ind/indicator_D7T5G_{year}.csv')      # Essex ICB
indicators_T6Y0W = pd.read_csv(f'input_data_ind/indicator_T6Y0W_{year}.csv')      # Norfolk and Suffolk ICB
indicators_Z9B2Z = pd.read_csv(f'input_data_ind/indicator_Z9B2Z_{year}.csv')      # West and North London ICB
indicators_S0E4D = pd.read_csv(f'input_data_ind/indicator_S0E4D_{year}.csv')      # Surrey and Sussex ICB
indicators_qox = pd.read_csv(f'input_data_ind/indicator_QOX_{year_v2}.csv')      # Bath and North East Somerset, Swindon and Wiltshire ICB
indicators_qhl = pd.read_csv(f'input_data_ind/indicator_QHL_{year_v2}.csv')      # Birmingham and Solihull ICB
indicators_qua = pd.read_csv(f'input_data_ind/indicator_QUA_{year_v2}.csv')      # Black Country ICB
indicators_quy = pd.read_csv(f'input_data_ind/indicator_QUY_{year_v2}.csv')      # Bristol, North Somerset and South Gloucestershire ICB
indicators_qyg = pd.read_csv(f'input_data_ind/indicator_QYG_{year_v2}.csv')      # Cheshire and Merseyside ICB
indicators_qt6 = pd.read_csv(f'input_data_ind/indicator_QT6_{year_v2}.csv')      # Cornwall and the Isles of Scilly ICB
indicators_qwu = pd.read_csv(f'input_data_ind/indicator_QWU_{year_v2}.csv')      # Coventry and Warwickshire ICB
indicators_qj2 = pd.read_csv(f'input_data_ind/indicator_QJ2_{year_v2}.csv')      # Derby and Derbyshire ICB
indicators_qjk = pd.read_csv(f'input_data_ind/indicator_QJK_{year_v2}.csv')      # Devon ICB
indicators_qvv = pd.read_csv(f'input_data_ind/indicator_QVV_{year_v2}.csv')      # Dorset ICB
indicators_qr1 = pd.read_csv(f'input_data_ind/indicator_QR1_{year_v2}.csv')      # Gloucestershire ICB
indicators_qop = pd.read_csv(f'input_data_ind/indicator_QOP_{year_v2}.csv')      # Greater Manchester ICB
indicators_qrl = pd.read_csv(f'input_data_ind/indicator_QRL_{year_v3}.csv')      # Hampshire and the Isle of Wight ICB
indicators_qgh = pd.read_csv(f'input_data_ind/indicator_QGH_{year_v2}.csv')      # Herefordshire and Worcestershire ICB
indicators_qoq = pd.read_csv(f'input_data_ind/indicator_QOQ_{year_v2}.csv')      # Humber and North Yorkshire ICB
indicators_qks = pd.read_csv(f'input_data_ind/indicator_QKS_{year_v2}.csv')      # Kent and Medway ICB
indicators_qe1 = pd.read_csv(f'input_data_ind/indicator_QE1_{year_v2}.csv')      # Lancashire and South Cumbria ICB
indicators_qk1 = pd.read_csv(f'input_data_ind/indicator_QK1_{year_v2}.csv')      # Leicester, Leicestershire and Rutland ICB
indicators_qjm = pd.read_csv(f'input_data_ind/indicator_QJM_{year_v2}.csv')      # Lincolnshire ICB
indicators_qhm = pd.read_csv(f'input_data_ind/indicator_QHM_{year_v2}.csv')      # North East and North Cumbria ICB
indicators_qmf = pd.read_csv(f'input_data_ind/indicator_QMF_{year_v2}.csv')      # North East London ICB
indicators_qpm = pd.read_csv(f'input_data_ind/indicator_QPM_{year_v2}.csv')      # Northamptonshire ICB
indicators_qt1 = pd.read_csv(f'input_data_ind/indicator_QT1_{year_v2}.csv')      # Nottingham and Nottinghamshire ICB
indicators_qoc = pd.read_csv(f'input_data_ind/indicator_QOC_{year_v2}.csv')      # Shropshire, Telford and Wrekin ICB
indicators_qsl = pd.read_csv(f'input_data_ind/indicator_QSL_{year_v2}.csv')      # Somerset ICB
indicators_qkk = pd.read_csv(f'input_data_ind/indicator_QKK_{year_v2}.csv')      # South East London ICB
indicators_qwe = pd.read_csv(f'input_data_ind/indicator_QWE_{year_v2}.csv')      # South West London ICB
indicators_qf7 = pd.read_csv(f'input_data_ind/indicator_QF7_{year_v2}.csv')      # South Yorkshire ICB
indicators_qnc = pd.read_csv(f'input_data_ind/indicator_QNC_{year_v2}.csv')      # Staffordshire and Stoke-on-Trent ICB
indicators_qwo = pd.read_csv(f'input_data_ind/indicator_QWO_{year_v2}.csv')      # West Yorkshire ICB


# Import the population data
# Males
m_pop_S1Y5D = pd.read_csv(f'input_data_m/m_pop_S1Y5D_{year}.csv')      
m_pop_D7T5G = pd.read_csv(f'input_data_m/m_pop_D7T5G_{year}.csv')      
m_pop_T6Y0W = pd.read_csv(f'input_data_m/m_pop_T6Y0W_{year}.csv')      
m_pop_Z9B2Z = pd.read_csv(f'input_data_m/m_pop_Z9B2Z_{year}.csv')      
m_pop_S0E4D = pd.read_csv(f'input_data_m/m_pop_S0E4D_{year}.csv')      
m_pop_qox = pd.read_csv(f'input_data_m/m_pop_QOX_{year}.csv')      
m_pop_qhl = pd.read_csv(f'input_data_m/m_pop_QHL_{year}.csv')       
m_pop_qua = pd.read_csv(f'input_data_m/m_pop_QUA_{year}.csv')       
m_pop_quy = pd.read_csv(f'input_data_m/m_pop_QUY_{year}.csv')       
m_pop_qyg = pd.read_csv(f'input_data_m/m_pop_QYG_{year}.csv')       
m_pop_qt6 = pd.read_csv(f'input_data_m/m_pop_QT6_{year}.csv')       
m_pop_qwu = pd.read_csv(f'input_data_m/m_pop_QWU_{year}.csv')       
m_pop_qj2 = pd.read_csv(f'input_data_m/m_pop_QJ2_{year}.csv')       
m_pop_qjk = pd.read_csv(f'input_data_m/m_pop_QJK_{year}.csv')       
m_pop_qvv = pd.read_csv(f'input_data_m/m_pop_QVV_{year}.csv')      
m_pop_qr1 = pd.read_csv(f'input_data_m/m_pop_QR1_{year}.csv')       
m_pop_qop = pd.read_csv(f'input_data_m/m_pop_QOP_{year}.csv')       
m_pop_qrl = pd.read_csv(f'input_data_m/m_pop_QRL_{year}.csv')       
m_pop_qgh = pd.read_csv(f'input_data_m/m_pop_QGH_{year}.csv')       
m_pop_qoq = pd.read_csv(f'input_data_m/m_pop_QOQ_{year}.csv')       
m_pop_qks = pd.read_csv(f'input_data_m/m_pop_QKS_{year}.csv')       
m_pop_qe1 = pd.read_csv(f'input_data_m/m_pop_QE1_{year}.csv')       
m_pop_qk1 = pd.read_csv(f'input_data_m/m_pop_QK1_{year}.csv')       
m_pop_qjm = pd.read_csv(f'input_data_m/m_pop_QJM_{year}.csv')       
m_pop_qhm = pd.read_csv(f'input_data_m/m_pop_QHM_{year}.csv')       
m_pop_qmf = pd.read_csv(f'input_data_m/m_pop_QMF_{year}.csv')       
m_pop_qpm = pd.read_csv(f'input_data_m/m_pop_QPM_{year}.csv')       
m_pop_qt1 = pd.read_csv(f'input_data_m/m_pop_QT1_{year}.csv')       
m_pop_qoc = pd.read_csv(f'input_data_m/m_pop_QOC_{year}.csv')       
m_pop_qsl = pd.read_csv(f'input_data_m/m_pop_QSL_{year}.csv')       
m_pop_qkk = pd.read_csv(f'input_data_m/m_pop_QKK_{year}.csv')       
m_pop_qwe = pd.read_csv(f'input_data_m/m_pop_QWE_{year}.csv')       
m_pop_qf7 = pd.read_csv(f'input_data_m/m_pop_QF7_{year}.csv')       
m_pop_qnc = pd.read_csv(f'input_data_m/m_pop_QNC_{year}.csv')       
m_pop_qwo = pd.read_csv(f'input_data_m/m_pop_QWO_{year}.csv')       

# Females
f_pop_S1Y5D = pd.read_csv(f'input_data_f/f_pop_S1Y5D_{year}.csv')       
f_pop_D7T5G = pd.read_csv(f'input_data_f/f_pop_D7T5G_{year}.csv')       
f_pop_T6Y0W = pd.read_csv(f'input_data_f/f_pop_T6Y0W_{year}.csv')       
f_pop_Z9B2Z = pd.read_csv(f'input_data_f/f_pop_Z9B2Z_{year}.csv')       
f_pop_S0E4D = pd.read_csv(f'input_data_f/f_pop_S0E4D_{year}.csv')
f_pop_qox = pd.read_csv(f'input_data_f/f_pop_QOX_{year}.csv')       
f_pop_qhl = pd.read_csv(f'input_data_f/f_pop_QHL_{year}.csv')       
f_pop_qua = pd.read_csv(f'input_data_f/f_pop_QUA_{year}.csv')       
f_pop_quy = pd.read_csv(f'input_data_f/f_pop_QUY_{year}.csv')       
f_pop_qyg = pd.read_csv(f'input_data_f/f_pop_QYG_{year}.csv')       
f_pop_qt6 = pd.read_csv(f'input_data_f/f_pop_QT6_{year}.csv')       
f_pop_qwu = pd.read_csv(f'input_data_f/f_pop_QWU_{year}.csv')       
f_pop_qj2 = pd.read_csv(f'input_data_f/f_pop_QJ2_{year}.csv')       
f_pop_qjk = pd.read_csv(f'input_data_f/f_pop_QJK_{year}.csv')       
f_pop_qvv = pd.read_csv(f'input_data_f/f_pop_QVV_{year}.csv')       
f_pop_qr1 = pd.read_csv(f'input_data_f/f_pop_QR1_{year}.csv')       
f_pop_qop = pd.read_csv(f'input_data_f/f_pop_QOP_{year}.csv')       
f_pop_qrl = pd.read_csv(f'input_data_f/f_pop_QRL_{year}.csv')       
f_pop_qgh = pd.read_csv(f'input_data_f/f_pop_QGH_{year}.csv')       
f_pop_qoq = pd.read_csv(f'input_data_f/f_pop_QOQ_{year}.csv')       
f_pop_qks = pd.read_csv(f'input_data_f/f_pop_QKS_{year}.csv')       
f_pop_qe1 = pd.read_csv(f'input_data_f/f_pop_QE1_{year}.csv')       
f_pop_qk1 = pd.read_csv(f'input_data_f/f_pop_QK1_{year}.csv')       
f_pop_qjm = pd.read_csv(f'input_data_f/f_pop_QJM_{year}.csv')       
f_pop_qhm = pd.read_csv(f'input_data_f/f_pop_QHM_{year}.csv')       
f_pop_qmf = pd.read_csv(f'input_data_f/f_pop_QMF_{year}.csv')       
f_pop_qpm = pd.read_csv(f'input_data_f/f_pop_QPM_{year}.csv')       
f_pop_qt1 = pd.read_csv(f'input_data_f/f_pop_QT1_{year}.csv')       
f_pop_qoc = pd.read_csv(f'input_data_f/f_pop_QOC_{year}.csv')       
f_pop_qsl = pd.read_csv(f'input_data_f/f_pop_QSL_{year}.csv')       
f_pop_qkk = pd.read_csv(f'input_data_f/f_pop_QKK_{year}.csv')       
f_pop_qwe = pd.read_csv(f'input_data_f/f_pop_QWE_{year}.csv')       
f_pop_qf7 = pd.read_csv(f'input_data_f/f_pop_QF7_{year}.csv')       
f_pop_qnc = pd.read_csv(f'input_data_f/f_pop_QNC_{year}.csv')       
f_pop_qwo = pd.read_csv(f'input_data_f/f_pop_QWO_{year}.csv')     


# do I need to close all these files above now e.g. 'indicators_qox.close()       







