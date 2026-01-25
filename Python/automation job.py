"""
Job Application Automation Script for Sayed Hamza
Automatically applies to Data Analytics jobs and sends follow-up emails
"""

import time
import schedule
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import logging
from datetime import datetime
import json
import os

# ============================================
# CONFIGURATION - UPDATE THESE VALUES
# ============================================

CONFIG = {
    # Your Profile Details
    "full_name": "Sayed Hamza",
    "email": "sayedmohammadhamza45@gmail.com",
    "phone": "+91-9717517469",
    "linkedin": "https://www.linkedin.com/in/Sayed-Hamza",
    "github": "https://github.com/Sayedcodes",
    "location": "Delhi, India",
    
    # Job Search Criteria
    "job_titles": ["Data Analyst", "Business Analyst", "Data Analytics", "Junior Data Analyst", "Power BI Analyst"],
    "keywords": ["Power BI", "SQL", "Excel", "Data Analytics", "Dashboard", "Python", "Tableau"],
    "experience_level": "entry",  # entry, mid, senior
    
    # File Paths - UPDATED WITH YOUR ACTUAL PATH
    "resume_path": "C:/Users/Sayed Mohammad Hamza/OneDrive/Desktop/Sayed_Hamza_Data_Analyst_Resume.pdf",
    "applied_jobs_log": "applied_jobs.json",
    
    # Email Configuration (for Gmail)
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587,
    "sender_email": "sayedmohammadhamza45@gmail.com",
    "sender_password": "xxxx xxxx xxxx xxxx",  # GENERATE APP PASSWORD FROM GMAIL
    
    # Job Portals Credentials
    "indeed": {
        "email": "sayedmohammadhamza45@gmail.com",
        "password": "your_indeed_password"
    },
    "naukri": {
        "email": "sayedmohammadhamza45@gmail.com",
        "password": "@Hamza2004"
    },
    "linkedin": {
        "email": "sayedmohammadhamza45@gmail.com",
        "password": "your_linkedin_password"
    },
    "internshala": {
        "email": "sayedmohammadhamza45@gmail.com",
        "password": "your_internshala_password"
    },
    
    # Settings
    "max_applications_per_day": 50,
    "run_time": "09:00",  # 9:00 AM
    "headless_mode": False,  # Set True to run without browser UI
    "apply_easy_apply_only": True  # Only apply to jobs with "Easy Apply"
}

# Customized Email Template for Sayed Hamza
EMAIL_TEMPLATE = """
Dear {hiring_manager},

I hope this email finds you well. I am writing to express my strong interest in the {job_title} position at {company_name}.

I am Sayed Hamza, currently pursuing my B.A. and Diploma in Data Science & Analytics from Jamia Millia Islamia and IT Vedant Academy, Delhi. I am a passionate Data Analyst with hands-on experience in building interactive dashboards and extracting actionable business insights.

My key skills and experience include:

📊 Data Visualization & BI Tools:
   • Power BI: Created HR Analytics Dashboard analyzing attrition trends using DAX
   • Excel: Built Office Supplies Sales Dashboard with interactive KPIs
   • Tableau: Experience in data visualization and reporting

💻 Technical Proficiency:
   • SQL: Proficient in queries, Group By, Joins for data extraction
   • Python: Working knowledge of data manipulation and ML workflows
   • GitHub & Streamlit: Built interactive applications and deployed projects

🎯 Recent Projects:
   • HR Analytics Dashboard: Analyzed employee attrition patterns
   • House Price Predictor: Explored regression and ML techniques
   • Shopping Cart System: Developed interactive web applications

I am particularly drawn to opportunities where I can leverage my analytical skills to drive data-driven decision-making. My portfolio demonstrates my ability to transform raw data into meaningful insights through interactive dashboards and reports.

I have attached my resume for your review. I would welcome the opportunity to discuss how my skills in Power BI, SQL, and Excel can contribute to your team's success.

Thank you for considering my application. I look forward to hearing from you.

Best regards,
Sayed Hamza

📧 sayedmohammadhamza45@gmail.com
📱 +91-9717517469
💼 LinkedIn: linkedin.com/in/Sayed-Hamza
💻 GitHub: github.com/Sayedcodes

Portfolio Links:
• HR Analytics Dashboard: [View on GitHub]
• Office Supplies Dashboard: [View on GitHub]
• All Projects: github.com/Sayedcodes
"""

