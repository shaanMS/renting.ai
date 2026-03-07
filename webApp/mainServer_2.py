from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import asyncio
import time
import random
from llm.llmContext import generateResponse
import os

# Create templates and static directories if they don't exist
# os.makedirs("templates", exist_ok=True)
# os.makedirs("static", exist_ok=True)
# os.makedirs("static/css", exist_ok=True)
# os.makedirs("static/js", exist_ok=True)

template = """
You are a real estate assistant.

Use ONLY the provided context.

If answer not found say:
"Sorry, relevant property not found."

Context:
{context}

User Question:
{question}

Answer in Hinglish.
"""

app = FastAPI(title="Property Search AI", description="Real Estate AI Assistant")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# Store conversation history (in production, use a database)
conversation_history = {}

# --------------------------------
# Streaming Response Generator
# --------------------------------
async def generate_streaming_response(template, query, session_id):
    """Generate streaming response with realistic typing animation"""
    
    try:
        # Simulate thinking/processing time
        thinking_phrases = [
            "🔍 Searching properties...",
            "📊 Analyzing listings...",
            "🏠 Finding best matches...",
            "✨ Preparing response...",
            "📝 Generating answer..."
        ]
        
        # Show thinking animation
        for phrase in thinking_phrases[:2]:  # Show first 2 thinking phrases
            yield f"data: {phrase}\n\n"
            await asyncio.sleep(0.5)
        
        # Get actual response from LLM
        result = await generateResponse(template, query)
        
        if not result or result.strip() == "":
            result = "Sorry, I couldn't find any relevant properties matching your criteria."
            
        # Stream the response character by character for typing effect
        current_text = ""
        words = result.split()
        
        for i, word in enumerate(words):
            # Add space between words
            if i > 0:
                current_text += " "
                yield f"data: {' '}\n\n"
                await asyncio.sleep(0.03)
            
            # Stream each character in the word
            for char in word:
                current_text += char
                yield f"data: {char}\n\n"
                # Variable typing speed for natural feel
                await asyncio.sleep(random.uniform(0.02, 0.05))
        
        # Store in conversation history
        if session_id not in conversation_history:
            conversation_history[session_id] = []
        
        conversation_history[session_id].append({
            "query": query,
            "response": result,
            "timestamp": time.time()
        })
        
        # Signal end of stream
        yield f"data: [DONE]\n\n"
        
    except Exception as e:
        error_msg = f"⚠️ Error processing your request: {str(e)}"
        yield f"data: {error_msg}\n\n"
        yield f"data: [DONE]\n\n"

# --------------------------------
# API Endpoints
# --------------------------------
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Serve the main chat interface"""
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "title": "Property Search AI"
        }
    )

@app.post("/api/stream")
async def stream_response(request: Request):
    """Stream AI response"""
    try:
        body = await request.json()
        query = body.get("query", "").strip()
        session_id = body.get("session_id", "default")
        
        if not query:
            return {"error": "Query cannot be empty"}
        
        return StreamingResponse(
            generate_streaming_response(template, query, session_id),
            media_type="text/event-stream",
            headers={
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "X-Accel-Buffering": "no"
            }
        )
    except Exception as e:
        return {"error": str(e)}

@app.get("/api/history/{session_id}")
async def get_history(session_id: str):
    """Get conversation history for a session"""
    return {"history": conversation_history.get(session_id, [])}

@app.delete("/api/history/{session_id}")
async def clear_history(session_id: str):
    """Clear conversation history for a session"""
    if session_id in conversation_history:
        conversation_history[session_id] = []
    return {"status": "History cleared"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)