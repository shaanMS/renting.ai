from fastapi import FastAPI
from pydantic import BaseModel
# from queryEmbeddingService import queryDispatcherService
from fastapi import FastAPI, Request
from sse_starlette.sse import EventSourceResponse
import asyncio
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


from fastapi.responses import StreamingResponse


'''to do :-   translation before vector creation and tranlated embeddings in origin vector db dono m apply karo '''



# app = FastAPI()

# # request body structure
# class QueryRequest(BaseModel):
#     query: str


# @app.get("/")
# def home():
#     return {"status": "server running"}


# @app.post("/search")
# def search(request: QueryRequest):

#     user_query = request.query
#     response = dispatchQuery(user_query)
    
    
    
    
    
#     return {
#         "message": "Query received",
#         "query": response
#     }
    
    
    
    
    
    
    
    

app = FastAPI()

templates = Jinja2Templates(directory="templates")
# --------------------------------
# SSE Generator
# --------------------------------
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )
    






async def fake_stream():

    text = "Bangladesh imposed daily limits on fuel sales: सरकार द्वारा तय नई सीमा के तहत अब पेट्रोल पंपों पर एक दिन में मोटरसाइकिल  सरकार द्वारा तय नई सीमा के तहत अब पेट्रोल पंपों पर एक दिन में मोटरसाइकिल  सरकार द्वारा तय नई सीमा के तहत अब पेट्रोल पंपों पर एक दिन में मोटरसाइकिल  सरकार द्वारा तय नई सीमा के तहत अब पेट्रोल पंपों पर एक दिन में मोटरसाइकिल  सरकार द्वारा तय नई सीमा के तहत अब पेट्रोल पंपों पर एक दिन में मोटरसाइकिल  सरकार द्वारा तय नई सीमा के तहत अब पेट्रोल पंपों पर एक दिन में मोटरसाइकिल  सरकार द्वारा तय नई सीमा के तहत अब पेट्रोल पंपों पर एक दिन में मोटरसाइकिल को अधिकतम 2 लीटर पेट्रोल/ऑक्टेन ही दिया जाएगा, जबकि निजी कारों को एक दिन में अधिकतम 10 "
    i = 0 
    for ch in text:
        i +=1
        if i%29 ==0:
             
         yield "\n"
        
        else :  
         yield f"{ch}"
        
        
        await asyncio.sleep(0.03)




 
    
    
    
async def event_generator(query: str):

    words = [
        "Processing",
        "your",
        "query:",
        query,
        "...",
        "Result",
        "will",
        "come",
        "here"
    ]

    for word in words:

        yield {
            "event": "message",
            "data": word
        }

        await asyncio.sleep(1)


# --------------------------------
# SSE Endpoint
# --------------------------------

# @app.post("/stream")
# async def stream_response(request: Request):

#     body = await request.json()

#     query = body.get("query", "")
    
    
    
    
#     return EventSourceResponse(
#         event_generator(query)
#     )
    
    
    
    
    
@app.post("/stream")
async def stream():

    return StreamingResponse(
        fake_stream(),
        media_type="text/event-stream"
    )