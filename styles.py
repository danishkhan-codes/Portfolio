# styles.py — Premium Portfolio CSS Engine

def get_css():
    """
    Returns a comprehensive premium CSS stylesheet with animations,
    glassmorphism, particle effects, and micro-interactions.
    Dark-mode only for a cinematic, premium feel.
    """

    css = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap');

    :root {
        --bg-primary: #080b11;
        --bg-secondary: #111622;
        --bg-card: rgba(17, 22, 34, 0.7);
        --border-subtle: rgba(56, 189, 248, 0.07);
        --border-hover: rgba(56, 189, 248, 0.35);
        --text-primary: #f8fafc;
        --text-secondary: #cbd5e1;
        --text-muted: #94a3b8;
        --accent-cyan: #38bdf8;
        --accent-purple: #818cf8;
        --accent-pink: #f472b6;
        --gradient-main: linear-gradient(135deg, #38bdf8 0%, #6366f1 50%, #818cf8 100%);
        --gradient-warm: linear-gradient(135deg, #38bdf8 0%, #34d399 100%);
        --gradient-glow: linear-gradient(135deg, rgba(56,189,248,0.1) 0%, rgba(99,102,241,0.1) 100%);
        --shadow-glow: 0 0 40px rgba(56, 189, 248, 0.07);
        --font-display: 'Space Grotesk', sans-serif;
        --font-body: 'Inter', sans-serif;
        --font-mono: 'JetBrains Mono', monospace;
    }

    /* ═══════════════════════════════════════════
       GLOBAL RESETS
       ═══════════════════════════════════════════ */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"],
    .main, .stApp {
        background-color: var(--bg-primary) !important;
        color: var(--text-primary);
        font-family: var(--font-body);
        overflow-y: auto !important;
        overflow-x: hidden !important;
        height: auto !important;
        min-height: 100vh !important;
    }

    [data-testid="stHeader"] {
        background-color: transparent !important;
    }

    /* Hide Streamlit sidebar */
    [data-testid="stSidebar"],
    [data-testid="stSidebarContent"],
    [data-testid="stSidebarNav"],
    [data-testid="stSidebarHeader"],
    [data-testid="stSidebarUserContent"],
    [data-testid="stSidebarCollapsedControl"],
    section[data-testid="stSidebar"] {
        display: none !important;
        width: 0px !important;
    }

    /* Container */
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 2rem !important;
        max-width: 1200px !important;
        margin: 0 auto !important;
    }

    .stVerticalBlock {
        gap: 0.5rem !important;
    }

    /* Hide default form borders */
    div[data-testid="stForm"] {
        border: none !important;
        background: transparent !important;
        padding: 0 !important;
        box-shadow: none !important;
    }

    /* ═══════════════════════════════════════════
       TYPOGRAPHY
       ═══════════════════════════════════════════ */
    h1, h2, h3, h4, h5, h6 {
        font-family: var(--font-display) !important;
        font-weight: 700;
        letter-spacing: -0.03em;
        margin-top: 0px !important;
        margin-bottom: 8px !important;
        padding-top: 0px !important;
    }

    .gradient-text {
        background: var(--gradient-main);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-family: var(--font-display);
        font-weight: 700;
        display: inline-block;
    }

    .section-label {
        font-family: var(--font-mono);
        font-size: 0.75rem;
        font-weight: 600;
        color: var(--accent-cyan);
        text-transform: uppercase;
        letter-spacing: 0.15em;
        margin-bottom: 6px;
        display: block;
    }

    .section-title {
        font-family: var(--font-display);
        font-size: 2rem;
        font-weight: 700;
        color: var(--text-primary);
        margin-bottom: 24px !important;
        line-height: 1.1;
    }

    /* ═══════════════════════════════════════════
       ANIMATED BACKGROUND PARTICLES
       ═══════════════════════════════════════════ */
    .particle-field {
        position: relative;
        overflow: hidden;
    }

    .particle-field::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background-image:
            radial-gradient(2px 2px at 20% 30%, rgba(56,189,248,0.3) 0%, transparent 100%),
            radial-gradient(2px 2px at 40% 70%, rgba(167,139,250,0.2) 0%, transparent 100%),
            radial-gradient(1px 1px at 60% 20%, rgba(244,114,182,0.2) 0%, transparent 100%),
            radial-gradient(2px 2px at 80% 50%, rgba(56,189,248,0.15) 0%, transparent 100%),
            radial-gradient(1px 1px at 10% 80%, rgba(167,139,250,0.25) 0%, transparent 100%),
            radial-gradient(1px 1px at 70% 90%, rgba(56,189,248,0.2) 0%, transparent 100%),
            radial-gradient(2px 2px at 90% 10%, rgba(244,114,182,0.15) 0%, transparent 100%),
            radial-gradient(1px 1px at 50% 50%, rgba(56,189,248,0.2) 0%, transparent 100%);
        animation: particle-drift 25s linear infinite;
        z-index: 0;
        pointer-events: none;
    }

    @keyframes particle-drift {
        0% { transform: translate(0, 0) rotate(0deg); }
        25% { transform: translate(-3%, 2%) rotate(2deg); }
        50% { transform: translate(2%, -1%) rotate(-1deg); }
        75% { transform: translate(-1%, 3%) rotate(1deg); }
        100% { transform: translate(0, 0) rotate(0deg); }
    }

    /* ═══════════════════════════════════════════
       HERO SECTION
       ═══════════════════════════════════════════ */
    .hero-container {
        position: relative;
        padding: 80px 0 50px 0;
        z-index: 1;
    }

    .hero-greeting {
        font-family: var(--font-mono);
        font-size: 1rem;
        color: var(--accent-cyan);
        margin-bottom: 12px;
        letter-spacing: 0.05em;
    }

    .hero-name {
        font-family: var(--font-display);
        font-size: 4rem;
        font-weight: 700;
        line-height: 1.05;
        margin-bottom: 16px;
        background: var(--gradient-main);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: gradient-shift 6s ease infinite;
        background-size: 200% 200%;
    }

    @keyframes gradient-shift {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }

    .hero-tagline {
        font-family: var(--font-body);
        font-size: 1.15rem;
        color: var(--text-secondary);
        line-height: 1.6;
        max-width: 650px;
        margin-bottom: 24px;
    }

    .hero-meta {
        font-size: 0.9rem;
        color: var(--text-muted);
        margin-bottom: 20px;
    }

    .hero-meta a {
        color: var(--accent-cyan);
        text-decoration: none;
        transition: color 0.2s ease;
    }
    .hero-meta a:hover {
        color: var(--accent-purple);
    }

    /* Social Icons */
    .social-row {
        display: flex;
        gap: 10px;
        margin-top: 10px;
    }

    .social-icon {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 42px;
        height: 42px;
        border-radius: 12px;
        background: var(--bg-card);
        border: 1px solid var(--border-subtle);
        color: var(--text-secondary) !important;
        text-decoration: none;
        font-size: 1.15rem;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        backdrop-filter: blur(10px);
    }

    .social-icon:hover {
        border-color: var(--accent-cyan);
        color: var(--accent-cyan) !important;
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(56, 189, 248, 0.2);
        background: rgba(56, 189, 248, 0.08);
    }

    /* ═══════════════════════════════════════════
       FLOATING NAV
       ═══════════════════════════════════════════ */
    .floating-nav {
        position: fixed;
        top: 16px;
        left: 50%;
        transform: translateX(-50%);
        z-index: 9999;
        background: rgba(3, 7, 18, 0.85);
        backdrop-filter: blur(20px) saturate(180%);
        -webkit-backdrop-filter: blur(20px) saturate(180%);
        border: 1px solid var(--border-subtle);
        border-radius: 50px;
        padding: 8px 28px;
        display: flex;
        gap: 24px;
        align-items: center;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
    }

    .nav-link {
        font-family: var(--font-body);
        font-size: 0.82rem;
        font-weight: 500;
        color: var(--text-muted) !important;
        text-decoration: none;
        transition: all 0.25s ease;
        letter-spacing: 0.02em;
        padding: 4px 0;
        position: relative;
    }

    .nav-link:hover {
        color: var(--accent-cyan) !important;
    }

    .nav-link::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        width: 0;
        height: 2px;
        background: var(--gradient-main);
        border-radius: 1px;
        transition: width 0.3s ease;
    }

    .nav-link:hover::after {
        width: 100%;
    }

    /* ═══════════════════════════════════════════
       STAT CARDS
       ═══════════════════════════════════════════ */
    .stat-card {
        text-align: center;
        background: var(--bg-card);
        border: 1px solid var(--border-subtle);
        border-radius: 16px;
        padding: 20px 12px;
        backdrop-filter: blur(10px);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }

    .stat-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        background: var(--gradient-main);
        opacity: 0;
        transition: opacity 0.3s ease;
    }

    .stat-card:hover {
        transform: translateY(-4px);
        border-color: var(--border-hover);
        box-shadow: var(--shadow-glow);
    }

    .stat-card:hover::before {
        opacity: 1;
    }

    .stat-icon {
        font-size: 1.6rem;
        margin-bottom: 8px;
        display: block;
    }

    .stat-val {
        font-size: 2rem;
        font-weight: 700;
        font-family: var(--font-display);
        background: var(--gradient-main);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1.1;
        margin-bottom: 4px;
    }

    .stat-label {
        font-size: 0.72rem;
        color: var(--text-muted);
        text-transform: uppercase;
        letter-spacing: 0.1em;
        font-weight: 500;
    }

    /* ═══════════════════════════════════════════
       SECTION DIVIDERS
       ═══════════════════════════════════════════ */
    .section-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent 0%, var(--border-subtle) 50%, transparent 100%);
        margin: 40px 0;
        border: none;
    }

    /* ═══════════════════════════════════════════
       GLASS CARDS
       ═══════════════════════════════════════════ */
    .glass-card {
        background: var(--bg-card);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid var(--border-subtle);
        border-radius: 16px;
        padding: 24px;
        transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }

    .glass-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(56,189,248,0.3), transparent);
        opacity: 0;
        transition: opacity 0.3s ease;
    }

    .glass-card:hover {
        transform: translateY(-4px);
        border-color: var(--border-hover);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3), var(--shadow-glow);
    }

    .glass-card:hover::before {
        opacity: 1;
    }

    /* ═══════════════════════════════════════════
       SKILL CARDS
       ═══════════════════════════════════════════ */
    .skill-item {
        background: var(--bg-card);
        border: 1px solid var(--border-subtle);
        border-radius: 12px;
        padding: 14px 16px;
        margin-bottom: 8px;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        backdrop-filter: blur(8px);
    }

    .skill-item:hover {
        border-color: var(--border-hover);
        transform: translateX(4px);
        box-shadow: 0 4px 20px rgba(56, 189, 248, 0.08);
    }

    .skill-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 8px;
    }

    .skill-name {
        font-family: var(--font-body);
        font-weight: 600;
        font-size: 0.88rem;
        color: var(--text-primary);
    }

    .skill-percent {
        font-family: var(--font-mono);
        font-size: 0.78rem;
        color: var(--accent-cyan);
        font-weight: 600;
    }

    .progress-track {
        width: 100%;
        height: 4px;
        background: rgba(148, 163, 184, 0.08);
        border-radius: 4px;
        overflow: hidden;
    }

    .progress-fill {
        height: 100%;
        border-radius: 4px;
        background: var(--gradient-main);
        transition: width 1.2s cubic-bezier(0.4, 0, 0.2, 1);
    }

    /* ═══════════════════════════════════════════
       SKILL CATEGORY HEADERS
       ═══════════════════════════════════════════ */
    .skill-category {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 14px;
        padding-bottom: 8px;
        border-bottom: 1px solid var(--border-subtle);
    }

    .skill-category-icon {
        font-size: 1.2rem;
    }

    .skill-category-name {
        font-family: var(--font-display);
        font-size: 1rem;
        font-weight: 600;
        color: var(--text-primary);
    }

    /* ═══════════════════════════════════════════
       PROJECT CARDS
       ═══════════════════════════════════════════ */
    .project-card {
        background: var(--bg-card);
        border: 1px solid var(--border-subtle);
        border-radius: 20px;
        padding: 28px;
        backdrop-filter: blur(10px);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }

    .project-card::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: var(--gradient-main);
        transform: scaleX(0);
        transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        transform-origin: left;
    }

    .project-card:hover {
        transform: translateY(-6px);
        border-color: var(--border-hover);
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.35), 0 0 40px rgba(56, 189, 248, 0.06);
    }

    .project-card:hover::after {
        transform: scaleX(1);
    }

    .project-title {
        font-family: var(--font-display);
        font-size: 1.3rem;
        font-weight: 700;
        color: var(--text-primary);
        margin-bottom: 12px;
    }

    .project-desc {
        font-size: 0.9rem;
        color: var(--text-secondary);
        line-height: 1.6;
        margin-bottom: 16px;
    }

    .project-features {
        list-style: none;
        padding: 0;
        margin: 0 0 16px 0;
    }

    .project-features li {
        position: relative;
        padding-left: 20px;
        margin-bottom: 8px;
        font-size: 0.85rem;
        color: var(--text-secondary);
        line-height: 1.5;
    }

    .project-features li::before {
        content: '▸';
        position: absolute;
        left: 0;
        color: var(--accent-cyan);
        font-weight: bold;
    }

    /* Tech Badges */
    .badge-row {
        display: flex;
        flex-wrap: wrap;
        gap: 6px;
        margin-bottom: 14px;
    }

    .tech-badge {
        display: inline-block;
        font-family: var(--font-mono);
        font-size: 0.68rem;
        font-weight: 500;
        color: var(--accent-cyan);
        background: rgba(56, 189, 248, 0.06);
        border: 1px solid rgba(56, 189, 248, 0.12);
        border-radius: 6px;
        padding: 3px 8px;
        transition: all 0.2s ease;
    }

    .tech-badge:hover {
        background: rgba(56, 189, 248, 0.12);
        border-color: rgba(56, 189, 248, 0.25);
        transform: translateY(-1px);
    }

    /* ═══════════════════════════════════════════
       TIMELINE
       ═══════════════════════════════════════════ */
    .timeline-wrapper {
        position: relative;
        padding-left: 28px;
    }

    .timeline-wrapper::before {
        content: '';
        position: absolute;
        top: 0;
        bottom: 0;
        left: 8px;
        width: 2px;
        background: linear-gradient(180deg, var(--accent-cyan), var(--accent-purple), transparent);
        border-radius: 2px;
    }

    .tl-item {
        position: relative;
        margin-bottom: 28px;
    }

    .tl-dot {
        position: absolute;
        left: -24px;
        top: 6px;
        width: 14px;
        height: 14px;
        border-radius: 50%;
        background: var(--bg-primary);
        border: 2px solid var(--accent-cyan);
        box-shadow: 0 0 12px rgba(56, 189, 248, 0.3);
        z-index: 2;
        transition: all 0.3s ease;
    }

    .tl-item:hover .tl-dot {
        background: var(--accent-cyan);
        box-shadow: 0 0 20px rgba(56, 189, 248, 0.5);
        transform: scale(1.3);
    }

    .tl-card {
        background: var(--bg-card);
        border: 1px solid var(--border-subtle);
        border-radius: 14px;
        padding: 18px 20px;
        backdrop-filter: blur(8px);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .tl-card:hover {
        border-color: var(--border-hover);
        transform: translateX(4px);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
    }

    .tl-role {
        font-family: var(--font-display);
        font-size: 1.05rem;
        font-weight: 700;
        color: var(--text-primary);
        margin-bottom: 2px;
    }

    .tl-org {
        font-size: 0.82rem;
        color: var(--accent-cyan);
        font-weight: 500;
        margin-bottom: 4px;
    }

    .tl-date {
        font-family: var(--font-mono);
        font-size: 0.72rem;
        color: var(--text-muted);
        margin-bottom: 10px;
    }

    .tl-list {
        list-style: none;
        padding: 0;
        margin: 0;
    }

    .tl-list li {
        position: relative;
        padding-left: 16px;
        margin-bottom: 5px;
        font-size: 0.82rem;
        color: var(--text-secondary);
        line-height: 1.5;
    }

    .tl-list li::before {
        content: '›';
        position: absolute;
        left: 0;
        color: var(--accent-purple);
        font-weight: bold;
        font-size: 1rem;
    }

    /* ═══════════════════════════════════════════
       CONTACT SECTION
       ═══════════════════════════════════════════ */
    .contact-wrapper {
        background: var(--bg-card);
        border: 1px solid var(--border-subtle);
        border-radius: 20px;
        padding: 32px;
        backdrop-filter: blur(10px);
        position: relative;
        overflow: hidden;
    }

    .contact-wrapper::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        background: var(--gradient-main);
    }

    /* Streamlit form inputs */
    div.stTextInput > div > div > input,
    div.stTextArea > div > div > textarea {
        background: var(--bg-secondary) !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        border-radius: 10px !important;
        color: var(--text-primary) !important;
        font-family: var(--font-body) !important;
        transition: all 0.3s ease !important;
    }

    div.stTextInput > div > div > input:focus,
    div.stTextArea > div > div > textarea:focus {
        border-color: var(--accent-cyan) !important;
        box-shadow: 0 0 0 2px rgba(56, 189, 248, 0.15) !important;
    }

    /* Placeholders visibility */
    div.stTextInput > div > div > input::placeholder,
    div.stTextArea > div > div > textarea::placeholder {
        color: var(--text-muted) !important;
        opacity: 0.7 !important;
    }

    /* Styles for labels to guarantee visibility */
    div.stTextInput label,
    div.stTextArea label,
    div[data-testid="stWidgetLabel"] p {
        color: var(--text-primary) !important;
        font-family: var(--font-display) !important;
        font-weight: 500 !important;
        font-size: 0.95rem !important;
        margin-bottom: 6px !important;
    }

    /* Submit button */
    div.stButton > button,
    div.stButton > button:first-child,
    div.stButton > button:active,
    div.stButton > button:focus,
    div[data-testid="stFormSubmitButton"] > button,
    div[data-testid="stFormSubmitButton"] > button:first-child,
    div[data-testid="stFormSubmitButton"] > button:active,
    div[data-testid="stFormSubmitButton"] > button:focus {
        background: linear-gradient(135deg, #38bdf8 0%, #6366f1 100%) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 12px 36px !important;
        font-family: var(--font-display) !important;
        font-weight: 600 !important;
        font-size: 0.92rem !important;
        letter-spacing: 0.02em !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.2) !important;
    }

    div.stButton > button:hover,
    div[data-testid="stFormSubmitButton"] > button:hover {
        background: linear-gradient(135deg, #0ea5e9 0%, #4f46e5 100%) !important;
        color: #ffffff !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(99, 102, 241, 0.4) !important;
    }

    /* ═══════════════════════════════════════════
       FOOTER
       ═══════════════════════════════════════════ */
    .premium-footer {
        text-align: center;
        padding: 40px 20px 20px 20px;
        margin-top: 40px;
        position: relative;
    }

    .premium-footer::before {
        content: '';
        position: absolute;
        top: 0;
        left: 20%;
        right: 20%;
        height: 1px;
        background: linear-gradient(90deg, transparent, var(--border-subtle), transparent);
    }

    .footer-text {
        font-family: var(--font-body);
        font-size: 0.8rem;
        color: var(--text-muted);
    }

    .footer-name {
        background: var(--gradient-main);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 600;
    }

    /* ═══════════════════════════════════════════
       SCROLL TO TOP
       ═══════════════════════════════════════════ */
    .scroll-top {
        position: fixed;
        bottom: 24px;
        right: 24px;
        width: 40px;
        height: 40px;
        border-radius: 12px;
        background: var(--bg-card);
        border: 1px solid var(--border-subtle);
        backdrop-filter: blur(10px);
        display: flex;
        align-items: center;
        justify-content: center;
        text-decoration: none;
        color: var(--text-secondary) !important;
        font-size: 0.9rem;
        z-index: 998;
        transition: all 0.3s ease;
    }

    .scroll-top:hover {
        border-color: var(--accent-cyan);
        color: var(--accent-cyan) !important;
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(56, 189, 248, 0.15);
    }

    /* ═══════════════════════════════════════════
       SCROLL PROGRESS BAR
       ═══════════════════════════════════════════ */
    .scroll-progress {
        position: fixed;
        top: 0;
        left: 0;
        height: 2px;
        background: var(--gradient-main);
        z-index: 99999;
        width: 100%;
        transform-origin: left;
        animation: scroll-progress-anim linear;
        animation-timeline: scroll();
    }

    @keyframes scroll-progress-anim {
        from { transform: scaleX(0); }
        to { transform: scaleX(1); }
    }

    /* ═══════════════════════════════════════════
       STREAMLIT TOGGLE OVERRIDE
       ═══════════════════════════════════════════ */
    div.stCheckbox, div[data-testid="stWidgetLabel"] {
        color: var(--text-secondary) !important;
    }

    /* ═══════════════════════════════════════════
       STRENGTH CHIPS (pure CSS hover)
       ═══════════════════════════════════════════ */
    .strength-chip {
        background: rgba(56, 189, 248, 0.04);
        border: 1px solid var(--border-subtle);
        border-radius: 10px;
        padding: 10px 14px;
        display: flex;
        align-items: center;
        gap: 8px;
        transition: all 0.25s ease;
        cursor: default;
    }

    .strength-chip:hover {
        border-color: rgba(56, 189, 248, 0.25);
        transform: translateX(4px);
        box-shadow: 0 4px 15px rgba(56, 189, 248, 0.08);
    }

    </style>
    <div class="scroll-progress"></div>
    """
    return css