# Short Email Template for Quick Applications
SHORT_EMAIL_TEMPLATE = """
Dear Hiring Team,

I am writing to apply for the {job_title} position at {company_name}.

As a Data Analyst skilled in Power BI, SQL, and Excel, I have hands-on experience building interactive dashboards and extracting business insights. I am currently pursuing my Diploma in Data Science & Analytics from IT Vedant Academy, Delhi.

Key Skills:
• Power BI, Tableau - Dashboard creation & DAX
• SQL - Data querying and analysis
• Python - Data manipulation and ML basics
• Excel - Advanced formulas, Pivot Tables

I have attached my resume and would love to discuss how I can contribute to your team.

Best regards,
Sayed Hamza
📧 sayedmohammadhamza45@gmail.com | 📱 +91-9717517469
GitHub: github.com/Sayedcodes
"""

# ============================================
# LOGGING SETUP - Fixed for Windows encoding
# ============================================

# Fix Windows console encoding for emojis
import sys
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('job_automation.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# ============================================
# UTILITY FUNCTIONS
# ============================================

def load_applied_jobs():
    """Load previously applied jobs from JSON file"""
    if os.path.exists(CONFIG['applied_jobs_log']):
        with open(CONFIG['applied_jobs_log'], 'r') as f:
            return json.load(f)
    return {"jobs": [], "count_today": 0, "last_date": "", "total_applications": 0}

def save_applied_job(job_data):
    """Save applied job to JSON file"""
    data = load_applied_jobs()
    
    today = datetime.now().strftime("%Y-%m-%d")
    if data["last_date"] != today:
        data["count_today"] = 0
        data["last_date"] = today
    
    # Check if already applied to this job
    job_key = f"{job_data['company']}_{job_data['title']}"
    existing_jobs = [f"{j['company']}_{j['title']}" for j in data["jobs"]]
    
    if job_key in existing_jobs:
        logger.info(f"Already applied to {job_data['title']} at {job_data['company']}")
        return data["count_today"], True
    
    data["jobs"].append(job_data)
    data["count_today"] += 1
    data["total_applications"] = data.get("total_applications", 0) + 1
    
    with open(CONFIG['applied_jobs_log'], 'w') as f:
        json.dump(data, f, indent=2)
    
    return data["count_today"], False

def setup_driver():
    """Setup Selenium WebDriver for Microsoft Edge - No Internet Required"""
    edge_options = EdgeOptions()
    if CONFIG['headless_mode']:
        edge_options.add_argument('--headless')
    edge_options.add_argument('--no-sandbox')
    edge_options.add_argument('--disable-dev-shm-usage')
    edge_options.add_argument('--disable-blink-features=AutomationControlled')
    edge_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    edge_options.add_experimental_option('useAutomationExtension', False)
    
    # Edge driver is usually available with Edge browser installation
    try:
        driver = webdriver.Edge(options=edge_options)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        driver.maximize_window()
        logger.info("✓ Edge browser opened successfully")
        return driver
    except Exception as e:
        logger.error(f"Edge driver error: {str(e)}")
        logger.error("\n" + "=" * 60)
        logger.error("EDGE DRIVER NOT FOUND!")
        logger.error("=" * 60)
        logger.error("Please download EdgeDriver manually:")
        logger.error("1. Check Edge version: Edge → ... → Help → About")
        logger.error("2. Download from: https://developer.microsoft.com/microsoft-edge/tools/webdriver/")
        logger.error("3. Extract msedgedriver.exe to script folder")
        logger.error("=" * 60)
        raise

# ============================================
# INDEED AUTOMATION
# ============================================

def apply_indeed_jobs():
    """Apply to jobs on Indeed.com"""
    driver = setup_driver()
    applied_count = 0
    
    try:
        logger.info("🔍 Starting Indeed job search...")
        
        for job_title in CONFIG['job_titles']:
            driver.get("https://in.indeed.com/")
            time.sleep(3)
            
            # Search for jobs
            try:
                search_box = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "text-input-what"))
                )
                location_box = driver.find_element(By.ID, "text-input-where")
                
                search_box.clear()
                search_box.send_keys(job_title)
                location_box.clear()
                location_box.send_keys(CONFIG['location'])
                
                search_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
                search_button.click()
                time.sleep(4)
                
                logger.info(f"Searching for: {job_title}")
                
                # Get job listings
                job_cards = driver.find_elements(By.CLASS_NAME, "job_seen_beacon")
                
                for idx, job in enumerate(job_cards[:15]):
                    try:
                        # Click on job card
                        driver.execute_script("arguments[0].scrollIntoView(true);", job)
                        time.sleep(1)
                        job.click()
                        time.sleep(3)
                        
                        # Get job details
                        try:
                            job_title_elem = driver.find_element(By.CSS_SELECTOR, "h2.jobsearch-JobInfoHeader-title span")
                            company_elem = driver.find_element(By.CSS_SELECTOR, "[data-testid='company-name']")
                            
                            job_title_text = job_title_elem.text
                            company_name = company_elem.text
                            
                            logger.info(f"📋 Found: {job_title_text} at {company_name}")
                            
                            # Check for Easy Apply button
                            apply_buttons = driver.find_elements(By.XPATH, 
                                "//button[contains(text(), 'Apply now') or contains(@class, 'indeed-apply-button')]")
                            
                            if apply_buttons:
                                apply_buttons[0].click()
                                time.sleep(3)
                                
                                # Handle application process
                                try:
                                    # Upload resume
                                    file_inputs = driver.find_elements(By.CSS_SELECTOR, "input[type='file']")
                                    if file_inputs:
                                        file_inputs[0].send_keys(CONFIG['resume_path'])
                                        time.sleep(2)
                                        logger.info("✓ Resume uploaded")
                                    
                                    # Fill name if required
                                    name_inputs = driver.find_elements(By.CSS_SELECTOR, "input[placeholder*='name' i]")
                                    if name_inputs:
                                        name_inputs[0].clear()
                                        name_inputs[0].send_keys(CONFIG['full_name'])
                                    
                                    # Fill email if required
                                    email_inputs = driver.find_elements(By.CSS_SELECTOR, "input[type='email']")
                                    if email_inputs:
                                        email_inputs[0].clear()
                                        email_inputs[0].send_keys(CONFIG['email'])
                                    
                                    # Fill phone if required
                                    phone_inputs = driver.find_elements(By.CSS_SELECTOR, "input[type='tel']")
                                    if phone_inputs:
                                        phone_inputs[0].clear()
                                        phone_inputs[0].send_keys(CONFIG['phone'])
                                    
                                    # Submit application
                                    submit_buttons = driver.find_elements(By.XPATH, 
                                        "//button[contains(text(), 'Submit') or contains(text(), 'Continue') or contains(text(), 'Apply')]")
                                    if submit_buttons:
                                        submit_buttons[0].click()
                                        time.sleep(3)
                                        
                                        # Save application record
                                        job_data = {
                                            "portal": "Indeed",
                                            "title": job_title_text,
                                            "company": company_name,
                                            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                            "url": driver.current_url
                                        }
                                        count, duplicate = save_applied_job(job_data)
                                        
                                        if not duplicate:
                                            applied_count += 1
                                            logger.info(f"✅ Successfully applied! (Total today: {count})")
                                        
                                        if count >= CONFIG['max_applications_per_day']:
                                            logger.info(f"🎯 Reached daily limit of {CONFIG['max_applications_per_day']}")
                                            return applied_count
                                except Exception as e:
                                    logger.warning(f"⚠️ Application form error: {str(e)}")
                            else:
                                logger.info("⏭️ No easy apply option available")
                                
                        except Exception as e:
                            logger.error(f"❌ Error getting job details: {str(e)}")
                            
                    except Exception as e:
                        logger.error(f"❌ Error processing job card: {str(e)}")
                        continue
                        
            except Exception as e:
                logger.error(f"❌ Search error for {job_title}: {str(e)}")
                
    except Exception as e:
        logger.error(f"❌ Indeed automation error: {str(e)}")
    finally:
        driver.quit()
    
    return applied_count

