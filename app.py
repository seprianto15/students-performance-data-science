import streamlit as st
import pandas as pd
import joblib
import os

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Student Performance",
    page_icon="🎓",
    layout="wide"
)

# --- 2. CREATE CSS CUSTOM  ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
    }
    .stNumberInput, .stSelectbox {
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. LOAD MODEL ---
@st.cache_resource
def load_model():
    # Gunakan path yang aman
    base_path = os.path.dirname(__file__)
    model_path = os.path.join(base_path, 'model', 'rdf_model.pkl')
    
    # Memuat model asli
    loaded_model = joblib.load(model_path)
    return loaded_model

model = load_model()
# Use feature from model
features = model.feature_names_in_

# --- 4. CREATE SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135810.png", width=200)
    st.title("About Project")
    st.info("""
    Dashboard ini menggunakan model **Random Forest** untuk memprediksi status akademik mahasiswa berdasarkan faktor ekonomi dan performa akademik.
    """)
    st.divider()
    st.caption("Copyright (c) Sianipar 2026")

# --- 5. HEADER DASHBOARD ---
st.title('Student Performance Analytics')
st.markdown("---")

# --- 6. INPUT DATA (Menggunakan Container & Tabs) ---
st.subheader("📝 Input Data")
with st.container():
    col1, col2, col3, col4 = st.columns(4)
    inputs = {}

    with col1:
        inputs["Previous_qualification_grade"] = st.number_input("Previous Qualification Grade", min_value=0.0, value=None)
        inputs["Admission_grade"] = st.number_input("Admission Grade", min_value=0.0, value=None)
        inputs["Tuition_fees_up_to_date"] = st.number_input("Tuition Fees Paid Up-to-date", min_value=0, value=None)

    with col2:
        inputs["Curricular_units_1st_sem_evaluations"] = st.number_input("Curricular Units Evaluations (1st Sem)", 
                                                                         min_value=0, 
                                                                         value=None)
        inputs["Curricular_units_1st_sem_approved"] = st.number_input("Curricular Units Approved (1st Sem)", 
                                                                      min_value=0.0, 
                                                                      value=None)
        inputs["Curricular_units_1st_sem_grade"] = st.number_input("Curricular Units Grade (1st Sem)", min_value=0.0, value=None)

    with col3:
        inputs["Curricular_units_2nd_sem_evaluations"] = st.number_input("Curricular Units Evaluations (2nd Sem)", 
                                                                         min_value=0, 
                                                                         value=None)
        inputs["Curricular_units_2nd_sem_approved"] = st.number_input("Curricular Units Approved (2nd Sem)", 
                                                                      min_value=0, 
                                                                      value=None)
        inputs["Curricular_units_2nd_sem_grade"] = st.number_input("Curricular Units Grade (2nd Sem)", min_value=0.0, value=None)

    with col4:
        inputs["Unemployment_rate"] = st.number_input("Unemployment Rate (%)", min_value=0.0, value=None)
        inputs["GDP"] = st.number_input("GDP Rate (%)", min_value=0.0, value=None)

# --- 7. TOMBOL PREDIKSI ---
st.markdown("<br>", unsafe_allow_html=True)
if st.button("🚀 CHECK STUDENT STATUS"):
    
    # Check for empty inputs
    if None in inputs.values():
        st.error("Please fill in all the required fields!")
    else:
        # Create DataFrame with column order matching the model's features
        input_df = pd.DataFrame([inputs])[features]

        try:
            # Get the class prediction
            res = model.predict(input_df)[0]
            # Get probabilities for all classes
            prob = model.predict_proba(input_df)[0]
        
            # Create status label
            status_labels = {0: "Dropout", 1: "Enrolled", 2: "Graduate"}
            res_text = status_labels.get(res, "Unknown")
            # Probability rate status
            probability = prob[res]

            st.divider()
            
            # --- 8. TAMPILAN HASIL (Menggunakan Card & Metric) ---
            st.subheader("🎯 Hasil Prediksi")
        
            # Matching the string result
            if res == 0:
                st.error(f"### ⚠️ STATUS : {res_text.upper()}")
            elif res == 1:
                st.info(f"### 📖 STATUS : {res_text.upper()}")
            else:
                st.success(f"### 🎓 STATUS : {res_text.upper()}")
        
            st.write(f"Probabilitas : **{probability:.2%}**")
    
            # Detail Probabilitas dengan Bar Chart
            with st.expander("Lihat Detail Probabilitas"):
                prob_df = pd.DataFrame({
                    'Status': status_labels.values(),
                    'Probability': prob
                })
                st.bar_chart(data=prob_df, x='Status', y='Probability')

        except Exception as e:
            st.error(f"Terjadi kesalahan saat prediksi: {e}")