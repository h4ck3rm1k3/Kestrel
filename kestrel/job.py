class Job :
    def __init__(self, jobid):
        self.jobid=jobid

    #@property
    def requires(self):
        return []
