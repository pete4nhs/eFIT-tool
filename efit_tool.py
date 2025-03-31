'''
@author: peter.saiu@nhs.net
Created: 2024
version: 0.2.1
Added on 31/3/2025

Description: 
The code in this streamlit script allows you to run the allocation calculations based on the 
user's preferences. 

Acknowledgements: Dan Chalk, Sammi Rosser, John Ford, Shylaja Thomas and Stefano Conti.

'''

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from  indicators_n_pop_data_25_26 import indicators_qox, indicators_qhg, indicators_qhl, \
    indicators_qua, indicators_quy, indicators_qu9, indicators_que, indicators_qyg, indicators_qt6, \
    indicators_qwu, indicators_qj2, indicators_qjk, indicators_qvv, indicators_qnq, indicators_qr1, \
    indicators_qop, indicators_qrl, indicators_qgh, indicators_qm7, indicators_qoq, indicators_qks, \
    indicators_qe1, indicators_qk1, indicators_qjm, indicators_qh8, indicators_qmm, indicators_qmj, \
    indicators_qhm, indicators_qmf, indicators_qrv, indicators_qpm, indicators_qt1, indicators_qoc, \
    indicators_qsl, indicators_qkk, indicators_qwe, indicators_qf7, indicators_qnc, indicators_qjg, \
    indicators_qxu, indicators_qnx, indicators_qwo
from indicators_n_pop_data_25_26 import m_pop_qox, m_pop_qhg, m_pop_qhl, m_pop_qua, m_pop_quy, \
    m_pop_qu9, m_pop_que, m_pop_qyg, m_pop_qt6, m_pop_qwu, m_pop_qj2, m_pop_qjk, m_pop_qvv, \
    m_pop_qnq, m_pop_qr1, m_pop_qop, m_pop_qrl, m_pop_qgh, m_pop_qm7, m_pop_qoq, m_pop_qks, \
    m_pop_qe1, m_pop_qk1, m_pop_qjm, m_pop_qh8, m_pop_qmm, m_pop_qmj, m_pop_qhm, m_pop_qmf, \
    m_pop_qrv, m_pop_qpm, m_pop_qt1, m_pop_qoc, m_pop_qsl, m_pop_qkk, m_pop_qwe, m_pop_qf7, \
    m_pop_qnc, m_pop_qjg, m_pop_qxu, m_pop_qnx, m_pop_qwo

from indicators_n_pop_data_25_26 import f_pop_qox, f_pop_qhg, f_pop_qhl, f_pop_qua, f_pop_quy, \
    f_pop_qu9, f_pop_que, f_pop_qyg, f_pop_qt6, f_pop_qwu, f_pop_qj2, f_pop_qjk, f_pop_qvv, \
    f_pop_qnq, f_pop_qr1, f_pop_qop, f_pop_qrl, f_pop_qgh, f_pop_qm7, f_pop_qoq, f_pop_qks, \
    f_pop_qe1, f_pop_qk1, f_pop_qjm, f_pop_qh8, f_pop_qmm, f_pop_qmj, f_pop_qhm, f_pop_qmf, \
    f_pop_qrv, f_pop_qpm, f_pop_qt1, f_pop_qoc, f_pop_qsl, f_pop_qkk, f_pop_qwe, f_pop_qf7, \
    f_pop_qnc, f_pop_qjg, f_pop_qxu, f_pop_qnx, f_pop_qwo


# Set page configuration
st.set_page_config(
    page_title="eFIT",
    page_icon="https://www.england.nhs.uk/wp-content/themes/nhsengland/static/img/favicon.ico",
    layout="wide",    # alternatively write "centered" 
    initial_sidebar_state="expanded",
    menu_items={
#        "More info": "https://www.heec.co.uk/resources/extra-funding-allocation-inequality-tool-efit/",   # not accepted key            
#        "Report a bug": "https://github.com/",    # amend with web address of my GitHub page
        "About": "This tool is designed to support ICBs to calculate the allocation of extra funding to General Practices. Please refer to the 'Tutorial' tab in the sidebar for User Guide for instructions." 
    },)

# The background colour is defined by the 'config' file in the '.streamlit' folder

# This is to add in a title for our web app's page (removed because title added as an image)
#st.title('Extra Funding allocation Inequality Tool (eFIT)')

# ADD TITLE AS IMAGE
#st.image('input_data_other/name_wo_logo_2.png', width=500)

# ADD OLD LOGO for C&P ICB 
#st.image('input_data_other/logos_n_name.png', width=750)

# ADD NEW LOGO for London Region 
st.image('input_data_other/london_logos_n_name.png', width=1050)

#These 17 lines make you insert text from a 'markdown' file (text written as markdown) 
#by reading in the file
INTRO_FILE = 'input_data_other/overview_gp.md'
def read_file_contents(file_name):
    ''''
    Read the contents of a file.
    Params:
    ------
    file_name: str
        Path to file.
    Returns:
    -------
    str
    '''
    with open(file_name) as f:
        return f.read()
    
# show the markdown
st.markdown(read_file_contents(INTRO_FILE))
################################################################################

icb_list = ['Bath and North East Somerset, Swindon and Wiltshire ICB', 'Bedfordshire, Luton and Milton Keynes ICB',
'Birmingham and Solihull ICB', 'Black Country ICB', 'Bristol, North Somerset and South Gloucestershire ICB',
'Buckinghamshire, Oxfordshire and Berkshire West ICB', 'Cambridgeshire and Peterborough ICB',
'Cheshire and Merseyside ICB', 'Cornwall and the Isles of Scilly ICB', 'Coventry and Warwickshire ICB',
'Derby and Derbyshire ICB', 'Devon ICB', 'Dorset ICB', 'Frimley ICB', 'Gloucestershire ICB',
'Greater Manchester ICB', 'Hampshire and Isle of Wight ICB', 'Herefordshire and Worcestershire ICB',
'Hertfordshire and West Essex ICB', 'Humber and North Yorkshire ICB', 'Kent and Medway ICB',
'Lancashire and South Cumbria ICB', 'Leicester, Leicestershire and Rutland ICB', 'Lincolnshire ICB',
'Mid and South Essex ICB', 'Norfolk and Waveney ICB', 'North Central London ICB', 
'North East and North Cumbria ICB', 'North East London ICB', 'North West London ICB',
'Northamptonshire ICB', 'Nottingham and Nottinghamshire ICB', 'Shropshire, Telford and Wrekin ICB',
'Somerset ICB', 'South East London ICB', 'South West London ICB', 'South Yorkshire ICB',
'Staffordshire and Stoke-on-Trent ICB', 'Suffolk and North East Essex ICB', 'Surrey Heartlands ICB',
'Sussex ICB', 'West Yorkshire ICB']

# SIDEBAR
icb_choice = st.sidebar.selectbox("**Select your ICB**:", icb_list, help="Select your ICB from the drop down list")

# Create a dictionary to store indicator dataframes for the indicators
icb_indicators_dict = {
'Bath and North East Somerset, Swindon and Wiltshire ICB': indicators_qox, 
'Bedfordshire, Luton and Milton Keynes ICB': indicators_qhg, 'Birmingham and Solihull ICB': indicators_qhl, 
'Black Country ICB': indicators_qua, 'Bristol, North Somerset and South Gloucestershire ICB': indicators_quy,
'Buckinghamshire, Oxfordshire and Berkshire West ICB': indicators_qu9, 'Cambridgeshire and Peterborough ICB': indicators_que,
'Cheshire and Merseyside ICB': indicators_qyg, 'Cornwall and the Isles of Scilly ICB': indicators_qt6, 
'Coventry and Warwickshire ICB': indicators_qwu,'Derby and Derbyshire ICB': indicators_qj2, 'Devon ICB': indicators_qjk, 
'Dorset ICB': indicators_qvv, 'Frimley ICB': indicators_qnq, 'Gloucestershire ICB': indicators_qr1, 'Greater Manchester ICB': indicators_qop, 
'Hampshire and Isle of Wight ICB': indicators_qrl, 'Herefordshire and Worcestershire ICB': indicators_qgh,
'Hertfordshire and West Essex ICB': indicators_qm7, 'Humber and North Yorkshire ICB': indicators_qoq, 
'Kent and Medway ICB': indicators_qks,'Lancashire and South Cumbria ICB': indicators_qe1, 'Leicester, Leicestershire and Rutland ICB': indicators_qk1, 
'Lincolnshire ICB': indicators_qjm, 'Mid and South Essex ICB': indicators_qh8, 'Norfolk and Waveney ICB': indicators_qmm, 
'North Central London ICB': indicators_qmj, 'North East and North Cumbria ICB': indicators_qhm, 'North East London ICB': indicators_qmf, 
'North West London ICB': indicators_qrv, 'Northamptonshire ICB': indicators_qpm, 'Nottingham and Nottinghamshire ICB': indicators_qt1, 
'Shropshire, Telford and Wrekin ICB': indicators_qoc, 'Somerset ICB': indicators_qsl, 'South East London ICB': indicators_qkk, 
'South West London ICB': indicators_qwe, 'South Yorkshire ICB': indicators_qf7, 'Staffordshire and Stoke-on-Trent ICB': indicators_qnc, 
'Suffolk and North East Essex ICB': indicators_qjg, 'Surrey Heartlands ICB': indicators_qxu, 'Sussex ICB': indicators_qnx, 
'West Yorkshire ICB': indicators_qwo}


# Create 2 dictionaries to store indicator dataframes for the population (for males and females)
pop_m_dict = {
'Bath and North East Somerset, Swindon and Wiltshire ICB': m_pop_qox, 
'Bedfordshire, Luton and Milton Keynes ICB': m_pop_qhg, 'Birmingham and Solihull ICB': m_pop_qhl, 
'Black Country ICB': m_pop_qua, 'Bristol, North Somerset and South Gloucestershire ICB': m_pop_quy,
'Buckinghamshire, Oxfordshire and Berkshire West ICB': m_pop_qu9, 'Cambridgeshire and Peterborough ICB': m_pop_que,
'Cheshire and Merseyside ICB': m_pop_qyg, 'Cornwall and the Isles of Scilly ICB': m_pop_qt6, 
'Coventry and Warwickshire ICB': m_pop_qwu,'Derby and Derbyshire ICB': m_pop_qj2, 'Devon ICB': m_pop_qjk, 
'Dorset ICB': m_pop_qvv, 'Frimley ICB': m_pop_qnq, 'Gloucestershire ICB': m_pop_qr1, 'Greater Manchester ICB': m_pop_qop, 
'Hampshire and Isle of Wight ICB': m_pop_qrl, 'Herefordshire and Worcestershire ICB': m_pop_qgh,
'Hertfordshire and West Essex ICB': m_pop_qm7, 'Humber and North Yorkshire ICB': m_pop_qoq, 
'Kent and Medway ICB': m_pop_qks,'Lancashire and South Cumbria ICB': m_pop_qe1, 'Leicester, Leicestershire and Rutland ICB':m_pop_qk1, 
'Lincolnshire ICB': m_pop_qjm, 'Mid and South Essex ICB': m_pop_qh8, 'Norfolk and Waveney ICB': m_pop_qmm, 
'North Central London ICB': m_pop_qmj, 'North East and North Cumbria ICB':m_pop_qhm, 'North East London ICB': m_pop_qmf, 
'North West London ICB': m_pop_qrv, 'Northamptonshire ICB': m_pop_qpm, 'Nottingham and Nottinghamshire ICB': m_pop_qt1, 
'Shropshire, Telford and Wrekin ICB': m_pop_qoc, 'Somerset ICB': m_pop_qsl, 'South East London ICB': m_pop_qkk, 
'South West London ICB': m_pop_qwe, 'South Yorkshire ICB': m_pop_qf7, 'Staffordshire and Stoke-on-Trent ICB': m_pop_qnc, 
'Suffolk and North East Essex ICB': m_pop_qjg, 'Surrey Heartlands ICB': m_pop_qxu, 'Sussex ICB': m_pop_qnx, 
'West Yorkshire ICB': m_pop_qwo}

pop_f_dict = {
'Bath and North East Somerset, Swindon and Wiltshire ICB': f_pop_qox, 
'Bedfordshire, Luton and Milton Keynes ICB': f_pop_qhg, 'Birmingham and Solihull ICB': f_pop_qhl, 
'Black Country ICB': f_pop_qua, 'Bristol, North Somerset and South Gloucestershire ICB': f_pop_quy,
'Buckinghamshire, Oxfordshire and Berkshire West ICB': f_pop_qu9, 'Cambridgeshire and Peterborough ICB': f_pop_que,
'Cheshire and Merseyside ICB': f_pop_qyg, 'Cornwall and the Isles of Scilly ICB': f_pop_qt6, 
'Coventry and Warwickshire ICB': f_pop_qwu,'Derby and Derbyshire ICB': f_pop_qj2, 'Devon ICB': f_pop_qjk, 
'Dorset ICB': f_pop_qvv, 'Frimley ICB': f_pop_qnq, 'Gloucestershire ICB': f_pop_qr1, 'Greater Manchester ICB': f_pop_qop, 
'Hampshire and Isle of Wight ICB': f_pop_qrl, 'Herefordshire and Worcestershire ICB': f_pop_qgh,
'Hertfordshire and West Essex ICB': f_pop_qm7, 'Humber and North Yorkshire ICB': f_pop_qoq, 
'Kent and Medway ICB': f_pop_qks,'Lancashire and South Cumbria ICB': f_pop_qe1, 'Leicester, Leicestershire and Rutland ICB': f_pop_qk1, 
'Lincolnshire ICB': f_pop_qjm, 'Mid and South Essex ICB': f_pop_qh8, 'Norfolk and Waveney ICB': f_pop_qmm, 
'North Central London ICB': f_pop_qmj, 'North East and North Cumbria ICB': f_pop_qhm, 'North East London ICB': f_pop_qmf, 
'North West London ICB': f_pop_qrv, 'Northamptonshire ICB': f_pop_qpm, 'Nottingham and Nottinghamshire ICB': f_pop_qt1, 
'Shropshire, Telford and Wrekin ICB': f_pop_qoc, 'Somerset ICB': f_pop_qsl, 'South East London ICB': f_pop_qkk, 
'South West London ICB': f_pop_qwe, 'South Yorkshire ICB': f_pop_qf7, 'Staffordshire and Stoke-on-Trent ICB': f_pop_qnc, 
'Suffolk and North East Essex ICB': f_pop_qjg, 'Surrey Heartlands ICB': f_pop_qxu, 'Sussex ICB': f_pop_qnx, 
'West Yorkshire ICB': f_pop_qwo}

# Get the selected dataframe based on user choice
selected_icb_for_ind = icb_indicators_dict.get(icb_choice, pd.DataFrame())
selected_icb_for_m_pop = pop_m_dict.get(icb_choice, pd.DataFrame())
selected_icb_for_f_pop = pop_f_dict.get(icb_choice, pd.DataFrame())


################################################################################
    
# Create a Streamlit Session State variable to store the 'user_number_input' value 
if 'user_num_input' not in st.session_state:
    # Set the default value for Streamlit
    st.session_state.user_num_input = 5000000  

with st.sidebar:
    # Use the session_state variable as the default value for the slider
    funding_input_changed = st.number_input('**Insert funding available (£)**', min_value=1000, 
                                        max_value=100000000, 
                                        value=st.session_state.user_num_input, 
                                        help='Funding available to be split among GP practices')

# Update the session_state variable when the slider value changes
st.session_state.user_num_input = funding_input_changed

# Update the funding variable in the model file
funding = st.session_state.user_num_input

################################################################################
# DEMOGRAPHICS: 1) AGE; 2) SEX

# Select AGE RANGE OF POPULATION from slider 
with st.sidebar: 
    st.write('-----------------------------------------------------------------')
    st.write('**Specify target demographics**')

# To call the min and max number selected in age slider, refer to them as 'slider_age[0]' and 'slider_age[1]', respectively 
    slider_age = st.slider('Age range from 0 to 95+',0,95,(25,75), step = 1,
                      help= 'Select the age range of the population targeted with this intervention')

# Select GENDER OF POPULATION from radio button
    gender_options = ['Both', 'Males', 'Females']
    gender_selected = st.radio('Gender',gender_options, horizontal = False, 
                               help= 'Select the gender of target population for this intervention')
    st.write('-----------------------------------------------------------------')


# Following selection from radio button, sum male and female populations if 'Both' is selected above

if gender_selected == 'Both':
    pop_size_selected = selected_icb_for_m_pop + selected_icb_for_f_pop

    # Add these 3 steps to rename the GP code column, otherwise it will have the GP code twice in the same cell, leading to errors
    # Beware: this way the 'GP code' column is at the final column (i.e. not first!)

    # Get the current column names
    current_columns_pop = pop_size_selected.columns.tolist()
    # Create a dictionary to map old column names to new column names
    column_mapping_pop = {current_columns_pop[0]: 'wrong gp cd'}
    # Rename the columns
    pop_size_selected.rename(columns=column_mapping_pop, inplace=True)

elif gender_selected == 'Males':
    pop_size_selected = selected_icb_for_m_pop
else:  # Females
    pop_size_selected = selected_icb_for_f_pop

# Sum the number of registered patients based on age range from slider_age[0] to slider_age[1] (inclusive)
pop_size_n_sex_selected = pd.DataFrame()
pop_size_n_sex_selected['Population'] = pop_size_selected.apply(lambda row: row[slider_age[0] +1:slider_age[1] + 2].sum(), axis=1)
pop_size_n_sex_selected['GP code'] = selected_icb_for_m_pop['GP code']

