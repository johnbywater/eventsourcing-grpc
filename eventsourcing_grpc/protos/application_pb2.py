# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: eventsourcing_grpc/protos/application.proto
"""Generated protocol buffer code."""
from google.protobuf import (
    descriptor as _descriptor,
    descriptor_pool as _descriptor_pool,
    message as _message,
    reflection as _reflection,
    symbol_database as _symbol_database,
)

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n+eventsourcing_grpc/protos/application.proto\x12\x12\x65ventsourcing_grpc"\x07\n\x05\x45mpty"B\n\rMethodRequest\x12\x13\n\x0bmethod_name\x18\x01'
    b" \x01(\t\x12\x0c\n\x04\x61rgs\x18\x02 \x01(\x0c\x12\x0e\n\x06kwargs\x18\x03"
    b' \x01(\x0c"\x1b\n\x0bMethodReply\x12\x0c\n\x04\x64\x61ta\x18\x01'
    b' \x01(\x0c"D\n\x14NotificationsRequest\x12\r\n\x05start\x18\x01'
    b" \x01(\t\x12\r\n\x05limit\x18\x02 \x01(\t\x12\x0e\n\x06topics\x18\x03"
    b' \x03(\t"k\n\x0cNotification\x12\n\n\x02id\x18\x01'
    b" \x01(\t\x12\x15\n\roriginator_id\x18\x02"
    b" \x01(\t\x12\x1a\n\x12originator_version\x18\x03 \x01(\t\x12\r\n\x05topic\x18\x04"
    b" \x01(\t\x12\r\n\x05state\x18\x05"
    b' \x01(\x0c"M\n\x12NotificationsReply\x12\x37\n\rnotifications\x18\x01'
    b" \x03(\x0b\x32"
    b' .eventsourcing_grpc.Notification2\x94\x02\n\x0b\x41pplication\x12>\n\x04Ping\x12\x19.eventsourcing_grpc.Empty\x1a\x19.eventsourcing_grpc.Empty"\x00\x12]\n\x15\x43\x61llApplicationMethod\x12!.eventsourcing_grpc.MethodRequest\x1a\x1f.eventsourcing_grpc.MethodReply"\x00\x12\x66\n\x10GetNotifications\x12(.eventsourcing_grpc.NotificationsRequest\x1a&.eventsourcing_grpc.NotificationsReply"\x00\x42=\n!io.eventsourcing_grpc.applicationB\x10\x41pplicationProtoP\x01\xa2\x02\x03\x45SAb\x06proto3'
)


_EMPTY = DESCRIPTOR.message_types_by_name["Empty"]
_METHODREQUEST = DESCRIPTOR.message_types_by_name["MethodRequest"]
_METHODREPLY = DESCRIPTOR.message_types_by_name["MethodReply"]
_NOTIFICATIONSREQUEST = DESCRIPTOR.message_types_by_name["NotificationsRequest"]
_NOTIFICATION = DESCRIPTOR.message_types_by_name["Notification"]
_NOTIFICATIONSREPLY = DESCRIPTOR.message_types_by_name["NotificationsReply"]
Empty = _reflection.GeneratedProtocolMessageType(
    "Empty",
    (_message.Message,),
    {
        "DESCRIPTOR": _EMPTY,
        "__module__": "eventsourcing_grpc.protos.application_pb2"
        # @@protoc_insertion_point(class_scope:eventsourcing_grpc.Empty)
    },
)
_sym_db.RegisterMessage(Empty)

MethodRequest = _reflection.GeneratedProtocolMessageType(
    "MethodRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _METHODREQUEST,
        "__module__": "eventsourcing_grpc.protos.application_pb2"
        # @@protoc_insertion_point(class_scope:eventsourcing_grpc.MethodRequest)
    },
)
_sym_db.RegisterMessage(MethodRequest)

MethodReply = _reflection.GeneratedProtocolMessageType(
    "MethodReply",
    (_message.Message,),
    {
        "DESCRIPTOR": _METHODREPLY,
        "__module__": "eventsourcing_grpc.protos.application_pb2"
        # @@protoc_insertion_point(class_scope:eventsourcing_grpc.MethodReply)
    },
)
_sym_db.RegisterMessage(MethodReply)

NotificationsRequest = _reflection.GeneratedProtocolMessageType(
    "NotificationsRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _NOTIFICATIONSREQUEST,
        "__module__": "eventsourcing_grpc.protos.application_pb2"
        # @@protoc_insertion_point(class_scope:eventsourcing_grpc.NotificationsRequest)
    },
)
_sym_db.RegisterMessage(NotificationsRequest)

Notification = _reflection.GeneratedProtocolMessageType(
    "Notification",
    (_message.Message,),
    {
        "DESCRIPTOR": _NOTIFICATION,
        "__module__": "eventsourcing_grpc.protos.application_pb2"
        # @@protoc_insertion_point(class_scope:eventsourcing_grpc.Notification)
    },
)
_sym_db.RegisterMessage(Notification)

NotificationsReply = _reflection.GeneratedProtocolMessageType(
    "NotificationsReply",
    (_message.Message,),
    {
        "DESCRIPTOR": _NOTIFICATIONSREPLY,
        "__module__": "eventsourcing_grpc.protos.application_pb2"
        # @@protoc_insertion_point(class_scope:eventsourcing_grpc.NotificationsReply)
    },
)
_sym_db.RegisterMessage(NotificationsReply)

_APPLICATION = DESCRIPTOR.services_by_name["Application"]
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = (
        b"\n!io.eventsourcing_grpc.applicationB\020ApplicationProtoP\001\242\002\003ESA"
    )
    _EMPTY._serialized_start = 67
    _EMPTY._serialized_end = 74
    _METHODREQUEST._serialized_start = 76
    _METHODREQUEST._serialized_end = 142
    _METHODREPLY._serialized_start = 144
    _METHODREPLY._serialized_end = 171
    _NOTIFICATIONSREQUEST._serialized_start = 173
    _NOTIFICATIONSREQUEST._serialized_end = 241
    _NOTIFICATION._serialized_start = 243
    _NOTIFICATION._serialized_end = 350
    _NOTIFICATIONSREPLY._serialized_start = 352
    _NOTIFICATIONSREPLY._serialized_end = 429
    _APPLICATION._serialized_start = 432
    _APPLICATION._serialized_end = 708
# @@protoc_insertion_point(module_scope)
