from date_time.date_time_functionalities import DateTime

class MoveTimeForward():
    def __init__(self, time_fwd: DateTime):
        self.time_fwd = DateTime.future_date()

    def execute(self):
        time = self.time_fwd
        return time
    