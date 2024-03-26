import streamlit as st

st.title("Hi, I am Joel")
# Title of the profile page
st.title('Joel Zhu')

# Add a profile picture
# st.image('path_to_image.jpg', width=150)

# Contact Information
st.subheader('Contact Information')
st.write('Phone: 425-652-3015')
st.write('Email: zhu1998@uw.edu')
st.write('Portfolio: https://maifile.cn/est')

# Work Experience
st.header('Work Experience')

# Experience 1
st.subheader('UX Design Intern | OKKI')
st.write('07/2023 – 09/2025')
st.write('''
- Designed and launched 5+ product features used by 1000+ users daily.
- Surveyed 50+ users and created wireframes.
- Collaborated with product managers and developers on an AI-SaaS product.
''')

# Experience 2
st.subheader('UX Designer | Uxpie')
st.write('04/2023 – 07/2025')
st.write('''
- Managed the redesign of the order feature for DrayEasy, improving usability.
- Discovered improvements by conducting competitive analysis and user interviews.
- Organized interviews with 11 users to develop core insights for redesign.
''')

# Education
st.header('Education')

# Education 1
st.subheader('University of Washington')
st.write('M.S. Technology Innovation')
st.write('Sep 2023 - Mar 2025, Seattle')

# Education 2
st.subheader('Chongqing University')
st.write('B. Architecture')
st.write('Sep 2016 - Mar 2021, China')

# Interests and Skills
st.header('Interests and Skills')
st.write('''
- Design: Figma, Adobe Photoshop, Adobe Illustrator, 3D Modelling Software
- Programming: Python
- Research: Usability Testing, Competitive Analysis, A/B Testing
''')

