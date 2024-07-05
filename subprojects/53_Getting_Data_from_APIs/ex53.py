import requests
from pprint import pprint
import sys
import csv

api_url = "http://learncodethehardway.com/api/course"

# list all courses
r = requests.get(api_url)
data = r.json()
pprint(data)

# get one course, full=true includes all modules
r = requests.get(api_url, params={
    "course_id": 1, "full": "true" })

data = r.json()
pprint(data)

# remember with? use it with csv