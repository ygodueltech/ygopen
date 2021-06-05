# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: net_common.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='net_common.proto',
  package='YGOpen.Proto.Net',
  syntax='proto3',
  serialized_options=b'H\003\370\001\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10net_common.proto\x12\x10YGOpen.Proto.Net\" \n\x04User\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\"\x0e\n\x0cServerPacketB\x05H\x03\xf8\x01\x01\x62\x06proto3'
)




_USER = _descriptor.Descriptor(
  name='User',
  full_name='YGOpen.Proto.Net.User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='YGOpen.Proto.Net.User.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='YGOpen.Proto.Net.User.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=70,
)


_SERVERPACKET = _descriptor.Descriptor(
  name='ServerPacket',
  full_name='YGOpen.Proto.Net.ServerPacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=86,
)

DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['ServerPacket'] = _SERVERPACKET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'net_common_pb2'
  # @@protoc_insertion_point(class_scope:YGOpen.Proto.Net.User)
  })
_sym_db.RegisterMessage(User)

ServerPacket = _reflection.GeneratedProtocolMessageType('ServerPacket', (_message.Message,), {
  'DESCRIPTOR' : _SERVERPACKET,
  '__module__' : 'net_common_pb2'
  # @@protoc_insertion_point(class_scope:YGOpen.Proto.Net.ServerPacket)
  })
_sym_db.RegisterMessage(ServerPacket)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
