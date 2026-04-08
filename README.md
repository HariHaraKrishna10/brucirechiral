# Artemether Chiral Center Analyzer
# Brucine Chiral Compound Analyzer (Python Streamlit)

A public educational website that visualizes a simplified 3D stereocenter model for **artemether** and lets learners switch between **R** and **S** configuration.
This version is designed to run without server bind errors on Streamlit-like platforms.

## Features
## Includes
- Brucine details
- Chiral center count
- R/S configuration
- Student details
- 2D structure view (XY scatter)
- 3D structure data view (XYZ coordinates)

- Interactive 3D viewer (rotate + zoom)
- Toggle between R and S configuration
- Visualized substituent priorities (CIP-style learning aid)
- Short explanation of how R/S assignment is determined
## Student details
- Name: Nalla Hari Hara Krishna
- Reg No: RA2511026050036
- Dept: CSE-AIML
- SEC: A

## Run locally

Because this project uses JavaScript modules, run it with a local static server.
## Run

```bash
python3 -m http.server 8000
pip install -r requirements.txt
streamlit run app.py
```

Then open: <http://localhost:8000>
## GitHub

```bash
git add .
git commit -m "Fix deployment errors with Streamlit app"
git push
```
