<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
</head>
<body>
<div style="max-width: 1200px; margin: 0 auto; padding: 20px; background: linear-gradient(135deg, #0a0a2e 0%, #1a1a4e 100%); color: #eef2ff; border-radius: 28px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">

<!-- HEADER SECTION -->
<div style="text-align: center; padding: 2rem 1rem 1rem;">
    <h1 style="font-size: 2.8rem; font-weight: 800; background: linear-gradient(135deg, #00D4FF, #0077B6); -webkit-background-clip: text; background-clip: text; color: transparent; margin: 0;">🦷 Miller Dental AI System</h1>
    <p style="font-size: 1.1rem; color: #b0b8d0;">AI‑Powered Backend for Smart Dental Appointment Management</p>
    <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; margin-top: 20px;">
        <span style="background: #2a2f45; padding: 5px 12px; border-radius: 30px; font-size: 0.8rem;">🐍 Python</span>
        <span style="background: #2a2f45; padding: 5px 12px; border-radius: 30px; font-size: 0.8rem;">🚀 FastAPI</span>
        <span style="background: #2a2f45; padding: 5px 12px; border-radius: 30px; font-size: 0.8rem;">🍃 MongoDB Atlas</span>
        <span style="background: #2a2f45; padding: 5px 12px; border-radius: 30px; font-size: 0.8rem;">🤖 Scikit-learn</span>
        <span style="background: #2a2f45; padding: 5px 12px; border-radius: 30px; font-size: 0.8rem;">📊 Cosine Similarity</span>
    </div>
</div>

<hr style="border-color: #2a2f45; margin: 25px 0;">

<!-- PROJECT OVERVIEW -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 25px 0;">
    <h2 style="color: #00D4FF; margin-top: 0;">📌 Project Overview</h2>
    <p>This project is an <strong>AI-powered backend system</strong> developed for the <strong>Miller Dental Website</strong>. The platform allows patients to explore dental services, view available dentists, and book appointments online.</p>
    <p>I designed and developed intelligent backend features that improve user experience – making the system smarter, more responsive, and data-driven. The AI system was built as a separate Python backend using <strong>FastAPI</strong> and later integrated with the main <strong>MongoDB Atlas</strong> database.</p>
</div>

<!-- MY ROLE -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 25px 0;">
    <h2 style="color: #00D4FF; margin-top: 0;">👨‍💻 My Role</h2>
    <p><strong>Rehman Ahmad</strong> – AI Developer Intern at TechNexus Virtual University</p>
    <p>I built <strong>four main intelligent features</strong> exposed through REST APIs:</p>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; margin-top: 15px;">
        <div style="background: #0b0f1c; padding: 12px; border-radius: 16px; text-align: center;">🦷 <strong>Dentist Recommendation</strong></div>
        <div style="background: #0b0f1c; padding: 12px; border-radius: 16px; text-align: center;">⏰ <strong>Time Slot Suggestion</strong></div>
        <div style="background: #0b0f1c; padding: 12px; border-radius: 16px; text-align: center;">💰 <strong>Price Estimation</strong></div>
        <div style="background: #0b0f1c; padding: 12px; border-radius: 16px; text-align: center;">📊 <strong>Patient Pattern Analysis</strong></div>
    </div>
</div>

<!-- DEVELOPMENT APPROACH -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 25px 0;">
    <h2 style="color: #00D4FF; margin-top: 0;">🔧 Development Approach – Two Phases</h2>
    <ul>
        <li><strong>Phase 1 – Sample Data:</strong> Created my own sample dataset (dentists, services, appointments, users) to build and test all AI features independently without waiting for the backend team.</li>
        <li><strong>Phase 2 – Live Database:</strong> Connected to MongoDB Atlas, analyzed real database structure, adjusted field mappings, and updated code to work with live data.</li>
    </ul>
</div>

<!-- FEATURES SECTION -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 25px 0;">
    <h2 style="color: #00D4FF; margin-top: 0;">✨ Features Implemented</h2>
    <div style="margin-bottom: 20px; padding: 15px; background: #0b0f1c; border-radius: 16px;">
        <h3 style="color: #FFD93D; margin-top: 0;">1. Dentist Recommendation System</h3>
        <p>Suggests the best dentist based on service selected by user using <strong>cosine similarity</strong>.</p>
        <ul><li>Matches dentist specialties with services → encodes features → applies similarity → returns top dentists</li></ul>
    </div>
    <div style="margin-bottom: 20px; padding: 15px; background: #0b0f1c; border-radius: 16px;">
        <h3 style="color: #FFD93D; margin-top: 0;">2. Time Slot Suggestion System</h3>
        <p>Shows available time slots for a dentist and prevents double booking.</p>
        <ul><li>Checks availability → fetches booked slots → removes occupied → returns free slots</li></ul>
    </div>
    <div style="margin-bottom: 20px; padding: 15px; background: #0b0f1c; border-radius: 16px;">
        <h3 style="color: #FFD93D; margin-top: 0;">3. Price Estimation System</h3>
        <p>Shows price and duration of a service before booking.</p>
        <ul><li>Searches service → returns price, duration, description → handles invalid requests</li></ul>
    </div>
    <div style="padding: 15px; background: #0b0f1c; border-radius: 16px;">
        <h3 style="color: #FFD93D; margin-top: 0;">4. Patient Pattern Analysis System</h3>
        <p>Analyzes patient history and predicts future visits.</p>
        <ul><li>Fetches appointments → calculates visit gaps → predicts next visit → classifies behavior (monthly/occasional)</li></ul>
    </div>
