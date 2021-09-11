from abc import ABC
import pickle


class Sala:

	def __init__(self, id_sala: int, numero: str):

		if isinstance(id_sala, int):
			self.__id_sala = id_sala

		if isinstance(numero, str):
			self.__numero = numero

	@property
	def id_sala(self):
		return self.__id_sala

	@property
	def numero(self):
		return self.__numero

	@numero.setter
	def numero(self, numero: str):

		if isinstance(numero, str):
			self.__numero = numero


class DAO(ABC):
	def __init__(self, datasource=''):
		self.__datasource = datasource
		self.__cache = {}
		try:
			self.__load()
		except FileNotFoundError:
			self.__dump()

	def __dump(self):
		pickle.dump(self.__cache, open(self.__datasource, 'wb'))

	def __load(self):
		self.__cache = pickle.load(open(self.__datasource, 'rb'))

	def add(self, key, obj):
		self.__cache[key] = obj
		self.__dump()

	def get(self, key):
		try:
			return self.__cache[key]
		except KeyError:
			pass

	def remove(self, key):
		try:
			self.__cache.pop(key)
			self.__dump()
		except KeyError:
			pass

	def get_all(self):
		return self.__cache.values()

class SalaDAO(DAO):
	def __init__(self):
		super().__init__('salas.pkl')

	def add(self, Sala: int):
		if (isinstance(Sala.id_sala, int)) and (Sala is not None) and isinstance(Sala, Sala.id_sala):
			super().add(Sala.id_sala, Sala)

	def get(self, key: int):
		if isinstance(key, int):
			return super().get(key)

	def remove(self, key: int):
		if isinstance(key, int):
			return super().remove(key)
