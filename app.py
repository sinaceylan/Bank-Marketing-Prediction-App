import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestRegressor

model = pickle.load(open('best_model.pkl', 'rb'))

def predict(model, input_df):
    predictions_df = model.predict(input_df)
    predictions = predictions_df[0]
    return predictions

def main():

    st.title('Bank Marketing Prediction App')
    st.write('Please input the data for prediction:')

    age = st.number_input('Age', min_value=0, max_value=100, step=1)
    job = st.selectbox('Select Job', options=["blue-collar", "services", "admin.", "entrepreneur", "self-employed", "technician", "management", "student", "retired", "housemaid", "unemployed"])
    marital = st.selectbox('Select Marital Status', options=["married", "single", "divorced"])
    education = st.selectbox('Select Education', options=["basic.9y", "high.school", "university.degree", "professional.course", "basic.6y", "basic.4y", "illiterate"])
    default = st.selectbox('Select Has Credit in Default?', options=["no", "yes"])
    housing = st.selectbox('Select Has Housing Loan?', options=["no", "yes"])
    loan = st.selectbox('Select Has Personal Loan?', options=["no", "yes"])
    contact = st.selectbox('Select Contact Communication Type', options=["cellular", "telephone"])
    month = st.selectbox('Select Last Contact Month', options=["may", "jun", "nov", "sep", "jul", "aug", "mar", "oct", "apr", "dec"])
    day_of_week = st.selectbox('Select Last Contact Day of the Week', options=["mon", "tue", "wed", "thu", "fri"])
    duration = st.number_input('Enter Last Contact Duration')
    campaign = st.number_input('Enter Number of Contacts Performed')
    pdays = st.number_input('Enter Number of Days Passed After Last Contact')
    previous = st.number_input('Enter Number of Contacts Performed Before this Campaign')
    poutcome = st.selectbox('Select Outcome of Previous Marketing Campaign', options=["nonexistent", "failure", "success"])
    emp_var_rate = st.number_input('Enter Employment Variation Rate')
    cons_price_idx = st.number_input('Enter Consumer Price Index')
    cons_conf_idx = st.number_input('Enter Consumer Confidence Index')
    euribor3m = st.number_input('Enter Euribor 3 Month Rate')
    nr_employed = st.number_input('Enter Number of Employees')

    user_data = {
        'age': age,
        'job': job,
        'marital': marital,
        'education': education,
        'default': default,
        'housing': housing,
        'loan': loan,
        'contact': contact,
        'month': month,
        'day_of_week': day_of_week,
        'duration': duration,
        'campaign': campaign,
        'pdays': pdays,
        'previous': previous,
        'poutcome': poutcome,
        'emp.var.rate': emp_var_rate,
        'cons.price.idx': cons_price_idx,
        'cons.conf.idx': cons_conf_idx,
        'euribor3m': euribor3m,
        'nr.employed': nr_employed
    }

    features = pd.DataFrame(user_data, index=[0])

    if st.button("Predict"):
        prediction = predict(model, features)

        if prediction == 0:
            prediction = "No"
        else:
            prediction = "Yes"

        st.success(f'Prediction : {prediction}')

if __name__ == "__main__":
    main()
