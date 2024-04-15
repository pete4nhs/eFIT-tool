"""
@author: peter.saiu@nhs.net
Created: 2024
version: 0.0.1

Description: 
The code in this streamlit script imports the population and indicators data which 
are then imported and run in the strealit app ('eFIT')      # 

"""

import pandas as pd

# Import the indicators data
indicators_qox = pd.read_csv('input_data_ind/QOX.csv')      # Bath and North East Somerset, Swindon and Wiltshire ICB
indicators_qhg = pd.read_csv('input_data_ind/QHG.csv')      # Bedfordshire, Luton and Milton Keynes ICB
indicators_qhl = pd.read_csv('input_data_ind/QHL.csv')      # Birmingham and Solihull ICB
indicators_qua = pd.read_csv('input_data_ind/QUA.csv')      # Black Country ICB
indicators_quy = pd.read_csv('input_data_ind/QUY.csv')      # Bristol, North Somerset and South Gloucestershire ICB
indicators_qu9 = pd.read_csv('input_data_ind/QU9.csv')      # Buckinghamshire, Oxfordshire and Berkshire West ICB
indicators_que = pd.read_csv('input_data_ind/QUE.csv')      # Cambridgeshire and Peterborough ICB
indicators_qyg = pd.read_csv('input_data_ind/QYG.csv')      # Cheshire and Merseyside ICB
indicators_qt6 = pd.read_csv('input_data_ind/QT6.csv')      # Cornwall and the Isles of Scilly ICB
indicators_qwu = pd.read_csv('input_data_ind/QWU.csv')      # Coventry and Warwickshire ICB
indicators_qj2 = pd.read_csv('input_data_ind/QJ2.csv')      # Derby and Derbyshire ICB
indicators_qjk = pd.read_csv('input_data_ind/QJK.csv')      # Devon ICB
indicators_qvv = pd.read_csv('input_data_ind/QVV.csv')      # Dorset ICB
indicators_qnq = pd.read_csv('input_data_ind/QNQ.csv')      # Frimley ICB
indicators_qr1 = pd.read_csv('input_data_ind/QR1.csv')      # Gloucestershire ICB
indicators_qop = pd.read_csv('input_data_ind/QOP.csv')      # Greater Manchester ICB
indicators_qrl = pd.read_csv('input_data_ind/QR1.csv')      # Hampshire and the Isle of Wight ICB
indicators_qgh = pd.read_csv('input_data_ind/QGH.csv')      # Herefordshire and Worcestershire ICB
indicators_qm7 = pd.read_csv('input_data_ind/QM7.csv')      # Hertfordshire and West Essex ICB
indicators_qoq = pd.read_csv('input_data_ind/QOQ.csv')      # Humber and North Yorkshire ICB
indicators_qks = pd.read_csv('input_data_ind/QKS.csv')      # Kent and Medway ICB
indicators_qe1 = pd.read_csv('input_data_ind/QE1.csv')      # Lancashire and South Cumbria ICB
indicators_qk1 = pd.read_csv('input_data_ind/QK1.csv')      # Leicester, Leicestershire and Rutland ICB
indicators_qjm = pd.read_csv('input_data_ind/QJM.csv')      # Lincolnshire ICB
indicators_qh8 = pd.read_csv('input_data_ind/QH8.csv')      # Mid and South Essex ICB
indicators_qmm = pd.read_csv('input_data_ind/QMM.csv')      # Norfolk and Waveney ICB
indicators_qmj = pd.read_csv('input_data_ind/QMJ.csv')      # North Central London ICB
indicators_qhm = pd.read_csv('input_data_ind/QHM.csv')      # North East and North Cumbria ICB
indicators_qmf = pd.read_csv('input_data_ind/QMF.csv')      # North East London ICB
indicators_qrv = pd.read_csv('input_data_ind/QRV.csv')      # North West London ICB
indicators_qpm = pd.read_csv('input_data_ind/QPM.csv')      # Northamptonshire ICB
indicators_qt1 = pd.read_csv('input_data_ind/QT1.csv')      # Nottingham and Nottinghamshire ICB
indicators_qoc = pd.read_csv('input_data_ind/QOC.csv')      # Shropshire, Telford and Wrekin ICB
indicators_qsl = pd.read_csv('input_data_ind/QSL.csv')      # Somerset ICB
indicators_qkk = pd.read_csv('input_data_ind/QKK.csv')      # South East London ICB
indicators_qwe = pd.read_csv('input_data_ind/QWE.csv')      # South West London ICB
indicators_qf7 = pd.read_csv('input_data_ind/QF7.csv')      # South Yorkshire ICB
indicators_qnc = pd.read_csv('input_data_ind/QNC.csv')      # Staffordshire and Stoke-on-Trent ICB
indicators_qjg = pd.read_csv('input_data_ind/QJG.csv')      # Suffolk and North East Essex ICB
indicators_qxu = pd.read_csv('input_data_ind/QXU.csv')      # Surrey Heartlands ICB
indicators_qnx = pd.read_csv('input_data_ind/QNX.csv')      # Sussex ICB
indicators_qwo = pd.read_csv('input_data_ind/QWO.csv')      # West Yorkshire ICB


