from pathlib import Path

import streamlit as st
from PIL import Image


current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd() #current working directory
css_file = current_dir/"styles"/"main.css"
resume_file = current_dir/"assets"/"Resume.pdf"
profile_pic = current_dir/"assets"/"Prof pic.png"
# _____GENERAL SETTINGS_____

PAGE_TITLE = "Digital CV | Nischal Maharjan"
PAGE_ICON =":wave:"
NAME = "Nischal Maharjan"
DESCRIPTION="""
Data Scientist, an aspiring python developer.
"""
EMAIL = "nischal.maharjan1233@gmail.com"
SOCIAL_MEDIA ={

"LinkedIn":
          "https://www.linkedin.com/in/nischal-maharjan-639284228/",
"GitHub":
        "https://github.com/nisch-mhrzn",

}
PROJECTS ={

"":""
}

st.set_page_config(page_title=PAGE_TITLE,page_icon=PAGE_ICON)


#---- LOAD CSS, PDF AND PROF PIC
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)

with open(resume_file,'rb') as pdf_file:
    PDFbyte = pdf_file.read()
    profile_pic = Image.open(profile_pic)

#----- HERO SECTION
col1 ,col2 = st.columns(2,gap='small')
with col1:
    st.image(profile_pic,width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write('📧',EMAIL)



#-----SOCIAL SETTINGS---
st.write("#")
cols =st.columns(len(SOCIAL_MEDIA))
for index , (platform,link)in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


#---EXPERIENCE AND QUALIFICATIONS
st.write('#')
st.subheader('Experience and Qualifications')
st.write("""
- 1.5 years experience on building python projects
- 1 years experience on building web applications
- Good understanding of Machine Learning and Deep Learning
- Excellent team-player and determined
""")

#---SKILLS---
st.write('#')
st.subheader('Hard skills')
st.write("""
- 📚 Programming : Python(Tensorflow,Keras,Numpy),C,C++,Javascript,CSS,HTML
- 🫙 Databases: MySQL

""")



