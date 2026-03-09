🤖 renting.ai

<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-0.104+-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
  <img src="https://img.shields.io/badge/Qdrant-1.7+-e84393?style=for-the-badge&logo=qdrant&logoColor=white"/>
  <img src="https://img.shields.io/badge/Sentence--Transformers-2.2+-FF6F00?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/OpenAI-1.3+-412991?style=for-the-badge&logo=openai&logoColor=white"/>
  <img src="https://img.shields.io/badge/LangChain-0.1+-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white"/>
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white"/>
</p>

<p align="center">
  <!img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=24&duration=3000&pause=1000&color=00B8B0&center=true&vCenter=true&width=500&lines=AI-Powered+Rental+Search;Natural+Language+Queries;;Lakhimpur+Kheri+→+Delhi-NCR" alt="Typing SVG" />
</p>

<div align="center">
  <h3>✨ AI-Powered Rental Discovery · Natural Language · ✨>

<a href="#-quick-setup"><strong>🚀 Quick Setup</strong></a> •
<a href="#-key-features"><strong>⭐ Features</strong></a> •
<a href="#-tech-stack"><strong>🛠️ Tech Stack</strong></a> •
<a href="#-project-structure"><strong>📁 Structure</strong></a>

</div>

<br/>

---

📋 Table of Contents

· 🎯 Overview
· ⭐ Key Features
· 🛠️ Tech Stack
· 📁 Project Structure
· 🚀 Quick Setup
· 🧠 How It Works
· 📊 Data Pipeline
· 🔧 Core Code
· 📈 Roadmap
· 📝 License

---

🎯 Overview

