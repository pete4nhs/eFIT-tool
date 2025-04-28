import streamlit as st

# This is to add in a title for our web app's page

st.title('Methodology')
st.write('For each indicator we have applied the following formula:')
# ADD equation (for 'single' indicator')
st.image('pages/single_equation.png', width=200)
st.write('')
st.write('For indicators where a lower indicator value results in more funding, the equation has been _reversed_. ')
st.write('')
st.write('Given that you can assign different weights to each indicator, the resulting equation is the following:')
# ADD equation (for all indicators')
st.image('pages/longer_equation.png', width=300)
st.write('where:')
st.image('pages/where.png', width=500)
st.write('')
st.warning('To be noted that some health data might be missing, hence we suggest to always double check your results.')

st.write('')
st.title('Data sources')
# Messages
st.write('Indicators data **for 2023/24**, including IMD scores (2019)* and prevalence (QOF) data, was extracted on 22/3/2025 from fingertips ( https://fingertips.phe.org.uk/ ).')
st.write('*For some ICBs, where new General Practices opened or merged/demerged (e.g. Cambridgeshire and Peterborough ICB and Nottingham and Nottinghamshire ICB), '
         'we have calculated their new IMD.')

st.write('Weighted population data is for 2024/25 and was extracted from: J–overall weighted populations by integrated care board and GP practice 2025 to 2026 '
         'at NHS England >> Supporting spreadsheets for 2025/26 allocations'
         'available at: https://www.england.nhs.uk/publication/supporting-spreadsheets-for-2025-26-allocations/ ')
st.write('General Practices population size data is as of March 2025 and was extracted from NHS Digital at: https://digital.nhs.uk/data-and-information/publications/statistical/patients-registered-at-a-gp-practice')
st.write()
st.write('**Version Control**')
st.write('This new data was added into the tool on 31/3/2025')



st.write('')
st.write('')
st.title('FAQs')
st.write('**Q:** What and who is this tool for?')
st.write('**A:** This tool is a calculator for ICB directors/managers ICB financial teams in England who receive **extra funding** '
         'for General Practices and wish to split the money based on **inequalities** and/or **local data**. ')
st.write('')
st.write('')
st.write('')
st.write('**Q:** Why do we need this tool?')
st.write('**A:** The allocation of general practice funding is well established nationally (with the variant of the Carr-Hill formula), '
         'but there is currently no national guidance on how to allocate discretionary additional funds in an equitable manner. '
         'Often ICBs resort to allocating funding per head of population, rather than considering inequalities and population need.'
         'This user‑friendly tool (eFIT) allows ICB managers to easily calculate various scenarios of how to split '
         'this funding by taking into consideration the health data associated with the intervention they are aiming to roll out. ')
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
st.write('')

st.write('**Acknowledgments**: We thank the Health Service Modelling Associates (HSMA) (https://sites.google.com/nihr.ac.uk/hsma/home ), Dr John Ford and Dr Stefano Conti from the Health Foundation.')
st.write('')
st.write('')
st.write(' **To report any bug, feedback or special requests please email: peter.saiu@nhs.net** ')
st.write('')
st.success('Please let us know if your organisation has used this tool')
