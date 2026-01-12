import json
from apscheduler.schedulers.background import BackgroundScheduler

STORAGE = "storage.json"

class Scheduler:
    def __init__(self, executor):
        self.executor = executor
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()
        self.jobs = self.load()
        for job in self.jobs:
            self.schedule(job)

    def schedule(self, job):
        h, m = map(int, job["time"].split(":"))
        self.scheduler.add_job(
            self.executor,
            "cron",
            hour=h,
            minute=m,
            args=[job["entity"], job["service"], job.get("data", {})]
        )

    def add(self, job):
        self.jobs.append(job)
        self.schedule(job)
        self.save()

    def list(self):
        return self.jobs

    def save(self):
        with open(STORAGE, "w") as f:
            json.dump(self.jobs, f)

    def load(self):
        try:
            with open(STORAGE) as f:
                return json.load(f)
        except:
            return []