# ============================================
# NAUKRI AUTOMATION
# ============================================

def apply_naukri_jobs():
    """Apply to jobs on Naukri.com"""
    driver = setup_driver()
    applied_count = 0
    
    try:
        logger.info("🔍 Starting Naukri job search...")
        driver.get("https://www.naukri.com/")
        time.sleep(3)
        
        # Login
        try:
            login_link = driver.find_element(By.ID, "login_Layer")
            login_link.click()
            time.sleep(2)
            
            email_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Enter your active Email ID / Username']"))
            )
            password_input = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter your password']")
            
            email_input.send_keys(CONFIG['naukri']['email'])
            password_input.send_keys(CONFIG['naukri']['password'])
            
            login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            login_button.click()
            time.sleep(5)
            logger.info("✓ Logged into Naukri")
            
        except Exception as e:
            logger.warning(f"⚠️ Naukri login issue: {str(e)}")
        
        # Search for each job title
        for job_title in CONFIG['job_titles'][:3]:  # Search top 3 titles
            search_url = f"https://www.naukri.com/{job_title.replace(' ', '-').lower()}-jobs-in-delhi"
            driver.get(search_url)
            time.sleep(4)
            
            logger.info(f"Searching: {job_title}")
            
            job_tuples = driver.find_elements(By.CLASS_NAME, "srp-jobtuple-wrapper")
            
            for job in job_tuples[:10]:
                try:
                    title_elem = job.find_element(By.CLASS_NAME, "title")
                    company_elem = job.find_element(By.CLASS_NAME, "comp-name")
                    
                    job_title_text = title_elem.text
                    company_name = company_elem.text
                    
                    logger.info(f"📋 Found: {job_title_text} at {company_name}")
                    
                    # Open job in new tab
                    job_link = title_elem.get_attribute("href")
                    driver.execute_script("window.open(arguments[0]);", job_link)
                    driver.switch_to.window(driver.window_handles[-1])
                    time.sleep(3)
                    
                    # Try to apply
                    try:
                        apply_button = WebDriverWait(driver, 5).until(
                            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Apply')]"))
                        )
                        apply_button.click()
                        time.sleep(2)
                        
                        job_data = {
                            "portal": "Naukri",
                            "title": job_title_text,
                            "company": company_name,
                            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            "url": driver.current_url
                        }
                        count, duplicate = save_applied_job(job_data)
                        
                        if not duplicate:
                            applied_count += 1
                            logger.info(f"✅ Successfully applied! (Total today: {count})")
                        
                        if count >= CONFIG['max_applications_per_day']:
                            driver.close()
                            driver.switch_to.window(driver.window_handles[0])
                            return applied_count
                            
                    except Exception as e:
                        logger.info("⏭️ Could not apply to this job")
                    
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                    time.sleep(2)
                    
                except Exception as e:
                    logger.error(f"❌ Error: {str(e)}")
                    if len(driver.window_handles) > 1:
                        driver.close()
                        driver.switch_to.window(driver.window_handles[0])
                    
    except Exception as e:
        logger.error(f"❌ Naukri automation error: {str(e)}")
    finally:
        driver.quit()
    
    return applied_count

