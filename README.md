# 🤖 NLP-Based Resume Screening Tool

An AI-powered resume screening web application that compares candidate resumes against job descriptions using advanced NLP techniques like semantic similarity and keyword extraction. This tool helps recruiters streamline the hiring process by automatically scoring and analyzing resume relevance.

---

## 🚀 Features

- ✅ Upload resume and job description PDFs
- 🧠 NLP-based semantic similarity scoring (BERT embeddings)
- 🗂️ Keyword extraction and matching
- 📊 Final weighted score for screening decisions
- 💻 Clean and responsive UI with modern CSS
- 🌐 Built with Flask (Python backend)

---


## 🧰 Tech Stack

| Layer        | Technology |
|--------------|------------|
| Frontend     | HTML, CSS (external), Jinja2 |
| Backend      | Python, Flask |
| NLP          | Sentence Transformers (BERT), Sklearn, PDFMiner |
| File Support | PDF upload and parsing |

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/rohanmulik05/NLP-Based-Resume-Screening-Tool.git
cd NLP-Based-Resume-Screening-Tool
```

### 2. Install dependencies

We recommend using a virtual environment.

```bash
pip install -r requirements.txt
```

Or manually install:

```bash
pip install flask sentence-transformers sklearn pdfminer.six
```

### 3. Run the app

```bash
python app.py
```

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 📂 Project Structure

```
NLP-Based-Resume-Screening-Tool/
│
├── app.py
├── requirements.txt
├── templates/
│   ├── index.html
│   └── result.html
└── static/
    └── styles.css

```

---

## ⚙️ How It Works

1. **File Upload**: Resume and Job Description PDFs are uploaded.
2. **Text Extraction**: Text is extracted from the PDFs using `pdfminer.six`.
3. **Keyword Matching**: Keywords from both documents are matched and scored.
4. **Semantic Similarity**: Sentence embeddings via `sentence-transformers` are used to calculate cosine similarity.
5. **Final Score**: Weighted average of keyword match (30%) and semantic similarity (70%) is shown.

---

## 📈 Future Improvements

- 🔍 OCR support for scanned PDFs
- 📑 Resume parsing with named entity recognition (NER)
- 🌐 Deployment on cloud (Render/Heroku/AWS)
- 🧾 Export results to PDF/CSV

---

## 👨‍💻 Author

**Rohan Mulik**  
[GitHub](https://github.com/rohanmulik05)

---

## 📄 License

This project is licensed under the MIT License.
