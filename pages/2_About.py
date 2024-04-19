import streamlit as st

# This is to add in a title for our web app's page
st.title('FAQs')
st.write('**Q:** What and who is this tool for?')
st.write('**A:** This tool is a calculator for ICB directors/managers ICB financial teams in England who receive **extra funding** '
         'for GP practices and wish to split the money based on **inequalities** and/or **local data**. ')
st.write('')
st.write('')
st.write('')
st.write("**Q:** Is there a way to calculate the allocation just based on reigistered population size (rather than weighted population)?")
st.write("**A:** Yes! If from the sidebar, you leave all the indicators boxes unselected (reading _'Choose an option'_), the allocation will be calculated solely based on the population size selected from the demographics section")
st.write('')
st.write('')
st.write('')
st.write("**Q:** When I try to upload my data from excel it gives the error 'UnicodeDecodeError: This app has encountered an error ...'")
st.write("**A:** You can only upload files in a '.csv' format. Hence, with your file open with excel, re-save the document in .csv (save as :arrow_right: format: 'csv')")
st.write('')
st.write('')
st.write('')
st.write("**Q:** What is the difference beween using this tool or just using a weighted population formula?")
st.write("**A:** Without specific instructions on how you want to split the funding, or depending on capacity of the financial team, monies might just be split using a weighted population formula. "
         "However, with this tool, you can tailor the alloction based on your local needs by selecting the demographics and local needs specific for your intervention. "
         "You can view the difference between using this eFIT tool and using a weighted population formula, by clicking the 'Show more detail' box and the expander at the bottom of the webpage.")


st.write('')
st.title('Methodology')
st.write('For each indicator we have applied the following formula:')
# ADD equation (for 'single' indicator')
st.image('single_equation.png', width=200)
st.write('Hence, given that you can assign different weights to each indicator, the resulting equation is the following:')
# ADD equation (for all indicators')
st.image('longer_equation.png', width=300)
st.write('where:')
st.image('where.png', width=500)

st.write('')
st.title('Data sources')
# Messages
st.write('Indicators data **for 2022/23**, including IMD scores (2019)* and prevalence (QOF) data, was extracted on 26/3/2024 from fingertips ( https://fingertips.phe.org.uk/ ).')
st.write('*Where new GP practices opened or merged/demerged (e.g. Cambridgeshire and Peterborough ICB and Nottingham and Nottinghamshire ICB), '
         'we have calculated their new IMD.')

st.write('Weighted population data is for 2024/25 and was extracted from: J-Overall weighted populations by ICB and GP practice 2023/24 to 2024/25 at NHS England >> Supporting spreadsheets for allocations 2023/24 to 2024/25'
         'available at: https://www.england.nhs.uk/publication/supporting-spreadsheets-for-allocations-2023-24-to-2024-25/ ')
st.write('GP practices population size data is as of March 2024 and were extracted from NHS Digital at: https://digital.nhs.uk/data-and-information/publications/statistical/patients-registered-at-a-gp-practice')



st.write('')
st.write('')
st.write('')
st.write(' **To report any bug, feedback or special requests please email: peter.saiu@nhs.net** ')