################################################################################

# MATCH ORDER
# To match the order of GP practices, between the population files and the indicator file,
# MERGE popupation into indicator dataframes based on 'GP code' column  
selected_icb_for_ind_n_pop = pd.merge(selected_icb_for_ind, pop_size_n_sex_selected, on='GP code', how='left')  



############################################

# Create a dataframe with a population for all ages and both m+f to calculate 'alloc per head' in weighted pop scenario (in last expander)
all_pop = pd.DataFrame()
all_men = selected_icb_for_m_pop.sum(axis=1, numeric_only = True)
all_women = selected_icb_for_f_pop.sum(axis=1, numeric_only = True)
all_pop['GP code'] = selected_icb_for_m_pop['GP code']
all_pop['Population'] = all_men + all_women

# Match order
all_pop_merged = pd.merge(selected_icb_for_ind, all_pop, on='GP code', how='left')  


################################################################################
# 'GP exclusion' function
# This function allows you to remove a GP practice from the list (and hence, from calculations)

# Prepare indicators data for selecting/unselecting GPs and to Match uploaded indicators
gp_list_to_deselect = pd.DataFrame()
gp_list_to_deselect['GP code'] = selected_icb_for_ind_n_pop['GP code']
gp_list_to_deselect['GP name'] = selected_icb_for_ind_n_pop['GP name']

# This is needed to 'assign' a tick in the selectbox ('True' = selected)
gp_list_to_deselect['tick'] = True

gp_exclusion_is_checked = st.checkbox('Exclude some GP practices from resource allocation', 
                                  help='Should you wish to exclude some GP practices from '
                                  'the calculation of allocation, untick them from the list')
st.write('')   # to leave a space between lines
selected_gps = pd.DataFrame()

if gp_exclusion_is_checked:
    selected_gps = st.data_editor(gp_list_to_deselect, column_config={"tick": st.column_config.CheckboxColumn("Select", default=False)}, hide_index=True,)

    # Filter the DataFrame based on selected rows
    selected_icb_for_ind_n_pop = selected_icb_for_ind_n_pop[selected_gps['tick']]

    # Filter the DataFrame based on selected rows (also for weighted pop scenario for expander)
    all_pop_merged = all_pop_merged[selected_gps['tick']]

################################################################################ 
       
# Hidden calculation
hidden_param = pd.DataFrame()
hidden_param['GP code'] = selected_icb_for_ind_n_pop['GP code']

# This creates a column of 'ones' to give a value to 'Choose an option' 
col_of_ones = 1 
hidden_param['ones'] = col_of_ones

################################################################################

# LISTED INDICATORS

# List the available indicators. 
indicators_list = ['Choose an option', 'IMD score (2019)', 'Weighted population', 'Bowel cancer screening coverage (age 60-74)', 'Breast cancer screening coverage (age 53-70)',
                   'Cervical cancer screening coverage (age 25-49)', 'Cervical cancer screening coverage (age 50-64)',
                   'Cancer prevalence (all ages)', 'Hypertension prevalence (all ages)', 
    'Last BP reading of patients (<80 yrs, with hypertension) <= 140/90 mmHg in the last 12 months',
    'Last BP reading of patients (80+ yrs, with hypertension) <= 150/90 mmHg in the last 12 months',
    'Patients who have a record of BP in the last 5 yrs (45+)', 'CHD prevalence (all ages)',
    'Stroke prevalence (all ages)', 'Smoking prevalence (15+)', 'CKD prevalence (18+)', 
    'Obesity prevalence (18+)', 'Diabetes prevalence (17+)',  
    'Patients with diabetes treated with a statin (with a history of CVD - excl. haem. stroke)',
    'People with type 2 diabetes who have received an annual foot check',
    'People with type 2 diabetes who received a cholesterol check', 
    'Asthma prevalence (6+ yrs)', 'COPD prevalence (all ages)', 'Mental Health prevalence (all ages)',
    'Depression incidence (18+)','Learning disability prevalence (all ages)', 'Dementia prevalence (all ages)', 
    'Osteoporosis prevalence (50+)', 'MMR vaccine uptake (at least 1 dose - age 1-1.5 yrs)']

################################################################################
# INITIALIZE PARAMETERS

# Initialize weights to default value of 'zero'
ind_2_weight = 0
ind_3_weight = 0

uploaded_ind_1_weight = 0    # needed
alloc_by_up_ind_1 = 0       # needed

uploaded_ind_2_weight = 0       # needed
alloc_by_up_ind_2 = 0           # needed

uploaded_ind_3_weight = 0       # needed
alloc_by_up_ind_3 = 0           # needed


# Initialise other parameters used to make sure that no more than 5 indicators are being selected 
# (between those from list and those uploaded)

name_indicator_1 = 'bla'
name_indicator_2 = 'bla'
name_indicator_3 = 'bla'

matched_uploaded_indicator_1 = pd.DataFrame()
matched_uploaded_indicator_2 = pd.DataFrame()
matched_uploaded_indicator_3 = pd.DataFrame()

wo_p_n_r_str_output_table = pd.DataFrame()
wo_p_n_r_str_output_table_sorted_per_h = pd.DataFrame()

################################################################################

# Create a dictionary to store indicator dataframes for the indicators
#(left: name of indicator as you want it to appear in tool; right: name as it appears in imported data file i.e. excel)

indicators_list_dict = {
    'IMD score (2019)': selected_icb_for_ind_n_pop['Deprivation score (IMD 2019)'],
    'Weighted population': selected_icb_for_ind_n_pop['Weighted population'],
    'Bowel cancer screening coverage (age 60-74)': selected_icb_for_ind_n_pop['Bowel cancer screening coverage: aged 60 to 74 years old'],
    'Breast cancer screening coverage (age 53-70)': selected_icb_for_ind_n_pop['Breast screening coverage: aged 53 to 70 years old'],     
    'Cervical cancer screening coverage (age 25-49)': selected_icb_for_ind_n_pop['Cervical screening coverage: aged 25 to 49 years old'], 
    'Cervical cancer screening coverage (age 50-64)': selected_icb_for_ind_n_pop['Cervical screening coverage: aged 50 to 64 years old'], 
    'Asthma prevalence (6+ yrs)': selected_icb_for_ind_n_pop['Asthma: QOF prevalence'],
    'Cancer prevalence (all ages)': selected_icb_for_ind_n_pop['Cancer: QOF prevalence'],
    'CHD prevalence (all ages)': selected_icb_for_ind_n_pop['CHD: QOF prevalence'],
    'MMR vaccine uptake (at least 1 dose - age 1-1.5 yrs)': selected_icb_for_ind_n_pop['Children who received at least 1 dose of MMR vaccine between the ages of 1 and 1.5 yrs'],
    'CKD prevalence (18+)': selected_icb_for_ind_n_pop['CKD: QOF prevalence'], 
    'COPD prevalence (all ages)': selected_icb_for_ind_n_pop['COPD: QOF prevalence'], 
    'Dementia prevalence (all ages)': selected_icb_for_ind_n_pop['Dementia: QOF prevalence'], 
    'Depression incidence (18+)': selected_icb_for_ind_n_pop['Depression: QOF incidence - new diagnosis'],
    'Diabetes prevalence (17+)': selected_icb_for_ind_n_pop['Diabetes: QOF prevalence'], 
    'Hypertension prevalence (all ages)': selected_icb_for_ind_n_pop['Hypertension: QOF prevalence'], 
    'Last BP reading of patients (<80 yrs, with hypertension) <= 140/90 mmHg in the last 12 months': selected_icb_for_ind_n_pop['Last BP reading of patients (<80 yrs, with hypertension), in the last 12 months is <= 140/90 mmHg (denominator incl. PCAs)'],
    'Last BP reading of patients (80+ yrs, with hypertension) <= 150/90 mmHg in the last 12 months': selected_icb_for_ind_n_pop['Last BP reading of patients (80+ yrs, with hypertension), in the last 12 months is <= 150/90 mmHg (denominator incl. PCAs)'],
    'Learning disability prevalence (all ages)': selected_icb_for_ind_n_pop['Learning disability: QOF prevalence'], 
    'Mental Health prevalence (all ages)': selected_icb_for_ind_n_pop['Mental Health: QOF prevalence'],
    'Obesity prevalence (18+)': selected_icb_for_ind_n_pop['Obesity: QOF prevalence (new definition)'], 
    'Osteoporosis prevalence (50+)': selected_icb_for_ind_n_pop['Osteoporosis: QOF prevalence'], 
    'Patients who have a record of BP in the last 5 yrs (45+)': selected_icb_for_ind_n_pop['Patients (aged 45+ yrs), who have a record of blood pressure in the last 5 yrs (denominator incl. PCAs)'], 
    'Patients with diabetes treated with a statin (with a history of CVD - excl. haem. stroke)': selected_icb_for_ind_n_pop['Patients with diabetes and a history of CVD (excl. haem. stroke) treated with a statin (denominator incl. PCAs)'],
    'People with type 2 diabetes who have received an annual foot check': selected_icb_for_ind_n_pop['People with type 2 diabetes who have received an annual foot check'],
    'People with type 2 diabetes who received a cholesterol check': selected_icb_for_ind_n_pop['People with type 2 diabetes who received a cholesterol check'], 
    'Smoking prevalence (15+)': selected_icb_for_ind_n_pop['Smoking: QOF prevalence'],
    'Stroke prevalence (all ages)': selected_icb_for_ind_n_pop['Stroke: QOF prevalence'],
    'Choose an option': hidden_param['ones']}

# Allocation for these indicators is indirectly proportional (the higher the value, the less the allocation)
# hence, their calculation needs 'reversing'
ind_needs_reversing = ['Bowel cancer screening coverage (age 60-74)', 'Breast cancer screening coverage (age 53-70)',
                       'Cervical cancer screening coverage (age 25-49)', 'Cervical cancer screening coverage (age 50-64)',
                       'MMR vaccine uptake (at least 1 dose - age 1-1.5 yrs)',
                       'Last BP reading of patients (<80 yrs, with hypertension) <= 140/90 mmHg in the last 12 months',
                       'Last BP reading of patients (80+ yrs, with hypertension) <= 150/90 mmHg in the last 12 months',
                       'Patients who have a record of BP in the last 5 yrs (45+)',
                       'Patients with diabetes treated with a statin (with a history of CVD - excl. haem. stroke)',
                       'People with type 2 diabetes who have received an annual foot check',
                       'People with type 2 diabetes who received a cholesterol check']

########################################################################################

# SIDEBAR

# Select the indicators
with st.sidebar:
    st.write('**Select up to three indicators**') 
    
# Listed Indicator 1    
    ind_1_choice = st.sidebar.selectbox("Indicator #1:", indicators_list, help="Select the first indicator")
    if ind_1_choice in ind_needs_reversing:
        st.write(':orange[(High values result in less money)]')
    elif ind_1_choice == 'Choose an option':
        st.write('')    
    elif ind_1_choice == 'Weighted population':
        st.write('')    
    else:
        st.write(':green[(High values result in more money)]')
    
    ind_1_weight = st.slider('**Weight**: contribution of indicator #1 (%)',0,100,50, step=1, 
                     help='Select what proportion of the funding should be allocated based on indicator #1)')

# Listed Indicators 2 & 3
# This part makes sure that the slider for indicator 2 and 3 only appear if an indicator
# is picked from the selectbox (hence, anything other than the  default 'choose an option')

    # For indicator 2
    ind_2_choice = st.sidebar.selectbox("Indicator #2 (optional):", indicators_list, 
                                        help="Select the second indicator")
    if ind_2_choice in ind_needs_reversing:
        st.write(':orange[(High values result in less money)]')
    elif ind_2_choice == 'Choose an option':
        st.write('')    
    elif ind_2_choice == 'Weighted population':
        st.write('')    
    else:
        st.write(':green[(High values result in more money)]')
    
    if ind_2_choice != 'Choose an option':
        ind_2_weight = st.slider('**Weight**: contribution of indicator #2 (%)',0,100,0, step=1,
                                 help='Select what proportion of the funding should be allocated based on indicator #2')
    else:
        ind_2_weight = 0

    # For indicator 3
    ind_3_choice = st.sidebar.selectbox("Indicator #3 (optional):", indicators_list,
                                        help="Select the third indicator")
    if ind_3_choice in ind_needs_reversing:
        st.write(':orange[(High values result in less money)]')
    elif ind_3_choice == 'Choose an option':
        st.write('')    
    elif ind_3_choice == 'Weighted population':
        st.write('')    
    else:
        st.write(':green[(High values result in more money)]')

    if ind_3_choice != 'Choose an option':
        ind_3_weight = st.slider('**Weight**: contribution of indicator #3 (%)',0,100,0, step=1,
                                 help='Select what proportion of the funding should be allocated based on indicator #3')
    else:
        ind_3_weight = 0


    indicators_weights = [(ind_1_choice, ind_1_weight), (ind_2_choice, ind_2_weight), (ind_3_choice, ind_3_weight)] 
    indicators_weights = [(indicator, weight) for indicator, weight in indicators_weights if weight > 0]

################################################################################

# Checkbox 'to check' if the user wants to add his/her own indicator data
    user_wants_to_upload_indicator = st.checkbox('Do you want to upload your indicator instead?', 
                                  help='Should you wish to use your own indicator data for your ICB, '
                                  "you can upload up to three files (in '.csv' format). "
                                  'Your file should include only two columns: column 1 '
                                  'should have the GP code and column 2 should have the indicator values '
                                  'for that GP practice')
 

    if user_wants_to_upload_indicator:
        # First Uploaded indicator 
        uploaded_file_1 = st.file_uploader("Upload your first indicator", type= ['csv', 'xlsx'])  # 4 some reason it crashes if I upload .xlsx files
        if uploaded_file_1 is not None: 
            uploaded_indicator_1 = pd.read_csv(uploaded_file_1) 
            df_uploaded_indicator_1 = pd.DataFrame(uploaded_indicator_1)
            name_indicator_1 = st.text_input("Enter name of your first indicator", 
                                                placeholder="Enter name of indicator", 
                                                label_visibility='collapsed')
            if name_indicator_1 is None or name_indicator_1 == "":
                name_indicator_1 = 'Uploaded indicator #1'
            high_gets_more_1 = st.radio('High value results in:', ["More funding", "Less funding"], horizontal = True,
                                        help='Select whether higher values for this indicator should result in allocating '
                                        'proportionally more money or less money than a lower indicator value')
            uploaded_ind_1_weight = st.slider(f'**Weight**: contribution of {name_indicator_1} (%)',0,100,0, step=1,
                                            help='Select what proportion of the funding should be allocated based on your first uploaded indicator')
                
            # Get the current column names
            current_columns_1 = df_uploaded_indicator_1.columns.tolist()
            # Create a dictionary to map old column names to new column names
            column_mapping_1 = {current_columns_1[0]: 'GP code', current_columns_1[1]: 'xyz'}
            # Rename the columns
            df_uploaded_indicator_1.rename(columns=column_mapping_1, inplace=True)
            # Match the uploaded indicator to the indicators listed
            matched_uploaded_indicator_1 = pd.merge(selected_icb_for_ind_n_pop['GP code'], df_uploaded_indicator_1, on='GP code', how='left')

            
            # Second Uploaded indicator 
            st.write('')
            st.write('')
            uploaded_file_2 = st.file_uploader("Upload your second indicator (optional)", type= ['csv'])
            if uploaded_file_2 is not None: 
                uploaded_indicator_2 = pd.read_csv(uploaded_file_2) 
                df_uploaded_indicator_2 = pd.DataFrame(uploaded_indicator_2)
                name_indicator_2 = st.text_input("Enter name of your second indicator",  
                                                placeholder="Enter name of indicator", 
                                                label_visibility='collapsed')

                if name_indicator_2 is None or name_indicator_2 == "":
                    name_indicator_2 = 'Uploaded indicator #2'
                high_gets_more_2 = st.radio('High value results in:', ["More funding ", "Less funding "], horizontal = True,
                                        help='Select whether higher values for this indicator should result in allocating '
                                        'proportionally more money or less money than a lower indicator value')

                uploaded_ind_2_weight = st.slider(f'**Weight**: contribution of {name_indicator_2} (%)',0,100,0, step=1,
                                        help='Select what proportion of the funding should be allocated based on your second uploaded indicator')

                # Get the current column names
                current_columns_2 = df_uploaded_indicator_2.columns.tolist()
                # Create a dictionary to map old column names to new column names
                column_mapping_2 = {current_columns_2[0]: 'GP code', current_columns_2[1]: 'xyz'}
                # Rename the columns
                df_uploaded_indicator_2.rename(columns=column_mapping_2, inplace=True)
                # Match the uploaded indicator to the indicators listed
                matched_uploaded_indicator_2 = pd.merge(selected_icb_for_ind_n_pop['GP code'], df_uploaded_indicator_2, on='GP code', how='left')

                # Third Uploaded indicator 
                st.write('')
                st.write('')
                uploaded_file_3 = st.file_uploader("Upload your third indicator (optional)", type= ['csv'])
                if uploaded_file_3 is not None: 
                    uploaded_indicator_3 = pd.read_csv(uploaded_file_3) 
                    df_uploaded_indicator_3 = pd.DataFrame(uploaded_indicator_3)
                    name_indicator_3 = st.text_input("Enter name of your third indicator",  
                                                placeholder="Enter name of indicator", 
                                                label_visibility='collapsed')

                    if name_indicator_3 is None or name_indicator_3 == "":
                        name_indicator_3 = 'Uploaded indicator #3'
                    high_gets_more_3 = st.radio('High value results in:', ["More funding  ", "Less funding  "], horizontal = True,
                                        help='Select whether higher values for this indicator should result in allocating '
                                        'proportionally more money or less money than a lower indicator value')

                    uploaded_ind_3_weight = st.slider(f'**Weight**: contribution of {name_indicator_3} (%)',0,100,0, step=1,
                                        help='Select what proportion of the funding should be allocated based on your third uploaded indicator')

                    # Get the current column names
                    current_columns_3 = df_uploaded_indicator_3.columns.tolist()
                    # Create a dictionary to map old column names to new column names
                    column_mapping_3 = {current_columns_3[0]: 'GP code', current_columns_3[1]: 'xyz'}
                    # Rename the columns
                    df_uploaded_indicator_3.rename(columns=column_mapping_3, inplace=True)
                    # Match the uploaded indicator to the indicators listed
                    matched_uploaded_indicator_3 = pd.merge(selected_icb_for_ind_n_pop['GP code'], df_uploaded_indicator_3, on='GP code', how='left')

            up_indicators_weights = [(name_indicator_1, uploaded_ind_1_weight), (name_indicator_2, uploaded_ind_2_weight), (name_indicator_3, uploaded_ind_3_weight)]
            up_indicators_weights = [(up_indicator, up_weight) for up_indicator, up_weight in up_indicators_weights if up_weight > 0]

