"""
@author: peter.saiu@nhs.net
Created: 2024
version: 0.0.1

Description: 
The code in this streamlit script imports the population and indicators data which 
are then imported and run in the strealit app ('eFIT')

"""

import pandas as pd

# Import the indicators data
indicators_qox = pd.read_csv('input_data_ind/qox.csv')
indicators_qhg = pd.read_csv('/input_data_ind/qhg.csv')
indicators_qhl = pd.read_csv('/input_data_ind/qhl.csv')
indicators_qua = pd.read_csv('input_data_ind/qua.csv')
indicators_quy = pd.read_csv('input_data_ind/quy.csv')
indicators_qu9 = pd.read_csv('input_data_ind/qu9.csv')
indicators_que = pd.read_csv('input_data_ind/que.csv')
indicators_qyg = pd.read_csv('input_data_ind/qyg.csv')
indicators_qt6 = pd.read_csv('input_data_ind/qt6.csv')
indicators_qwu = pd.read_csv('input_data_ind/qwu.csv')
indicators_qj2 = pd.read_csv('input_data_ind/qj2.csv')
indicators_qjk = pd.read_csv('input_data_ind/qjk.csv')
indicators_qvv = pd.read_csv('input_data_ind/qvv.csv')
indicators_qnq = pd.read_csv('input_data_ind/qnq.csv')
indicators_qr1 = pd.read_csv('input_data_ind/qr1.csv')
indicators_qop = pd.read_csv('input_data_ind/qop.csv')
indicators_qrl = pd.read_csv('input_data_ind/qrl.csv')
indicators_qgh = pd.read_csv('input_data_ind/qgh.csv')
indicators_qm7 = pd.read_csv('input_data_ind/qm7.csv')
indicators_qoq = pd.read_csv('input_data_ind/qoq.csv')
indicators_qks = pd.read_csv('input_data_ind/qks.csv')
indicators_qe1 = pd.read_csv('input_data_ind/qe1.csv')
indicators_qk1 = pd.read_csv('input_data_ind/qk1.csv')
indicators_qjm = pd.read_csv('input_data_ind/qjm.csv')
indicators_qh8 = pd.read_csv('input_data_ind/qh8.csv')
indicators_qmm = pd.read_csv('input_data_ind/qmm.csv')
indicators_qmj = pd.read_csv('input_data_ind/qmj.csv')
indicators_qhm = pd.read_csv('input_data_ind/qhm.csv')
indicators_qmf = pd.read_csv('input_data_ind/qmf.csv')
indicators_qrv = pd.read_csv('input_data_ind/qrv.csv')
indicators_qpm = pd.read_csv('input_data_ind/qpm.csv')
indicators_qt1 = pd.read_csv('input_data_ind/qt1.csv')
indicators_qoc = pd.read_csv('input_data_ind/qoc.csv')
indicators_qsl = pd.read_csv('input_data_ind/qsl.csv')
indicators_qkk = pd.read_csv('input_data_ind/qkk.csv')
indicators_qwe = pd.read_csv('input_data_ind/qwe.csv')
indicators_qf7 = pd.read_csv('input_data_ind/qf7.csv')
indicators_qnc = pd.read_csv('input_data_ind/qnc.csv')
indicators_qjg = pd.read_csv('input_data_ind/qjg.csv')
indicators_qxu = pd.read_csv('input_data_ind/qxu.csv')
indicators_qnx = pd.read_csv('input_data_ind/qnx.csv')
indicators_qwo = pd.read_csv('input_data_ind/qwo.csv')


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







