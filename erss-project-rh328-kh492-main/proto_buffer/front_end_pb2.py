# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: front_end.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x66ront_end.proto\" \n\x0b\x46PlaceOrder\x12\x11\n\tpackageid\x18\x01 \x02(\x03\"/\n\nFAssociate\x12\x0e\n\x06userid\x18\x01 \x02(\t\x12\x11\n\tpackageid\x18\x02 \x02(\x03\"F\n\tFCommands\x12\x19\n\x03\x62uy\x18\x01 \x01(\x0b\x32\x0c.FPlaceOrder\x12\x1e\n\tassociate\x18\x02 \x01(\x0b\x32\x0b.FAssociate\"\x1d\n\nBResponses\x12\x0f\n\x07isValid\x18\x01 \x02(\x08')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'front_end_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _FPLACEORDER._serialized_start=19
  _FPLACEORDER._serialized_end=51
  _FASSOCIATE._serialized_start=53
  _FASSOCIATE._serialized_end=100
  _FCOMMANDS._serialized_start=102
  _FCOMMANDS._serialized_end=172
  _BRESPONSES._serialized_start=174
  _BRESPONSES._serialized_end=203
# @@protoc_insertion_point(module_scope)