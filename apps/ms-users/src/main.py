from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from config.settings import Settings


"""
define logger,
metrics
shutdownHooks
"""

app = FastAPI(
    title="MS-Users",
    version="1.0.0",
    description="Microservice for user management",
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-frontend-domain.com"],  # Adjust as needed
    allow_methods=[],
    allow_headers=["Authorization", "Content-Type"],
)

# Setup NATS Transport onto app

# Health check endpoint
@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}

# HTTPS server setup
if __name__ == "__main__":
    settings = Settings()
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=settings.PORT,
        ssl_keyfile=settings.SSL_KEYFILE,
        ssl_certfile=settings.SSL_CERTFILE,
    )