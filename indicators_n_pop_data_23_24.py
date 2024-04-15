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
indicators_qrl = pd.read_csv('input_data_ind/QRL.csv')      # Hampshire and the Isle of Wight ICB
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
m_pop_qox = pd.read_csv('input_data_m/m_pop_qox.csv')       
m_pop_qhg = pd.read_csv('input_data_m/m_pop_qhg.csv')       
m_pop_qhl = pd.read_csv('input_data_m/m_pop_qhl.csv')       
m_pop_qua = pd.read_csv('input_data_m/m_pop_qua.csv')       
m_pop_quy = pd.read_csv('input_data_m/m_pop_quy.csv')       
m_pop_qu9 = pd.read_csv('input_data_m/m_pop_qu9.csv')       
m_pop_que = pd.read_csv('input_data_m/m_pop_que.csv')       
m_pop_qyg = pd.read_csv('input_data_m/m_pop_qyg.csv')       
m_pop_qt6 = pd.read_csv('input_data_m/m_pop_qt6.csv')       
m_pop_qwu = pd.read_csv('input_data_m/m_pop_qwu.csv')       
m_pop_qj2 = pd.read_csv('input_data_m/m_pop_qj2.csv')       
m_pop_qjk = pd.read_csv('input_data_m/m_pop_qjk.csv')       
m_pop_qvv = pd.read_csv('input_data_m/m_pop_qvv.csv')      
m_pop_qnq = pd.read_csv('input_data_m/m_pop_qnq.csv')       
m_pop_qr1 = pd.read_csv('input_data_m/m_pop_qr1.csv')       
m_pop_qop = pd.read_csv('input_data_m/m_pop_qop.csv')       
m_pop_qrl = pd.read_csv('input_data_m/m_pop_qrl.csv')       
m_pop_qgh = pd.read_csv('input_data_m/m_pop_qgh.csv')       
m_pop_qm7 = pd.read_csv('input_data_m/m_pop_qm7.csv')       
m_pop_qoq = pd.read_csv('input_data_m/m_pop_qoq.csv')       
m_pop_qks = pd.read_csv('input_data_m/m_pop_qks.csv')       
m_pop_qe1 = pd.read_csv('input_data_m/m_pop_qe1.csv')       
m_pop_qk1 = pd.read_csv('input_data_m/m_pop_qk1.csv')       
m_pop_qjm = pd.read_csv('input_data_m/m_pop_qjm.csv')       
m_pop_qh8 = pd.read_csv('input_data_m/m_pop_qh8.csv')       
m_pop_qmm = pd.read_csv('input_data_m/m_pop_qmm.csv')       
m_pop_qmj = pd.read_csv('input_data_m/m_pop_qmj.csv')       
m_pop_qhm = pd.read_csv('input_data_m/m_pop_qhm.csv')       
m_pop_qmf = pd.read_csv('input_data_m/m_pop_qmf.csv')       
m_pop_qrv = pd.read_csv('input_data_m/m_pop_qrv.csv')       
m_pop_qpm = pd.read_csv('input_data_m/m_pop_qpm.csv')       
m_pop_qt1 = pd.read_csv('input_data_m/m_pop_qt1.csv')       
m_pop_qoc = pd.read_csv('input_data_m/m_pop_qoc.csv')       
m_pop_qsl = pd.read_csv('input_data_m/m_pop_qsl.csv')       
m_pop_qkk = pd.read_csv('input_data_m/m_pop_qkk.csv')       
m_pop_qwe = pd.read_csv('input_data_m/m_pop_qwe.csv')       
m_pop_qf7 = pd.read_csv('input_data_m/m_pop_qf7.csv')       
m_pop_qnc = pd.read_csv('input_data_m/m_pop_qnc.csv')       
m_pop_qjg = pd.read_csv('input_data_m/m_pop_qjg.csv')       
m_pop_qxu = pd.read_csv('input_data_m/m_pop_qxu.csv')       
m_pop_qnx = pd.read_csv('input_data_m/m_pop_qnx.csv')       
m_pop_qwo = pd.read_csv('input_data_m/m_pop_qwo.csv')       

