from TaskList.models import Tasks

class DeleteRecordClass:
	def __init__( self, request ):
		self.request 	= request
		self.id 		= request.GET.get('id', False)
		
	def validation( self ):
		if not self.request.user.is_authenticated: return 'Użytkownik musi być zalogowany'
		
		try: 
			username = self.request.user.username
			obj = Tasks.objects.get(id=self.id)

		except:
			return 'Rekord nie istnieje'
		
		return True
		
	def delete( self ):
		validation = self.validation()
		if not isinstance(validation, bool): return validation
		
		user = Tasks.objects.filter(id=self.id)
		user.delete()
		
		return True