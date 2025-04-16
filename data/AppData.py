from typing import final
from abc import ABC, abstractmethod

@final
class AppData:
    
    def __init__(self, path: str, urls: list[str]):
        self.__path = path
        self.__urls = [] if urls == None else urls
        
    @property
    def path(self):
        return self.__path
    
    @property
    def urls(self):
        return self.__urls
    
