# Smart Resume Screening Tool (Mini ATS)

This is a simple web app I built to check how well a resume matches a job description using Python and basic NLP techniques.

---

## About the Project

I created this project after learning about how companies use Applicant Tracking Systems (ATS) to screen resumes.  
The app lets users upload a resume (PDF) and paste a job description to get:

- A match score (how well the resume fits the job)  
- A list of missing skills that can be improved  

Building this helped me understand how Natural Language Processing works in real-world applications.
## Features
- Upload a resume in PDF format  
- Paste a job description  
- Get a resume–job match percentage  
- See missing skills from the job description  
- Simple and clean web interface using Streamlit  
## Technologies Used
- Python  
- PyPDF2 for extracting text from PDF files  
- Regular expressions for basic text cleaning  
- Scikit-learn for TF-IDF and similarity calculation  
- Streamlit for building the web app interface  
- Git and GitHub for version control  

## How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/saipraneeth525/resume-screening-ats.git
