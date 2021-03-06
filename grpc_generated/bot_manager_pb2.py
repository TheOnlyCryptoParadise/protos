# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bot_manager.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import bot_comm_pb2 as bot__comm__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='bot_manager.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11\x62ot_manager.proto\x1a\x0e\x62ot_comm.proto\"\x89\x01\n\x10\x43reateBotRequest\x12\x0e\n\x06userId\x18\x01 \x01(\x04\x12\x0f\n\x07\x62otName\x18\x02 \x01(\t\x12\x14\n\x0cstrategyName\x18\x03 \x01(\t\x12\x12\n\nconfigName\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x15\n\rpostponeStart\x18\x06 \x01(\x08\"1\n\x10UpdateStrRequest\x12\r\n\x05\x62otId\x18\x01 \x01(\x04\x12\x0e\n\x06newStr\x18\x02 \x01(\t\"\x87\x01\n\x11\x43reateBotResponse\x12\r\n\x05\x62otId\x18\x01 \x01(\x04\x12\x0e\n\x06userId\x18\x02 \x01(\x04\x12\x0f\n\x07\x62otName\x18\x03 \x01(\t\x12 \n\x06status\x18\x04 \x01(\x0e\x32\x10.OperationStatus\x12\x14\n\x07message\x18\x05 \x01(\tH\x00\x88\x01\x01\x42\n\n\x08_message\"\x9f\x01\n\x18\x42otStatusAddressResponse\x12\r\n\x05\x62otId\x18\x01 \x01(\x04\x12\x1d\n\tbotStatus\x18\x02 \x01(\x0e\x32\n.BotStatus\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x01(\t\x12\"\n\x08opStatus\x18\x04 \x01(\x0e\x32\x10.OperationStatus\x12\x14\n\x07message\x18\x05 \x01(\tH\x00\x88\x01\x01\x42\n\n\x08_message\"?\n\x0f\x42otStatusStruct\x12\r\n\x05\x62otId\x18\x01 \x01(\x04\x12\x1d\n\tbotStatus\x18\x02 \x01(\x0e\x32\n.BotStatus\"\x81\x01\n\x14\x42otsStatusesResponse\x12#\n\tbotStatus\x18\x01 \x03(\x0b\x32\x10.BotStatusStruct\x12\"\n\x08opStatus\x18\x02 \x01(\x0e\x32\x10.OperationStatus\x12\x14\n\x07message\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\n\n\x08_message\"/\n\rBotNameStruct\x12\r\n\x05\x62otId\x18\x01 \x01(\x04\x12\x0f\n\x07\x62otName\x18\x02 \x01(\t\"{\n\x11\x42otsNamesResponse\x12 \n\x08\x62otNames\x18\x01 \x03(\x0b\x32\x0e.BotNameStruct\x12\"\n\x08opStatus\x18\x02 \x01(\x0e\x32\x10.OperationStatus\x12\x14\n\x07message\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\n\n\x08_message\"\x9c\x02\n\x0f\x42otInfoResponse\x12\r\n\x05\x62otId\x18\x01 \x01(\x04\x12\x0e\n\x06userId\x18\x02 \x01(\x04\x12\x0f\n\x07\x62otName\x18\x03 \x01(\t\x12\x14\n\x0cstrategyName\x18\x04 \x01(\t\x12\x12\n\nconfigName\x18\x05 \x01(\t\x12\r\n\x05pairs\x18\x06 \x03(\t\x12\x1d\n\tbotStatus\x18\x07 \x01(\x0e\x32\n.BotStatus\x12\x14\n\x0c\x63reationTime\x18\x08 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\t \x01(\t\x12\'\n\x08opStatus\x18\n \x01(\x0e\x32\x10.OperationStatusH\x00\x88\x01\x01\x12\x14\n\x07message\x18\x0b \x01(\tH\x01\x88\x01\x01\x42\x0b\n\t_opStatusB\n\n\x08_message\"|\n\x10\x46ullInfoResponse\x12\"\n\x08\x62otsInfo\x18\x01 \x03(\x0b\x32\x10.BotInfoResponse\x12\"\n\x08opStatus\x18\x02 \x01(\x0e\x32\x10.OperationStatus\x12\x14\n\x07message\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\n\n\x08_message*1\n\tBotStatus\x12\x0b\n\x07RUNNING\x10\x00\x12\n\n\x06PAUSED\x10\x01\x12\x0b\n\x07STOPPED\x10\x02\x32\x8e\x05\n\x16\x42otManagerCommunicator\x12\x34\n\tCreateBot\x12\x11.CreateBotRequest\x1a\x12.CreateBotResponse\"\x00\x12(\n\tRemoveBot\x12\x0b.BotRequest\x1a\x0c.BotResponse\"\x00\x12(\n\tResumeBot\x12\x0b.BotRequest\x1a\x0c.BotResponse\"\x00\x12\'\n\x08PauseBot\x12\x0b.BotRequest\x1a\x0c.BotResponse\"\x00\x12&\n\x07StopBot\x12\x0b.BotRequest\x1a\x0c.BotResponse\"\x00\x12.\n\tRenameBot\x12\x11.UpdateStrRequest\x1a\x0c.BotResponse\"\x00\x12\x39\n\x14UpdateBotDescription\x12\x11.UpdateStrRequest\x1a\x0c.BotResponse\"\x00\x12<\n\x0fGetBotsStatuses\x12\x10.BotsDataRequest\x1a\x15.BotsStatusesResponse\"\x00\x12\x36\n\x0cGetBotsNames\x12\x10.BotsDataRequest\x1a\x12.BotsNamesResponse\"\x00\x12-\n\nGetBotInfo\x12\x0b.BotRequest\x1a\x10.BotInfoResponse\"\x00\x12\x34\n\x0bGetFullInfo\x12\x10.BotsDataRequest\x1a\x11.FullInfoResponse\"\x00\x12\x18\n\x04Ping\x12\x06.Empty\x1a\x06.Empty\"\x00\x12\x39\n\rGetBotAddress\x12\x0b.BotRequest\x1a\x19.BotStatusAddressResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[bot__comm__pb2.DESCRIPTOR,])

