import streamlit as st
from quadrado import Quadrado

class QuadradoUI:
    def main():
        st.header("Cálculo da área do Quadrado")
        a = st.text_input("Informe a base/Altura")
        if st.button("Calcular"):
            q = Quadrado(float(a))
            st.write(q)
            st.write(f"Área = {q.calc_area()}")

            
        