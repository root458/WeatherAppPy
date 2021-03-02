from datetime import datetime
from threading import Thread

class TimeDetails(Thread):

    def __init__(self,other):
        super(TimeDetails,self).__init__()
        self.time = datetime.now().strftime('%B, %d %Y %H:%M')
        self.object = other

    def run(self):
        (self.object).set_up_file(self.time)


