import streamlit as st

# Set page title
st.title("Simple Resume Builder")

# Personal Information
st.header("Personal Information")
name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone")
address = st.text_input("Address")

# Professional Summary
st.header("Professional Summary")
summary = st.text_area("Write a brief summary about yourself")

# Work Experience
st.header("Work Experience")
exp_count = st.number_input("Number of experiences", min_value=1, max_value=3, value=1)

experiences = []
for i in range(exp_count):
    st.subheader(f"Experience {i+1}")
    company = st.text_input(f"Company Name {i+1}")
    position = st.text_input(f"Position {i+1}")
    duration = st.text_input(f"Duration {i+1} (e.g., Jan 2020 - Present)")
    duties = st.text_area(f"Job Duties {i+1}")
    
    experiences.append({
        "company": company,
        "position": position,
        "duration": duration,
        "duties": duties
    })

# Education
st.header("Education")
education = st.text_area("Education Details (e.g., Bachelor's in Computer Science - XYZ University, 2020)")

# Skills
st.header("Skills")
skills = st.text_area("List your key skills")

# Generate Resume
if st.button("Generate Resume"):
    st.markdown("---")
    st.header("Your Resume")
    
    # Display Personal Information
    st.markdown(f"# {name}")
    st.markdown(f"Email: {email}  \nPhone: {phone}  \nAddress: {address}")
    
    # Display Professional Summary
    st.markdown("## Professional Summary")
    st.write(summary)
    
    # Display Work Experience
    st.markdown("## Work Experience")
    for exp in experiences:
        st.markdown(f"### {exp['position']} at {exp['company']}")
        st.markdown(f"*{exp['duration']}*")
        st.write(exp['duties'])
    
    # Display Education
    st.markdown("## Education")
    st.write(education)
    
    # Display Skills
    st.markdown("## Skills")
    st.write(skills)

# Instructions
st.sidebar.title("Instructions")
st.sidebar.write("""
1. Fill in your personal details
2. Write a professional summary
3. Add your work experience
4. Include your education
5. List your skills
6. Click 'Generate Resume' to see your resume
""")