# Females
f_pop_qox = pd.read_csv('input_data_f/f_pop_qox.csv')       
f_pop_qhg = pd.read_csv('input_data_f/f_pop_qhg.csv')       
f_pop_qhl = pd.read_csv('input_data_f/f_pop_qhl.csv')       
f_pop_qua = pd.read_csv('input_data_f/f_pop_qua.csv')       
f_pop_quy = pd.read_csv('input_data_f/f_pop_quy.csv')       
f_pop_qu9 = pd.read_csv('input_data_f/f_pop_qu9.csv')       
f_pop_que = pd.read_csv('input_data_f/f_pop_que.csv')       
f_pop_qyg = pd.read_csv('input_data_f/f_pop_qyg.csv')       
f_pop_qt6 = pd.read_csv('input_data_f/f_pop_qt6.csv')       
f_pop_qwu = pd.read_csv('input_data_f/f_pop_qwu.csv')       
f_pop_qj2 = pd.read_csv('input_data_f/f_pop_qj2.csv')       
f_pop_qjk = pd.read_csv('input_data_f/f_pop_qjk.csv')       
f_pop_qvv = pd.read_csv('input_data_f/f_pop_qvv.csv')       
f_pop_qnq = pd.read_csv('input_data_f/f_pop_qnq.csv')       
f_pop_qr1 = pd.read_csv('input_data_f/f_pop_qr1.csv')       
f_pop_qop = pd.read_csv('input_data_f/f_pop_qop.csv')       
f_pop_qrl = pd.read_csv('input_data_f/f_pop_qrl.csv')       
f_pop_qgh = pd.read_csv('input_data_f/f_pop_qgh.csv')       
f_pop_qm7 = pd.read_csv('input_data_f/f_pop_qm7.csv')       
f_pop_qoq = pd.read_csv('input_data_f/f_pop_qoq.csv')       
f_pop_qks = pd.read_csv('input_data_f/f_pop_qks.csv')       
f_pop_qe1 = pd.read_csv('input_data_f/f_pop_qe1.csv')       
f_pop_qk1 = pd.read_csv('input_data_f/f_pop_qk1.csv')       
f_pop_qjm = pd.read_csv('input_data_f/f_pop_qjm.csv')       
f_pop_qh8 = pd.read_csv('input_data_f/f_pop_qh8.csv')       
f_pop_qmm = pd.read_csv('input_data_f/f_pop_qmm.csv')       
f_pop_qmj = pd.read_csv('input_data_f/f_pop_qmj.csv')       
f_pop_qhm = pd.read_csv('input_data_f/f_pop_qhm.csv')       
f_pop_qmf = pd.read_csv('input_data_f/f_pop_qmf.csv')       
f_pop_qrv = pd.read_csv('input_data_f/f_pop_qrv.csv')       
f_pop_qpm = pd.read_csv('input_data_f/f_pop_qpm.csv')       
f_pop_qt1 = pd.read_csv('input_data_f/f_pop_qt1.csv')       
f_pop_qoc = pd.read_csv('input_data_f/f_pop_qoc.csv')       
f_pop_qsl = pd.read_csv('input_data_f/f_pop_qsl.csv')       
f_pop_qkk = pd.read_csv('input_data_f/f_pop_qkk.csv')       
f_pop_qwe = pd.read_csv('input_data_f/f_pop_qwe.csv')       
f_pop_qf7 = pd.read_csv('input_data_f/f_pop_qf7.csv')       
f_pop_qnc = pd.read_csv('input_data_f/f_pop_qnc.csv')       
f_pop_qjg = pd.read_csv('input_data_f/f_pop_qjg.csv')       
f_pop_qxu = pd.read_csv('input_data_f/f_pop_qxu.csv')       
f_pop_qnx = pd.read_csv('input_data_f/f_pop_qnx.csv')       
f_pop_qwo = pd.read_csv('input_data_f/f_pop_qwo.csv')       


# do I need to close all these files above now e.g. 'indicators_qox.close()       







