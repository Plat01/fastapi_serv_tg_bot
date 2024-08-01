import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI, BackgroundTasks

from app.tg_bot import bot, dispatcher as dp
from app.config import settings


async def start_bot():
    await dp.start_polling(bot)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    # models.Base.metadata.create_all(bind=engine)
    # logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    await bot.send_message(
        chat_id=settings.NOTIFICATION_ID,
        text="✅ Bot has been started with polling mode"
    )

    # Start bot in a background
    bot_task = asyncio.create_task(start_bot())

    yield

    # Shutdown logic
    bot_task.cancel()  # Cancel the polling task
    try:
        await bot_task
    except asyncio.CancelledError:
        pass
    await bot.session.close()


# Create FastAPI app with lifespan
app: FastAPI = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "FastAPI is running!"}


# app.add_api_route(**router.updates_route)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