# ============================================
# LINKEDIN AUTOMATION
# ============================================

def apply_linkedin_jobs():
    """Apply to jobs on LinkedIn"""
    driver = setup_driver()
    applied_count = 0
    
    try:
        logger.info("🔍 Starting LinkedIn job search...")
        driver.get("https://www.linkedin.com/login")
        time.sleep(3)
        
        # Login
        try:
            username_input = driver.find_element(By.ID, "username")
            password_input = driver.find_element(By.ID, "password")
            
            username_input.send_keys(CONFIG['linkedin']['email'])
            password_input.send_keys(CONFIG['linkedin']['password'])
            
            login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            login_button.click()
            time.sleep(5)
            logger.info("✓ Logged into LinkedIn")
            
        except Exception as e:
            logger.error(f"❌ LinkedIn login failed: {str(e)}")
            return 0
        
        # Search jobs
        jobs_url = f"https://www.linkedin.com/jobs/search/?keywords=Data%20Analyst&location=Delhi%2C%20India&f_AL=true"
        driver.get(jobs_url)
        time.sleep(4)
        
        job_cards = driver.find_elements(By.CLASS_NAME, "job-card-container")
        
        for job in job_cards[:15]:
            try:
                job.click()
                time.sleep(2)
                
                # Check for Easy Apply button
                easy_apply_buttons = driver.find_elements(By.CSS_SELECTOR, "button[aria-label*='Easy Apply']")
                
                if easy_apply_buttons:
                    easy_apply_buttons[0].click()
                    time.sleep(2)
                    
                    # Get job details
                    try:
                        job_title_text = driver.find_element(By.CSS_SELECTOR, "h2.job-title").text
                        company_name = driver.find_element(By.CSS_SELECTOR, ".job-details-jobs-unified-top-card__company-name").text
                        
                        logger.info(f"📋 Applying: {job_title_text} at {company_name}")
                        
                        # Submit if no additional questions
                        submit_buttons = driver.find_elements(By.CSS_SELECTOR, "button[aria-label='Submit application']")
                        if submit_buttons:
                            submit_buttons[0].click()
                            time.sleep(2)
                            
                            job_data = {
                                "portal": "LinkedIn",
                                "title": job_title_text,
                                "company": company_name,
                                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                "url": driver.current_url
                            }
                            count, duplicate = save_applied_job(job_data)
                            
                            if not duplicate:
                                applied_count += 1
                                logger.info(f"✅ Successfully applied! (Total today: {count})")
                            
                            if count >= CONFIG['max_applications_per_day']:
                                return applied_count
                    except:
                        pass
                        
            except Exception as e:
                logger.error(f"❌ Error: {str(e)}")
                continue
                
    except Exception as e:
        logger.error(f"❌ LinkedIn automation error: {str(e)}")
    finally:
        driver.quit()
    
    return applied_count

