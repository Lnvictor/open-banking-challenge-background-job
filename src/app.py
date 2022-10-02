from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

import config
from connections.mongo import Mongo
from functions.open_banking import save_organizations
from repositories.participants_repository import ParticipantsRepository


def schedule():
    scheduler = BlockingScheduler()
    mongo = Mongo(config.MONGO_USERNAME, config.MONGO_PASSWORD, config.MONGO_HOST, config.MONGO_PORT, config.MONGO_DB)
    connection = mongo.get_connection()
    repository = ParticipantsRepository(connection=connection)
    scheduler.add_job(save_organizations, 'interval', (repository,), minutes=config.SCHEDULER_TIMER,
                      next_run_time=datetime.now())
    scheduler.start()


if __name__ == '__main__':
    schedule()
