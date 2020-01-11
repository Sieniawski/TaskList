from TaskList.models import Tasks

class AddTaskClass:
	def __init__( self, request ):
		self.request 	= request
		self.task 			= request.POST.get('Task', False)
		self.date 			= request.POST.get('Date', False)
		self.priority 		= request.POST.get('Priority', False)
		self.type 			= request.POST.get('Type', False)
		
		self.errors = []
		
	def validation( self ):
		if not self.task: self.errors.append("Proszę wypełnić pole 'Zadanie'!")
		if not self.date: self.errors.append("Proszę wypełnić pole 'Data'!")
		if not self.priority: self.errors.append("Proszę wypełnić pole 'Priorytet'!")
		if not self.type: self.errors.append("Proszę wypełnić pole 'Rodzaj'!")
		
	def addTask( self ):
		self.validation()
		
		if len(self.errors) > 0: 
			return self.errors
		
		record = Tasks(
			Task 		= self.task, 
			Date 		= self.date,
			Priority 	= self.priority,
			Type		= self.type,
			AddedBy		= self.request.user.username
		)
		record.save()
		
		return True
		