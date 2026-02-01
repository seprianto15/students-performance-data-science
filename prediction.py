import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('rdf_model.pkl')

# Ambil nama fitur dari model
features = model.feature_names_in_

# Judul dan deskripsi dashboard
st.title('🧑‍🏫 Student Performance Dashboard')

# Set four columns for input
col1, col2, col3, col4 = st.columns(4)

inputs = {}

with col1:
    inputs["Previous_qualification_grade"] = st.number_input("Previous Qualification Grade", min_value=0.0, value=None)
    inputs["Admission_grade"] = st.number_input("Admission Grade", min_value=0.0, value=None)
    inputs["Tuition_fees_up_to_date"] = st.number_input("Tuition Fees Paid Up-to-date", min_value=0, value=None)

with col2:
    inputs["Curricular_units_1st_sem_evaluations"] = st.number_input("Curricular Units Evaluations (1st Sem)", min_value=0, value=None)
    inputs["Curricular_units_1st_sem_approved"] = st.number_input("Curricular Units Approved (1st Sem)", min_value=0.0, value=None)
    inputs["Curricular_units_1st_sem_grade"] = st.number_input("Curricular Units Grade (1st Sem)", min_value=0.0, value=None)

with col3:
    inputs["Curricular_units_2nd_sem_evaluations"] = st.number_input("Curricular Units Evaluations (2nd Sem)", min_value=0, value=None)
    inputs["Curricular_units_2nd_sem_approved"] = st.number_input("Curricular Units Approved (2nd Sem)", min_value=0, value=None)
    inputs["Curricular_units_2nd_sem_grade"] = st.number_input("Curricular Units Grade (2nd Sem)", min_value=0.0, value=None)

with col4:
    inputs["Unemployment_rate"] = st.number_input("Unemployment Rate (%)", min_value=0.0, value=None)
    inputs["GDP"] = st.number_input("GDP Rate (%)", min_value=0.0, value=None)
    

# --- Tombol Prediksi ---

if st.button("Check Student Status"):
    
    # Check for empty inputs
    if None in inputs.values():
        st.error("Please fill in all the required fields!")
    else:
        # Create DataFrame with column order matching the model's features
        input_df = pd.DataFrame([inputs])[features]
 
    # Execution of prediction
    try:
        # Get the class prediction (directly as a string)
        res = model.predict(input_df)[0]

        # Get probabilities for all classes
        prob = model.predict_proba(input_df)[0]
        
        # Create status label
        status_labels = {0: "Dropout", 1: "Enrolled", 2: "Graduate"}
        res_text = status_labels.get(res, "Unknown")
        
        # Menghitung probability rate status
        probability = prob[res]
        
        st.divider()
        
        # Matching the string result
        if res == 0:
            st.error(f"### ⚠️ STATUS : {res_text.upper()}")
        elif res == 1:
            st.info(f"### 📖 STATUS : {res_text.upper()}")
        else:
            st.success(f"### 🎓 STATUS : {res_text.upper()}")
        
        st.write(f"Probabilitas : **{probability:.2%}**")
    
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")