################################################################################          

selected_ind_1_w_correct_icb = indicators_list_dict.get(ind_1_choice, pd.DataFrame())      
selected_ind_2_w_correct_icb = indicators_list_dict.get(ind_2_choice, pd.DataFrame())     
selected_ind_3_w_correct_icb = indicators_list_dict.get(ind_3_choice, pd.DataFrame())       

##################################################################################

# For the calculations below, the weights of indicators need to add up to 100%, so 
# a remainder will be calculated based on the population size selected above. 
# Hence, automatically adjust 'prop_pop' based on the value of the 3 indicators

if ind_1_choice == 'Choose an option':
    prop_pop = 100 - ind_2_weight - ind_3_weight - uploaded_ind_1_weight - uploaded_ind_2_weight - uploaded_ind_3_weight
else:    
    prop_pop = 100 - ind_1_weight - ind_2_weight - ind_3_weight - uploaded_ind_1_weight - uploaded_ind_2_weight - uploaded_ind_3_weight

################################################################################
with st.sidebar:
    st.write('')
    if prop_pop > 0:
        st.warning('The weighting of the indicators should add up to 100%, otherwise '
                 f'the remainder will be allocated based on population size. Currently **{prop_pop}%** '
                 'is being allocated based on registered population size', icon="⚠️") 
    elif prop_pop <0:
        st.error('IMPORTANT! The weighting selected **cannot be greater than 100%.**' 
                 ' Please amend the weighting', icon="⚠️")
    else:
        st.write()

################################################################################

                                # THE EQUATION #        
                # Update the equation based on the input by user #

#######################################################################################
#                                                                                     #
#  The equation used to split the money and allocate it aming GP practices/PCN is:    #
#                                                                                     #
#                                   bz * cz                                           #
#                             a = __________ * d                                      #
#                                  Σ(b_all*c_all)                                     #
#                                                                                     #
# where:                                                                              #
# a = allocation                                                                      #
# bz = population of GP practice 'z'                                                  #
# cz = indicator score (e.g. IMD) of GP practice 'z'                                  #
# Σ(b_all*c_all) = sum of all GP practices population * their indicator score e.g.IMD #
# d = total funding available                                                         #
#                                                                                     #
#                                                                                     #
#                          APPLY FOR ALL INDICATORS USED                              #
#                                                                                     #
#######################################################################################

# Perform multiplications handling 'NaN' values with 'fillna(0)'
# The 'fillna(0)' is used to replace 'NaN' values with '0' before performing the multiplication. 
# This way, you still get a result for each row in the population dataframe. 
# It is essential, otherwise total allocation would not add up to funding


# Allocation by population size
pop_x_one = selected_icb_for_ind_n_pop['Population']    
sum_pop = selected_icb_for_ind_n_pop['Population'].sum()      

prop_pop_div_100 = prop_pop / 100
alloc_by_pop = pop_x_one.fillna(0) / sum_pop * funding * prop_pop_div_100

# Allocation by Indicator #1
if ind_1_choice in ind_needs_reversing:
    sum_selected_ind_1_w_correct_icb = selected_ind_1_w_correct_icb.sum()
    ind_1_reversed = 1 - (selected_ind_1_w_correct_icb/sum_selected_ind_1_w_correct_icb)
    pop_x_ind_1 = ind_1_reversed * selected_icb_for_ind_n_pop['Population']
    sum_pop_x_ind_1 = pop_x_ind_1.sum()      

elif ind_1_choice == 'Weighted population':
    pop_x_ind_1 = selected_ind_1_w_correct_icb 
    sum_pop_x_ind_1 = pop_x_ind_1.sum()

else:
    pop_x_ind_1 = selected_ind_1_w_correct_icb * selected_icb_for_ind_n_pop['Population']
    sum_pop_x_ind_1 = pop_x_ind_1.sum()

alloc_by_ind_1 = pop_x_ind_1.fillna(0) / sum_pop_x_ind_1 * funding

        # Allocation by Indicator #2
if ind_2_choice in ind_needs_reversing:
    sum_selected_ind_2_w_correct_icb = selected_ind_2_w_correct_icb.sum()
    ind_2_reversed = 1 - (selected_ind_2_w_correct_icb/sum_selected_ind_2_w_correct_icb)
    pop_x_ind_2 = ind_2_reversed * selected_icb_for_ind_n_pop['Population']
    sum_pop_x_ind_2 = pop_x_ind_2.sum()

elif ind_2_choice == 'Weighted population':
    pop_x_ind_2 = selected_ind_2_w_correct_icb
    sum_pop_x_ind_2 = pop_x_ind_2.sum()

else:
    pop_x_ind_2 = selected_ind_2_w_correct_icb * selected_icb_for_ind_n_pop['Population']
    sum_pop_x_ind_2 = pop_x_ind_2.sum()

alloc_by_ind_2 = pop_x_ind_2.fillna(0) / sum_pop_x_ind_2 * funding

        # Allocation by Indicator #3
if ind_3_choice in ind_needs_reversing:
    sum_selected_ind_3_w_correct_icb = selected_ind_3_w_correct_icb.sum()
    ind_3_reversed = 1 - (selected_ind_3_w_correct_icb/sum_selected_ind_3_w_correct_icb)
    pop_x_ind_3 = ind_3_reversed * selected_icb_for_ind_n_pop['Population']
    sum_pop_x_ind_3 = pop_x_ind_3.sum()

elif ind_3_choice == 'Weighted population':
    pop_x_ind_3 = selected_ind_3_w_correct_icb
    sum_pop_x_ind_3 = pop_x_ind_3.sum()

else:
    pop_x_ind_3 = selected_ind_3_w_correct_icb * selected_icb_for_ind_n_pop['Population']
    sum_pop_x_ind_3 = pop_x_ind_3.sum()

alloc_by_ind_3 = pop_x_ind_3.fillna(0) / sum_pop_x_ind_3 * funding

#########################

# Allocation by Uploaded Indicator #1
if uploaded_ind_1_weight > 0:
    if high_gets_more_1 == "Less funding":
        sum_up_ind_1 = matched_uploaded_indicator_1['xyz'].sum()                   
        prop_of_sum_up_1 = matched_uploaded_indicator_1['xyz']/sum_up_ind_1
        up_ind_1_reversed = 1- prop_of_sum_up_1
        pop_x_up_ind_1 = up_ind_1_reversed * selected_icb_for_ind_n_pop['Population']
    else:
        pop_x_up_ind_1 = matched_uploaded_indicator_1['xyz'] * selected_icb_for_ind_n_pop['Population']
        
    sum_pop_x_up_ind_1 = pop_x_up_ind_1.sum()
    alloc_by_up_ind_1 = pop_x_up_ind_1.fillna(0) / sum_pop_x_up_ind_1 * funding

# Allocation by Uploaded Indicator #2
if uploaded_ind_2_weight > 0:
    if high_gets_more_2 == "Less funding ":
        sum_up_ind_2 = matched_uploaded_indicator_2['xyz'].sum()
        prop_of_sum_up_2 = matched_uploaded_indicator_2['xyz']/sum_up_ind_2
        up_ind_2_reversed = 1- prop_of_sum_up_2
        pop_x_up_ind_2 = up_ind_2_reversed * selected_icb_for_ind_n_pop['Population']
    else:
        pop_x_up_ind_2 = matched_uploaded_indicator_2['xyz'] * selected_icb_for_ind_n_pop['Population']
    
    sum_pop_x_up_ind_2 = pop_x_up_ind_2.sum()
    alloc_by_up_ind_2 = pop_x_up_ind_2.fillna(0) / sum_pop_x_up_ind_2 * funding

# Allocation by Uploaded Indicator #3
if uploaded_ind_3_weight > 0:
    if high_gets_more_3 == "Less funding  ":
        sum_up_ind_3 = matched_uploaded_indicator_3['xyz'].sum()
        prop_of_sum_up_3 = matched_uploaded_indicator_3['xyz']/sum_up_ind_3
        up_ind_3_reversed = 1- prop_of_sum_up_3
        pop_x_up_ind_3 = up_ind_3_reversed * selected_icb_for_ind_n_pop['Population']
    else:
        pop_x_up_ind_3 = matched_uploaded_indicator_3['xyz'] * selected_icb_for_ind_n_pop['Population']

    sum_pop_x_up_ind_3 = pop_x_up_ind_3.sum()
    alloc_by_up_ind_3 = pop_x_up_ind_3.fillna(0) / sum_pop_x_up_ind_3 * funding


################################################################################

# Allocation from indicators
alloc_by_ind_1_weighted = (alloc_by_ind_1 * ind_1_weight)/100
alloc_by_ind_2_weighted = (alloc_by_ind_2 * ind_2_weight)/100
alloc_by_ind_3_weighted = (alloc_by_ind_3 * ind_3_weight)/100

alloc_by_up_ind_1_weighted = (alloc_by_up_ind_1 * uploaded_ind_1_weight)/100
alloc_by_up_ind_2_weighted = (alloc_by_up_ind_2 * uploaded_ind_2_weight)/100
alloc_by_up_ind_3_weighted = (alloc_by_up_ind_3 * uploaded_ind_3_weight)/100

alloc_by_indicators = alloc_by_ind_1_weighted + alloc_by_ind_2_weighted + alloc_by_ind_3_weighted + \
    alloc_by_up_ind_1_weighted + alloc_by_up_ind_2_weighted + alloc_by_up_ind_3_weighted 

# TOTAL ALLOCATION
tot_alloc = alloc_by_pop + alloc_by_indicators

# ALLOCATION PER HEAD
alloc_per_head = tot_alloc / selected_icb_for_ind_n_pop['Population'].fillna(0)

################################################################################

# Include Button

# Initialise 'Calculate_button_ticked' as False so that 'disclaimer' appears only if 'clicked'
calculate_button_ticked = False

if st.button("**Calculate**", type="primary"):
    calculate_button_ticked = True
    with st.spinner('Running calculations...'):

    # Output files:
    # There are 2 options:
    # 1. 'str_output_files': shows only 'total allocation' and 'allocation per patient'
    # 2. 'str_extra_output_file': as above but displays also breakdown of total allocation (only if box is checked)

        # Output (option #1)
        str_output_table = pd.DataFrame()
        str_output_table['GP name'] = selected_icb_for_ind_n_pop['GP name'] 
        str_output_table['GP code'] = selected_icb_for_ind_n_pop['GP code']
        # add population column and commas
        str_output_table['Population'] = selected_icb_for_ind_n_pop['Population'].fillna(0).apply(lambda x: "{:,}".format(int(x)))

        for ind_weight, ind_choice, selected_ind_w_correct_icb in zip([ind_1_weight, ind_2_weight, ind_3_weight],
                                                                    [ind_1_choice, ind_2_choice, ind_3_choice],
                                                                    [selected_ind_1_w_correct_icb, selected_ind_2_w_correct_icb, selected_ind_3_w_correct_icb]):

            if ind_weight > 0:
# If weighted pop is selected in any of the three listed indicator boxes, add them in output table, round it to 0 decimal and add comma
                if ind_choice == 'Weighted population':
                    str_output_table['Weighted population'] = selected_ind_w_correct_icb
                    round_pop = ['Weighted population']
                    str_output_table[round_pop] = str_output_table[round_pop].map(
                        lambda x: "{:,.0f}".format(x) if isinstance(x, (int, float)) else x)
                elif ind_choice == 'IMD score (2019)':
                    str_output_table[f'{ind_choice}'] = selected_ind_w_correct_icb.apply(
                        lambda x: "{:,.1f}".format(x) if isinstance(x, (int, float)) else x)
                else:
                    str_output_table[f'{ind_choice} (%)'] = selected_ind_w_correct_icb
                    # Round all others to 1 decimal point
                    rounded_indicator_name = ind_choice
                    str_output_table[f'{rounded_indicator_name} (%)'] = str_output_table[f'{ind_choice} (%)'].apply(  
                        lambda x: "{:,.1f}".format(x) if isinstance(x, (int, float)) else x)


        # If indicators have been uploaded, add them in output table, round them to 0 decimal and add comma
        for uploaded_weight, name_indicator, matched_uploaded_indicator in zip([uploaded_ind_1_weight, uploaded_ind_2_weight, uploaded_ind_3_weight],
                                                                               [name_indicator_1, name_indicator_2, name_indicator_3],
                                                                               [matched_uploaded_indicator_1, matched_uploaded_indicator_2, matched_uploaded_indicator_3]):
            if uploaded_weight > 0:
                str_output_table[name_indicator] = matched_uploaded_indicator['xyz']
                # round to 1 decimal pt
                round_uploaded = [name_indicator]
                str_output_table[round_uploaded] = str_output_table[round_uploaded].map(
                    lambda x: "{:,.1f}".format(x) if isinstance(x, (int, float)) else x)

        # This removes 'Choose an option' from the output if no indicator is selected
        str_output_table['Choose an option (%)'] = selected_icb_for_ind_n_pop['GP name']
        str_output_table.drop(columns=['Choose an option (%)'], inplace=True)

        str_output_table['Total allocation (£)'] = tot_alloc
        str_output_table['Allocation per patient (£)'] = alloc_per_head

        # Sort values (descending) by total allocation      
        str_output_table = str_output_table.sort_values(by='Total allocation (£)', ascending=False)

        # keep a copy before modifying to use for bar chart (below)
        wo_p_n_r_str_output_table = str_output_table.copy()         
        wo_p_n_r_str_output_table_sorted_per_h = str_output_table.copy()    

        # add commas and round to 2 decimal points the newly added columns
        round_output = ['Total allocation (£)', 'Allocation per patient (£)']
        str_output_table[round_output] = str_output_table[round_output].map(
            lambda x: "{:,.2f}".format(x) if isinstance(x, (int, float)) else x)


################################################################################