# Import the population data
# Males
m_pop_qox = pd.read_csv('input_data_m/m_pop_QOX.csv')       
m_pop_qhg = pd.read_csv('input_data_m/m_pop_QHG.csv')       
m_pop_qhl = pd.read_csv('input_data_m/m_pop_QHL.csv')       
m_pop_qua = pd.read_csv('input_data_m/m_pop_QUA.csv')       
m_pop_quy = pd.read_csv('input_data_m/m_pop_QUY.csv')       
m_pop_qu9 = pd.read_csv('input_data_m/m_pop_QU9.csv')       
m_pop_que = pd.read_csv('input_data_m/m_pop_QUE.csv')       
m_pop_qyg = pd.read_csv('input_data_m/m_pop_QYG.csv')       
m_pop_qt6 = pd.read_csv('input_data_m/m_pop_AT6.csv')       
m_pop_qwu = pd.read_csv('input_data_m/m_pop_QWU.csv')       
m_pop_qj2 = pd.read_csv('input_data_m/m_pop_QJ2.csv')       
m_pop_qjk = pd.read_csv('input_data_m/m_pop_QJK.csv')       
m_pop_qvv = pd.read_csv('input_data_m/m_pop_QVV.csv')      
m_pop_qnq = pd.read_csv('input_data_m/m_pop_QNQ.csv')       
m_pop_qr1 = pd.read_csv('input_data_m/m_pop_QR1.csv')       
m_pop_qop = pd.read_csv('input_data_m/m_pop_QOP.csv')       
m_pop_qrl = pd.read_csv('input_data_m/m_pop_QRL.csv')       
m_pop_qgh = pd.read_csv('input_data_m/m_pop_QGH.csv')       
m_pop_qm7 = pd.read_csv('input_data_m/m_pop_QM7.csv')       
m_pop_qoq = pd.read_csv('input_data_m/m_pop_QOQ.csv')       
m_pop_qks = pd.read_csv('input_data_m/m_pop_QKS.csv')       
m_pop_qe1 = pd.read_csv('input_data_m/m_pop_QE1.csv')       
m_pop_qk1 = pd.read_csv('input_data_m/m_pop_QK1.csv')       
m_pop_qjm = pd.read_csv('input_data_m/m_pop_QJM.csv')       
m_pop_qh8 = pd.read_csv('input_data_m/m_pop_QH8.csv')       
m_pop_qmm = pd.read_csv('input_data_m/m_pop_QMM.csv')       
m_pop_qmj = pd.read_csv('input_data_m/m_pop_QMJ.csv')       
m_pop_qhm = pd.read_csv('input_data_m/m_pop_QHM.csv')       
m_pop_qmf = pd.read_csv('input_data_m/m_pop_QMF.csv')       
m_pop_qrv = pd.read_csv('input_data_m/m_pop_QRV.csv')       
m_pop_qpm = pd.read_csv('input_data_m/m_pop_QPM.csv')       
m_pop_qt1 = pd.read_csv('input_data_m/m_pop_QT1.csv')       
m_pop_qoc = pd.read_csv('input_data_m/m_pop_QOC.csv')       
m_pop_qsl = pd.read_csv('input_data_m/m_pop_QSL.csv')       
m_pop_qkk = pd.read_csv('input_data_m/m_pop_QKK.csv')       
m_pop_qwe = pd.read_csv('input_data_m/m_pop_QWE.csv')       
m_pop_qf7 = pd.read_csv('input_data_m/m_pop_QF7.csv')       
m_pop_qnc = pd.read_csv('input_data_m/m_pop_QNC.csv')       
m_pop_qjg = pd.read_csv('input_data_m/m_pop_QJG.csv')       
m_pop_qxu = pd.read_csv('input_data_m/m_pop_QXU.csv')       
m_pop_qnx = pd.read_csv('input_data_m/m_pop_QNX.csv')       
m_pop_qwo = pd.read_csv('input_data_m/m_pop_QWO.csv')       

