#!/usr/bin/python

## Modules
import json
import redis
from flask import Flask, request


## API Class
class RESTwall:

	## Variables
	port = 8080
	wall = Flask(__name__)

	## Handles requests
	@wall.route('/<id>', methods=['POST', 'GET'])
	def handler(id):
		r = redis.Redis()
		data = request.data
		if request.method == 'POST':
			r.set(id,data)
		data = r.get(id)
		if data == None: data = ''
		return(data)

	## Runs the daemon
	def run(self):
		self.wall.run(host="0.0.0.0", port=self.port)

rest = RESTwall()
rest.run()
