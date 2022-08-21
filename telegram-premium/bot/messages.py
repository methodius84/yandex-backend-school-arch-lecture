import abc
from cgitb import text

import telegram as tg
import telegram.ext as tg_ext 

class BaseMessages(abc.ABC):
    @abc.abstractmethod
    def start(self) -> str:
        raise NotImplemented
    
    @abc.abstractmethod
    def help(self) -> str:
        raise NotImplemented

    @abc.abstractmethod
    def echo(self, text:str) -> str:
        raise NotImplemented

class RegularUser(BaseMessages):
    def start(self) -> str:
        return 'Privet!'

    def help(self) -> str:
        return 'Вам нужно приобрести подписку, чтобы общаться со мной'

    def echo(self, text:str) -> str:
        return 'Вам нужно приобрести подписку, чтобы общаться со мной'

class PremiumUser(RegularUser):
    def start(self) -> str:
        return 'Здравствуйте!'

    def help(self) -> str:
        return 'Скоро свяжусь с тобой!'

    def echo(self, text:str) -> str:
        return f'{text}'

def get_messages(user: tg.User) -> BaseMessages:
    if user.is_premium:
        return PremiumUser()
    return RegularUser()