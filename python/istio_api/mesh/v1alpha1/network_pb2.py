# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mesh/v1alpha1/network.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mesh/v1alpha1/network.proto',
  package='istio.mesh.v1alpha1',
  syntax='proto3',
  serialized_pb=_b('\n\x1bmesh/v1alpha1/network.proto\x12\x13istio.mesh.v1alpha1\"\xd6\x02\n\x07Network\x12\x0c\n\x04name\x18\x01 \x01(\t\x12@\n\tendpoints\x18\x02 \x03(\x0b\x32-.istio.mesh.v1alpha1.Network.NetworkEndpoints\x12\x42\n\x08gateways\x18\x03 \x03(\x0b\x32\x30.istio.mesh.v1alpha1.Network.IstioNetworkGateway\x1a\x46\n\x10NetworkEndpoints\x12\x13\n\tfrom_cidr\x18\x01 \x01(\tH\x00\x12\x17\n\rfrom_registry\x18\x02 \x01(\tH\x00\x42\x04\n\x02ne\x1ao\n\x13IstioNetworkGateway\x12\x1f\n\x15registry_service_name\x18\x01 \x01(\tH\x00\x12\x11\n\x07\x61\x64\x64ress\x18\x02 \x01(\tH\x00\x12\x0c\n\x04port\x18\x03 \x01(\r\x12\x10\n\x08locality\x18\x04 \x01(\tB\x04\n\x02gwB\x1cZ\x1aistio.io/api/mesh/v1alpha1b\x06proto3')
)




_NETWORK_NETWORKENDPOINTS = _descriptor.Descriptor(
  name='NetworkEndpoints',
  full_name='istio.mesh.v1alpha1.Network.NetworkEndpoints',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='from_cidr', full_name='istio.mesh.v1alpha1.Network.NetworkEndpoints.from_cidr', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='from_registry', full_name='istio.mesh.v1alpha1.Network.NetworkEndpoints.from_registry', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='ne', full_name='istio.mesh.v1alpha1.Network.NetworkEndpoints.ne',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=212,
  serialized_end=282,
)

_NETWORK_ISTIONETWORKGATEWAY = _descriptor.Descriptor(
  name='IstioNetworkGateway',
  full_name='istio.mesh.v1alpha1.Network.IstioNetworkGateway',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='registry_service_name', full_name='istio.mesh.v1alpha1.Network.IstioNetworkGateway.registry_service_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='istio.mesh.v1alpha1.Network.IstioNetworkGateway.address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='istio.mesh.v1alpha1.Network.IstioNetworkGateway.port', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='locality', full_name='istio.mesh.v1alpha1.Network.IstioNetworkGateway.locality', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='gw', full_name='istio.mesh.v1alpha1.Network.IstioNetworkGateway.gw',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=284,
  serialized_end=395,
)

_NETWORK = _descriptor.Descriptor(
  name='Network',
  full_name='istio.mesh.v1alpha1.Network',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='istio.mesh.v1alpha1.Network.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endpoints', full_name='istio.mesh.v1alpha1.Network.endpoints', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gateways', full_name='istio.mesh.v1alpha1.Network.gateways', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_NETWORK_NETWORKENDPOINTS, _NETWORK_ISTIONETWORKGATEWAY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=53,
  serialized_end=395,
)

_NETWORK_NETWORKENDPOINTS.containing_type = _NETWORK
_NETWORK_NETWORKENDPOINTS.oneofs_by_name['ne'].fields.append(
  _NETWORK_NETWORKENDPOINTS.fields_by_name['from_cidr'])
_NETWORK_NETWORKENDPOINTS.fields_by_name['from_cidr'].containing_oneof = _NETWORK_NETWORKENDPOINTS.oneofs_by_name['ne']
_NETWORK_NETWORKENDPOINTS.oneofs_by_name['ne'].fields.append(
  _NETWORK_NETWORKENDPOINTS.fields_by_name['from_registry'])
_NETWORK_NETWORKENDPOINTS.fields_by_name['from_registry'].containing_oneof = _NETWORK_NETWORKENDPOINTS.oneofs_by_name['ne']
_NETWORK_ISTIONETWORKGATEWAY.containing_type = _NETWORK
_NETWORK_ISTIONETWORKGATEWAY.oneofs_by_name['gw'].fields.append(
  _NETWORK_ISTIONETWORKGATEWAY.fields_by_name['registry_service_name'])
_NETWORK_ISTIONETWORKGATEWAY.fields_by_name['registry_service_name'].containing_oneof = _NETWORK_ISTIONETWORKGATEWAY.oneofs_by_name['gw']
_NETWORK_ISTIONETWORKGATEWAY.oneofs_by_name['gw'].fields.append(
  _NETWORK_ISTIONETWORKGATEWAY.fields_by_name['address'])
_NETWORK_ISTIONETWORKGATEWAY.fields_by_name['address'].containing_oneof = _NETWORK_ISTIONETWORKGATEWAY.oneofs_by_name['gw']
_NETWORK.fields_by_name['endpoints'].message_type = _NETWORK_NETWORKENDPOINTS
_NETWORK.fields_by_name['gateways'].message_type = _NETWORK_ISTIONETWORKGATEWAY
DESCRIPTOR.message_types_by_name['Network'] = _NETWORK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Network = _reflection.GeneratedProtocolMessageType('Network', (_message.Message,), dict(

  NetworkEndpoints = _reflection.GeneratedProtocolMessageType('NetworkEndpoints', (_message.Message,), dict(
    DESCRIPTOR = _NETWORK_NETWORKENDPOINTS,
    __module__ = 'mesh.v1alpha1.network_pb2'
    # @@protoc_insertion_point(class_scope:istio.mesh.v1alpha1.Network.NetworkEndpoints)
    ))
  ,

  IstioNetworkGateway = _reflection.GeneratedProtocolMessageType('IstioNetworkGateway', (_message.Message,), dict(
    DESCRIPTOR = _NETWORK_ISTIONETWORKGATEWAY,
    __module__ = 'mesh.v1alpha1.network_pb2'
    # @@protoc_insertion_point(class_scope:istio.mesh.v1alpha1.Network.IstioNetworkGateway)
    ))
  ,
  DESCRIPTOR = _NETWORK,
  __module__ = 'mesh.v1alpha1.network_pb2'
  # @@protoc_insertion_point(class_scope:istio.mesh.v1alpha1.Network)
  ))
_sym_db.RegisterMessage(Network)
_sym_db.RegisterMessage(Network.NetworkEndpoints)
_sym_db.RegisterMessage(Network.IstioNetworkGateway)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z\032istio.io/api/mesh/v1alpha1'))
# @@protoc_insertion_point(module_scope)