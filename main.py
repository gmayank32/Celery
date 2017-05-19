import task


for i in xrange(100000):

	task.add.delay(i,i+1)