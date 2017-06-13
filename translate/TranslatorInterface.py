from abc import ABCMeta, abstractmethod

class TranslatorInterface:
    __metaclass__ = ABCMeta

    @abstractmethod
    def translate(self, word, _from, _to): raise NotImplementedError