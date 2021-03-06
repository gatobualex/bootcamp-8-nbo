class NotesApplication(object):
	def __init__(self,author):
		if author == None:
			self.author = None
		else:
			self.author = author
		self.notes_list = []
		
	def create(self, note_content):
		self.notes_list.append(note_content)
	
	def list(self):
		for position in range(len(self.notes_list)):
			print "Note ID: %s" % position
			print self.notes_list[position]
			print "By Author %s" % self.author
	
	def get(self, note_id):
		return self.notes_list[note_id]
		
	def search(self, search_text):
		print "Showing results for search %s" % search_text
		for position in range(len(self.notes_list)):
			idx = self.notes_list[position].find(search_text, 0, len(self.notes_list))
			if idx >= 0:
				print "Note ID: %s" % position
				print self.notes_list[position]
				print "By Author %s" % self.author
		else:
			print "No result found"
	
	def edit(self, note_id, new_content):
		self.notes_list[note_id] = new_content
	
notes_app = NotesApplication("Alex Magana")