# Females
f_pop_qox = pd.read_csv('input_data_f/f_pop_QOX.csv')       
f_pop_qhg = pd.read_csv('input_data_f/f_pop_QHG.csv')       
f_pop_qhl = pd.read_csv('input_data_f/f_pop_QHL.csv')       
f_pop_qua = pd.read_csv('input_data_f/f_pop_QUA.csv')       
f_pop_quy = pd.read_csv('input_data_f/f_pop_QUY.csv')       
f_pop_qu9 = pd.read_csv('input_data_f/f_pop_QU9.csv')       
f_pop_que = pd.read_csv('input_data_f/f_pop_QUE.csv')       
f_pop_qyg = pd.read_csv('input_data_f/f_pop_QYG.csv')       
f_pop_qt6 = pd.read_csv('input_data_f/f_pop_QT6.csv')       
f_pop_qwu = pd.read_csv('input_data_f/f_pop_QWU.csv')       
f_pop_qj2 = pd.read_csv('input_data_f/f_pop_QJ2.csv')       
f_pop_qjk = pd.read_csv('input_data_f/f_pop_QJK.csv')       
f_pop_qvv = pd.read_csv('input_data_f/f_pop_QVV.csv')       
f_pop_qnq = pd.read_csv('input_data_f/f_pop_QNQ.csv')       
f_pop_qr1 = pd.read_csv('input_data_f/f_pop_QR1.csv')       
f_pop_qop = pd.read_csv('input_data_f/f_pop_QOP.csv')       
f_pop_qrl = pd.read_csv('input_data_f/f_pop_QRL.csv')       
f_pop_qgh = pd.read_csv('input_data_f/f_pop_QGH.csv')       
f_pop_qm7 = pd.read_csv('input_data_f/f_pop_QM7.csv')       
f_pop_qoq = pd.read_csv('input_data_f/f_pop_QOQ.csv')       
f_pop_qks = pd.read_csv('input_data_f/f_pop_QKS.csv')       
f_pop_qe1 = pd.read_csv('input_data_f/f_pop_QE1.csv')       
f_pop_qk1 = pd.read_csv('input_data_f/f_pop_QK1.csv')       
f_pop_qjm = pd.read_csv('input_data_f/f_pop_QJM.csv')       
f_pop_qh8 = pd.read_csv('input_data_f/f_pop_QH8.csv')       
f_pop_qmm = pd.read_csv('input_data_f/f_pop_QMM.csv')       
f_pop_qmj = pd.read_csv('input_data_f/f_pop_QMJ.csv')       
f_pop_qhm = pd.read_csv('input_data_f/f_pop_QHM.csv')       
f_pop_qmf = pd.read_csv('input_data_f/f_pop_QMF.csv')       
f_pop_qrv = pd.read_csv('input_data_f/f_pop_QRV.csv')       
f_pop_qpm = pd.read_csv('input_data_f/f_pop_QPM.csv')       
f_pop_qt1 = pd.read_csv('input_data_f/f_pop_QT1.csv')       
f_pop_qoc = pd.read_csv('input_data_f/f_pop_QOC.csv')       
f_pop_qsl = pd.read_csv('input_data_f/f_pop_QSL.csv')       
f_pop_qkk = pd.read_csv('input_data_f/f_pop_QKK.csv')       
f_pop_qwe = pd.read_csv('input_data_f/f_pop_QWE.csv')       
f_pop_qf7 = pd.read_csv('input_data_f/f_pop_QF7.csv')       
f_pop_qnc = pd.read_csv('input_data_f/f_pop_QNC.csv')       
f_pop_qjg = pd.read_csv('input_data_f/f_pop_QJG.csv')       
f_pop_qxu = pd.read_csv('input_data_f/f_pop_QXU.csv')       
f_pop_qnx = pd.read_csv('input_data_f/f_pop_QNX.csv')       
f_pop_qwo = pd.read_csv('input_data_f/f_pop_QWO.csv')       


# do I need to close all these files above now e.g. 'indicators_qox.close()       







