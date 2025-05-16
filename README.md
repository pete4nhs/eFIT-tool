# eFIT-tool
extra funding allocation calculator for primary care in England

The problem:
While core funding for NHS primary care in England is well regulated (by using a variant of the Carr-Hill formula), there is no national guidance/methodology to allocate extra funding for primary care by Integrated Care Boards (ICBs) - the old CCGs that commisioned services. Every ICB has many programme directors/project managers for the various disease areas who can split the money at their own discretion who might not take into consideration available data and might just split the money equally (by population size) - effectively widen inequalities even further.
I propose to use an equation from the Inequality Strategy for Cambridgeshire and Peterborough (by Dr John Ford) which splits the money based on deprivation score and local needs. For example, if a cancer team receives extra funding for FIT screening, I calculate the allocation of extra funding to GP practices based on bowel cancer screening uptake data and give more to those who have low uptake (in a proportional way). Many publicly available health indicators are listed in the tool, so a team focusing on diabetes can use data on diabetes etc. However, even if programme managers were aware of the equation, they might not know how to calculate the allocation and might need analysts to do it for them in Excel.

The solution:
This eFIT tool  is a user-friendly Streamlit web-app where a user would input the amount of funding, select the ICB, specify the demographics (age and gender for intervention) and tweak the indicator and the weights (e.g. to give more based inequality or prevalence of disease etc).  Upon hitting the 'Calculate' button the result is instantaneous and you can download the table with the calculated allocations.
By making this tool available to all ICBs in England, we can establish a general consensus on how ICBs can promptly split extra funding to primary care taking into consideration inequalities and local needs.

The tool can be accessed at this web address: https://efit-tool.streamlit.app/