# Messages summarising which indicators contribute to what

        if prop_pop <0:
            st.error('IMPORTANT! The weighting selected **cannot be greater than 100%.**' 
                 ' Please amend the weighting', icon="⚠️")
        else:
            st.success('Done!')
            if prop_pop >0:
                if uploaded_ind_1_weight >0 and uploaded_ind_2_weight ==0 and uploaded_ind_3_weight == 0:
                    if ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight > 0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice} and {name_indicator_1}' 
                            f' to be {ind_2_weight}%, {ind_3_weight}% and {uploaded_ind_1_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice}, {ind_3_choice} and {name_indicator_1}' 
                            f' to be {ind_1_weight}%, {ind_2_weight}%, {ind_3_weight}% and {uploaded_ind_1_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight == 0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice} and {name_indicator_1}' 
                            f' to be {ind_2_weight}% and {uploaded_ind_1_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice} and {name_indicator_1}' 
                            f' to be {ind_1_weight}%, {ind_2_weight}% and {uploaded_ind_1_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight ==0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {name_indicator_1}' 
                            f' to be {uploaded_ind_1_weight}% '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice} and {name_indicator_1}' 
                            f' to be {ind_1_weight}% and {uploaded_ind_1_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight >0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice} and {name_indicator_1}' 
                            f' to be {ind_3_weight}% and {uploaded_ind_1_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_3_choice} and {name_indicator_1}' 
                            f' to be {ind_1_weight}%, {ind_3_weight}% and {uploaded_ind_1_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight >0:
                        st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice} and {name_indicator_1}' 
                        f' to be {ind_3_weight}% and {uploaded_ind_1_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight == 0:
                        st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice} and {name_indicator_1}' 
                        f' to be {ind_2_weight}% and {uploaded_ind_1_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight > 0:
                        st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice} and {name_indicator_1}' 
                        f' to be {ind_2_weight}%, {ind_3_weight}% and {uploaded_ind_1_weight}%, respectively. '
                        f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight == 0:
                        st.write(f'You selected the proportion of the funding allocated based on {name_indicator_1} to be {uploaded_ind_1_weight}%. '
                        f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')


                if uploaded_ind_1_weight == 0 and uploaded_ind_2_weight > 0 and uploaded_ind_3_weight == 0:
                    if ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight > 0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice} and {name_indicator_2}' 
                            f' to be {ind_2_weight}%, {ind_3_weight}% and {uploaded_ind_2_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice}, {ind_3_choice} and {name_indicator_2}' 
                            f' to be {ind_1_weight}%, {ind_2_weight}%, {ind_3_weight}% and {uploaded_ind_2_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight == 0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice} and {name_indicator_2}' 
                            f' to be {ind_2_weight}% and {uploaded_ind_2_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice} and {name_indicator_2}' 
                            f' to be {ind_1_weight}%, {ind_2_weight}% and {uploaded_ind_2_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight ==0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {name_indicator_2}' 
                            f' to be {uploaded_ind_2_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice} and {name_indicator_2}' 
                            f' to be {ind_1_weight}% and {uploaded_ind_2_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight >0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice} and {name_indicator_2}' 
                            f' to be {ind_3_weight}% and {uploaded_ind_2_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_3_choice} and {name_indicator_2}' 
                            f' to be {ind_1_weight}%, {ind_3_weight}% and {uploaded_ind_2_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight >0:
                        st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice} and {name_indicator_2}' 
                        f' to be {ind_3_weight}% and {uploaded_ind_2_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight == 0:
                        st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice} and {name_indicator_2}' 
                        f' to be {ind_2_weight}% and {uploaded_ind_2_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight > 0:
                        st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice} and {name_indicator_2}' 
                        f' to be {ind_2_weight}%, {ind_3_weight}% and {uploaded_ind_2_weight}%, respectively. '
                        f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight == 0:
                        st.write(f'You selected the proportion of the funding allocated based on {name_indicator_2} to be {uploaded_ind_2_weight}%. '
                        f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                
                if uploaded_ind_1_weight == 0 and uploaded_ind_2_weight == 0 and uploaded_ind_3_weight > 0:
                    if ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight > 0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice} and {name_indicator_3}' 
                            f' to be {ind_2_weight}%, {ind_3_weight}% and {uploaded_ind_3_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice}, {ind_3_choice} and {name_indicator_3}' 
                            f' to be {ind_1_weight}%, {ind_2_weight}%, {ind_3_weight}% and {uploaded_ind_3_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight == 0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice} and {name_indicator_3}' 
                            f' to be {ind_2_weight}% and {uploaded_ind_3_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice} and {name_indicator_3}' 
                            f' to be {ind_1_weight}%, {ind_2_weight}% and {uploaded_ind_3_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight ==0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {name_indicator_3}' 
                            f' to be {uploaded_ind_3_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice} and {name_indicator_3}' 
                            f' to be {ind_1_weight}% and {uploaded_ind_3_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight >0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice} and {name_indicator_3}' 
                            f' to be {ind_3_weight}% and {uploaded_ind_3_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_3_choice} and {name_indicator_3}' 
                            f' to be {ind_1_weight}%, {ind_3_weight}% and {uploaded_ind_3_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight >0:
                        st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice} and {name_indicator_3}' 
                        f' to be {ind_3_weight}% and {uploaded_ind_3_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight == 0:
                        st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice} and {name_indicator_3}' 
                        f' to be {ind_2_weight}% and {uploaded_ind_3_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight > 0:
                        st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice} and {name_indicator_3}' 
                        f' to be {ind_2_weight}%, {ind_3_weight}% and {uploaded_ind_3_weight}%, respectively. '
                        f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight == 0:
                        st.write(f'You selected the proportion of the funding allocated based on {name_indicator_3} to be {uploaded_ind_3_weight}%. '
                        f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')

                if uploaded_ind_1_weight >0 and uploaded_ind_2_weight >0 and uploaded_ind_3_weight == 0:
                    if ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight > 0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice}, {name_indicator_1} and {name_indicator_2}' 
                            f' to be {ind_2_weight}%, {ind_3_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_2_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice}, {ind_3_choice}, {name_indicator_1} and {name_indicator_2}' 
                            f' to be {ind_1_weight}%, {ind_2_weight}%, {ind_3_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_2_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight == 0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {name_indicator_1} and {name_indicator_2}' 
                            f' to be {ind_2_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_2_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice}, {name_indicator_1} and {name_indicator_2}' 
                            f' to be {ind_1_weight}%, {ind_2_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_2_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight ==0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {name_indicator_1} and {name_indicator_2}' 
                            f' to be {uploaded_ind_1_weight}% and {uploaded_ind_2_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {name_indicator_1} and {name_indicator_2}' 
                            f' to be {ind_1_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_2_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight >0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice}, {name_indicator_1} and {name_indicator_2}' 
                            f' to be {ind_3_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_2_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_3_choice}, {name_indicator_1} and {name_indicator_2}' 
                            f' to be {ind_1_weight}%, {ind_3_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_2_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight >0:
                        st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice}, {name_indicator_1} and {name_indicator_2}' 
                        f' to be {ind_3_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_2_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight == 0:
                        st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {name_indicator_1} and {name_indicator_2}' 
                        f' to be {ind_2_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_2_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight > 0:
                        st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice}, {name_indicator_1} and {name_indicator_2}' 
                        f' to be {ind_2_weight}%, {ind_3_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_2_weight}%, respectively. '
                        f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight == 0:
                        st.write(f'You selected the proportion of the funding allocated based on {name_indicator_1} and {name_indicator_2} to be {uploaded_ind_1_weight}% and {uploaded_ind_1_weight}%, respectively. '
                        f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')

                if uploaded_ind_1_weight ==0 and uploaded_ind_2_weight >0 and uploaded_ind_3_weight > 0:
                    if ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight > 0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice}, {name_indicator_2} and {name_indicator_3}' 
                            f' to be {ind_2_weight}%, {ind_3_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice}, {ind_3_choice}, {name_indicator_2} and {name_indicator_3}' 
                            f' to be {ind_1_weight}%, {ind_2_weight}%, {ind_3_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight == 0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {name_indicator_2} and {name_indicator_3}' 
                            f' to be {ind_2_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice}, {name_indicator_2} and {name_indicator_3}' 
                            f' to be {ind_1_weight}%, {ind_2_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight ==0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {name_indicator_2} and {name_indicator_3}' 
                            f' to be {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {name_indicator_2} and {name_indicator_3}' 
                            f' to be {ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight >0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice}, {name_indicator_2} and {name_indicator_3}' 
                            f' to be {ind_3_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_3_choice}, {name_indicator_2} and {name_indicator_3}' 
                            f' to be {ind_1_weight}%, {ind_3_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight >0:
                        st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice}, {name_indicator_2} and {name_indicator_3}' 
                        f' to be {ind_3_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight == 0:
                        st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {name_indicator_2} and {name_indicator_3}' 
                        f' to be {ind_2_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight > 0:
                        st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice}, {name_indicator_2} and {name_indicator_3}' 
                        f' to be {ind_2_weight}%, {ind_3_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively. '
                        f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight == 0:
                        st.write(f'You selected the proportion of the funding allocated based on {name_indicator_2} and {name_indicator_3} to be {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively. '
                        f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')

                if uploaded_ind_1_weight >0 and uploaded_ind_2_weight == 0 and uploaded_ind_3_weight > 0:
                    if ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight > 0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice}, {name_indicator_1} and {name_indicator_3}' 
                            f' to be {ind_2_weight}%, {ind_3_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_3_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice}, {ind_3_choice}, {name_indicator_1} and {name_indicator_3}' 
                            f' to be {ind_1_weight}%, {ind_2_weight}%, {ind_3_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_3_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight == 0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {name_indicator_1} and {name_indicator_3}' 
                            f' to be {ind_2_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_3_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice}, {name_indicator_1} and {name_indicator_3}' 
                            f' to be {ind_1_weight}%, {ind_2_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_3_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight ==0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {name_indicator_1} and {name_indicator_3}' 
                            f' to be {uploaded_ind_1_weight}% and {uploaded_ind_3_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {name_indicator_1} and {name_indicator_3}' 
                            f' to be {ind_1_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_3_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight >0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice}, {name_indicator_1} and {name_indicator_3}' 
                            f' to be {ind_3_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_3_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_3_choice}, {name_indicator_1} and {name_indicator_3}' 
                            f' to be {ind_1_weight}%, {ind_3_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_3_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight >0:
                        st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice}, {name_indicator_1} and {name_indicator_3}' 
                        f' to be {ind_3_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_3_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight == 0:
                        st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {name_indicator_1} and {name_indicator_3}' 
                        f' to be {ind_2_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_3_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight > 0:
                        st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice}, {name_indicator_1} and {name_indicator_3}' 
                        f' to be {ind_2_weight}%, {ind_3_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_3_weight}%, respectively. '
                        f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight == 0:
                        st.write(f'You selected the proportion of the funding allocated based on {name_indicator_1} and {name_indicator_3} to be {uploaded_ind_1_weight}% and {uploaded_ind_3_weight}%, respectively. '
                        f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
            
                if uploaded_ind_1_weight >0 and uploaded_ind_2_weight >0 and uploaded_ind_3_weight >0:
                    if ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight > 0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice}, {name_indicator_1}, {name_indicator_2} and {name_indicator_3}' 
                            f' to be {ind_2_weight}%, {ind_3_weight}%, {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice}, {ind_3_choice}, {name_indicator_1}, {name_indicator_2} and {name_indicator_3}' 
                            f' to be {ind_1_weight}%, {ind_2_weight}%, {ind_3_weight}%, {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight == 0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {name_indicator_1}, {name_indicator_2} and {name_indicator_3}' 
                            f' to be {ind_2_weight}%, {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice}, {name_indicator_1}, {name_indicator_2} and {name_indicator_3}' 
                            f' to be {ind_1_weight}%, {ind_2_weight}%, {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight ==0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {name_indicator_1}, {name_indicator_2} and {name_indicator_3}' 
                            f' to be {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {name_indicator_1}, {name_indicator_2} and {name_indicator_3}' 
                            f' to be {ind_1_weight}%, {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight >0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice}, {name_indicator_1}, {name_indicator_2} and {name_indicator_3}' 
                            f' to be {ind_3_weight}%, {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_3_choice}, {name_indicator_1}, {name_indicator_2} and {name_indicator_3}' 
                            f' to be {ind_1_weight}%, {ind_3_weight}%, {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight >0:
                        st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice}, {name_indicator_1}, {name_indicator_2} and {name_indicator_3}' 
                        f' to be {ind_3_weight}%, {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight == 0:
                        st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {name_indicator_1}, {name_indicator_2} and {name_indicator_3}' 
                        f' to be {ind_2_weight}%, {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight > 0:
                        st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice}, {name_indicator_1}, {name_indicator_2} and {name_indicator_3}' 
                        f' to be {ind_2_weight}%, {ind_3_weight}%, {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively. '
                        f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight == 0:
                        st.write(f'You selected the proportion of the funding allocated based on {name_indicator_1}, {name_indicator_2} and {name_indicator_3}' 
                                 f' to be {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively. '
                        f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')

                elif uploaded_ind_1_weight == 0 and uploaded_ind_2_weight == 0 and uploaded_ind_3_weight == 0:
                    if ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight > 0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice} and {ind_3_choice}' 
                            f' to be {ind_2_weight}% and {ind_3_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice} and {ind_3_choice}' 
                            f' to be {ind_1_weight}%, {ind_2_weight}% and {ind_3_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight == 0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}' 
                            f' to be {ind_2_weight}%. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice} and {ind_2_choice}' 
                            f' to be {ind_1_weight}% and {ind_2_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight ==0:
                        if ind_1_choice == 'Choose an option':
                            st.write('You selected to allocate the funding soley based on registered population size.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}' 
                            f' to be {ind_1_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight >0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice}' 
                            f' to be {ind_3_weight}%. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice} and {ind_3_choice}' 
                            f' to be {ind_1_weight}% and {ind_3_weight}%, respectively. '
                            f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight >0:
                        st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice}' 
                        f' to be {ind_3_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight == 0:
                        st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}' 
                        f' to be {ind_2_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight > 0:
                        st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice} and {ind_3_choice}' 
                        f' to be {ind_2_weight}% and {ind_3_weight}%, respectively. '
                        f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight == 0:
                        st.write('You selected to allocate the funding soley based on registered population size.')


            elif prop_pop == 0:
                if uploaded_ind_1_weight >0 and uploaded_ind_2_weight == 0 and uploaded_ind_3_weight == 0:
                    if ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight > 0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice} and {name_indicator_1}' 
                            f' to be {ind_2_weight}%, {ind_3_weight}% and {uploaded_ind_1_weight}%, respectively.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice}, {ind_3_choice} and {name_indicator_1}' 
                            f' to be {ind_1_weight}%, {ind_2_weight}%, {ind_3_weight}% and {uploaded_ind_1_weight}%, respectively.')
                    elif ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight == 0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice} and {name_indicator_1}' 
                            f' to be {ind_2_weight}% and {uploaded_ind_1_weight}%, respectively.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice} and {name_indicator_1}' 
                            f' to be {ind_1_weight}%, {ind_2_weight}% and {uploaded_ind_1_weight}%, respectively.')
                    elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight ==0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected to allocate the funding soley based on {name_indicator_1}')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice} and {name_indicator_1}' 
                            f' to be {ind_1_weight}% and {uploaded_ind_1_weight}%.')
                    elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight >0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice} and {name_indicator_1}' 
                            f' to be {ind_3_weight}% and {uploaded_ind_1_weight}%, respectively.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_3_choice} and {name_indicator_1}' 
                            f' to be {ind_1_weight}%, {ind_3_weight}% and {uploaded_ind_1_weight}%, respectively.')
                    elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight >0:
                        st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice} and {name_indicator_1}' 
                        f' to be {ind_3_weight}% and {uploaded_ind_1_weight}%.')
                    elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight == 0:
                        st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice} and {name_indicator_1}' 
                        f' to be {ind_2_weight}% and {uploaded_ind_1_weight}%.')
                    elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight > 0:
                        st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice} and {name_indicator_1}' 
                        f' to be {ind_2_weight}%, {ind_3_weight}% and {uploaded_ind_1_weight}%, respectively.')
                    elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight == 0:
                        st.write(f'You selected the proportion of the funding allocated based on {name_indicator_1}.')

                if uploaded_ind_1_weight == 0 and uploaded_ind_2_weight >0 and uploaded_ind_3_weight == 0:
                    if ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight > 0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice} and {name_indicator_2}' 
                            f' to be {ind_2_weight}%, {ind_3_weight}% and {uploaded_ind_2_weight}%, respectively.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice}, {ind_3_choice} and {name_indicator_2}' 
                            f' to be {ind_1_weight}%, {ind_2_weight}%, {ind_3_weight}% and {uploaded_ind_2_weight}%, respectively.')
                    elif ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight == 0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice} and {name_indicator_2}' 
                            f' to be {ind_2_weight}% and {uploaded_ind_2_weight}%, respectively.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice} and {name_indicator_2}' 
                            f' to be {ind_1_weight}%, {ind_2_weight}% and {uploaded_ind_2_weight}%, respectively.')
                    elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight ==0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected to allocate the funding soley based on {name_indicator_2}')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice} and {name_indicator_2}' 
                            f' to be {ind_1_weight}% and {uploaded_ind_2_weight}%.')
                    elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight >0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice} and {name_indicator_2}' 
                            f' to be {ind_3_weight}% and {uploaded_ind_2_weight}%, respectively.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_3_choice} and {name_indicator_2}' 
                            f' to be {ind_1_weight}%, {ind_3_weight}% and {uploaded_ind_2_weight}%, respectively.')
                    elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight >0:
                        st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice} and {name_indicator_2}' 
                        f' to be {ind_3_weight}% and {uploaded_ind_2_weight}%.')
                    elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight == 0:
                        st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice} and {name_indicator_2}' 
                        f' to be {ind_2_weight}% and {uploaded_ind_2_weight}%.')
                    elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight > 0:
                        st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice} and {name_indicator_2}' 
                        f' to be {ind_2_weight}%, {ind_3_weight}% and {uploaded_ind_2_weight}%, respectively.')
                    elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight == 0:
                        st.write(f'You selected the proportion of the funding allocated based on {name_indicator_2}.')

                if uploaded_ind_1_weight == 0 and uploaded_ind_2_weight == 0 and uploaded_ind_3_weight > 0:
                    if ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight > 0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice} and {name_indicator_3}' 
                            f' to be {ind_2_weight}%, {ind_3_weight}% and {uploaded_ind_3_weight}%, respectively.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice}, {ind_3_choice} and {name_indicator_3}' 
                            f' to be {ind_1_weight}%, {ind_2_weight}%, {ind_3_weight}% and {uploaded_ind_3_weight}%, respectively.')
                    elif ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight == 0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice} and {name_indicator_3}' 
                            f' to be {ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice} and {name_indicator_3}' 
                            f' to be {ind_1_weight}%, {ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                    elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight ==0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected to allocate the funding soley based on {name_indicator_3}')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice} and {name_indicator_3}' 
                            f' to be {ind_1_weight}% and {uploaded_ind_3_weight}%.')
                    elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight >0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice} and {name_indicator_3}' 
                            f' to be {ind_3_weight}% and {uploaded_ind_3_weight}%, respectively.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_3_choice} and {name_indicator_3}' 
                            f' to be {ind_1_weight}%, {ind_3_weight}% and {uploaded_ind_3_weight}%, respectively.')
                    elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight >0:
                        st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice} and {name_indicator_3}' 
                        f' to be {ind_3_weight}% and {uploaded_ind_3_weight}%.')
                    elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight == 0:
                        st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice} and {name_indicator_3}' 
                        f' to be {ind_2_weight}% and {uploaded_ind_3_weight}%.')
                    elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight > 0:
                        st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice} and {name_indicator_3}' 
                        f' to be {ind_2_weight}%, {ind_3_weight}% and {uploaded_ind_3_weight}%, respectively.')
                    elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight == 0:
                        st.write(f'You selected the proportion of the funding allocated based on {name_indicator_3}.')

                if uploaded_ind_1_weight >0 and uploaded_ind_2_weight >0 and uploaded_ind_3_weight == 0:
                    if ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight > 0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice}, {name_indicator_1} and {name_indicator_2}' 
                            f' to be {ind_2_weight}%, {ind_3_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_2_weight}%, respectively.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice}, {ind_3_choice}, {name_indicator_1} and {name_indicator_2}' 
                            f' to be {ind_1_weight}%, {ind_2_weight}%, {ind_3_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_2_weight}%, respectively.')
                    elif ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight == 0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {name_indicator_1} and {name_indicator_2}' 
                            f' to be {ind_2_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_2_weight}%, respectively.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice}, {name_indicator_1} and {name_indicator_2}' 
                            f' to be {ind_1_weight}%, {ind_2_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_2_weight}%, respectively.')
                    elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight ==0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {name_indicator_1} and {name_indicator_2}' 
                            f' to be {uploaded_ind_1_weight}% and {uploaded_ind_2_weight}%, respectively.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {name_indicator_1} and {name_indicator_2}' 
                            f' to be {ind_1_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_2_weight}%.')
                    elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight >0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice}, {name_indicator_1} and {name_indicator_2}' 
                            f' to be {ind_3_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_2_weight}%, respectively.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_3_choice}, {name_indicator_1} and {name_indicator_2}' 
                            f' to be {ind_1_weight}%, {ind_3_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_2_weight}%, respectively.')
                    elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight >0:
                        st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice}, {name_indicator_1} and {name_indicator_2}' 
                        f' to be {ind_3_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_2_weight}%.')
                    elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight == 0:
                        st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {name_indicator_1} and {name_indicator_2}' 
                        f' to be {ind_2_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_2_weight}%.')
                    elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight > 0:
                        st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice}, {name_indicator_1} and {name_indicator_2}' 
                        f' to be {ind_2_weight}%, {ind_3_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_2_weight}%, respectively.')
                    elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight == 0:
                        st.write(f'You selected the proportion of the funding allocated based on {name_indicator_1} and {name_indicator_2}'
                                  f' to be {uploaded_ind_1_weight}% and {uploaded_ind_2_weight}%, respectively.')

                if uploaded_ind_1_weight == 0 and uploaded_ind_2_weight >0 and uploaded_ind_3_weight > 0:
                    if ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight > 0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice}, {name_indicator_2} and {name_indicator_3}' 
                            f' to be {ind_2_weight}%, {ind_3_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice}, {ind_3_choice}, {name_indicator_2} and {name_indicator_3}' 
                            f' to be {ind_1_weight}%, {ind_2_weight}%, {ind_3_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                    elif ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight == 0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {name_indicator_2} and {name_indicator_3}' 
                            f' to be {ind_2_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice}, {name_indicator_2} and {name_indicator_3}' 
                            f' to be {ind_1_weight}%, {ind_2_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                    elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight ==0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {name_indicator_2} and {name_indicator_3}' 
                            f' to be {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {name_indicator_2} and {name_indicator_3}' 
                            f' to be {ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%.')
                    elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight >0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice}, {name_indicator_2} and {name_indicator_3}' 
                            f' to be {ind_3_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_3_choice}, {name_indicator_2} and {name_indicator_3}' 
                            f' to be {ind_1_weight}%, {ind_3_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                    elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight >0:
                        st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice}, {name_indicator_2} and {name_indicator_3}' 
                        f' to be {ind_3_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%.')
                    elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight == 0:
                        st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {name_indicator_2} and {name_indicator_3}' 
                        f' to be {ind_2_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%.')
                    elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight > 0:
                        st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice}, {name_indicator_2} and {name_indicator_3}' 
                        f' to be {ind_2_weight}%, {ind_3_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                    elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight == 0:
                        st.write(f'You selected the proportion of the funding allocated based on {name_indicator_2} and {name_indicator_3}'
                                  f' to be {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                        
                if uploaded_ind_1_weight > 0 and uploaded_ind_2_weight == 0 and uploaded_ind_3_weight > 0:
                    if ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight > 0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice}, {name_indicator_1} and {name_indicator_3}' 
                            f' to be {ind_2_weight}%, {ind_3_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice}, {ind_3_choice}, {name_indicator_1} and {name_indicator_3}' 
                            f' to be {ind_1_weight}%, {ind_2_weight}%, {ind_3_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_3_weight}%, respectively.')
                    elif ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight == 0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {name_indicator_1} and {name_indicator_3}' 
                            f' to be {ind_2_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice}, {name_indicator_1} and {name_indicator_3}' 
                            f' to be {ind_1_weight}%, {ind_2_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_3_weight}%, respectively.')
                    elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight ==0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {name_indicator_1} and {name_indicator_3}' 
                            f' to be {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {name_indicator_1} and {name_indicator_3}' 
                            f' to be {ind_1_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_3_weight}%.')
                    elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight >0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice}, {name_indicator_1} and {name_indicator_3}' 
                            f' to be {ind_3_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_3_choice}, {name_indicator_1} and {name_indicator_3}' 
                            f' to be {ind_1_weight}%, {ind_3_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_3_weight}%, respectively.')
                    elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight >0:
                        st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice}, {name_indicator_1} and {name_indicator_3}' 
                        f' to be {ind_3_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_3_weight}%.')
                    elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight == 0:
                        st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {name_indicator_1} and {name_indicator_3}' 
                        f' to be {ind_2_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_3_weight}%.')
                    elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight > 0:
                        st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice}, {name_indicator_1} and {name_indicator_3}' 
                        f' to be {ind_2_weight}%, {ind_3_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_3_weight}%, respectively.')
                    elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight == 0:
                        st.write(f'You selected the proportion of the funding allocated based on {name_indicator_1} and {name_indicator_3}'
                                  f' to be {uploaded_ind_1_weight}% and {uploaded_ind_3_weight}%, respectively.')
                        
                if  uploaded_ind_1_weight >0 and uploaded_ind_2_weight > 0 and uploaded_ind_3_weight >0:
                    if ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight > 0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice}, {name_indicator_1}, {name_indicator_2} and {name_indicator_3}' 
                            f' to be {ind_2_weight}%, {ind_3_weight}%,  {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice}, {ind_3_choice}, {name_indicator_1}, {name_indicator_2} and {name_indicator_3}' 
                            f' to be {ind_1_weight}%, {ind_2_weight}%, {ind_3_weight}%, {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                    elif ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight == 0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {name_indicator_1}, {name_indicator_2} and {name_indicator_3}' 
                            f' to be {ind_2_weight}%, {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice}, {name_indicator_1}, {name_indicator_2} and {name_indicator_3}' 
                            f' to be {ind_1_weight}%, {ind_2_weight}%, {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                    elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight ==0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {name_indicator_1}, {name_indicator_2} and {name_indicator_3}' 
                            f' to be {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {name_indicator_1}, {name_indicator_2} and {name_indicator_3}' 
                            f' to be {ind_1_weight}%, {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                    elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight >0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice}, {name_indicator_1}, {name_indicator_2} and {name_indicator_3}' 
                            f' to be {ind_3_weight}%,  {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_3_choice}, {name_indicator_1}, {name_indicator_2} and {name_indicator_3}' 
                            f' to be {ind_1_weight}%, {ind_3_weight}%, {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                    elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight >0:
                        st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice}, {name_indicator_1}, {name_indicator_2} and {name_indicator_3}' 
                        f' to be {ind_3_weight}%, {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                    elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight == 0:
                        st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {name_indicator_1}, {name_indicator_2} and {name_indicator_3}' 
                        f' to be {ind_2_weight}%, {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                    elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight > 0:
                        st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice}, {name_indicator_1}, {name_indicator_2} and {name_indicator_3}' 
                        f' to be {ind_2_weight}%, {ind_3_weight}%, {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                    elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight == 0:
                        st.write(f'You selected the proportion of the funding allocated based on {name_indicator_1}, {name_indicator_2} and {name_indicator_3}'
                        f' to be {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')

                elif uploaded_ind_1_weight == 0 and uploaded_ind_2_weight == 0 and uploaded_ind_3_weight == 0:
                    if ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight > 0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice} and {ind_3_choice}' 
                            f' to be {ind_2_weight}% and {ind_3_weight}%, respectively.')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice} and {ind_3_choice}' 
                            f' to be {ind_1_weight}%, {ind_2_weight}% and {ind_3_weight}%, respectively.')
                    elif ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight == 0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected to allocate the funding soley based on {ind_2_choice}')
                        else:
                            st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice} and {ind_2_choice}' 
                            f' to be {ind_1_weight}% and {ind_2_weight}%, respectively.') 
                    elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight ==0:
                        if ind_1_choice == 'Choose an option':
                            st.write(f'You selected to allocate the funding soley based on registered population size.')
                        else:
                            st.write(f'You selected to allocate the funding soley based on {ind_1_choice}.')
                    elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight >0:
                            st.write(f'You selected to allocate the funding soley based on {ind_3_choice}.')
                    elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight >0:
                            st.write(f'You selected to allocate the funding soley based on {ind_3_choice}.')
                    elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight == 0:
                            st.write(f'You selected to allocate the funding soley based on {ind_2_choice}.')
                    elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight > 0:
                        st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice} and {ind_3_choice}' 
                        f' to be {ind_2_weight}% and {ind_3_weight}%, respectively.')

            st.write(f"Hence, based on your preferences, the allocation to each GP practice in _{icb_choice}_ is the following:")

            # Show results (table)
            st.dataframe(str_output_table, hide_index=True)

