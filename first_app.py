import streamlit as st
import math

st.title("A-Level Study Tools (Physics & Chem)")
st.header("1. Projectile Motion Calc")

v_init = st.number_input("Enter Initial Velocity (u) in m/s", value=15.0)
launch_angle = st.slider("Angle in degrees", 0, 90, 45)

g = 9.81 
theta = math.radians(launch_angle)

vel = v_init ** 2
sin2theta = math.sin(2 * theta)


horizontal_range = (vel * sin2theta) / g

st.info(f"The calculated horizontal range is: {round(horizontal_range, 2)} meters")
st.markdown("---")


st.header("2. Molarity / Concentration Solver")

moles_n = st.number_input("Number of Moles (n)", value=0.5)
volume_v = st.number_input("Volume of Solution (Litre)", value=1.0)

if volume_v > 0:
    conc = moles_n / volume_v
    st.success(f"Concentration (C) = {round(conc, 4)} mol/dm^3")
else:
    st.error("Volume cannot be zero!")