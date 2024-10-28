import streamlit as st

# This is to add in a title for our web app's page
st.title('**Tutorial**')
st.write('Please have a look at our video for a short tutorial on how to use the eFIT tool')

video_file = open('pages/video_tutorial.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)

st.write('')
st.write('')
st.write('')
st.write(' **To report any bug, feedback or special requests please email: peter.saiu@nhs.net** ')
st.write('')
st.success('Please let us know if your organisation has used this tool')