################################################################################
            # Add message if GP practices are missing indicator values 
#            n_of_listed_ind = len(selected_icb_for_ind_n_pop)
#            nan_ind_1 = str_output_table[ind_1_choice].isna().sum()
#            nan_ind_2 = 6 # amend accordingly "
#            nan_ind_3 = 1 # amend accordingly "
#            nan_up_ind_1 = 0 # amend accordingly "
#            nan_up_ind_2 = 2 # amend accordingly "
#            nan_up_ind_3 = 0 # amend accordingly "

#            nan_in_indicators_selected = [nan_ind_1, nan_ind_2, nan_ind_3, nan_up_ind_1, nan_up_ind_2, nan_up_ind_3]
#            max_nan =  max(nan_in_indicators_selected)
#            if max_nan == 0:
#                st.write()
#            else:
#                st.warning(f'BEWARE: Out of the {n_of_listed_ind} GP practices, {max_nan} are missing one or more indicator values which is affecting their allocation.')
#                st.write(f'nan in ind 1 = {nan_ind_1}')






            # COPY AFTER EXTRA_OUTPUT_PART!

################################################################################


        # Add statement to clarify discrepancy in values between pop vs weighted pop 
        # (which arise if the selected demographics does not comprise the entire GP practice size)   
            if ind_1_choice == 'Weighted population' or ind_2_choice == 'Weighted population' or ind_3_choice == 'Weighted population':
                if slider_age[0] >0 and slider_age[1] <95:
                    st.info("*Note: If you notice a discrepancy in the output above between values in the 'Population' and 'Weighted "
                             "population' columns, it is because the 'Weighted population' represents the entire population for that GP "
                             "practice. Hence, when selecting 'Weighted population', you might want to consider selecting the entire population size "
                                 "(from the 'age' and 'gender' options on the left)" )
                elif gender_selected != 'Both':
                    st.info("*Note: If you notice a discrepancy in the output above between values in the 'Population' and 'Weighted "
                             "population' columns, it is because the 'Weighted population' represents the entire population for that GP "
                             "practice. Hence, when selecting 'Weighted population', you might want to consider selecting the entire population size "
                                 "(from the 'age' and 'gender' options on the left)" )
                else:
                    st.write()


            # ADD DOWNLOAD BUTTON

            # IMPORTANT: Cache the conversion to prevent computation on every rerun
            @st.cache_data

            # Define function to convert DataFrame to csv
            def convert_df(df):
                return df.to_csv(index=False).encode('utf-8')

            csv = convert_df(str_output_table)
            st.download_button(label="**Download table**", data=csv, file_name=f'Allocations for {icb_choice}.csv',key="output_table")
            st.write('')
            st.write('')


################################################################################
    # OPTION TO OPEN AN EXPANDER TO DISPLAY A CHART
        if prop_pop <0:
            st.write('')
        else:
            with st.expander(':blue[Click here to display the chart]'):

                tab1, tab2 = st.tabs(["Total allocation", "Allocation per patient"])

                with tab1:                              # use for 'Total allocation'
                    y1 = wo_p_n_r_str_output_table['GP name']
                    x1 = wo_p_n_r_str_output_table['Total allocation (£)']

                # Create a figure object and an axes object, and add the axes object as a subplot of the figure object
                    trace_total = go.Bar (x = x1[::-1], y = y1[::-1], orientation='h')

                    data_1 = go.Figure([trace_total])   
                    data_1.update_layout(autosize=False,            #This stops plotly overriding our sizing wishes
                                        height=len(y1)*15,     # the height parameter defines how tall the plot is
    # (cont.) # the number of GP surgeries may vary substantially across different ICBs so here we look at the number of GPs in the plot (the length of y1) and multiply it by 15 pixels. 
                                        margin=go.layout.Margin(t=30), # this removes a big gap at the top of the chart
                                        title=f"Resource allocation for {icb_choice}",  # Add chart title
    #                                     title_x=0.5,         # Center chart title 
                                        xaxis=dict(title="Total allocation (£)", automargin=True, showgrid = True))         # Add title to x axis
                    data_1.update_yaxes(automargin=True, # The automargin parameter just ensures that the figure is adjusted so that long names don't get cut off
                                        dtick=1)     # This ensures we get a label for every GP surgery and it won't skip any and avoids overlapping labels
                    data_1.update_traces(hovertemplate='£ %{x:,.2f}<extra></extra>')  # Format hover text to display rounded values to 2 decimal points and '£' sign
                    # Show the figure
                    st.plotly_chart(data_1, use_container_width=True)

                with tab2:                          # use for 'Allocation per patient'
                # Sort the DataFrame by 'Allocation per patient' in descending order
                    wo_p_n_r_str_output_table_sorted_per_h = wo_p_n_r_str_output_table_sorted_per_h.sort_values(by='Allocation per patient (£)')
                    y2 = wo_p_n_r_str_output_table_sorted_per_h['GP name']
                    x2 = wo_p_n_r_str_output_table_sorted_per_h['Allocation per patient (£)']

                # Create a figure object and an axes object, and add the axes object as a subplot of the figure object
                    trace_p_h = go.Bar (x = x2, y = y2, orientation='h')
                    data_2 = go.Figure([trace_p_h])
                    data_2.update_layout(autosize=False, height=len(y2)*15,margin=go.layout.Margin(t=30),
                                        title=f"Resource allocation for {icb_choice}", 
                                        xaxis=dict(title="Allocation per patient (£)", automargin=True, showgrid = True))
                    data_2.update_yaxes(automargin=True, dtick=1)                
                    # Show the figure
                    st.plotly_chart(data_2, use_container_width=True)


   
################################################################################
# Initialise 'button_ticked' as False so that last expander ('Comparison with weighted pop') appears only if more_detail is 'checked'
button_ticked = False

if ind_1_weight ==100 or ind_2_weight ==100 or ind_3_weight ==100 or prop_pop == 100:
    st.write()
if prop_pop <0:
    st.write('')
else:
    st.write('')
    more_detail_is_checked = st.checkbox('Show more detail', 
                                  help='Show the breakdown of how the indicators selected and/or '
                                  'population size contribute towards the total allocation')

    if more_detail_is_checked:
        button_ticked = True      # This allows the last expander ('Comparison with weighted pop') to appear