</div>

<!-- FOLDER STRUCTURE -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 25px 0;">
    <h2 style="color: #00D4FF; margin-top: 0;">📁 Project Structure</h2>
    <pre style="background: #0b0f1c; padding: 15px; border-radius: 16px; overflow-x: auto; color: #b0c4de; font-size: 0.85rem;">
MILLER_DENTAL_WEBSITE_CODE/
│
├── Final_Full_System/
│   ├── __pycache__/
│   ├── .env
│   ├── data.py
│   ├── main.py
│   ├── model.py
│   └── seed_data.py
│
├── Patient-Pattern/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── main.py
│   ├── model.py
│   └── sample_data.py
│
├── Price-Estimation/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── main.py
│   ├── model.py
│   └── sample_data.py
│
├── recommendation-system/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── main.py
│   ├── model.py
│   ├── requirements.txt
│   └── sample_data.py
│
├── Time-Slot-Suggestion/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── main.py
│   ├── model.py
│   └── sample_data.py
│
└── README.md
    </pre>
</div>

<!-- DATABASE -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 25px 0;">
    <h2 style="color: #00D4FF; margin-top: 0;">🗄️ Database – MongoDB Atlas</h2>
    <p><strong>Collections:</strong> Users, Dentists, Services, Appointments</p>
</div>

<!-- API ENDPOINTS -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 25px 0;">
    <h2 style="color: #00D4FF; margin-top: 0;">🔗 API Endpoints</h2>
    <table style="width:100%; border-collapse: collapse;">
        <tr style="background: #0b0f1c; text-align: left;">
            <th style="padding: 10px;">Endpoint</th>
            <th style="padding: 10px;">Method</th>
            <th style="padding: 10px;">Purpose</th>
        </tr>
        <tr style="border-bottom:1px solid #2a2f45;"><td style="padding: 8px;"><code>/</code></td><td>GET</td><td>Health check & system info</td></tr>
        <tr style="border-bottom:1px solid #2a2f45;"><td style="padding: 8px;"><code>/ai/recommend-dentist</code></td><td>GET</td><td>Recommend best dentist</td></tr>
        <tr style="border-bottom:1px solid #2a2f45;"><td style="padding: 8px;"><code>/ai/available-slots</code></td><td>GET</td><td>Show available time slots</td></tr>
        <tr style="border-bottom:1px solid #2a2f45;"><td style="padding: 8px;"><code>/ai/price-estimate</code></td><td>GET</td><td>Show service price</td></tr>
        <tr><td style="padding: 8px;"><code>/ai/patient-pattern</code></td><td>GET</td><td>Analyze patient history</td></tr>
    </table>
</div>

<!-- CHALLENGES -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 25px 0;">
    <h2 style="color: #00D4FF; margin-top: 0;">⚡ Challenges & Solutions</h2>
    <ul>
        <li><strong>MongoDB SSL errors</strong> – Fixed with proper connection parameters</li>
        <li><strong>Field name mismatches</strong> – Analyzed live schema & updated mappings</li>
        <li><strong>NaN values causing failures</strong> – Implemented data cleaning before processing</li>
        <li><strong>ObjectId serialization</strong> – Converted ObjectId to string in JSON responses</li>
    </ul>
</div>

<!-- TECH STACK -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 25px 0;">
    <h2 style="color: #00D4FF; margin-top: 0;">🛠️ Technologies Used</h2>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); gap: 10px;">
        <div>🐍 Python</div><div>🚀 FastAPI</div><div>🍃 MongoDB Atlas</div>
        <div>📦 PyMongo</div><div>📊 Pandas</div><div>🔢 NumPy</div>
        <div>🤖 Scikit-learn</div><div>📬 Postman</div><div>🐙 GitHub</div>
    </div>
</div>

<!-- GITHUB -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 25px 0; text-align: center;">
    <h2 style="color: #00D4FF; margin-top: 0;">📁 GitHub Repository</h2>
    <a href="https://github.com/RehmanAhmad333/ai-miller-dental-application" target="_blank" style="background: #0077B6; color: white; padding: 12px 28px; border-radius: 40px; text-decoration: none; font-weight: 600; display: inline-block;">🔗 View on GitHub</a>
</div>

<!-- CONCLUSION -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 25px 0;">
    <h2 style="color: #00D4FF; margin-top: 0;">📝 Conclusion</h2>
    <p>This project provided hands-on experience building real-world AI systems integrated with live databases. Skills gained include backend development, API design, machine learning implementation, and production-level debugging – a complete <strong>end-to-end development experience</strong>.</p>
</div>

<!-- FOOTER -->
<div style="text-align: center; padding: 1.5rem 0; border-top: 1px solid #2a2f45; margin-top: 20px; color: #6f7a9e;">
    <p><strong>Rehman Ahmad</strong> | AI Developer Intern at TechNexus Virtual University</p>
    <p>Built with dedication during AI Developer Internship • May 1, 2026</p>
</div>

</div>
</body>
</html>