
import streamlit as st

# Sidinställningar
st.set_page_config(page_title="GreenByte AI", layout="centered")

# Titel
st.title("GreenByte AI 🌱")
st.subheader("Beräkna Energi-Informationsindex (EII) för inaktiv data")

# Beskrivning
st.markdown("""
GreenByte EII-verktyget hjälper dig att avgöra om en digital fil är värd att behålla eller bör tas bort.

**EII = Filstorlek (MB) dividerat med antal åtkomster per månad**
""")

# Inmatningar
size = st.number_input("🔢 Filstorlek (MB)", min_value=0.1, step=0.1, value=50.0)
access = st.number_input("📥 Antal åtkomster per månad", min_value=0, step=1, value=5)

# Beräkning
if access == 0:
    eii = size * 10  # Högsta risk
else:
    eii = size / access

# Visa resultat
st.metric(label="📊 EII-värde", value=round(eii, 2))

if eii > 5:
    st.warning("Denna fil är sannolikt resursslösande och bör granskas.")
else:
    st.success("Filen anses vara optimerad och effektiv.")

# Fotnot
st.caption("GreenByte AI © – Utvecklad för gröna datacenter")
