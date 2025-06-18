import streamlit as st
from quadrado import Quadrado

class QuadradoUI2:
    def main():
        st.title("Cálculo com quadrado")
        a = st.text_input("Informe a base/altura do quadrado \n")
        st.button("Calcular")

        try:
            q = Quadrado(float(a))
            st.write(q)
            st.write(f"Área: {q.calc_area():.2f}")
        except ValueError:
            st.warning("Digite um valor antes de calcular.")
            return

        