from abc import ABC, abstractmethod
from admin import AdminQuery
from clerk import AttendantQuery

class InterfaceUser(ABC):

    @abstractmethod
    def type_user(self):
        pass
