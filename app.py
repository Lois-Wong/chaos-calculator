import streamlit as st
from data import drinks, stages
from calc import calc_bac, calc_chaos_score

st.title("Chaos Calculator")

weight = st.number_input("Weight (lbs)", min_value=80, max_value=300, value=110)
sex = st.selectbox("Sex", ["Female", "Male"])

st.subheader("Drinks")
selections = {}
for drink in drinks:
    selections[drink["name"]] = st.number_input(drink["name"], min_value=0, max_value=20, value=0, key=drink["name"])

if st.button("Calculate my chaos"):
    total_alcohol_grams = sum(
        drink["alcohol_grams"] * selections[drink["name"]]
        for drink in drinks
    )
    bac = calc_bac(total_alcohol_grams, weight, sex)
    score = calc_chaos_score(bac, 0, 0)
    st.write(f"BAC: {bac:.3f}")
    st.write(f"Chaos score: {score}")
    st.write(stages[score]['description'])