_BOTSTATUS = _descriptor.EnumDescriptor(
  name='BotStatus',
  full_name='BotStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RUNNING', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PAUSED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STOPPED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1312,
  serialized_end=1361,
)
_sym_db.RegisterEnumDescriptor(_BOTSTATUS)

BotStatus = enum_type_wrapper.EnumTypeWrapper(_BOTSTATUS)
RUNNING = 0
PAUSED = 1
STOPPED = 2



_CREATEBOTREQUEST = _descriptor.Descriptor(
  name='CreateBotRequest',
  full_name='CreateBotRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userId', full_name='CreateBotRequest.userId', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='botName', full_name='CreateBotRequest.botName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='strategyName', full_name='CreateBotRequest.strategyName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='configName', full_name='CreateBotRequest.configName', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='CreateBotRequest.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='postponeStart', full_name='CreateBotRequest.postponeStart', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_end=175,
)


_UPDATESTRREQUEST = _descriptor.Descriptor(
  name='UpdateStrRequest',
  full_name='UpdateStrRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='botId', full_name='UpdateStrRequest.botId', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='newStr', full_name='UpdateStrRequest.newStr', index=1,
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
  serialized_start=177,
  serialized_end=226,
)


_CREATEBOTRESPONSE = _descriptor.Descriptor(
  name='CreateBotResponse',
  full_name='CreateBotResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='botId', full_name='CreateBotResponse.botId', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='userId', full_name='CreateBotResponse.userId', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='botName', full_name='CreateBotResponse.botName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='CreateBotResponse.status', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='CreateBotResponse.message', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
    _descriptor.OneofDescriptor(
      name='_message', full_name='CreateBotResponse._message',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=229,
  serialized_end=364,
)


_BOTSTATUSADDRESSRESPONSE = _descriptor.Descriptor(
  name='BotStatusAddressResponse',
  full_name='BotStatusAddressResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='botId', full_name='BotStatusAddressResponse.botId', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='botStatus', full_name='BotStatusAddressResponse.botStatus', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='BotStatusAddressResponse.address', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='opStatus', full_name='BotStatusAddressResponse.opStatus', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='BotStatusAddressResponse.message', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
    _descriptor.OneofDescriptor(
      name='_message', full_name='BotStatusAddressResponse._message',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=367,
  serialized_end=526,
)


_BOTSTATUSSTRUCT = _descriptor.Descriptor(
  name='BotStatusStruct',
  full_name='BotStatusStruct',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='botId', full_name='BotStatusStruct.botId', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='botStatus', full_name='BotStatusStruct.botStatus', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=528,
  serialized_end=591,
)


_BOTSSTATUSESRESPONSE = _descriptor.Descriptor(
  name='BotsStatusesResponse',
  full_name='BotsStatusesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='botStatus', full_name='BotsStatusesResponse.botStatus', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='opStatus', full_name='BotsStatusesResponse.opStatus', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='BotsStatusesResponse.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
    _descriptor.OneofDescriptor(
      name='_message', full_name='BotsStatusesResponse._message',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=594,
  serialized_end=723,
)


_BOTNAMESTRUCT = _descriptor.Descriptor(
  name='BotNameStruct',
  full_name='BotNameStruct',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='botId', full_name='BotNameStruct.botId', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='botName', full_name='BotNameStruct.botName', index=1,
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
  serialized_start=725,
  serialized_end=772,
)


_BOTSNAMESRESPONSE = _descriptor.Descriptor(
  name='BotsNamesResponse',
  full_name='BotsNamesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='botNames', full_name='BotsNamesResponse.botNames', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='opStatus', full_name='BotsNamesResponse.opStatus', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='BotsNamesResponse.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
    _descriptor.OneofDescriptor(
      name='_message', full_name='BotsNamesResponse._message',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=774,
  serialized_end=897,
)


_BOTINFORESPONSE = _descriptor.Descriptor(
  name='BotInfoResponse',
  full_name='BotInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='botId', full_name='BotInfoResponse.botId', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='userId', full_name='BotInfoResponse.userId', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='botName', full_name='BotInfoResponse.botName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='strategyName', full_name='BotInfoResponse.strategyName', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='configName', full_name='BotInfoResponse.configName', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pairs', full_name='BotInfoResponse.pairs', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='botStatus', full_name='BotInfoResponse.botStatus', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='creationTime', full_name='BotInfoResponse.creationTime', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='BotInfoResponse.description', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='opStatus', full_name='BotInfoResponse.opStatus', index=9,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='BotInfoResponse.message', index=10,
      number=11, type=9, cpp_type=9, label=1,
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
    _descriptor.OneofDescriptor(
      name='_opStatus', full_name='BotInfoResponse._opStatus',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_message', full_name='BotInfoResponse._message',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=900,
  serialized_end=1184,
)


_FULLINFORESPONSE = _descriptor.Descriptor(
  name='FullInfoResponse',
  full_name='FullInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='botsInfo', full_name='FullInfoResponse.botsInfo', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='opStatus', full_name='FullInfoResponse.opStatus', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='FullInfoResponse.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
    _descriptor.OneofDescriptor(
      name='_message', full_name='FullInfoResponse._message',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1186,
  serialized_end=1310,
)

_CREATEBOTRESPONSE.fields_by_name['status'].enum_type = bot__comm__pb2._OPERATIONSTATUS
_CREATEBOTRESPONSE.oneofs_by_name['_message'].fields.append(
  _CREATEBOTRESPONSE.fields_by_name['message'])
_CREATEBOTRESPONSE.fields_by_name['message'].containing_oneof = _CREATEBOTRESPONSE.oneofs_by_name['_message']
_BOTSTATUSADDRESSRESPONSE.fields_by_name['botStatus'].enum_type = _BOTSTATUS
_BOTSTATUSADDRESSRESPONSE.fields_by_name['opStatus'].enum_type = bot__comm__pb2._OPERATIONSTATUS
_BOTSTATUSADDRESSRESPONSE.oneofs_by_name['_message'].fields.append(
  _BOTSTATUSADDRESSRESPONSE.fields_by_name['message'])
_BOTSTATUSADDRESSRESPONSE.fields_by_name['message'].containing_oneof = _BOTSTATUSADDRESSRESPONSE.oneofs_by_name['_message']
_BOTSTATUSSTRUCT.fields_by_name['botStatus'].enum_type = _BOTSTATUS
_BOTSSTATUSESRESPONSE.fields_by_name['botStatus'].message_type = _BOTSTATUSSTRUCT
_BOTSSTATUSESRESPONSE.fields_by_name['opStatus'].enum_type = bot__comm__pb2._OPERATIONSTATUS
_BOTSSTATUSESRESPONSE.oneofs_by_name['_message'].fields.append(
  _BOTSSTATUSESRESPONSE.fields_by_name['message'])
_BOTSSTATUSESRESPONSE.fields_by_name['message'].containing_oneof = _BOTSSTATUSESRESPONSE.oneofs_by_name['_message']
_BOTSNAMESRESPONSE.fields_by_name['botNames'].message_type = _BOTNAMESTRUCT
_BOTSNAMESRESPONSE.fields_by_name['opStatus'].enum_type = bot__comm__pb2._OPERATIONSTATUS
_BOTSNAMESRESPONSE.oneofs_by_name['_message'].fields.append(
  _BOTSNAMESRESPONSE.fields_by_name['message'])
_BOTSNAMESRESPONSE.fields_by_name['message'].containing_oneof = _BOTSNAMESRESPONSE.oneofs_by_name['_message']
_BOTINFORESPONSE.fields_by_name['botStatus'].enum_type = _BOTSTATUS
_BOTINFORESPONSE.fields_by_name['opStatus'].enum_type = bot__comm__pb2._OPERATIONSTATUS
_BOTINFORESPONSE.oneofs_by_name['_opStatus'].fields.append(
  _BOTINFORESPONSE.fields_by_name['opStatus'])
_BOTINFORESPONSE.fields_by_name['opStatus'].containing_oneof = _BOTINFORESPONSE.oneofs_by_name['_opStatus']
_BOTINFORESPONSE.oneofs_by_name['_message'].fields.append(
  _BOTINFORESPONSE.fields_by_name['message'])
_BOTINFORESPONSE.fields_by_name['message'].containing_oneof = _BOTINFORESPONSE.oneofs_by_name['_message']
_FULLINFORESPONSE.fields_by_name['botsInfo'].message_type = _BOTINFORESPONSE
_FULLINFORESPONSE.fields_by_name['opStatus'].enum_type = bot__comm__pb2._OPERATIONSTATUS
_FULLINFORESPONSE.oneofs_by_name['_message'].fields.append(
  _FULLINFORESPONSE.fields_by_name['message'])
_FULLINFORESPONSE.fields_by_name['message'].containing_oneof = _FULLINFORESPONSE.oneofs_by_name['_message']
DESCRIPTOR.message_types_by_name['CreateBotRequest'] = _CREATEBOTREQUEST
DESCRIPTOR.message_types_by_name['UpdateStrRequest'] = _UPDATESTRREQUEST
DESCRIPTOR.message_types_by_name['CreateBotResponse'] = _CREATEBOTRESPONSE
DESCRIPTOR.message_types_by_name['BotStatusAddressResponse'] = _BOTSTATUSADDRESSRESPONSE
DESCRIPTOR.message_types_by_name['BotStatusStruct'] = _BOTSTATUSSTRUCT
DESCRIPTOR.message_types_by_name['BotsStatusesResponse'] = _BOTSSTATUSESRESPONSE
DESCRIPTOR.message_types_by_name['BotNameStruct'] = _BOTNAMESTRUCT
DESCRIPTOR.message_types_by_name['BotsNamesResponse'] = _BOTSNAMESRESPONSE
DESCRIPTOR.message_types_by_name['BotInfoResponse'] = _BOTINFORESPONSE
DESCRIPTOR.message_types_by_name['FullInfoResponse'] = _FULLINFORESPONSE
DESCRIPTOR.enum_types_by_name['BotStatus'] = _BOTSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateBotRequest = _reflection.GeneratedProtocolMessageType('CreateBotRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEBOTREQUEST,
  '__module__' : 'bot_manager_pb2'
  # @@protoc_insertion_point(class_scope:CreateBotRequest)
  })
_sym_db.RegisterMessage(CreateBotRequest)

UpdateStrRequest = _reflection.GeneratedProtocolMessageType('UpdateStrRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATESTRREQUEST,
  '__module__' : 'bot_manager_pb2'
  # @@protoc_insertion_point(class_scope:UpdateStrRequest)
  })
_sym_db.RegisterMessage(UpdateStrRequest)

CreateBotResponse = _reflection.GeneratedProtocolMessageType('CreateBotResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEBOTRESPONSE,
  '__module__' : 'bot_manager_pb2'
  # @@protoc_insertion_point(class_scope:CreateBotResponse)
  })
_sym_db.RegisterMessage(CreateBotResponse)

BotStatusAddressResponse = _reflection.GeneratedProtocolMessageType('BotStatusAddressResponse', (_message.Message,), {
  'DESCRIPTOR' : _BOTSTATUSADDRESSRESPONSE,
  '__module__' : 'bot_manager_pb2'
  # @@protoc_insertion_point(class_scope:BotStatusAddressResponse)
  })
_sym_db.RegisterMessage(BotStatusAddressResponse)

BotStatusStruct = _reflection.GeneratedProtocolMessageType('BotStatusStruct', (_message.Message,), {
  'DESCRIPTOR' : _BOTSTATUSSTRUCT,
  '__module__' : 'bot_manager_pb2'
  # @@protoc_insertion_point(class_scope:BotStatusStruct)
  })
_sym_db.RegisterMessage(BotStatusStruct)

BotsStatusesResponse = _reflection.GeneratedProtocolMessageType('BotsStatusesResponse', (_message.Message,), {
  'DESCRIPTOR' : _BOTSSTATUSESRESPONSE,
  '__module__' : 'bot_manager_pb2'
  # @@protoc_insertion_point(class_scope:BotsStatusesResponse)
  })
_sym_db.RegisterMessage(BotsStatusesResponse)

BotNameStruct = _reflection.GeneratedProtocolMessageType('BotNameStruct', (_message.Message,), {
  'DESCRIPTOR' : _BOTNAMESTRUCT,
  '__module__' : 'bot_manager_pb2'
  # @@protoc_insertion_point(class_scope:BotNameStruct)
  })
_sym_db.RegisterMessage(BotNameStruct)

BotsNamesResponse = _reflection.GeneratedProtocolMessageType('BotsNamesResponse', (_message.Message,), {
  'DESCRIPTOR' : _BOTSNAMESRESPONSE,
  '__module__' : 'bot_manager_pb2'
  # @@protoc_insertion_point(class_scope:BotsNamesResponse)
  })
_sym_db.RegisterMessage(BotsNamesResponse)

BotInfoResponse = _reflection.GeneratedProtocolMessageType('BotInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _BOTINFORESPONSE,
  '__module__' : 'bot_manager_pb2'
  # @@protoc_insertion_point(class_scope:BotInfoResponse)
  })
_sym_db.RegisterMessage(BotInfoResponse)

FullInfoResponse = _reflection.GeneratedProtocolMessageType('FullInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _FULLINFORESPONSE,
  '__module__' : 'bot_manager_pb2'
  # @@protoc_insertion_point(class_scope:FullInfoResponse)
  })
_sym_db.RegisterMessage(FullInfoResponse)



_BOTMANAGERCOMMUNICATOR = _descriptor.ServiceDescriptor(
  name='BotManagerCommunicator',
  full_name='BotManagerCommunicator',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1364,
  serialized_end=2018,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateBot',
    full_name='BotManagerCommunicator.CreateBot',
    index=0,
    containing_service=None,
    input_type=_CREATEBOTREQUEST,
    output_type=_CREATEBOTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RemoveBot',
    full_name='BotManagerCommunicator.RemoveBot',
    index=1,
    containing_service=None,
    input_type=bot__comm__pb2._BOTREQUEST,
    output_type=bot__comm__pb2._BOTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ResumeBot',
    full_name='BotManagerCommunicator.ResumeBot',
    index=2,
    containing_service=None,
    input_type=bot__comm__pb2._BOTREQUEST,
    output_type=bot__comm__pb2._BOTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='PauseBot',
    full_name='BotManagerCommunicator.PauseBot',
    index=3,
    containing_service=None,
    input_type=bot__comm__pb2._BOTREQUEST,
    output_type=bot__comm__pb2._BOTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StopBot',
    full_name='BotManagerCommunicator.StopBot',
    index=4,
    containing_service=None,
    input_type=bot__comm__pb2._BOTREQUEST,
    output_type=bot__comm__pb2._BOTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RenameBot',
    full_name='BotManagerCommunicator.RenameBot',
    index=5,
    containing_service=None,
    input_type=_UPDATESTRREQUEST,
    output_type=bot__comm__pb2._BOTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateBotDescription',
    full_name='BotManagerCommunicator.UpdateBotDescription',
    index=6,
    containing_service=None,
    input_type=_UPDATESTRREQUEST,
    output_type=bot__comm__pb2._BOTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetBotsStatuses',
    full_name='BotManagerCommunicator.GetBotsStatuses',
    index=7,
    containing_service=None,
    input_type=bot__comm__pb2._BOTSDATAREQUEST,
    output_type=_BOTSSTATUSESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetBotsNames',
    full_name='BotManagerCommunicator.GetBotsNames',
    index=8,
    containing_service=None,
    input_type=bot__comm__pb2._BOTSDATAREQUEST,
    output_type=_BOTSNAMESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetBotInfo',
    full_name='BotManagerCommunicator.GetBotInfo',
    index=9,
    containing_service=None,
    input_type=bot__comm__pb2._BOTREQUEST,
    output_type=_BOTINFORESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetFullInfo',
    full_name='BotManagerCommunicator.GetFullInfo',
    index=10,
    containing_service=None,
    input_type=bot__comm__pb2._BOTSDATAREQUEST,
    output_type=_FULLINFORESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Ping',
    full_name='BotManagerCommunicator.Ping',
    index=11,
    containing_service=None,
    input_type=bot__comm__pb2._EMPTY,
    output_type=bot__comm__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetBotAddress',
    full_name='BotManagerCommunicator.GetBotAddress',
    index=12,
    containing_service=None,
    input_type=bot__comm__pb2._BOTREQUEST,
    output_type=_BOTSTATUSADDRESSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BOTMANAGERCOMMUNICATOR)

DESCRIPTOR.services_by_name['BotManagerCommunicator'] = _BOTMANAGERCOMMUNICATOR

# @@protoc_insertion_point(module_scope)