# ============================================
# EMAIL AUTOMATION
# ============================================

def send_follow_up_email(job_data, hr_email=None, use_short_template=False):
    """Send follow-up email to HR"""
    try:
        msg = MIMEMultipart()
        msg['From'] = CONFIG['sender_email']
        msg['To'] = hr_email if hr_email else "careers@company.com"
        msg['Subject'] = f"Application for {job_data['title']} Position - Sayed Hamza"
        
        template = SHORT_EMAIL_TEMPLATE if use_short_template else EMAIL_TEMPLATE
        
        body = template.format(
            hiring_manager="Hiring Manager",
            job_title=job_data['title'],
            company_name=job_data['company']
        )
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Attach resume if file exists
        if os.path.exists(CONFIG['resume_path']):
            with open(CONFIG['resume_path'], 'rb') as f:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(f.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', 
                              f"attachment; filename= Sayed_Hamza_Data_Analyst_Resume.pdf")
                msg.attach(part)
        
        # Send email
        server = smtplib.SMTP(CONFIG['smtp_server'], CONFIG['smtp_port'])
        server.starttls()
        server.login(CONFIG['sender_email'], CONFIG['sender_password'])
        server.send_message(msg)
        server.quit()
        
        logger.info(f"📧 Follow-up email sent for {job_data['company']}")
        return True
        
    except Exception as e:
        logger.error(f"❌ Email error: {str(e)}")
        return False

# ============================================
# MAIN AUTOMATION FUNCTION
# ============================================

