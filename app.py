import streamlit as st

st.set_page_config(page_title="Brucine Chiral Analyzer", layout="wide")

BRUCINE = {
    "name": "Brucine",
    "formula": "C23H26N2O4",
    "chiral_count": 7,
    "rs": [
        {"center": "C1", "config": "S"},
        {"center": "C5", "config": "R"},
        {"center": "C6", "config": "S"},
        {"center": "C7", "config": "S"},
        {"center": "C9", "config": "R"},
        {"center": "C10", "config": "R"},
        {"center": "C11", "config": "S"},
    ],
}

STUDENT = {
    "Name": "Nalla Hari Hara Krishna",
    "Reg No": "RA2511026050036",
    "Dept": "CSE-AIML",
    "SEC": "A",
}

ATOMS = [
    {"atom": "C1", "x": 0.0, "y": 0.0, "z": 0.0},
    {"atom": "C5", "x": 1.4, "y": 0.8, "z": 0.5},
    {"atom": "C6", "x": -1.2, "y": 1.0, "z": 0.3},
    {"atom": "C7", "x": 0.4, "y": -1.3, "z": 1.0},
    {"atom": "C9", "x": 2.2, "y": 1.2, "z": 0.9},
    {"atom": "C10", "x": -2.0, "y": 1.7, "z": 0.7},
    {"atom": "C11", "x": 1.1, "y": -2.1, "z": 1.8},
    {"atom": "O", "x": 0.2, "y": 0.2, "z": -1.6},
    {"atom": "N1", "x": -0.9, "y": 2.0, "z": -0.2},
    {"atom": "N2", "x": 0.5, "y": -2.4, "z": 0.1},
]

st.title("Brucine Chiral Compound Analyzer")
st.caption("Python Streamlit app (no custom HTML/CSS files)")

left, right = st.columns(2)

with left:
    st.subheader("Compound Details")
    st.write(f"**Name:** {BRUCINE['name']}")
    st.write(f"**Molecular Formula:** {BRUCINE['formula']}")
    st.write(f"**Number of Chiral Centers:** {BRUCINE['chiral_count']}")

    st.subheader("R/S Configuration")
    st.table(BRUCINE["rs"])

with right:
    st.subheader("Student Details")
    st.table([{"Field": k, "Value": v} for k, v in STUDENT.items()])

st.subheader("2D Structure (X-Y projection)")
xy_data = [{"Atom": a["atom"], "X": a["x"], "Y": a["y"]} for a in ATOMS]
st.scatter_chart(xy_data, x="X", y="Y", color=None, size=None)
st.dataframe(xy_data, use_container_width=True)

st.subheader("3D Structure (X-Y-Z coordinates)")
st.write("Use the table below as the 3D coordinate model for Brucine atoms.")
st.dataframe(ATOMS, use_container_width=True)

st.info("Run with: streamlit run app.py")
