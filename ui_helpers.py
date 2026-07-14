# utils/ui_helpers.py — Premium UI Components (Fixed for Streamlit)
import streamlit as st

def st_html(html_str):
    """
    Cleans a multiline HTML string by stripping newlines and leading/trailing whitespace
    from each line, preventing Streamlit's Markdown engine from incorrectly parsing
    indented HTML as a code block. Renders the resulting clean HTML.
    """
    cleaned = "".join(line.strip() for line in html_str.split("\n"))
    st.markdown(cleaned, unsafe_allow_html=True)


def render_hero(name, location, email, phone, github, linkedin):
    """Renders the premium animated hero section."""
    st_html(f"""
    <div class="particle-field">
        <div class="hero-container">
            <div class="hero-greeting">👋 Hello, I'm</div>
            <div class="hero-name">{name}</div>
            <div class="hero-tagline">
                Building intelligent systems with data. I transform raw datasets into
                predictive models, interactive dashboards, and actionable insights
                using Python, SQL, and machine learning.
            </div>
            <div class="hero-meta">
                📍 {location} &nbsp;&bull;&nbsp;
                <a href="mailto:{email}">{email}</a> &nbsp;&bull;&nbsp;
                📞 {phone}
            </div>
            <div class="social-row">
                <a href="{github}" target="_blank" class="social-icon" title="GitHub">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
                </a>
                <a href="{linkedin}" target="_blank" class="social-icon" title="LinkedIn">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
                </a>
                <a href="mailto:{email}" class="social-icon" title="Email">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2"></rect><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"></path></svg>
                </a>
            </div>
        </div>
    </div>
    """)


def render_stat_card(val, label, icon):
    """Renders a premium animated stat card."""
    st_html(f"""
    <div class="stat-card">
        <span class="stat-icon">{icon}</span>
        <div class="stat-val">{val}</div>
        <div class="stat-label">{label}</div>
    </div>
    """)


def render_section_header(label, title):
    """Renders a premium section header with monospace label + display title."""
    st_html(f"""
    <span class="section-label">{label}</span>
    <div class="section-title">{title}</div>
    """)


def render_skill_card(name, level, icon):
    """Renders a skill item with animated progress bar."""
    st_html(f"""
    <div class="skill-item">
        <div class="skill-header">
            <span class="skill-name">{icon} {name}</span>
            <span class="skill-percent">{level}%</span>
        </div>
        <div class="progress-track">
            <div class="progress-fill" style="width: {level}%;"></div>
        </div>
    </div>
    """)


def render_skill_category(icon, name):
    """Renders a skill category header."""
    st_html(f"""
    <div class="skill-category">
        <span class="skill-category-icon">{icon}</span>
        <span class="skill-category-name">{name}</span>
    </div>
    """)


def render_project_card(title, tech_badges, desc, features):
    """Renders a premium project card with hover effects."""
    badges_html = "".join([f'<span class="tech-badge">{t}</span>' for t in tech_badges])
    features_html = "".join([f'<li>{f}</li>' for f in features])
    st_html(f"""
    <div class="project-card">
        <div class="project-title">{title}</div>
        <div class="badge-row">{badges_html}</div>
        <div class="project-desc">{desc}</div>
        <ul class="project-features">{features_html}</ul>
    </div>
    """)


def render_timeline_item(role, org, date, bullets, skills=None):
    """
    Renders a single timeline entry as a self-contained card.
    """
    resp_html = "".join([f'<li>{r}</li>' for r in bullets])
    skills_html = ""
    if skills:
        badges = "".join([f'<span class="tech-badge">{s}</span>' for s in skills])
        skills_html = f'<div style="margin-top:10px; display:flex; flex-wrap:wrap; gap:4px;">{badges}</div>'

    st_html(f"""
    <div class="tl-card">
        <div class="tl-role">{role}</div>
        <div class="tl-org">{org}</div>
        <div class="tl-date">{date}</div>
        <ul class="tl-list">{resp_html}</ul>
        {skills_html}
    </div>
    """)


def render_scroll_to_top():
    """Renders a floating scroll-to-top button."""
    st_html("""
    <a href="#" class="scroll-top" title="Back to top">↑</a>
    """)


def render_footer():
    """Renders the premium minimalist footer."""
    st_html("""
    <div class="premium-footer">
        <div class="footer-text">
            Designed & built by <span class="footer-name">Mohammed Danish Khan</span>
            &nbsp;·&nbsp; © 2026
        </div>
    </div>
    """)
