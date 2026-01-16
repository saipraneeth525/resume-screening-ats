import streamlit as st
from PyPDF2 import PdfReader
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ---------- PDF TEXT EXTRACTION ----------
def extract_text_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text


# ---------- TEXT CLEANING ----------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z ]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


# ---------- MATCH SCORE ----------
def get_match_score(resume, jd):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume, jd])
    score = cosine_similarity(vectors[0], vectors[1])[0][0]
    return score


# ---------- MISSING SKILLS ----------
skills_list = [
    "python", "sql", "machine learning", "data analysis", "nlp",
    "deep learning", "excel", "power bi", "tableau", "aws", "docker"
]

def find_missing_skills(resume, jd):
    missing = []
    for skill in skills_list:
        if skill in jd and skill not in resume:
            missing.append(skill)
    return missing


# ---------- STREAMLIT UI ----------
st.title("Smart Resume Screening Tool (Mini ATS)")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")
jd_text = st.text_area("Paste Job Description")

if uploaded_file and jd_text:
    resume_text = extract_text_from_pdf(uploaded_file)
    
    resume_clean = clean_text(resume_text)
    jd_clean = clean_text(jd_text)

    score = get_match_score(resume_clean, jd_clean)
    missing_skills = find_missing_skills(resume_clean, jd_clean)

    st.subheader("Results")
    st.write(f"Match Score: **{score*100:.2f}%**")

    if missing_skills:
        st.write("Missing Skills:", ", ".join(missing_skills))
    else:
        st.write("No major skills missing ✅")
