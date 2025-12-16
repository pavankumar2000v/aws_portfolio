# main.py  (Updated to exactly match your latest resume PDF – 100% accurate content)
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

# Create folders if missing (for local development)
os.makedirs("static", exist_ok=True)
os.makedirs("templates", exist_ok=True)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    data = {
        "name": "PAVAN KUMAR V",
        "title": "Junior DevOps Engineer",
        "location": "Bangalore, India",
        "phone": "+91 7090167278",
        "email": "pavankumar2000v@gmail.com",
        # Add LinkedIn if you have one (optional)
        # "linkedin": "https://www.linkedin.com/in/your-profile",

        # Professional Summary – exact bullet points from your resume
        "professional_summary": [
            "Junior DevOps Engineer with 2+ years of progressive experience (including internships and ongoing project deployments) in application deployment, infrastructure automation, server management, log monitoring, and scripting in production and industrial environments.",
            "Skilled in Linux-based deployments, Python and Shell automation, database operations, and ensuring high-availability systems integrated with PLC-controlled manufacturing lines.",
            "Experienced in transitioning from application support and IoT development to core DevOps practices.",
            "Hands-on contributions to CI/CD workflows, containerization experiments (Docker), and cloud basics (AWS EC2/S3).",
            "Passionate about building scalable, automated pipelines to enhance deployment reliability, reduce downtime, and improve overall operational efficiency."
        ],

        # Technical Skills – structured as categories with skill lists
        "technical_skills": [
            {"category": "Cloud & Infrastructure", "skills": "AWS Basics (EC2, S3), Linux Server Management, Docker, Kubernetes Basics"},
            {"category": "CI/CD & Automation", "skills": "Jenkins, Git/GitHub, Python Scripting, Shell Scripting"},
            {"category": "Monitoring & Logging", "skills": "Log Analysis, Server Performance Monitoring, Grafana Basics"},
            {"category": "Databases", "skills": "MySQL, DBeaver, SQL Query Automation, VS Code"},
            {"category": "Other DevOps Tools", "skills": "Terraform (Learning), GitOps Principles"},
            {"category": "Core Skills", "skills": "Application Deployment, Troubleshooting, IoT/Edge Deployment, PLC Integration"}
        ],

        # Professional Experience
        "professional_experience": [
            {
                "title": "Junior DevOps Engineer",
                "company": "Sense-Ops Tech Solutions – Bangalore, India",
                "duration": "Aug 2023 – July 2025",
                "client": "Hero MotoCorp Vida Electric Vehicle Battery Project",
                "responsibilities": [
                    "Automated deployment processes for manufacturing applications on production Linux servers using Python and Shell scripts, minimizing downtime in live plant operations connected to PLC-controlled CNC machines.",
                    "Monitored server performance, conducted in-depth log analysis, and resolved issues proactively to maintain 99%+ application stability in high-volume EV production environments.",
                    "Built and maintained real-time monitoring dashboards using Grafana to visualize key operational data server metrics, production line status, and application performance, enabling faster decision-making and proactive issue detection for the client team.",
                    "Designed and executed data validation workflows with DBeaver and SQL on MySQL databases, preventing data discrepancies and ensuring operational integrity.",
                    "Performed comprehensive manual testing, bug identification, and documentation prior to deployments, coordinating with cross-functional teams for smooth releases.",
                    "Served as primary client contact for technical queries, generating and delivering operational reports to support decision-making.",
                    "Explored containerization with Docker for application portability and consistency across environments."
                ]
            },
            {
                "title": "DevOps & IoT Intern",
                "company": "Sense-Ops Tech Solutions, Bangalore, India",
                "duration": "May 2023 – July 2023",
                "responsibilities": [
                    "Developed automation scripts in Python for deploying and configuring IoT applications on Raspberry Pi and embedded Linux devices.",
                    "Set up version control workflows with Git, enabling team collaboration and reproducible builds for hardware-software prototypes.",
                    "Performed end-to-end testing, debugging, and log-based troubleshooting, laying foundation for reliable deployment practices."
                ]
            }
        ],

        # Project Experience – with bullet points under each project
        "project_experience": [
            {
                "title": "Automated Deployment Pipeline for EV Manufacturing Application (Production Project)",
                "points": [
                    "Built Shell and Python-based automation for deploying applications to production servers integrated with PLC systems.",
                    "Implemented log monitoring scripts and database validation checks, simulating CI/CD stages for zero-downtime releases.",
                    "Result: Streamlined deployments in a high-stakes manufacturing environment supporting EV battery production."
                ]
            },
            {
                "title": "Dockerized IoT Monitoring System – Industrial 3D Scanner",
                "points": [
                    "Containerized a Raspberry Pi-based 3D scanner application using Docker for portable deployment.",
                    "Automated data pipeline from LiDAR sensors to MySQL database with Python scripts, including basic orchestration testing.",
                    "Added log aggregation and alerting, demonstrating DevOps principles in edge computing."
                ]
            },
            {
                "title": "CI/CD Experiment with Jenkins & Docker (Personal DevOps Project – 2025)",
                "points": [
                    "Set up a Jenkins pipeline for a sample web application, integrating Git, Docker builds, and automated testing.",
                    "Deployed to local Kubernetes cluster (Minikube), achieving automated blue-green deployments.",
                    "Incorporated monitoring with Prometheus basics for container health checks. (GitHub: Add link – Highly recommended to create this)"
                ]
            },
            {
                "title": "Cloud Infrastructure Basics on AWS (Self-Learning Project – Ongoing)",
                "points": [
                    "Provisioned EC2 instances and S3 storage using AWS Free Tier, with basic Terraform scripts for IaC.",
                    "Deployed a simple Python application with automated setup via Shell scripts."
                ]
            }
        ],

        # Education
        "education": {
            "degree": "Bachelor of Engineering in Mechatronics Engineering",
            "institution": "The Oxford College of Engineering, Bangalore",
            "graduated": "Graduated: August 2023",
            "gpa": "GPA: 6.5"
        }
    }
    return templates.TemplateResponse("index.html", {"request": request, "data": data})