#       st.empty()    
        with st.spinner('Running calculations...'):

                # Output (option #2)
                str_extra_output_table = pd.DataFrame()
                str_extra_output_table['GP name'] = selected_icb_for_ind_n_pop['GP name']
                str_extra_output_table['GP code'] = selected_icb_for_ind_n_pop['GP code']
                # add population column and commas
                str_extra_output_table['Population'] = selected_icb_for_ind_n_pop['Population'].fillna(0).apply(lambda x: "{:,}".format(int(x)))

                # If weighted pop is selected in any of the three listed indicator boxes, add them in output table, round it to 0 decimal and add comma
                for ind_weight, ind_choice, selected_ind_w_correct_icb in zip([ind_1_weight, ind_2_weight, ind_3_weight],
                                                                      [ind_1_choice, ind_2_choice, ind_3_choice],
                                                                      [selected_ind_1_w_correct_icb, selected_ind_2_w_correct_icb, selected_ind_3_w_correct_icb]):

                    if ind_weight > 0:

                        ########################################
        # If weighted pop is selected in any of the three listed indicator boxes, add them in output table, round it to 0 decimal and add comma
                        if ind_choice == 'Weighted population':
                            str_extra_output_table['Weighted population'] = selected_ind_w_correct_icb
                            round_pop = ['Weighted population']
                            str_extra_output_table[round_pop] = str_extra_output_table[round_pop].map(
                                lambda x: "{:,.0f}".format(x) if isinstance(x, (int, float)) else x)
                            # Round to 1 decimal point
                        elif ind_choice == 'IMD score (2019)':
                            str_extra_output_table[ind_choice] = selected_ind_w_correct_icb.apply(
                                lambda x: "{:,.1f}".format(x) if isinstance(x, (int, float)) else x)
                        else:
                            str_extra_output_table[f'{ind_choice} (%)'] = selected_ind_w_correct_icb
                            # Add '%' sign and round all others to 1 decimal point
                            rounded_indicator_name = ind_choice
                            str_extra_output_table[f'{rounded_indicator_name} (%)'] = str_extra_output_table[f'{ind_choice} (%)'].apply(
                                lambda x: "{:,.1f}".format(x) if isinstance(x, (int, float)) else x)

                # This section has been restored as original version (w/o 'for' function) otherwise later crashes if displays the chart with 'extra' columns

                # If indicators have been uploaded, add them in output table, round them to 0 decimal and add comma
                if uploaded_ind_1_weight >0:
                    str_extra_output_table[f'{name_indicator_1}'] = matched_uploaded_indicator_1['xyz']
                    # round to 1 decimal pt
                    round_uploaded = [f'{name_indicator_1}']
                    str_extra_output_table[round_uploaded] = str_extra_output_table[round_uploaded].map(lambda x: "{:,.1f}".format(x) if isinstance(x, (int, float)) else x)
                if uploaded_ind_2_weight >0:
                    str_extra_output_table[f'{name_indicator_2}'] = matched_uploaded_indicator_2['xyz']
                    # round to 1 decimal pt
                    round_uploaded = [f'{name_indicator_2}']
                    str_extra_output_table[round_uploaded] = str_extra_output_table[round_uploaded].map(lambda x: "{:,.1f}".format(x) if isinstance(x, (int, float)) else x)
                if uploaded_ind_3_weight >0:
                    str_extra_output_table[f'{name_indicator_3}'] = matched_uploaded_indicator_3['xyz']
                    # round to 1 decimal pt
                    round_uploaded = [f'{name_indicator_3}']
                    str_extra_output_table[round_uploaded] = str_extra_output_table[round_uploaded].map(lambda x: "{:,.1f}".format(x) if isinstance(x, (int, float)) else x)

                # This adds in the output table the amount allocated to each GP practice by that specific indicator; values are rounded them to 2 decimal and commas are added
                if ind_1_weight > 0:
                    str_extra_output_table[f'Allocation by {ind_1_choice} (£)'] = alloc_by_ind_1_weighted     
                    # add commas and round to 2 decimal points the newly calculated columns
                    round_output_x1 = [f'Allocation by {ind_1_choice} (£)']
                    str_extra_output_table[round_output_x1] = str_extra_output_table[round_output_x1].map(lambda x: '{:,.2f}'.format(x) if isinstance(x, (int, float)) else x)

                if ind_2_weight >0:
                    str_extra_output_table[f'Allocation by {ind_2_choice} (£)'] = alloc_by_ind_2_weighted  
                    # add commas and round to 2 decimal points the newly calculated columns
                    pound_n_round_output_x2 = [f'Allocation by {ind_2_choice} (£)']
                    str_extra_output_table[pound_n_round_output_x2] = str_extra_output_table[pound_n_round_output_x2].map(lambda x: "{:,.2f}".format(x) if isinstance(x, (int, float)) else x)

                if ind_3_weight >0:
                    str_extra_output_table[f'Allocation by {ind_3_choice} (£)'] = alloc_by_ind_3_weighted   
                    # add commas and round to 2 decimal points the newly calculated columns
                    round_output_x3 = [f'Allocation by {ind_3_choice} (£)']
                    str_extra_output_table[round_output_x3] = str_extra_output_table[round_output_x3].map(lambda x: "{:,.2f}".format(x) if isinstance(x, (int, float)) else x)

                if uploaded_ind_1_weight > 0:
                    str_extra_output_table[f'Allocation by {name_indicator_1} (£)'] = alloc_by_up_ind_1_weighted     
                    # add commas and round to 2 decimal points the newly calculated columns
                    round_output_u1 = [f'Allocation by {name_indicator_1} (£)']
                    str_extra_output_table[round_output_u1] = str_extra_output_table[round_output_u1].map(lambda x: "{:,.2f}".format(x) if isinstance(x, (int, float)) else x)

                if uploaded_ind_2_weight > 0:
                    str_extra_output_table[f'Allocation by {name_indicator_2} (£)'] = alloc_by_up_ind_2_weighted     
                    # add commas and round to 2 decimal points the newly calculated columns
                    round_output_u2 = [f'Allocation by {name_indicator_2} (£)']
                    str_extra_output_table[round_output_u2] = str_extra_output_table[round_output_u2].map(lambda x: "{:,.2f}".format(x) if isinstance(x, (int, float)) else x)

                if uploaded_ind_3_weight > 0:
                    str_extra_output_table[f'Allocation by {name_indicator_3} (£)'] = alloc_by_up_ind_3_weighted     
                    # add commas and round to 2 decimal points the newly calculated columns
                    round_output_u3 = [f'Allocation by {name_indicator_3} (£)']
                    str_extra_output_table[round_output_u3] = str_extra_output_table[round_output_u3].map(lambda x: "{:,.2f}".format(x) if isinstance(x, (int, float)) else x)

                if prop_pop >0:
                    str_extra_output_table['Allocation by population size (£)'] = alloc_by_pop
                    # add commas and round to 2 decimal points the newly calculated columns
                    round_output_x_pop = ['Allocation by population size (£)']
                    str_extra_output_table[round_output_x_pop] = str_extra_output_table[round_output_x_pop].map(lambda x: "{:,.2f}".format(x) if isinstance(x, (int, float)) else x)


                # This removes 'Choose an option' from the output if no indicator is selected
                str_extra_output_table['Choose an option (%)'] = selected_icb_for_ind_n_pop['GP name']
                str_extra_output_table.drop(columns=['Choose an option (%)'], inplace=True)

                str_extra_output_table['Total allocation (£)'] = tot_alloc
                str_extra_output_table['Allocation per patient (£)'] = alloc_per_head

                # Sort values (descending) by total allocation      
                # (Sort before adding '£'sign or will sort 4-digits values first and then <4 digits values)
                str_extra_output_table = str_extra_output_table.sort_values(by='Total allocation (£)', ascending=False)

                # keep a copy before modifying to use for bar chart (below)
                wo_rnd_str_x_output_table = str_extra_output_table.copy()         
                wo_rnd_str_x_output_table_sorted_per_h = str_extra_output_table.copy() 

                round_output_f2 = ['Total allocation (£)', 'Allocation per patient (£)']
                str_extra_output_table[round_output_f2] = str_extra_output_table[round_output_f2].map(lambda x: "{:,.2f}".format(x) if isinstance(x, (int, float)) else x)


                # Messages summarising which indicators contribute to what
                if prop_pop <0:
                    st.write(f'<span style="color: red;">IMPORTANT! The weighting selected cannot be greater than 100%. Please amend the weighting</span>', unsafe_allow_html=True)
                else:
                    st.success('Done!')
                    if prop_pop >0:
                        if uploaded_ind_1_weight >0 and uploaded_ind_2_weight ==0 and uploaded_ind_3_weight == 0:
                            if ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight > 0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice} and {name_indicator_1}' 
                                    f' to be {ind_2_weight}%, {ind_3_weight}% and {uploaded_ind_1_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice}, {ind_3_choice} and {name_indicator_1}' 
                                    f' to be {ind_1_weight}%, {ind_2_weight}%, {ind_3_weight}% and {uploaded_ind_1_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight == 0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice} and {name_indicator_1}' 
                                    f' to be {ind_2_weight}% and {uploaded_ind_1_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice} and {name_indicator_1}' 
                                    f' to be {ind_1_weight}%, {ind_2_weight}% and {uploaded_ind_1_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight ==0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {name_indicator_1}' 
                                    f' to be {uploaded_ind_1_weight}% '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice} and {name_indicator_1}' 
                                    f' to be {ind_1_weight}% and {uploaded_ind_1_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight >0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice} and {name_indicator_1}' 
                                    f' to be {ind_3_weight}% and {uploaded_ind_1_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_3_choice} and {name_indicator_1}' 
                                    f' to be {ind_1_weight}%, {ind_3_weight}% and {uploaded_ind_1_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight >0:
                                st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice} and {name_indicator_1}' 
                                f' to be {ind_3_weight}% and {uploaded_ind_1_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight == 0:
                                st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice} and {name_indicator_1}' 
                                f' to be {ind_2_weight}% and {uploaded_ind_1_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight > 0:
                                st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice} and {name_indicator_1}' 
                                f' to be {ind_2_weight}%, {ind_3_weight}% and {uploaded_ind_1_weight}%, respectively. '
                                f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight == 0:
                                st.write(f'You selected the proportion of the funding allocated based on {name_indicator_1} to be {uploaded_ind_1_weight}%. '
                                f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')


                        if uploaded_ind_1_weight == 0 and uploaded_ind_2_weight > 0 and uploaded_ind_3_weight == 0:
                            if ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight > 0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice} and {name_indicator_2}' 
                                    f' to be {ind_2_weight}%, {ind_3_weight}% and {uploaded_ind_2_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice}, {ind_3_choice} and {name_indicator_2}' 
                                    f' to be {ind_1_weight}%, {ind_2_weight}%, {ind_3_weight}% and {uploaded_ind_2_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight == 0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice} and {name_indicator_2}' 
                                    f' to be {ind_2_weight}% and {uploaded_ind_2_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice} and {name_indicator_2}' 
                                    f' to be {ind_1_weight}%, {ind_2_weight}% and {uploaded_ind_2_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight ==0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {name_indicator_2}' 
                                    f' to be {uploaded_ind_2_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice} and {name_indicator_2}' 
                                    f' to be {ind_1_weight}% and {uploaded_ind_2_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight >0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice} and {name_indicator_2}' 
                                    f' to be {ind_3_weight}% and {uploaded_ind_2_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_3_choice} and {name_indicator_2}' 
                                    f' to be {ind_1_weight}%, {ind_3_weight}% and {uploaded_ind_2_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight >0:
                                st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice} and {name_indicator_2}' 
                                f' to be {ind_3_weight}% and {uploaded_ind_2_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight == 0:
                                st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice} and {name_indicator_2}' 
                                f' to be {ind_2_weight}% and {uploaded_ind_2_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight > 0:
                                st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice} and {name_indicator_2}' 
                                f' to be {ind_2_weight}%, {ind_3_weight}% and {uploaded_ind_2_weight}%, respectively. '
                                f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight == 0:
                                st.write(f'You selected the proportion of the funding allocated based on {name_indicator_2} to be {uploaded_ind_2_weight}%. '
                                f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                        
                        if uploaded_ind_1_weight == 0 and uploaded_ind_2_weight == 0 and uploaded_ind_3_weight > 0:
                            if ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight > 0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice} and {name_indicator_3}' 
                                    f' to be {ind_2_weight}%, {ind_3_weight}% and {uploaded_ind_3_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice}, {ind_3_choice} and {name_indicator_3}' 
                                    f' to be {ind_1_weight}%, {ind_2_weight}%, {ind_3_weight}% and {uploaded_ind_3_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight == 0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice} and {name_indicator_3}' 
                                    f' to be {ind_2_weight}% and {uploaded_ind_3_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice} and {name_indicator_3}' 
                                    f' to be {ind_1_weight}%, {ind_2_weight}% and {uploaded_ind_3_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight ==0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {name_indicator_3}' 
                                    f' to be {uploaded_ind_3_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice} and {name_indicator_3}' 
                                    f' to be {ind_1_weight}% and {uploaded_ind_3_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight >0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice} and {name_indicator_3}' 
                                    f' to be {ind_3_weight}% and {uploaded_ind_3_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_3_choice} and {name_indicator_3}' 
                                    f' to be {ind_1_weight}%, {ind_3_weight}% and {uploaded_ind_3_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight >0:
                                st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice} and {name_indicator_3}' 
                                f' to be {ind_3_weight}% and {uploaded_ind_3_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight == 0:
                                st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice} and {name_indicator_3}' 
                                f' to be {ind_2_weight}% and {uploaded_ind_3_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight > 0:
                                st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice} and {name_indicator_3}' 
                                f' to be {ind_2_weight}%, {ind_3_weight}% and {uploaded_ind_3_weight}%, respectively. '
                                f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight == 0:
                                st.write(f'You selected the proportion of the funding allocated based on {name_indicator_3} to be {uploaded_ind_3_weight}%. '
                                f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')

                        if uploaded_ind_1_weight >0 and uploaded_ind_2_weight >0 and uploaded_ind_3_weight == 0:
                            if ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight > 0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice}, {name_indicator_1} and {name_indicator_2}' 
                                    f' to be {ind_2_weight}%, {ind_3_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_2_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice}, {ind_3_choice}, {name_indicator_1} and {name_indicator_2}' 
                                    f' to be {ind_1_weight}%, {ind_2_weight}%, {ind_3_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_2_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight == 0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {name_indicator_1} and {name_indicator_2}' 
                                    f' to be {ind_2_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_2_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice}, {name_indicator_1} and {name_indicator_2}' 
                                    f' to be {ind_1_weight}%, {ind_2_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_2_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight ==0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {name_indicator_1} and {name_indicator_2}' 
                                    f' to be {uploaded_ind_1_weight}% and {uploaded_ind_2_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {name_indicator_1} and {name_indicator_2}' 
                                    f' to be {ind_1_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_2_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight >0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice}, {name_indicator_1} and {name_indicator_2}' 
                                    f' to be {ind_3_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_2_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_3_choice}, {name_indicator_1} and {name_indicator_2}' 
                                    f' to be {ind_1_weight}%, {ind_3_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_2_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight >0:
                                st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice}, {name_indicator_1} and {name_indicator_2}' 
                                f' to be {ind_3_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_2_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight == 0:
                                st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {name_indicator_1} and {name_indicator_2}' 
                                f' to be {ind_2_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_2_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight > 0:
                                st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice}, {name_indicator_1} and {name_indicator_2}' 
                                f' to be {ind_2_weight}%, {ind_3_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_2_weight}%, respectively. '
                                f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight == 0:
                                st.write(f'You selected the proportion of the funding allocated based on {name_indicator_1} and {name_indicator_2} to be {uploaded_ind_1_weight}% and {uploaded_ind_1_weight}%, respectively. '
                                f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')

                        if uploaded_ind_1_weight ==0 and uploaded_ind_2_weight >0 and uploaded_ind_3_weight > 0:
                            if ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight > 0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice}, {name_indicator_2} and {name_indicator_3}' 
                                    f' to be {ind_2_weight}%, {ind_3_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice}, {ind_3_choice}, {name_indicator_2} and {name_indicator_3}' 
                                    f' to be {ind_1_weight}%, {ind_2_weight}%, {ind_3_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight == 0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {name_indicator_2} and {name_indicator_3}' 
                                    f' to be {ind_2_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice}, {name_indicator_2} and {name_indicator_3}' 
                                    f' to be {ind_1_weight}%, {ind_2_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight ==0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {name_indicator_2} and {name_indicator_3}' 
                                    f' to be {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {name_indicator_2} and {name_indicator_3}' 
                                    f' to be {ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight >0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice}, {name_indicator_2} and {name_indicator_3}' 
                                    f' to be {ind_3_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_3_choice}, {name_indicator_2} and {name_indicator_3}' 
                                    f' to be {ind_1_weight}%, {ind_3_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight >0:
                                st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice}, {name_indicator_2} and {name_indicator_3}' 
                                f' to be {ind_3_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight == 0:
                                st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {name_indicator_2} and {name_indicator_3}' 
                                f' to be {ind_2_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight > 0:
                                st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice}, {name_indicator_2} and {name_indicator_3}' 
                                f' to be {ind_2_weight}%, {ind_3_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively. '
                                f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight == 0:
                                st.write(f'You selected the proportion of the funding allocated based on {name_indicator_2} and {name_indicator_3} to be {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively. '
                                f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')

                        if uploaded_ind_1_weight >0 and uploaded_ind_2_weight == 0 and uploaded_ind_3_weight > 0:
                            if ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight > 0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice}, {name_indicator_1} and {name_indicator_3}' 
                                    f' to be {ind_2_weight}%, {ind_3_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_3_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice}, {ind_3_choice}, {name_indicator_1} and {name_indicator_3}' 
                                    f' to be {ind_1_weight}%, {ind_2_weight}%, {ind_3_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_3_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight == 0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {name_indicator_1} and {name_indicator_3}' 
                                    f' to be {ind_2_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_3_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice}, {name_indicator_1} and {name_indicator_3}' 
                                    f' to be {ind_1_weight}%, {ind_2_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_3_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight ==0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {name_indicator_1} and {name_indicator_3}' 
                                    f' to be {uploaded_ind_1_weight}% and {uploaded_ind_3_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {name_indicator_1} and {name_indicator_3}' 
                                    f' to be {ind_1_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_3_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight >0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice}, {name_indicator_1} and {name_indicator_3}' 
                                    f' to be {ind_3_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_3_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_3_choice}, {name_indicator_1} and {name_indicator_3}' 
                                    f' to be {ind_1_weight}%, {ind_3_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_3_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight >0:
                                st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice}, {name_indicator_1} and {name_indicator_3}' 
                                f' to be {ind_3_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_3_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight == 0:
                                st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {name_indicator_1} and {name_indicator_3}' 
                                f' to be {ind_2_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_3_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight > 0:
                                st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice}, {name_indicator_1} and {name_indicator_3}' 
                                f' to be {ind_2_weight}%, {ind_3_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_3_weight}%, respectively. '
                                f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight == 0:
                                st.write(f'You selected the proportion of the funding allocated based on {name_indicator_1} and {name_indicator_3} to be {uploaded_ind_1_weight}% and {uploaded_ind_3_weight}%, respectively. '
                                f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                    
                        if uploaded_ind_1_weight >0 and uploaded_ind_2_weight >0 and uploaded_ind_3_weight >0:
                            if ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight > 0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice}, {name_indicator_1}, {name_indicator_2} and {name_indicator_3}' 
                                    f' to be {ind_2_weight}%, {ind_3_weight}%, {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice}, {ind_3_choice}, {name_indicator_1}, {name_indicator_2} and {name_indicator_3}' 
                                    f' to be {ind_1_weight}%, {ind_2_weight}%, {ind_3_weight}%, {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight == 0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {name_indicator_1}, {name_indicator_2} and {name_indicator_3}' 
                                    f' to be {ind_2_weight}%, {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice}, {name_indicator_1}, {name_indicator_2} and {name_indicator_3}' 
                                    f' to be {ind_1_weight}%, {ind_2_weight}%, {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight ==0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {name_indicator_1}, {name_indicator_2} and {name_indicator_3}' 
                                    f' to be {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {name_indicator_1}, {name_indicator_2} and {name_indicator_3}' 
                                    f' to be {ind_1_weight}%, {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight >0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice}, {name_indicator_1}, {name_indicator_2} and {name_indicator_3}' 
                                    f' to be {ind_3_weight}%, {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_3_choice}, {name_indicator_1}, {name_indicator_2} and {name_indicator_3}' 
                                    f' to be {ind_1_weight}%, {ind_3_weight}%, {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight >0:
                                st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice}, {name_indicator_1}, {name_indicator_2} and {name_indicator_3}' 
                                f' to be {ind_3_weight}%, {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight == 0:
                                st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {name_indicator_1}, {name_indicator_2} and {name_indicator_3}' 
                                f' to be {ind_2_weight}%, {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight > 0:
                                st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice}, {name_indicator_1}, {name_indicator_2} and {name_indicator_3}' 
                                f' to be {ind_2_weight}%, {ind_3_weight}%, {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively. '
                                f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight == 0:
                                st.write(f'You selected the proportion of the funding allocated based on {name_indicator_1}, {name_indicator_2} and {name_indicator_3}' 
                                        f' to be {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively. '
                                f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')

                        elif uploaded_ind_1_weight == 0 and uploaded_ind_2_weight == 0 and uploaded_ind_3_weight == 0:
                            if ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight > 0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice} and {ind_3_choice}' 
                                    f' to be {ind_2_weight}% and {ind_3_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice} and {ind_3_choice}' 
                                    f' to be {ind_1_weight}%, {ind_2_weight}% and {ind_3_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight == 0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}' 
                                    f' to be {ind_2_weight}%. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice} and {ind_2_choice}' 
                                    f' to be {ind_1_weight}% and {ind_2_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight ==0:
                                if ind_1_choice == 'Choose an option':
                                    st.write('You selected to allocate the funding soley based on registered population size.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}' 
                                    f' to be {ind_1_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight >0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice}' 
                                    f' to be {ind_3_weight}%. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice} and {ind_3_choice}' 
                                    f' to be {ind_1_weight}% and {ind_3_weight}%, respectively. '
                                    f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight >0:
                                st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice}' 
                                f' to be {ind_3_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight == 0:
                                st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}' 
                                f' to be {ind_2_weight}%. The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight > 0:
                                st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice} and {ind_3_choice}' 
                                f' to be {ind_2_weight}% and {ind_3_weight}%, respectively. '
                                f'The remaining {prop_pop}% of unassigned weighting will be based on registered population size.')
                            elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight == 0:
                                st.write('You selected to allocate the funding soley based on registered population size.')


                    elif prop_pop == 0:
                        if uploaded_ind_1_weight >0 and uploaded_ind_2_weight == 0 and uploaded_ind_3_weight == 0:
                            if ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight > 0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice} and {name_indicator_1}' 
                                    f' to be {ind_2_weight}%, {ind_3_weight}% and {uploaded_ind_1_weight}%, respectively.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice}, {ind_3_choice} and {name_indicator_1}' 
                                    f' to be {ind_1_weight}%, {ind_2_weight}%, {ind_3_weight}% and {uploaded_ind_1_weight}%, respectively.')
                            elif ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight == 0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice} and {name_indicator_1}' 
                                    f' to be {ind_2_weight}% and {uploaded_ind_1_weight}%, respectively.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice} and {name_indicator_1}' 
                                    f' to be {ind_1_weight}%, {ind_2_weight}% and {uploaded_ind_1_weight}%, respectively.')
                            elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight ==0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected to allocate the funding soley based on {name_indicator_1}')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice} and {name_indicator_1}' 
                                    f' to be {ind_1_weight}% and {uploaded_ind_1_weight}%.')
                            elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight >0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice} and {name_indicator_1}' 
                                    f' to be {ind_3_weight}% and {uploaded_ind_1_weight}%, respectively.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_3_choice} and {name_indicator_1}' 
                                    f' to be {ind_1_weight}%, {ind_3_weight}% and {uploaded_ind_1_weight}%, respectively.')
                            elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight >0:
                                st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice} and {name_indicator_1}' 
                                f' to be {ind_3_weight}% and {uploaded_ind_1_weight}%.')
                            elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight == 0:
                                st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice} and {name_indicator_1}' 
                                f' to be {ind_2_weight}% and {uploaded_ind_1_weight}%.')
                            elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight > 0:
                                st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice} and {name_indicator_1}' 
                                f' to be {ind_2_weight}%, {ind_3_weight}% and {uploaded_ind_1_weight}%, respectively.')
                            elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight == 0:
                                st.write(f'You selected the proportion of the funding allocated based on {name_indicator_1}.')

                        if uploaded_ind_1_weight == 0 and uploaded_ind_2_weight >0 and uploaded_ind_3_weight == 0:
                            if ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight > 0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice} and {name_indicator_2}' 
                                    f' to be {ind_2_weight}%, {ind_3_weight}% and {uploaded_ind_2_weight}%, respectively.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice}, {ind_3_choice} and {name_indicator_2}' 
                                    f' to be {ind_1_weight}%, {ind_2_weight}%, {ind_3_weight}% and {uploaded_ind_2_weight}%, respectively.')
                            elif ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight == 0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice} and {name_indicator_2}' 
                                    f' to be {ind_2_weight}% and {uploaded_ind_2_weight}%, respectively.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice} and {name_indicator_2}' 
                                    f' to be {ind_1_weight}%, {ind_2_weight}% and {uploaded_ind_2_weight}%, respectively.')
                            elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight ==0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected to allocate the funding soley based on {name_indicator_2}')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice} and {name_indicator_2}' 
                                    f' to be {ind_1_weight}% and {uploaded_ind_2_weight}%.')
                            elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight >0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice} and {name_indicator_2}' 
                                    f' to be {ind_3_weight}% and {uploaded_ind_2_weight}%, respectively.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_3_choice} and {name_indicator_2}' 
                                    f' to be {ind_1_weight}%, {ind_3_weight}% and {uploaded_ind_2_weight}%, respectively.')
                            elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight >0:
                                st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice} and {name_indicator_2}' 
                                f' to be {ind_3_weight}% and {uploaded_ind_2_weight}%.')
                            elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight == 0:
                                st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice} and {name_indicator_2}' 
                                f' to be {ind_2_weight}% and {uploaded_ind_2_weight}%.')
                            elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight > 0:
                                st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice} and {name_indicator_2}' 
                                f' to be {ind_2_weight}%, {ind_3_weight}% and {uploaded_ind_2_weight}%, respectively.')
                            elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight == 0:
                                st.write(f'You selected the proportion of the funding allocated based on {name_indicator_2}.')

                        if uploaded_ind_1_weight == 0 and uploaded_ind_2_weight == 0 and uploaded_ind_3_weight > 0:
                            if ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight > 0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice} and {name_indicator_3}' 
                                    f' to be {ind_2_weight}%, {ind_3_weight}% and {uploaded_ind_3_weight}%, respectively.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice}, {ind_3_choice} and {name_indicator_3}' 
                                    f' to be {ind_1_weight}%, {ind_2_weight}%, {ind_3_weight}% and {uploaded_ind_3_weight}%, respectively.')
                            elif ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight == 0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice} and {name_indicator_3}' 
                                    f' to be {ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice} and {name_indicator_3}' 
                                    f' to be {ind_1_weight}%, {ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                            elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight ==0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected to allocate the funding soley based on {name_indicator_3}.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice} and {name_indicator_3}' 
                                    f' to be {ind_1_weight}% and {uploaded_ind_3_weight}%.')
                            elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight >0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice} and {name_indicator_3}' 
                                    f' to be {ind_3_weight}% and {uploaded_ind_3_weight}%, respectively.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_3_choice} and {name_indicator_3}' 
                                    f' to be {ind_1_weight}%, {ind_3_weight}% and {uploaded_ind_3_weight}%, respectively.')
                            elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight >0:
                                st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice} and {name_indicator_3}' 
                                f' to be {ind_3_weight}% and {uploaded_ind_3_weight}%.')
                            elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight == 0:
                                st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice} and {name_indicator_3}' 
                                f' to be {ind_2_weight}% and {uploaded_ind_3_weight}%.')
                            elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight > 0:
                                st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice} and {name_indicator_3}' 
                                f' to be {ind_2_weight}%, {ind_3_weight}% and {uploaded_ind_3_weight}%, respectively.')
                            elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight == 0:
                                st.write(f'You selected the proportion of the funding allocated based on {name_indicator_3}.')

                        if uploaded_ind_1_weight >0 and uploaded_ind_2_weight >0 and uploaded_ind_3_weight == 0:
                            if ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight > 0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice}, {name_indicator_1} and {name_indicator_2}' 
                                    f' to be {ind_2_weight}%, {ind_3_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_2_weight}%, respectively.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice}, {ind_3_choice}, {name_indicator_1} and {name_indicator_2}' 
                                    f' to be {ind_1_weight}%, {ind_2_weight}%, {ind_3_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_2_weight}%, respectively.')
                            elif ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight == 0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {name_indicator_1} and {name_indicator_2}' 
                                    f' to be {ind_2_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_2_weight}%, respectively.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice}, {name_indicator_1} and {name_indicator_2}' 
                                    f' to be {ind_1_weight}%, {ind_2_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_2_weight}%, respectively.')
                            elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight ==0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {name_indicator_1} and {name_indicator_2}' 
                                    f' to be {uploaded_ind_1_weight}% and {uploaded_ind_2_weight}%, respectively.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {name_indicator_1} and {name_indicator_2}' 
                                    f' to be {ind_1_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_2_weight}%.')
                            elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight >0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice}, {name_indicator_1} and {name_indicator_2}' 
                                    f' to be {ind_3_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_2_weight}%, respectively.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_3_choice}, {name_indicator_1} and {name_indicator_2}' 
                                    f' to be {ind_1_weight}%, {ind_3_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_2_weight}%, respectively.')
                            elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight >0:
                                st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice}, {name_indicator_1} and {name_indicator_2}' 
                                f' to be {ind_3_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_2_weight}%.')
                            elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight == 0:
                                st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {name_indicator_1} and {name_indicator_2}' 
                                f' to be {ind_2_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_2_weight}%.')
                            elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight > 0:
                                st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice}, {name_indicator_1} and {name_indicator_2}' 
                                f' to be {ind_2_weight}%, {ind_3_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_2_weight}%, respectively.')
                            elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight == 0:
                                st.write(f'You selected the proportion of the funding allocated based on {name_indicator_1} and {name_indicator_2}'
                                        f' to be {uploaded_ind_1_weight}% and {uploaded_ind_2_weight}%, respectively.')

                        if uploaded_ind_1_weight == 0 and uploaded_ind_2_weight >0 and uploaded_ind_3_weight > 0:
                            if ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight > 0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice}, {name_indicator_2} and {name_indicator_3}' 
                                    f' to be {ind_2_weight}%, {ind_3_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice}, {ind_3_choice}, {name_indicator_2} and {name_indicator_3}' 
                                    f' to be {ind_1_weight}%, {ind_2_weight}%, {ind_3_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                            elif ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight == 0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {name_indicator_2} and {name_indicator_3}' 
                                    f' to be {ind_2_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice}, {name_indicator_2} and {name_indicator_3}' 
                                    f' to be {ind_1_weight}%, {ind_2_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                            elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight ==0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {name_indicator_2} and {name_indicator_3}' 
                                    f' to be {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {name_indicator_2} and {name_indicator_3}' 
                                    f' to be {ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%.')
                            elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight >0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice}, {name_indicator_2} and {name_indicator_3}' 
                                    f' to be {ind_3_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_3_choice}, {name_indicator_2} and {name_indicator_3}' 
                                    f' to be {ind_1_weight}%, {ind_3_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                            elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight >0:
                                st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice}, {name_indicator_2} and {name_indicator_3}' 
                                f' to be {ind_3_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%.')
                            elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight == 0:
                                st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {name_indicator_2} and {name_indicator_3}' 
                                f' to be {ind_2_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%.')
                            elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight > 0:
                                st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice}, {name_indicator_2} and {name_indicator_3}' 
                                f' to be {ind_2_weight}%, {ind_3_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                            elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight == 0:
                                st.write(f'You selected the proportion of the funding allocated based on {name_indicator_2} and {name_indicator_3}'
                                        f' to be {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                                
                        if uploaded_ind_1_weight > 0 and uploaded_ind_2_weight == 0 and uploaded_ind_3_weight > 0:
                            if ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight > 0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice}, {name_indicator_1} and {name_indicator_3}' 
                                    f' to be {ind_2_weight}%, {ind_3_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice}, {ind_3_choice}, {name_indicator_1} and {name_indicator_3}' 
                                    f' to be {ind_1_weight}%, {ind_2_weight}%, {ind_3_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_3_weight}%, respectively.')
                            elif ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight == 0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {name_indicator_1} and {name_indicator_3}' 
                                    f' to be {ind_2_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice}, {name_indicator_1} and {name_indicator_3}' 
                                    f' to be {ind_1_weight}%, {ind_2_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_3_weight}%, respectively.')
                            elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight ==0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {name_indicator_1} and {name_indicator_3}' 
                                    f' to be {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {name_indicator_1} and {name_indicator_3}' 
                                    f' to be {ind_1_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_3_weight}%.')
                            elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight >0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice}, {name_indicator_1} and {name_indicator_3}' 
                                    f' to be {ind_3_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_3_choice}, {name_indicator_1} and {name_indicator_3}' 
                                    f' to be {ind_1_weight}%, {ind_3_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_3_weight}%, respectively.')
                            elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight >0:
                                st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice}, {name_indicator_1} and {name_indicator_3}' 
                                f' to be {ind_3_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_3_weight}%.')
                            elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight == 0:
                                st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {name_indicator_1} and {name_indicator_3}' 
                                f' to be {ind_2_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_3_weight}%.')
                            elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight > 0:
                                st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice}, {name_indicator_1} and {name_indicator_3}' 
                                f' to be {ind_2_weight}%, {ind_3_weight}%, {uploaded_ind_1_weight}% and {uploaded_ind_3_weight}%, respectively.')
                            elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight == 0:
                                st.write(f'You selected the proportion of the funding allocated based on {name_indicator_1} and {name_indicator_3}'
                                        f' to be {uploaded_ind_1_weight}% and {uploaded_ind_3_weight}%, respectively.')
                                
                        if  uploaded_ind_1_weight >0 and uploaded_ind_2_weight > 0 and uploaded_ind_3_weight >0:
                            if ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight > 0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice}, {name_indicator_1}, {name_indicator_2} and {name_indicator_3}' 
                                    f' to be {ind_2_weight}%, {ind_3_weight}%,  {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice}, {ind_3_choice}, {name_indicator_1}, {name_indicator_2} and {name_indicator_3}' 
                                    f' to be {ind_1_weight}%, {ind_2_weight}%, {ind_3_weight}%, {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                            elif ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight == 0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {name_indicator_1}, {name_indicator_2} and {name_indicator_3}' 
                                    f' to be {ind_2_weight}%, {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice}, {name_indicator_1}, {name_indicator_2} and {name_indicator_3}' 
                                    f' to be {ind_1_weight}%, {ind_2_weight}%, {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                            elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight ==0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {name_indicator_1}, {name_indicator_2} and {name_indicator_3}' 
                                    f' to be {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {name_indicator_1}, {name_indicator_2} and {name_indicator_3}' 
                                    f' to be {ind_1_weight}%, {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                            elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight >0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice}, {name_indicator_1}, {name_indicator_2} and {name_indicator_3}' 
                                    f' to be {ind_3_weight}%,  {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_3_choice}, {name_indicator_1}, {name_indicator_2} and {name_indicator_3}' 
                                    f' to be {ind_1_weight}%, {ind_3_weight}%, {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                            elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight >0:
                                st.write(f'You selected the proportion of the funding allocated based on {ind_3_choice}, {name_indicator_1}, {name_indicator_2} and {name_indicator_3}' 
                                f' to be {ind_3_weight}%, {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                            elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight == 0:
                                st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {name_indicator_1}, {name_indicator_2} and {name_indicator_3}' 
                                f' to be {ind_2_weight}%, {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                            elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight > 0:
                                st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice}, {ind_3_choice}, {name_indicator_1}, {name_indicator_2} and {name_indicator_3}' 
                                f' to be {ind_2_weight}%, {ind_3_weight}%, {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')
                            elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight == 0:
                                st.write(f'You selected the proportion of the funding allocated based on {name_indicator_1}, {name_indicator_2} and {name_indicator_3}'
                                f' to be {uploaded_ind_1_weight}%, {uploaded_ind_2_weight}% and {uploaded_ind_3_weight}%, respectively.')

                        elif uploaded_ind_1_weight == 0 and uploaded_ind_2_weight == 0 and uploaded_ind_3_weight == 0:
                            if ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight > 0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice} and {ind_3_choice}' 
                                    f' to be {ind_2_weight}% and {ind_3_weight}%, respectively.')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice}, {ind_2_choice} and {ind_3_choice}' 
                                    f' to be {ind_1_weight}%, {ind_2_weight}% and {ind_3_weight}%, respectively.')
                            elif ind_1_weight >0 and ind_2_weight > 0 and ind_3_weight == 0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected to allocate the funding soley based on {ind_2_choice}')
                                else:
                                    st.write(f'You selected the proportion of the funding allocated based on {ind_1_choice} and {ind_2_choice}' 
                                    f' to be {ind_1_weight}% and {ind_2_weight}%, respectively.')
                            elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight ==0:
                                if ind_1_choice == 'Choose an option':
                                    st.write(f'You selected to allocate the funding soley based on registered population size.')
                                else:
                                    st.write(f'You selected to allocate the funding soley based on {ind_1_choice}.')
                            elif ind_1_weight >0 and ind_2_weight == 0 and ind_3_weight >0:
                                    st.write(f'You selected to allocate the funding soley based on {ind_3_choice}.')
                            elif ind_1_weight == 0 and ind_2_weight == 0 and ind_3_weight >0:
                                    st.write(f'You selected to allocate the funding soley based on {ind_3_choice}.')
                            elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight == 0:
                                    st.write(f'You selected to allocate the funding soley based on {ind_2_choice}.')
                            elif ind_1_weight == 0 and ind_2_weight > 0 and ind_3_weight > 0:
                                st.write(f'You selected the proportion of the funding allocated based on {ind_2_choice} and {ind_3_choice}' 
                                f' to be {ind_2_weight}% and {ind_3_weight}%, respectively.')

                    st.write(f"Hence, based on your preferences, the allocation to each GP practice in _{icb_choice}_ is the following:")


                # Show results (table)
                st.dataframe(str_extra_output_table, hide_index=True)

                # Add statement to clarify discrepancy in values between pop vs weighted pop 
                # (which arise if the selected demographics does not comprise the entire GP practice size)   
                if ind_1_choice == 'Weighted population' or ind_2_choice == 'Weighted population' or ind_3_choice == 'Weighted population':
                    if slider_age[0] >0 and slider_age[1] <95:
                        st.info("*Note: If you notice a discrepancy in the output above between values in the 'Population' and 'Weighted "
                             "population' columns, it is because the 'Weighted population' represents the entire population for that GP "
                             "practice. Hence, when selecting 'Weighted population', you might want to consider selecting the entire population size "
                                 "(from the 'age' and 'gender' options on the left)")
                    elif gender_selected != 'Both':
                        st.info("*Note: If you notice a discrepancy in the output above between values in the 'Population' and 'Weighted "
                             "population' columns, it is because the 'Weighted population' represents the entire population for that GP "
                             "practice. Hence, when selecting 'Weighted population', you might want to consider selecting the entire population size "
                                 "(from the 'age' and 'gender' options on the left)")
                    else:
                        st.write()


                # ADD DOWNLOAD BUTTON

                # IMPORTANT: Cache the conversion to prevent computation on every rerun
                @st.cache_data

                # Define function to convert DataFrame to csv
                def convert_df(df):
                    return df.to_csv(index=False).encode('utf-8')

                csv = convert_df(str_extra_output_table)
                st.download_button(label="**Download table**", data=csv, file_name=f'Allocations for {icb_choice}.csv',key="extra_output_table")
                st.write('')
                st.write('')

