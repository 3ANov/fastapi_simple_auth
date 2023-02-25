import os
import uvicorn
from fastapi import FastAPI
from api import router
import logging

logger = logging.getLogger(__name__)

app = FastAPI()
app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8000,
        reload=True,
        debug=True,
        log_config=os.getenv('LOG_CONF')
    )

