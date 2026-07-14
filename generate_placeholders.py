# utils/generate_placeholders.py
import os
from PIL import Image, ImageDraw, ImageFont

def generate_assets():
    # Base directories
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    assets_dir = os.path.join(base_dir, "assets")
    cert_dir = os.path.join(assets_dir, "certificates")
    proj_dir = os.path.join(assets_dir, "project_images")
    
    os.makedirs(cert_dir, exist_ok=True)
    os.makedirs(proj_dir, exist_ok=True)

    # 1. Generate Profile Image (profile.jpg) - Gradient with Text
    profile_path = os.path.join(assets_dir, "profile.jpg")
    if not os.path.exists(profile_path):
        img = Image.new("RGB", (400, 400), color="#0a0f1d")
        draw = ImageDraw.Draw(img)
        # Draw a beautiful circle representing a profile glow
        draw.ellipse([50, 50, 350, 350], fill="#111827", outline="#00f2fe", width=6)
        # Draw Initials
        # Since we might not have custom fonts loaded, let's draw text with default font size
        try:
            draw.text((200, 200), "MDK", fill="#ffffff", anchor="mm", font_size=60)
        except TypeError:
            # Fallback for older PIL versions
            draw.text((150, 170), "MDK", fill="#ffffff")
        img.save(profile_path, "JPEG")
        print(f"Created {profile_path}")

    # 2. Generate CricVerse Project Image
    cric_path = os.path.join(proj_dir, "cricverse.jpg")
    if not os.path.exists(cric_path):
        img = Image.new("RGB", (600, 350), color="#1e3a8a")
        draw = ImageDraw.Draw(img)
        try:
            draw.text((300, 175), "CricVerse Analytics", fill="#00f2fe", anchor="mm", font_size=36)
            draw.text((300, 230), "AI & Match Predictions", fill="#ffffff", anchor="mm", font_size=18)
        except TypeError:
            draw.text((150, 150), "CricVerse Analytics", fill="#00f2fe")
        img.save(cric_path, "JPEG")
        print(f"Created {cric_path}")

    # 3. Generate Expense Tracker Project Image
    exp_path = os.path.join(proj_dir, "expense_tracker.jpg")
    if not os.path.exists(exp_path):
        img = Image.new("RGB", (600, 350), color="#0f766e")
        draw = ImageDraw.Draw(img)
        try:
            draw.text((300, 175), "Expense Tracker", fill="#38bdf8", anchor="mm", font_size=36)
            draw.text((300, 230), "Data Visualization Dashboard", fill="#ffffff", anchor="mm", font_size=18)
        except TypeError:
            draw.text((150, 150), "Expense Tracker", fill="#38bdf8")
        img.save(exp_path, "JPEG")
        print(f"Created {exp_path}")

    # 4. Generate Certificate Image
    cert_img_path = os.path.join(cert_dir, "data_analytics_genai.jpg")
    if not os.path.exists(cert_img_path):
        img = Image.new("RGB", (800, 600), color="#111827")
        draw = ImageDraw.Draw(img)
        draw.rectangle([40, 40, 760, 560], outline="#facc15", width=8)
        try:
            draw.text((400, 150), "Google Developer Partner", fill="#eab308", anchor="mm", font_size=28)
            draw.text((400, 280), "Data Analytics with Generative AI", fill="#ffffff", anchor="mm", font_size=36)
            draw.text((400, 380), "Certified: Mohammed Danish Khan", fill="#38bdf8", anchor="mm", font_size=20)
        except TypeError:
            draw.text((200, 150), "Google Developer Partner", fill="#eab308")
            draw.text((200, 250), "Data Analytics with Generative AI", fill="#ffffff")
        img.save(cert_img_path, "JPEG")
        print(f"Created {cert_img_path}")

    # 5. Generate Resume PDF (resume.pdf)
    resume_path = os.path.join(assets_dir, "resume.pdf")
    if not os.path.exists(resume_path):
        # Write minimal valid PDF
        minimal_pdf = b'''%PDF-1.4
1 0 obj <</Type /Catalog /Pages 2 0 R>> endobj
2 0 obj <</Type /Pages /Kids [3 0 R] /Count 1>> endobj
3 0 obj <</Type /Page /Parent 2 0 R /Resources <<>> /MediaBox [0 0 595 842] /Contents 4 0 R>> endobj
4 0 obj <</Length 180>> stream
BT
/F1 24 Tf
100 750 Td
(Mohammed Danish Khan - Resume) Tj
/F1 14 Tf
0 -40 Td
(Aspiring Data Analyst | Python Developer) Tj
0 -20 Td
(Email: Danish.k1709@gmail.com | Phone: +91 8169387986) Tj
0 -40 Td
(Education: Bachelor of Engineering in Computer CS/AI/ML - 8.0 CGPA) Tj
0 -40 Td
(Projects: CricVerse, Expense Tracker Analytics) Tj
ET
endstream
endobj
xref
0 5
0000000000 65535 f 
0000000009 00000 n 
0000000056 00000 n 
0000000111 00000 n 
0000000212 00000 n 
trailer <</Size 5 /Root 1 0 R>>
startxref
441
%%EOF
'''
        with open(resume_path, "wb") as f:
            f.write(minimal_pdf)
        print(f"Created {resume_path}")

if __name__ == "__main__":
    generate_assets()
