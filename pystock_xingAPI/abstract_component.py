#abstract_component.py
import threading

class AbstractComponent:
	logger = None
	def init(self):
		pass
	def finalize(self):
		pass

class AbstractQueryProviderComponent(AbstractComponent):
	async_query_availabale = False
	def getAvailableQueryCodeSet(self):
		raise NotImplementedError('You have to override AbstractQueryProviderComponent.getAvailableQuerySet method')
	def query(self, query_code, arg_set):
		raise NotImplementedError('You have to override AbstractQueryProviderComponent.query method')

class AbstractSubscriptionProviderComponent(AbstractComponent):
	def getAvailableSubscriptionCodeSet(self):
		raise NotImplementedError('You have to override AbstractSubscriptionProviderComponent.getAvailableSubscriptionSet method')
	def subscribe(self, subscribe_code, arg_set, queue):
		raise NotImplementedError('You have to override AbstractSubscriptionProviderComponent.subscribe method')
	def unsubscribe(self, subscribe_code, arg_set, queue):
		raise NotImplementedError('You have to override AbstractSubscriptionProviderComponent.unsubscribe method')