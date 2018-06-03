from apscheduler.schedulers.blocking import BlockingScheduler
import os

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour='9-10', minute='*/2')
def scheduled_job():
    #os.system("scrapy crawlall")
    print('hello')

print('start')
sched.start()
print("end")



