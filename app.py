# app.py — Premium Data Scientist Portfolio
import streamlit as st

# ── Page Config ──────────────────────────────────────────
st.set_page_config(
    page_title="Mohammed Danish Khan — Data Scientist",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── Imports ──────────────────────────────────────────────
from data.portfolio_data import PERSONAL_INFO, STATS, ABOUT_ME, SKILLS, PROJECTS, EXPERIENCE, EDUCATION
from styles import get_css
from utils.ui_helpers import (
    st_html, render_hero, render_stat_card,
    render_section_header, render_skill_card, render_skill_category,
    render_project_card, render_timeline_item,
    render_scroll_to_top, render_footer
)

# ── Apply Premium CSS ────────────────────────────────────
st.markdown(get_css(), unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════
#  SECTION 1 — HERO
# ═══════════════════════════════════════════════════════════
render_hero(
    name=PERSONAL_INFO["name"],
    location=PERSONAL_INFO["location"],
    email=PERSONAL_INFO["email"],
    phone=PERSONAL_INFO["phone"],
    github=PERSONAL_INFO["github"],
    linkedin=PERSONAL_INFO["linkedin"]
)

# ── Stats Row ────────────────────────────────────────────
stat_cols = st.columns(4, gap="medium")
for i, stat in enumerate(STATS):
    with stat_cols[i]:
        render_stat_card(stat["value"], stat["label"], stat["icon"])

st_html("<hr class='section-divider'>")

# ═══════════════════════════════════════════════════════════
#  SECTION 2 — ABOUT (Education + Competencies)
# ═══════════════════════════════════════════════════════════
render_section_header("// about", "Academic Foundation & Core Strengths")

col_edu, col_str = st.columns([3, 2], gap="large")

with col_edu:
    edu = EDUCATION[0]
    st_html(f"""
    <div class="glass-card">
        <div style="display:flex; align-items:center; gap:10px; margin-bottom:12px;">
            <span style="font-size:1.6rem;">🎓</span>
            <div>
                <div style="font-family:var(--font-display); font-size:1.1rem; font-weight:700; color:var(--text-primary);">
                    {edu['degree']}
                </div>
                <div style="font-family:var(--font-mono); font-size:0.78rem; color:var(--accent-cyan);">
                    {edu.get('specialization', '')}
                </div>
            </div>
        </div>
        <div style="font-size:0.88rem; color:var(--text-secondary); line-height:1.6;">
            <strong style="color:var(--text-primary);">{edu['institution']}</strong><br>
            CGPA: <strong style="color:var(--accent-cyan);">{edu['cgpa']}</strong>
            &nbsp;·&nbsp; {edu['duration']}
        </div>
    </div>
    """)

with col_str:
    strengths_items = ""
    for s in ABOUT_ME["strengths"]:
        strengths_items += f"""
        <div class="strength-chip">
            <span style="color:var(--accent-cyan); font-size:0.85rem;">✦</span>
            <span style="font-size:0.82rem; font-weight:500; color:var(--text-secondary);">{s}</span>
        </div>
        """
    st_html(f"""
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px;">
        {strengths_items}
    </div>
    """)

st_html("<hr class='section-divider'>")

# ═══════════════════════════════════════════════════════════
#  SECTION 3 — SKILLS
# ═══════════════════════════════════════════════════════════
render_section_header("// skills", "Technical Arsenal")

categories = list(SKILLS.keys())
category_icons = ["💻", "🤖", "📊", "🛠️"]

col_s1, col_s2 = st.columns(2, gap="large")

with col_s1:
    for idx in [0, 2]:
        render_skill_category(category_icons[idx], categories[idx])
        for skill in SKILLS[categories[idx]]:
            render_skill_card(skill["name"], skill["level"], skill["icon"])
        st_html("<div style='height:16px;'></div>")

with col_s2:
    for idx in [1, 3]:
        render_skill_category(category_icons[idx], categories[idx])
        for skill in SKILLS[categories[idx]]:
            render_skill_card(skill["name"], skill["level"], skill["icon"])
        st_html("<div style='height:16px;'></div>")

st_html("<hr class='section-divider'>")

# ═══════════════════════════════════════════════════════════
#  SECTION 4 — PROJECTS
# ═══════════════════════════════════════════════════════════
render_section_header("// projects", "Featured Work")

proj1_col, proj2_col = st.columns(2, gap="large")

# ── Project 1: CricVerse ─────────────────────────────────
with proj1_col:
    render_project_card(
        title=PROJECTS[0]["title"],
        tech_badges=PROJECTS[0]["technologies"],
        desc=PROJECTS[0]["description"],
        features=PROJECTS[0]["features"]
    )

# ── Project 2: Expense Tracker ───────────────────────────
with proj2_col:
    render_project_card(
        title=PROJECTS[1]["title"],
        tech_badges=PROJECTS[1]["technologies"],
        desc=PROJECTS[1]["description"],
        features=PROJECTS[1]["features"]
    )

st_html("<hr class='section-divider'>")

# ═══════════════════════════════════════════════════════════
#  SECTION 5 — JOURNEY (Experience + Education Timeline)
# ═══════════════════════════════════════════════════════════
render_section_header("// journey", "Experience & Education")

# Experience Subheading
st_html("<div style='font-family:var(--font-display); font-size:1.3rem; font-weight:600; color:var(--text-primary); margin-top:10px; margin-bottom:15px;'>💼 Professional Experience</div>")

col_job1, col_job2 = st.columns(2, gap="large")
with col_job1:
    job = EXPERIENCE[0]
    render_timeline_item(
        role=job["role"],
        org=f"{job['organization']} · {job['location']}",
        date=job["duration"],
        bullets=job["responsibilities"],
        skills=job.get("skills")
    )
with col_job2:
    job = EXPERIENCE[1]
    render_timeline_item(
        role=job["role"],
        org=f"{job['organization']} · {job['location']}",
        date=job["duration"],
        bullets=job["responsibilities"],
        skills=job.get("skills")
    )

st_html("<div style='height:25px;'></div>")

# Education Subheading
st_html("<div style='font-family:var(--font-display); font-size:1.3rem; font-weight:600; color:var(--text-primary); margin-bottom:15px;'>🎓 Academic Chronology</div>")

edu_entry = EDUCATION[0]
render_timeline_item(
    role=edu_entry["degree"],
    org=f"{edu_entry.get('specialization', '')} · {edu_entry['institution']}",
    date=edu_entry["duration"],
    bullets=edu_entry["bullets"]
)

st_html("<hr class='section-divider'>")

# ═══════════════════════════════════════════════════════════
#  SECTION 6 — CONTACT
# ═══════════════════════════════════════════════════════════
render_section_header("// contact", "Let's Connect")

col_info, col_form = st.columns([2, 3], gap="large")

with col_info:
    st_html(f"""
    <div class="glass-card">
        <div style="font-family:var(--font-display); font-size:1.3rem; font-weight:700;
                    color:var(--text-primary); margin-bottom:12px;">
            Get in touch
        </div>
        <div style="font-size:0.9rem; color:var(--text-secondary); line-height:1.7; margin-bottom:20px;">
            I'm always open to discussing data science projects,
            collaboration opportunities, or just having an interesting conversation
            about AI and machine learning.
        </div>
        <div style="display:flex; flex-direction:column; gap:12px;">
            <div style="display:flex; align-items:center; gap:10px;">
                <span style="color:var(--accent-cyan);">✉️</span>
                <a href="mailto:{PERSONAL_INFO['email']}" style="color:var(--text-secondary); text-decoration:none; font-size:0.88rem;">
                    {PERSONAL_INFO['email']}
                </a>
            </div>
            <div style="display:flex; align-items:center; gap:10px;">
                <span style="color:var(--accent-cyan);">📞</span>
                <span style="color:var(--text-secondary); font-size:0.88rem;">{PERSONAL_INFO['phone']}</span>
            </div>
            <div style="display:flex; align-items:center; gap:10px;">
                <span style="color:var(--accent-cyan);">📍</span>
                <span style="color:var(--text-secondary); font-size:0.88rem;">{PERSONAL_INFO['location']}</span>
            </div>
        </div>
    </div>
    """)

with col_form:
    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Name", placeholder="Your name")
        email = st.text_input("Email", placeholder="your@email.com")
        message = st.text_area("Message", placeholder="Write your message here...", height=120)
        submit = st.form_submit_button("Send Message →")
        if submit:
            if not name or not email or not message:
                st.error("Please fill in all fields.")
            elif "@" not in email:
                st.error("Please enter a valid email address.")
            else:
                st.success(f"Thanks, {name}! Your message has been sent. I'll get back to you shortly.")
                st.toast("Message sent! 🚀")

# ── Footer ───────────────────────────────────────────────
render_scroll_to_top()
render_footer()
