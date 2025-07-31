from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os


from pdfminer.high_level import extract_text
from rake_nltk import Rake
from sentence_transformers import SentenceTransformer, util
import nltk

# Ensure NLTK stopwords are downloaded
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

# Initialize app and config
app = Flask(__name__, static_folder='static', template_folder='templates')

app.config['UPLOAD_FOLDER'] = 'uploads'

# Load models
rake = Rake()
model = SentenceTransformer('all-MiniLM-L6-v2')

# Utility Functions
def extract_pdf_text(file_path):
    try:
        return extract_text(file_path)
    except Exception as e:
        return f"Error: Failed to open or read PDF file: {e}"

def extract_keywords(text, max_keywords=15):
    rake.extract_keywords_from_text(text)
    return rake.get_ranked_phrases()[:max_keywords]

def calculate_semantic_score(resume_text, job_text):
    resume_embed = model.encode(resume_text, convert_to_tensor=True)
    job_embed = model.encode(job_text, convert_to_tensor=True)
    similarity = util.pytorch_cos_sim(resume_embed, job_embed).item() * 100
    return round(similarity, 2)

def calculate_keyword_overlap(resume_keywords, job_keywords):
    matches = set(resume_keywords) & set(job_keywords)
    if not job_keywords:
        return 0.0
    return round((len(matches) / len(job_keywords)) * 100, 2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'resume' not in request.files or 'job' not in request.files:
        return "Please upload both Resume and Job Description PDFs."

    resume_file = request.files['resume']
    job_file = request.files['job']

    if resume_file.filename == '' or job_file.filename == '':
        return "One of the files is empty."

    # Save the uploaded files
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    resume_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(resume_file.filename))
    job_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(job_file.filename))

    resume_file.save(resume_path)
    job_file.save(job_path)

    # Extract text
    resume_text = extract_pdf_text(resume_path)
    job_text = extract_pdf_text(job_path)

    if resume_text.startswith("Error") or job_text.startswith("Error"):
        return resume_text if resume_text.startswith("Error") else job_text

    # Extract keywords
    resume_keywords = extract_keywords(resume_text)
    job_keywords = extract_keywords(job_text)

    # Scores
    semantic_score = calculate_semantic_score(resume_text, job_text)
    keyword_score = calculate_keyword_overlap(resume_keywords, job_keywords)

    # Final weighted score: 70% semantic + 30% keyword match
    final_score = round((0.7 * semantic_score) + (0.3 * keyword_score), 2)

    return render_template(
        'result.html',
        semantic_score=semantic_score,
        keyword_score=keyword_score,
        final_score=final_score,
        resume_keywords=resume_keywords,
        job_keywords=job_keywords
    )

if __name__ == '__main__':
    app.run(debug=True)
