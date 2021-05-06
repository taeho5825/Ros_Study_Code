"""augogenerated by genpy from basics/WordCountRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

class WordCountRequest(genpy.Message):
    _md5sum = "6f897d3845272d18053a750c1cfb862a"
    _type = "basics/WordCountRequest"
    _has_header = False #flag to mark the presence of a Header object
"""
    __slot__ = ['words']
    _slot_types = ['string']

    def __init__(self, *args, **kwds):
        """
        Constructor. Any message fields that are implicitly/explicitly
        set to None will be assigned a default value. The recommend
        use is keyword arguments as this is more robust to future message
        changes. You cannot mix in-order arguments and keyword arguments.

        The available fileds are:
            words

        :param args: complete set of field values, in .msg order
        :param kwds: use keyword arguments corresponding to message field names
        to set specific fields.
        """
        if args or kwds:
            super(WordCountRequest, self).__init__(*args, **kwds)
            #message fields cannot be None, assign default values for those that are
        if self.words is None:
            self.words = ''
        else:
            self.words = ''

        def _get_types(self):
            ..."""
        
        def serialize(self, buff):
            ...
        def deserialize(self, str):
            ...
        def serialize_numpy(self, buff, numpy):
            ...
        def deserialize_numpy(self, str, numpy):
            ...
class WordCountRequest(genpy.Message):
    ...

class WordCount(genpy.Message):
    ...

