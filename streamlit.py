import streamlit as st

creditUnit = []
weighted_gp = []

st.markdown("""
<style>
.css-czk5ss.e16jpq800
{
        visibility:hidden;
}
.css-h5rgaw.ea3mdgi1{
        visibility:hidden;     
}
</style>
""", unsafe_allow_html=True)

count = 0
default = 1

def calculateGpa():
    global count  
    gradingSystem = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1, 'F': 0}
    courses = st.number_input("Enter total number of courses taken: ", key=f"courses_{count}" , min_value=1, value=1)
    
    for i in range(courses):
        count += 1  
        value = st.text_input(f'Enter Grade of course {i+1}:', key=f"value_{count}_{i + 1}").upper()
        if value and not value.isalpha():
            st.warning("Enter valid character")
            
        sc = gradingSystem.get(value, -1)  
        
        if sc == 0:
            st.write('Invalid grade given')
            break
        
        credit = st.number_input(f'Enter credit unit of course {i+1}:', key=f"credit_{count}_{i + 1}" , min_value=1, value=1)
        creditUnit.append(credit)
        weighted_gp.append(sc * credit)

        if creditUnit == 0:
            return "N/A" 
    
    total_weighted_gp = sum(weighted_gp)
    total_credit_units = sum(creditUnit)
    
    return (total_weighted_gp / total_credit_units)

def calculateCgpa():
    global count  
    sem = st.number_input("How many semesters have you done?: ", key=f"sem_{count}" , min_value=1, value=1)
    
    if not isinstance(sem, int):
        st.write('Invalid input for the number of semesters.')
        return
    
    cgpa_calc = []
    
    for j in range(sem):
        st.write("Information for semester {}".format(j + 1))
        cgpa = calculateGpa()
        cgpa_calc.append(cgpa)
    
    return sum(cgpa_calc) / sem 

st.title('Welcome to our CGPA and GPA calculator\n')    
choice = st.number_input('Enter 1 for GPA and 2 for CGPA calculator: ' , min_value=1, max_value=2, value=1)
if choice == 1:
    count += 1  
    st.write(f'Your current GP is:  {calculateGpa() :.2f}')
elif choice == 2:
    count += 1  
    st.write(f'Your current CGPA is:   {calculateCgpa() :.2f}')
else:
    st.write('Invalid Input given') 