def run_job_automation():
    """Main function to run job application automation"""
    logger.info("=" * 70)
    logger.info("🚀 JOB APPLICATION AUTOMATION - SAYED HAMZA")
    logger.info("=" * 70)
    
    data = load_applied_jobs()
    today = datetime.now().strftime("%Y-%m-%d")
    
    logger.info(f"📊 Total applications sent: {data.get('total_applications', 0)}")
    logger.info(f"📅 Today's date: {today}")
    
    if data["last_date"] == today and data["count_today"] >= CONFIG['max_applications_per_day']:
        logger.info(f"✋ Already reached daily limit of {CONFIG['max_applications_per_day']} applications")
        return
    
    total_applied = 0
    
    # Apply on Indeed
    logger.info("\n" + "=" * 70)
    logger.info("📍 INDEED.COM")
    logger.info("=" * 70)
    indeed_count = apply_indeed_jobs()
    total_applied += indeed_count
    logger.info(f"✓ Indeed applications: {indeed_count}")
    
    # Apply on Naukri
    if total_applied < CONFIG['max_applications_per_day']:
        logger.info("\n" + "=" * 70)
        logger.info("📍 NAUKRI.COM")
        logger.info("=" * 70)
        naukri_count = apply_naukri_jobs()
        total_applied += naukri_count
        logger.info(f"✓ Naukri applications: {naukri_count}")
    
    # Apply on LinkedIn
    if total_applied < CONFIG['max_applications_per_day']:
        logger.info("\n" + "=" * 70)
        logger.info("📍 LINKEDIN")
        logger.info("=" * 70)
        linkedin_count = apply_linkedin_jobs()
        total_applied += linkedin_count
        logger.info(f"✓ LinkedIn applications: {linkedin_count}")
    
    logger.info("\n" + "=" * 70)
    logger.info(f"🎯 TOTAL APPLICATIONS TODAY: {total_applied}")
    logger.info(f"📈 OVERALL TOTAL: {data.get('total_applications', 0) + total_applied}")
    logger.info("=" * 70)
    
    if total_applied > 0:
        logger.info("✅ Job automation completed successfully!")
    else:
        logger.info("⚠️ No applications submitted. Check portal credentials and job availability.")

# ============================================
# SCHEDULER
# ============================================

def schedule_job_automation():
    """Schedule the automation to run at specified time"""
    schedule.every().day.at(CONFIG['run_time']).do(run_job_automation)
    
    logger.info(f"⏰ Job automation scheduled to run daily at {CONFIG['run_time']}")
    logger.info("🛑 Press Ctrl+C to stop the scheduler\n")
    
    while True:
        schedule.run_pending()
        time.sleep(60)

# ============================================
# MAIN EXECUTION
# ============================================

if __name__ == "__main__":
    print("""
    ╔═══════════════════════════════════════════════════════════════╗
    ║                                                               ║
    ║       JOB APPLICATION AUTOMATION FOR SAYED HAMZA             ║
    ║                                                               ║
    ║   Automatically applies to Data Analyst positions            ║
    ║   Target: Indeed, Naukri, LinkedIn                          ║
    ║                                                               ║
    ╚═══════════════════════════════════════════════════════════════╝
    """)
    
    print("\n⚙️  SETUP CHECKLIST:")
    print("━" * 65)
    print("1. ✓ Install: pip install selenium schedule")
    print("2. ⚠️  Download EdgeDriver manually:")
    print("   └─ https://developer.microsoft.com/microsoft-edge/tools/webdriver/")
    print("   └─ Match your Edge version & extract to script folder")
    print("3. ✅ Resume path: Already configured!")
    print("4. ⚠️  UPDATE: Portal passwords (Indeed, Naukri, LinkedIn)")
    print("5. ⚠️  GMAIL: Create App Password and update CONFIG")
    print("   └─ Account → Security → 2-Step → App Passwords")
    print("━" * 65)
    
    # Check if resume exists
    if not os.path.exists(CONFIG['resume_path']):
        print(f"\n❌ ERROR: Resume not found at: {CONFIG['resume_path']}")
        print("Please update the 'resume_path' in CONFIG section\n")
        exit(1)
    
    print(f"\n✓ Resume found: {CONFIG['resume_path']}")
    print(f"✓ Email: {CONFIG['email']}")
    print(f"✓ Phone: {CONFIG['phone']}")
    print(f"✓ Location: {CONFIG['location']}")
    print(f"✓ Max applications per day: {CONFIG['max_applications_per_day']}")
    print(f"✓ Scheduled time: {CONFIG['run_time']}\n")
    
    choice = input("🚀 Run automation now or schedule? (now/schedule/test): ").lower().strip()
    
    if choice == 'now':
        print("\n🔄 Starting job application automation...\n")
        run_job_automation()
    elif choice == 'schedule':
        print(f"\n⏰ Scheduling automation to run at {CONFIG['run_time']} daily...")
        schedule_job_automation()
    elif choice == 'test':
        print("\n🧪 Running test mode (will apply to max 3 jobs)...")
        CONFIG['max_applications_per_day'] = 3
        run_job_automation()
    else:
        print("\n❌ Invalid choice. Please run again and select 'now', 'schedule', or 'test'")