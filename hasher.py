import numpy as np
import hashlib

def hash_response(response):
	"""Returns a hash of a response"""
	lst = list(response)
	return hashlib.sha1("".join(sorted(lst)))
  
