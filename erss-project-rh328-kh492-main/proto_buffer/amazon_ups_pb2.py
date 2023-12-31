# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: amazon_ups.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x61mazon_ups.proto\"\x1c\n\tAUConnect\x12\x0f\n\x07worldid\x18\x01 \x02(\x03\".\n\x0bUAConnected\x12\x0f\n\x07worldid\x18\x01 \x02(\x03\x12\x0e\n\x06result\x18\x02 \x02(\t\"\\\n\x06\x41Order\x12\n\n\x02id\x18\x01 \x02(\x03\x12\x13\n\x0b\x64\x65scription\x18\x02 \x02(\t\x12\r\n\x05\x63ount\x18\x03 \x02(\x05\x12\t\n\x01x\x18\x04 \x02(\x05\x12\t\n\x01y\x18\x05 \x02(\x05\x12\x0c\n\x04whid\x18\x06 \x02(\x05\"V\n\x0c\x41UPlaceOrder\x12\x0e\n\x06userid\x18\x01 \x01(\t\x12\x16\n\x05order\x18\x02 \x02(\x0b\x32\x07.AOrder\x12\x0e\n\x06shipid\x18\x03 \x02(\x03\x12\x0e\n\x06seqnum\x18\x04 \x02(\x03\"C\n\x11\x41UAssociateUserId\x12\x0e\n\x06userid\x18\x01 \x02(\t\x12\x0e\n\x06shipid\x18\x02 \x02(\x03\x12\x0e\n\x06seqnum\x18\x03 \x02(\x03\"<\n\x0b\x41UCallTruck\x12\r\n\x05whnum\x18\x01 \x02(\x05\x12\x0e\n\x06shipid\x18\x02 \x03(\x03\x12\x0e\n\x06seqnum\x18\x03 \x02(\x03\"?\n\x0eUATruckArrived\x12\x0f\n\x07truckid\x18\x01 \x02(\x05\x12\x0c\n\x04whid\x18\x02 \x02(\x05\x12\x0e\n\x06seqnum\x18\x03 \x02(\x03\"F\n\x13\x41UUpdateTruckStatus\x12\x0f\n\x07truckid\x18\x01 \x02(\x05\x12\x0e\n\x06status\x18\x02 \x02(\t\x12\x0e\n\x06seqnum\x18\x03 \x02(\x03\"C\n\x10\x41UTruckGoDeliver\x12\x0f\n\x07truckid\x18\x01 \x02(\x05\x12\x0e\n\x06shipid\x18\x02 \x03(\x03\x12\x0e\n\x06seqnum\x18\x03 \x02(\x03\"G\n\x15UAUpdatePackageStatus\x12\x0e\n\x06shipid\x18\x01 \x02(\x03\x12\x0e\n\x06status\x18\x02 \x02(\t\x12\x0e\n\x06seqnum\x18\x03 \x02(\x03\"N\n\x16UAUpdatePackageAddress\x12\x0e\n\x06shipid\x18\x01 \x02(\x03\x12\t\n\x01x\x18\x02 \x02(\x05\x12\t\n\x01y\x18\x03 \x02(\x05\x12\x0e\n\x06seqnum\x18\x04 \x02(\x03\"8\n\x03\x45rr\x12\x0b\n\x03\x65rr\x18\x01 \x02(\t\x12\x14\n\x0coriginseqnum\x18\x02 \x02(\x03\x12\x0e\n\x06seqnum\x18\x03 \x02(\x03\"\xf7\x01\n\nAUMessages\x12\x1c\n\x05order\x18\x01 \x03(\x0b\x32\r.AUPlaceOrder\x12+\n\x0f\x61ssociateUserId\x18\x02 \x03(\x0b\x32\x12.AUAssociateUserId\x12\x1f\n\tcallTruck\x18\x03 \x03(\x0b\x32\x0c.AUCallTruck\x12/\n\x11updateTruckStatus\x18\x04 \x03(\x0b\x32\x14.AUUpdateTruckStatus\x12)\n\x0etruckGoDeliver\x18\x05 \x03(\x0b\x32\x11.AUTruckGoDeliver\x12\x13\n\x05\x65rror\x18\x06 \x03(\x0b\x32\x04.Err\x12\x0c\n\x04\x61\x63ks\x18\x07 \x03(\x03\"\xc2\x01\n\nUAMessages\x12%\n\x0ctruckArrived\x18\x01 \x03(\x0b\x32\x0f.UATruckArrived\x12\x33\n\x13updatePackageStatus\x18\x02 \x03(\x0b\x32\x16.UAUpdatePackageStatus\x12\x35\n\x14updatePackageAddress\x18\x03 \x03(\x0b\x32\x17.UAUpdatePackageAddress\x12\x13\n\x05\x65rror\x18\x04 \x03(\x0b\x32\x04.Err\x12\x0c\n\x04\x61\x63ks\x18\x05 \x03(\x03')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'amazon_ups_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _AUCONNECT._serialized_start=20
  _AUCONNECT._serialized_end=48
  _UACONNECTED._serialized_start=50
  _UACONNECTED._serialized_end=96
  _AORDER._serialized_start=98
  _AORDER._serialized_end=190
  _AUPLACEORDER._serialized_start=192
  _AUPLACEORDER._serialized_end=278
  _AUASSOCIATEUSERID._serialized_start=280
  _AUASSOCIATEUSERID._serialized_end=347
  _AUCALLTRUCK._serialized_start=349
  _AUCALLTRUCK._serialized_end=409
  _UATRUCKARRIVED._serialized_start=411
  _UATRUCKARRIVED._serialized_end=474
  _AUUPDATETRUCKSTATUS._serialized_start=476
  _AUUPDATETRUCKSTATUS._serialized_end=546
  _AUTRUCKGODELIVER._serialized_start=548
  _AUTRUCKGODELIVER._serialized_end=615
  _UAUPDATEPACKAGESTATUS._serialized_start=617
  _UAUPDATEPACKAGESTATUS._serialized_end=688
  _UAUPDATEPACKAGEADDRESS._serialized_start=690
  _UAUPDATEPACKAGEADDRESS._serialized_end=768
  _ERR._serialized_start=770
  _ERR._serialized_end=826
  _AUMESSAGES._serialized_start=829
  _AUMESSAGES._serialized_end=1076
  _UAMESSAGES._serialized_start=1079
  _UAMESSAGES._serialized_end=1273
# @@protoc_insertion_point(module_scope)
