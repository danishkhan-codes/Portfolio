# Mohammed Danish Khan - Premium Streamlit Portfolio

A premium, recruiter-ready, completely responsive web portfolio built using Python and Streamlit. Features glassmorphism, animated elements (typing, timeline, metrics), dark/light mode toggles, and direct PDF resume rendering.

## 🚀 Features

- **Theme Toggler**: Dynamically toggle between dark and light themes (glassmorphic styling adapts automatically).
- **Home (Hero) Section**: Smooth Typing animation Carousel with Typed.js, custom-styled avatar container with pulsating glow, and recruiter impact metrics.
- **Interactive Projects Page**: Search project names/keywords, filter by technology badges, and view interactive comparison plots (Plotly).
- **Experience & Education Timeline**: Clean vertical scroll timelines custom-coded using raw HTML/CSS nodes inside Streamlit.
- **Embedded Resume Viewer**: Direct inline rendering of the resume PDF on the webpage with real-time download tracking analytics.
- **Contact Form**: Secure validation, feedback state, and Toast alert triggers.

## 📁 Folder Structure

```
danish_portfolio/
├── app.py                  # Main page layouts and sidebar routing
├── styles.py               # Theme stylesheets (dynamic dark/light layouts)
├── requirements.txt        # PIP dependencies
├── README.md               # Setup and guides
├── data/
│   ├── portfolio_data.py   # Portfolio copy, lists, and metadata structures
│   └── analytics.json      # Persistent local visitor & download counter
├── utils/
│   ├── ui_helpers.py       # Helper tools for rendering timeline, skills, and stats
│   ├── analytics.py        # Controller for reading/writing analytics counter
│   └── generate_placeholders.py  # Script for generating sample assets (run once)
└── assets/
    ├── profile.jpg         # Profile picture
    ├── resume.pdf          # Professional Resume PDF
    ├── certificates/       # Certificates directory
    └── project_images/     # Project thumbnails directory
```

## 🛠️ Local Setup

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Generate Placeholders (Optional)**
   If placeholders aren't created automatically, run the helper utility:
   ```bash
   python utils/generate_placeholders.py
   ```

3. **Run Application**
   ```bash
   streamlit run app.py
   ```

4. Open your browser and navigate to `http://localhost:8501`.