renting.ai is an AI-powered semantic rental search platform that understands natural language queries in Hindi/English mix. Built for small-town India, starting with Lakhimpur Kheri (UP's largest district) and expanding to Lucknow → Delhi-NCR → Mumbai.

The Problem

Traditional rental portals (99acres/Magicbricks) fail in small towns because:

· ❌ Rigid dropdown filters don't understand natural language
· ❌ Listings are scattered and inconsistent
· ❌ Keyword search misses semantic meaning

The Solution

```bash
Type: "2 BHK with parking near mandi under ₹12k in Lakhimpur"
      ↓
AI understands: 2 bedrooms + parking + near market + budget ₹12,000
      ↓
Returns: Hyper-relevant results + AI-generated summary
```

---

⭐ Key Features

<div align="center">
  <table>
    <tr>
      <td align="center" width="25%">
        <h3>🧠</h3>
        <b>Semantic Search</b>
        <p>Hindi/English mix queries, no exact keywords needed</p>
      </td>
      <td align="center" width="25%">
        <h3>🔄</h3>
        <b>Hybrid RAG</b>
        <p>Vector similarity + structured filters (85%+ relevance)</p>
      </td>
      <td align="center" width="25%">
        <h3>🤖</h3>
        <b>LLM Summaries</b>
        <p>OpenAI-generated helpful responses in Hinglish</p>
      </td>
      <td align="center" width="25%">
        <h3>🗄️</h3>
        <b>Vector DB</b>
        <p>Qdrant with 384-dim embeddings (all-MiniLM-L6-v2)</p>
      </td>
    </tr>
    <tr>
      <td align="center">
        <h3>⚡</h3>
        <b>FastAPI</b>
        <p>Async, high-performance backend</p>
      </td>
      <td align="center">
        <h3>📱</h3>
        <b>Mobile-First</b>
        <p>Responsive UI works on 2G networks</p>
      </td>
      <td align="center">
        <h3>📊</h3>
        <b>ETL Pipeline</b>
        <p>CSV → Enrichment → Embeddings → Qdrant</p>
      </td>
      <td align="center">
        <h3>🎯</h3>
        <b>Local Focus</b>
        <p>Built for small-town India (UP rentals)</p>
      </td>
    </tr>
  </table>
</div>

---

🛠️ Tech Stack

<div align="center">
  <table>
    <tr>
      <th colspan="2" align="center">Backend & API</th>
      <th colspan="2" align="center">AI/ML Core</th>
    </tr>
    <tr>
      <td><b>FastAPI</b></td>
      <td>0.104+ (async framework)</td>
      <td><b>Sentence-Transformers</b></td>
      <td>2.2+ (384-dim embeddings)</td>
    </tr>
    <tr>
      <td><b>Uvicorn</b></td>
      <td>ASGI server</td>
      <td><b>Qdrant</b></td>
      <td>1.7+ (vector database)</td>
    </tr>
    <tr>
      <td><b>OpenAI</b></td>
      <td>1.3+ (GPT-4 for summaries)</td>
      <td><b>LangChain</b></td>
      <td>0.1+ (RAG chains)</td>
    </tr>
    <tr>
      <th colspan="2" align="center">Data Processing</th>
      <th colspan="2" align="center">Frontend</th>
    </tr>
    <tr>
      <td><b>Pandas</b></td>
      <td>2.0+ (ETL operations)</td>
      <td><b>Jinja2</b></td>
      <td>HTML templating</td>
    </tr>
    <tr>
      <td><b>SQLite</b></td>
      <td>Structured database</td>
      <td><b>CSS3/JS</b></td>
      <td>Responsive UI</td>
    </tr>
    <tr>
      <td><b>Faker</b></td>
      <td>Mock data generation</td>
      <td><b>HTML5</b></td>
      <td>Search forms + results</td>
    </tr>
  </table>
</div>

📦 Core Dependencies

```txt
fastapi==0.104.1
uvicorn[standard]==0.24.0
qdrant-client==1.7.0
sentence-transformers==2.2.2
openai==1.3.0
langchain==0.1.0
pandas==2.1.3
faker==20.1.0
jinja2==3.1.2
python-dotenv==1.0.0
```

---

📁 Project Structure

```
renting.ai/
├── 📂 contextGenerations/          # Data enrichment
│   └── 📄 csvToJson.py             # CSV → enriched JSON
│
├── 📂 database/                     # SQLite setup
│   └── 📄 sqlliteDatabase.py        # Schema + data import
│
├── 📂 queryEmbeddingService/        # Query processing
│   ├── 📄 queryDispatcherService.py # RAG orchestration
│   ├── 📄 queryEmbedderService.py   # Query → embedding
│   └── 📄 queryValidationService.py # Input validation
│
├── 📂 vectorsProcessing/            # Vector storage
│   └── 📄 saveEmbeddings.py         # Qdrant batch upsert
│
├── 📂 webApp/                       # Main FastAPI app
│   ├── 📄 main.py                    # API routes
│   ├── 📂 databases/                  # DB connections
│   ├── 📂 embeddingService/           # Embedding utils
│   ├── 📂 langchainRag/                # RAG implementation
│   ├── 📂 llm/                         # OpenAI integration
│   ├── 📂 static/                       # CSS/JS assets
│   ├── 📂 templates/                     # Jinja2 HTML
│   │   ├── 📄 index.html                  # Search form
│   │   └── 📄 results.html                 # Results display
│   └── 📂 vectorService/                   # Qdrant queries
│
├── 📂 static/                        # Global assets
├── 📄 .gitignore
├── 📄 README.md
├── 📄 requirements.txt
└── 📄 requirements - Copy.txt
```

---

🚀 Quick Setup

Prerequisites

· Python 3.10+
· Docker (for Qdrant)
· OpenAI API key

Installation

```bash
# 1. Clone repository
git clone https://github.com/shaanMS/renting.ai.git
cd renting.ai

# 2. Create virtual environment
python -m venv venv

# 3. Activate environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Start Qdrant (Docker)
docker run -p 6333:6333 qdrant/qdrant

# 6. Set up environment variables
cp .env.example .env
# Edit .env with your OpenAI API key

# 7. Run data pipeline
python contextGenerations/csvToJson.py
python database/sqlliteDatabase.py
python vectorsProcessing/saveEmbeddings.py

# 8. Start FastAPI server
cd webApp
uvicorn main:app --reload --port 8000
```

Environment Variables

```env
OPENAI_API_KEY=sk-your-key-here
QDRANT_HOST=localhost
QDRANT_PORT=6333
DATABASE_PATH=../database/rentals.db
ENVIRONMENT=development
```

---

🧠 How It Works

RAG Pipeline Flow

```
User Query: "2 BHK with parking near mandi under ₹12k in Lakhimpur"
         │
         ▼
┌─────────────────┐
│ 1. Validate     │ → Remove dangerous chars, check length
└─────────────────┘
         │
         ▼
┌─────────────────┐
│ 2. Embed        │ → all-MiniLM-L6-v2 → 384-dim vector
└─────────────────┘
         │
         ▼
┌──────────────────────────────────┐
│ 3. Hybrid Retrieval              │
│  ┌─────────────┐  ┌─────────────┐│
│  │ Qdrant      │  │ SQLite      ││
│  │ Semantic    │  │ Structured  ││
│  │ Similarity  │  │ Filters     ││
│  └─────────────┘  └─────────────┘│
│         │              │         │
│         └──────┬───────┘         │
│                ▼                 │
│         ┌─────────────┐          │
│         │ Fuse Results│          │
│         └─────────────┘          │
└──────────────────────────────────┘
         │
         ▼
┌─────────────────┐
│ 4. Build Context│ → Create prompt from top results
└─────────────────┘
         │
         ▼
┌─────────────────┐
│ 5. LLM Generate │ → OpenAI GPT-4 → Hinglish summary
└─────────────────┘
         │
         ▼
┌─────────────────┐
│ 6. Return       │ → JSON + results.html
└─────────────────┘
```

---

📊 Data Pipeline

ETL Process

```
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│ Rentals1 │───▶│ Enriched │───▶│  SQLite  │───▶│  Qdrant  │
│   CSV    │    │   JSON   │    │ Storage  │    │ Vectors  │
└──────────┘    └──────────┘    └──────────┘    └──────────┘
     │               │               │               │
     ▼               ▼               ▼               ▼
原始数据      search_text      30+ fields      384-dim
             field added      structured       embeddings
```

Sample Data Enrichment

```python
# Original CSV
{
    "ad_id": 1001,
    "property_type": "Apartment",
    "bhk": 2,
    "rent": 11500,
    "locality": "Mandi Road",
    "city": "Lakhimpur",
    "description": "Spacious 2BHK near market"
}

# After enrichment
{
    "search_text": "Apartment in Mandi Road, Lakhimpur. 2 BHK, ₹11500 rent. Spacious 2BHK near market. Amenities: parking, power backup",
    # ... original fields preserved
}
```

---

🔧 Core Code

1. Data Enrichment

```python
# contextGenerations/csvToJson.py
import pandas as pd

df = pd.read_csv('Rentals1.csv')
df['search_text'] = df.apply(lambda row: 
    f"{row['property_type']} in {row['locality']}, {row['city']}. "
    f"{row['bhk']} BHK, ₹{row['rent']} rent. {row['description']}", axis=1)
df.to_json('rentals_enriched.json', orient='records', indent=2)
```

2. Vector Storage

```python
# vectorsProcessing/saveEmbeddings.py
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')
client = QdrantClient(host="localhost", port=6333)

# Batch upsert (BATCH_SIZE=100)
for i in range(0, len(data), 100):
    batch = data[i:i+100]
    embeddings = model.encode([item['search_text'] for item in batch])
    # ... upsert to Qdrant
```

3. Main API

```python
# webApp/main.py
from fastapi import FastAPI, Request, Form
from queryEmbeddingService.queryDispatcherService import dispatch_query

app = FastAPI()

@app.post("/search")
async def search(query: str = Form(...)):
    results = dispatch_query(query)
    return templates.TemplateResponse("results.html", {"results": results})
```

---

📈 Roadmap

✅ Completed (MVP v0.2)

· Core RAG architecture
· Qdrant vector storage
· SQLite structured data
· Basic search UI
· Lakhimpur Kheri dataset

🚀 Next Up (v0.5)

· Add Lucknow dataset
· Improve UI/UX with Tailwind
· Add rate limiting
· Docker Compose setup

🎯 Future (v1.0)

· Pan-India expansion
· Mobile app (React Native)
· Owner dashboard
· Payment integration

---

📝 License

<div align="center">
  <p><strong>MIT License</strong></p>
  <p>Copyright © 2026 Shaan, India</p>
  <p>Built with ❤️ for Bharat's rental ecosystem</p>
</div>

---

<div align="center">
  <h3>⭐ Star this repository if you found it useful! ⭐</h3>

  <p>
    <a href="https://github.com/shaanMS/renting.ai/stargazers">
      <img src="https://img.shields.io/github/stars/shaanMS/renting.ai?style=social"/>
    </a>
    <a href="https://github.com/shaanMS/renting.ai/network/members">
      <img src="https://img.shields.io/github/forks/shaanMS/renting.ai?style=social"/>
    </a>
    <a href="https://github.com/shaanMS/renting.ai/issues">
      <img src="https://img.shields.io/github/issues/shaanMS/renting.ai?style=social"/>
    </a>
  </p>

  <p>
    <i>Questions? Open an issue on GitHub</i>
  </p>

  <p>
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=16&duration=2000&pause=500&color=00B8B0&center=true&vCenter=true&width=300&lines=Star+if+you+like+it!;Fork+to+contribute!;Share+with+friends!" alt="Footer Animation" />
  </p>
</div>
