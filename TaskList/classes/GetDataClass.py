from TaskList.models import Tasks

class GetDataClass:
	def __init__( self, request ):
		self.request 	= request
		
	def getData( self ):
		rows = Tasks.objects.filter(AddedBy=self.request.user.username).order_by('Date')
		return rows