################################################################################
                # OPTION TO CLICK AN EXPANDER TO DISPLAY A CHART
                with st.expander(':blue[Click here to display the chart]'):
                    tab1, tab2 = st.tabs(["Total allocation", "Allocation per patient"])

                    with tab1:                              # use for 'Total allocation'
                        y1 = wo_rnd_str_x_output_table['GP name']
 
                    # Create a figure object and an axes object, and add the axes object as a subplot of the figure object
                        bar_traces = []
                        if uploaded_ind_1_weight >0:
                            for ind_choice, ind_weight in indicators_weights:
                                x_123 = wo_rnd_str_x_output_table[f'Allocation by {ind_choice} (£)']
                                bar_traces.append(go.Bar(x=x_123[::-1], y=y1[::-1], name=ind_choice, orientation='h'))
                            for up_indicator, up_weight in up_indicators_weights:
                                x_up123 = wo_rnd_str_x_output_table[f'Allocation by {up_indicator} (£)']
                                bar_traces.append(go.Bar(x=x_up123[::-1], y=y1[::-1], name=up_indicator, orientation='h'))
                            if prop_pop >0:
                                x_pop = wo_rnd_str_x_output_table['Allocation by population size (£)']
                                bar_traces.append(go.Bar(x=x_pop[::-1], y=y1[::-1], name='Population', orientation='h'))
                        else:
                            for ind_choice, ind_weight in indicators_weights:
                                x_123 = wo_rnd_str_x_output_table[f'Allocation by {ind_choice} (£)']
                                bar_traces.append(go.Bar(x=x_123[::-1], y=y1[::-1], name=ind_choice, orientation='h'))
                            if prop_pop >0:
                                x_pop = wo_rnd_str_x_output_table['Allocation by population size (£)']
                                bar_traces.append(go.Bar(x=x_pop[::-1], y=y1[::-1], name='Population', orientation='h'))
                        data_1 = go.Figure(bar_traces)
                        data_1.update_layout(autosize=False, height=len(y1)*15,margin=go.layout.Margin(t=30),
                                             title=f"Resource allocation for {icb_choice}", 
                                             xaxis=dict(title="Total allocation (£)", automargin=True, showgrid = True),barmode='stack', 
                                             legend_traceorder="normal", 
                                             legend=dict(orientation="h", y=-0.06, x=0.0))   
                        data_1.update_yaxes(automargin=True, dtick=1)
                        # Format hover text to display rounded values to 2 decimal points and '£' sign
                        data_1.update_traces(hovertemplate='£ %{x:,.2f}<extra></extra>')

                        # Show the figure
                        st.plotly_chart(data_1, use_container_width=True)

                    with tab2:                          # use for 'Allocation per patient'
                    # Sort the DataFrame by 'Allocation per patient' in descending order
                        wo_rnd_str_x_output_table_sorted_per_h = wo_rnd_str_x_output_table_sorted_per_h.sort_values(by='Allocation per patient (£)')
                        y2 = wo_rnd_str_x_output_table_sorted_per_h['GP name']
                        x2 = wo_rnd_str_x_output_table_sorted_per_h['Allocation per patient (£)']

                    # Create a figure object and an axes object, and add the axes object as a subplot of the figure object
                        trace_p_h = go.Bar (x = x2, y = y2, orientation='h')
                        data_2 = go.Figure([trace_p_h])
                        data_2.update_layout(autosize=False, height=len(y2)*15,margin=go.layout.Margin(t=30),
                                     title=f"Resource allocation for {icb_choice}", 
                                     xaxis=dict(title="Allocation per patient (£)", automargin=True, showgrid = True))
                        data_2.update_yaxes(automargin=True, dtick=1)
                        # Format hover text to display rounded values to 2 decimal points and '£' sign
                        data_2.update_traces(hovertemplate='£ %{x:,.2f}<extra></extra>')

                        # Show the figure
                        st.plotly_chart(data_2, use_container_width=True)


