# renting.ai

**AI-Powered Semantic Rental Search Platform**

renting.ai is a next-generation rental discovery engine that goes beyond traditional keyword filters. It uses natural language processing and AI to understand nuanced queries like "2BHK in Lakhimpur Kheri under ₹15,000 with parking and near market" and delivers accurate, context-rich results.

### Key Features
- **Intelligent Natural Language Search** — Handles real-user phrasing with semantic understanding.
- **Hybrid RAG Retrieval** — Combines vector similarity (semantic) + structured filters (rent, bedrooms, location, amenities) for best-in-class accuracy.
- **Tech Stack**:
  - Embeddings: Sentence-Transformers
  - Vector Database: Qdrant
  - LLM: OpenAI (for concise, helpful responses)
  - Backend & API: FastAPI + Uvicorn
  - Storage: SQLite + Pandas-enriched data pipeline
  - Data Prep: CSV → JSON with generated search_text for better matching
- **Modular & Scalable Design** — Clean separation of data ingestion, embedding, query processing, and web UI.

### Current Scope & Future Plans
- **Now**: Focused on **Lakhimpur Kheri district** (Uttar Pradesh's largest district, bordering Nepal) and surrounding areas including Lucknow. Ideal for local users seeking rentals in semi-urban/rural parts of UP.
- **Future**: Expansion to top Indian cities (Delhi-NCR, Mumbai, Bangalore, Hyderabad, Pune, Chennai, etc.) with multi-city data ingestion, improved filtering, and cloud scaling.

### Why renting.ai?
Most rental portals still rely on rigid dropdowns and exact keywords — missing the intent behind casual searches.  
renting.ai makes finding a home effortless and accurate, especially in regions like Lakhimpur Kheri where options are scattered and traditional apps fall short.

### Current Status
Working prototype with:
- Data processing & enrichment pipeline
- SQLite + Qdrant hybrid storage
- Vector embedding & similarity search
- Basic FastAPI + Jinja2 web interface
- RAG chain for natural responses

### Quick Start (Local Setup)
```bash
# 1. Clone the repo
git clone https://github.com/shaanMS/renting.ai.git
cd renting.ai

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set OpenAI API key
export OPENAI_API_KEY="sk-..."

# 4. Prepare & load data (run once)
python contextGenerations/csvToJson.py
python database/sqlliteDatabase.py
python vectorsProcessing/saveEmbeddings.py

# 5. Start the app
uvicorn webApp.main:app --reload