import time
from celery import Celery
from celery.utils.log import get_task_logger
import employer
import soiskatel

logger = get_task_logger(__name__)

app = Celery('tasks', broker='redis://redis:6379/0', backend='redis://redis:6379/0')


@app.task()
def send_email_employer(dataFormDict: dict):
    dataForm = employer.DataForm(dataFormDict)
    logger.info('Got Request - Starting work with employer mail')
    employer.send_to_employer(dataForm)
    employer.send_to_KursNaSever(dataForm)
    logger.info('Work for employer mail Finished')


@app.task()
def send_email_soiskatel(dataFormDict: dict):
    dataForm = soiskatel.DataForm(dataFormDict)
    logger.info('Got Request - Starting work with soiskatel email')
    soiskatel.send_to_soiskatel(dataForm)
    soiskatel.send_to_KursNaSever(dataForm)
    logger.info('Work for soiskatel email Finished ')