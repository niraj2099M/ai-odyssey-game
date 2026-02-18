from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from story_app.routers import story, job


app = FastAPI(
    title="AI Odyssey game",
    description="APIs to generate cool storiy games"
    version="0.1.0"
    docs_url="/docs",
    redoc_url="/redoc",    
)

app.add_middleware(
    CORSMiddleware,
    #allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# app.include_router(story.router, prefix=settings.API_PREFIX)
# app.include_router(job.router, prefix=settings.API_PREFIX)