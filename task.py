from celery import Celery
import redis
app = Celery("task",backend="redis://",broker="redis://")
@app.task
def add(x, y):
	print x+y