################################################################################

# Display an EXPANDER to show the difference if you would have used a weighted pop formula
# (only if 'weighted population' formula was not selected and if prop_pop is not <0)
if ind_1_choice == "Weighted population" and ind_1_weight == 100:
    st.write('')
elif ind_2_choice == "Weighted population" and ind_2_weight == 100:
    st.write('')
elif ind_3_choice == "Weighted population" and ind_3_weight == 100:
    st.write('')
elif prop_pop <0:
    st.write('')
elif button_ticked == True:   
    st.write('')
    st.write('')
    with st.expander(":blue[Click here to show the difference between your selection and a 'weighted population' formula]"):
        tab1wp, tab2wp, tab3wp = st.tabs(["Table", "Chart: Total allocation", "Chart: Allocation per patient"])

        # Calculate using weighted pop
        wt_pop_x_1 = selected_icb_for_ind_n_pop['Weighted population']
        sum_wt_pop_x_1 = wt_pop_x_1.sum()
        alloc_wt_pop = wt_pop_x_1.fillna(0) / sum_wt_pop_x_1 * funding

        alloc_wt_pop_p_head = alloc_wt_pop.fillna(0) /all_pop_merged['Population']    

############################################
        # Parameters for Tab2wp and Tab3wp
        comp_to_wt_pop = pd.DataFrame()
        comp_to_wt_pop['GP name'] = selected_icb_for_ind_n_pop['GP name']
        y_wp = comp_to_wt_pop['GP name']
        comp_to_wt_pop['with eFIT (£)'] = tot_alloc   
        comp_to_wt_pop['with weighted population (£)'] = alloc_wt_pop
        comp_to_wt_pop['with eFIT(£)'] = alloc_per_head
        comp_to_wt_pop['with weighted population(£)'] = alloc_wt_pop_p_head

        with tab1wp:                                            # use for Table
            data = {
                ('', 'GP name'): selected_icb_for_ind_n_pop['GP name'],
                ('', 'GP code'): selected_icb_for_ind_n_pop['GP code'],
                ('Population', 'with eFIT'): selected_icb_for_ind_n_pop['Population'],
                ('Population', 'Weighted'): selected_icb_for_ind_n_pop['Weighted population'],
                ('Total allocation (£)', 'with eFIT'): tot_alloc,
                ('Total allocation (£)', 'with weighted population'): alloc_wt_pop,
                ('Allocation per patient (£)', 'with eFIT'): alloc_per_head,
                ('Allocation per patient (£)', 'with weighted population'): alloc_wt_pop_p_head }

            # Creating MultiIndex
#            index = pd.MultiIndex.from_product(data)       # it doesn't seem to be needed to have a multiindexed dataframe

            # Creating DataFrame
            comp_to_wt_pop_table = pd.DataFrame(data)

            # Sorting by 'Total allocation' 'with eFIT (£)'
            comp_to_wt_pop_table = comp_to_wt_pop_table.sort_values(by=('Total allocation (£)', 'with eFIT'), ascending=False)
            # add commas to population 
            comp_to_wt_pop_table['Population', 'with eFIT'] = comp_to_wt_pop_table['Population', 'with eFIT'].apply(lambda x: "{:,}".format(x))

            # Convert specified columns to numeric before formatting
            # (to weighted population: add commas and round to zero decimal point) 
#            comp_to_wt_pop_table['Population', 'Weighted'] = pd.to_numeric(comp_to_wt_pop_table['Population', 'Weighted'])
            comp_to_wt_pop_table['Population', 'Weighted'] = comp_to_wt_pop_table['Population', 'Weighted'].apply(lambda x: "{:,.0f}".format(x))

            # (to remaining columns: add commas and round to zero decimal point) 
            columns_to_format = [('Total allocation (£)', 'with eFIT'), 
                                 ('Total allocation (£)', 'with weighted population'),
                                ('Allocation per patient (£)', 'with eFIT'),
                                ('Allocation per patient (£)', 'with weighted population')]

            for column in columns_to_format:
                comp_to_wt_pop_table[column] = pd.to_numeric(comp_to_wt_pop_table[column])
                comp_to_wt_pop_table[column] = comp_to_wt_pop_table[column].apply(lambda x: "{:,.2f}".format(x))

            # Show results (table)
            st.dataframe(comp_to_wt_pop_table, hide_index=True)

            # Add download  button
            @st.cache_data
            def convert_df(df):
            # IMPORTANT: Cache the conversion to prevent computation on every rerun
                return df.to_csv(index=False).encode('utf-8')

            csv = convert_df(comp_to_wt_pop_table)
            st.download_button(label="Download comparison table", data=csv, file_name=f'Allocations for {icb_choice}.csv', key = 'weight_pop')

        with tab2wp:                                # use for 'Total allocation'
            # Sort the DataFrame by 'Allocation per patient' in descending order
#            comp_to_wt_pop = comp_to_wt_pop.sort_values(by='with eFIT (£)', ascending=False)    # delete, this messes up things!

            x1eF = [-float(x) for x in comp_to_wt_pop['with eFIT (£)']]          # Make values negative otherwise it overlaps with other bar
            x1wp = comp_to_wt_pop['with weighted population (£)']

            # Create a figure object and 2 axes object (?), and add the axes object as a subplot of the figure object (?)
            bar_traces_wp = go.Figure()
            bar_traces_wp.add_trace(go.Bar(y=y_wp[::-1], x=x1eF[::-1], name='with eFIT', orientation='h', offset=-0.0))
            bar_traces_wp.add_trace(go.Bar(y=y_wp[::-1], x=x1wp[::-1], name='with weighted population', orientation='h', offset=0.0))
            # Format hover text to display rounded values to 2 decimal points and '£' sign
            bar_traces_wp.update_traces(hovertemplate='%{y}: £ %{x:,.2f}<extra></extra>')
            # Update layout
            bar_traces_wp.update_layout(autosize=False, height=len(y_wp)*15,margin=go.layout.Margin(t=30),
                title="Total allocation comparison between your selection with 'eFIT' tool or 'weighted population' formula",
                xaxis=dict(title="Total allocation (£)", showgrid = True), 
                yaxis_title="GP name",
                yaxis_visible=False,
                barmode='relative',  # Display bars side by side
                bargap=0.1,  # Adjust gap between bars
                legend=dict(orientation="h", x=0.42, y=1.1))  # Adjust legend position
            bar_traces_wp.update_yaxes(automargin=True, dtick=1)

            # Show the figure
            st.plotly_chart(bar_traces_wp, use_container_width=True)

        with tab3wp:                          # use for 'Allocation per patient'
            # Sort the DataFrame by 'Allocation per patient' in descending order

            x2eF = [-float(x) for x in comp_to_wt_pop['with eFIT(£)']]          # Make values negative otherwise it overlaps with other bar
            x2wp = comp_to_wt_pop['with weighted population(£)']

            # Create a figure object and 2 axes object (?), and add the axes object as a subplot of the figure object (?)
            bar_traces_wp_p_h = go.Figure()
            bar_traces_wp_p_h.add_trace(go.Bar(y=y_wp[::-1], x=x2eF[::-1], name='with eFIT', orientation='h', offset=-0.0))
            bar_traces_wp_p_h.add_trace(go.Bar(y=y_wp[::-1], x=x2wp[::-1], name='with weighted population', orientation='h', offset=0.0))
            # Format hover text to display rounded values to 2 decimal points and '£' sign
            bar_traces_wp_p_h.update_traces(hovertemplate='%{y}: £ %{x:,.2f}<extra></extra>')
            # Update layout
            bar_traces_wp_p_h.update_layout(autosize=False, height=len(y_wp)*15,margin=go.layout.Margin(t=30),
                title="Comparison of allocation per patient between your selection with 'eFIT' or 'weighted population' formula",
                xaxis=dict(title="Allocation per patient (£)", showgrid = True), 
                yaxis_title="GP name",
                yaxis_visible=False,
                barmode='relative',  # Display bars side by side
                bargap=0.1,  # Adjust gap between bars
                legend=dict(orientation="h", x=0.42, y=1.1))  # Adjust legend position
            bar_traces_wp_p_h.update_yaxes(automargin=True, dtick=1)

            # Show the figure
            st.plotly_chart(bar_traces_wp_p_h, use_container_width=True)


# Add disclaimer
if calculate_button_ticked == True:
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.warning('Health data can be inaccurate. Consider checking important information.')

if button_ticked == True:
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.warning('Health data can be inaccurate. Consider checking important information.')

# End of Code
