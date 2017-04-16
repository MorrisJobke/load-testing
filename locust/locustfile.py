from locust import HttpLocust, TaskSet, task
from requests.auth import HTTPBasicAuth
import requests
import random

class UserBehavior(TaskSet):
    auth = None

    def on_start(self):
        i = random.randint(0, 201)
        self.user = 'user' + '{:03d}'.format(i)
        print self.user
        self.auth = HTTPBasicAuth(self.user, 'abc123abc!')

    #@task(10)
    def propfind(self):
        self.client.request("PROPFIND", "/remote.php/webdav", auth=self.auth)

    #@task(1)
    def uploadSmall(self):
        filename = str(random.randint(0, 50000)) + "small.dat"
        with open('/tmp/sample-small.dat', 'rb') as f:
            response = self.client.put("/remote.php/dav/files/" + self.user + "/" + filename,
                                       auth=self.auth, data=f, name="/remote.php/dav/files/[user]/small.dat")

        if r.status_code != requests.codes.created:
            return

        for i in range(0, 5):
            self.client.get("/remote.php/dav/files/" + self.user + "/" + filename,
                            auth=self.auth, name="/remote.php/dav/files/[user]/small.dat")

        self.client.delete("/remote.php/dav/files/" + self.user + "/" + filename,
                           auth=self.auth, name="/remote.php/dav/files/[user]/small.dat")

    @task(1)
    def uploadMedium(self):
        filename = str(random.randint(0, 50000)) + "medium.dat"
        with open('/tmp/sample-medium.dat', 'rb') as f:
            response = self.client.put("/remote.php/dav/files/" + self.user + "/" + filename,
                                auth=self.auth, data=f, name="/remote.php/dav/files/[user]/medium.dat")
        
        if response.status_code != requests.codes.created:
            return

        #for i in range(0, 5):
        #    self.client.get("/remote.php/dav/files/" + self.user + "/" + filename,
        #                    auth=self.auth, name="/remote.php/dav/files/[user]/medium.dat")

        self.client.delete("/remote.php/dav/files/" + self.user + "/" + filename,
                           auth=self.auth, name="/remote.php/dav/files/[user]/medium.dat")

    #@task(1)
    def uploadLarge(self):
        filename = str(random.randint(0, 50000)) + "large.dat"
        with open('/tmp/sample-large.dat', 'rb') as f:
            response = self.client.put("/remote.php/dav/files/" + self.user + "/" + filename,
                                auth=self.auth, data=f, name="/remote.php/dav/files/[user]/large.dat")


        if response.status_code != requests.codes.created:
            return

        #for i in range(0, 1):
        self.client.get("/remote.php/dav/files/" + self.user + "/" + filename,
                        auth=self.auth, name="/remote.php/dav/files/[user]/large.dat")

        self.client.delete("/remote.php/dav/files/" + self.user + "/" + filename,
                           auth=self.auth, name="/remote.php/dav/files/[user]/large.dat")
class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 500
    max_wait = 1000

"""
dd if=/dev/urandom of=/tmp/sample-small.dat bs=756938 count=1 
dd if=/dev/urandom of=/tmp/sample-medium.dat bs=4569380 count=1
dd if=/dev/urandom of=/tmp/sample-large.dat bs=34549338 count=10
"""
