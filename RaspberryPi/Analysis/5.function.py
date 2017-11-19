doc=""

print(doc)

def fuck():
	global doc
	doc = "done!"

fuck()

print(doc)
