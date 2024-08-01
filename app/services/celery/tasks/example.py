"""
the example task
"""
import asyncio

from app.services.celery import celery_app
from app.tg_bot.tasks import send_message_to_admin


@celery_app.task
def example_task(name: str) -> None:
    """
    simple example task for celery app
    """
    asyncio.run(send_message_to_admin("Work!"))
