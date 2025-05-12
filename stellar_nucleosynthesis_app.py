
import streamlit as st
import matplotlib.pyplot as plt

# Function to calculate likelihood of stellar end-states based on solar mass
def calculate_end_states(solar_mass):
    if solar_mass < 8:
        return {'White Dwarf': 80, 'Neutron Star': 10, 'Supernova': 5, 'Black Hole': 5}
    elif solar_mass < 20:
        return {'White Dwarf': 10, 'Neutron Star': 40, 'Supernova': 40, 'Black Hole': 10}
    else:
        return {'White Dwarf': 5, 'Neutron Star': 10, 'Supernova': 35, 'Black Hole': 50}

# Streamlit app
st.title("Stellar Nucleosynthesis Simulator")

# Sliders for r-process and p-process
r_process = st.slider("r-process Contribution", 0, 100, 50)
p_process = st.slider("p-process Contribution", 0, 100, 50)

# Slider for solar mass
solar_mass = st.slider("Solar Mass", 0.1, 50.0, 1.0)

# Calculate end states likelihood
end_states = calculate_end_states(solar_mass)

# Display pie chart of end states likelihood
fig, ax = plt.subplots()
ax.pie(end_states.values(), labels=end_states.keys(), autopct='%1.1f%%')
ax.axis('equal')
st.pyplot(fig)

# Display information about stellar nucleosynthesis
st.write("""
### Stellar Nucleosynthesis Process
- **r-process**: Rapid neutron capture process.
- **p-process**: Proton capture process.
- **Solar Mass**: Mass of the star relative to the Sun.

### Likelihood of Stellar End-States
- **White Dwarf**: Low mass stars (< 8 solar masses).
- **Neutron Star**: Intermediate mass stars (8–20 solar masses).
- **Supernova**: Intermediate to high mass stars.
- **Black Hole**: High mass stars (> 20 solar masses).
""")
