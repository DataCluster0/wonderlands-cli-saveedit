# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: OakShared.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name='OakShared.proto',
    package='OakSave',
    syntax='proto3',
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x0fOakShared.proto\x12\x07OakSave\"\'\n\x04Vec3\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\"=\n\x14GameStatSaveGameData\x12\x12\n\nstat_value\x18\x01 \x01(\x05\x12\x11\n\tstat_path\x18\x02 \x01(\t\"T\n\x19InventoryCategorySaveData\x12%\n\x1d\x62\x61se_category_definition_hash\x18\x01 \x01(\r\x12\x10\n\x08quantity\x18\x02 \x01(\x05\">\n\x12OakSDUSaveGameData\x12\x11\n\tsdu_level\x18\x01 \x01(\x05\x12\x15\n\rsdu_data_path\x18\x02 \x01(\t\"c\n!RegisteredDownloadableEntitlement\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08\x63onsumed\x18\x02 \x01(\r\x12\x12\n\nregistered\x18\x03 \x01(\x08\x12\x0c\n\x04seen\x18\x04 \x01(\x08\"\xa6\x01\n\"RegisteredDownloadableEntitlements\x12%\n\x1d\x65ntitlement_source_asset_path\x18\x01 \x01(\t\x12\x17\n\x0f\x65ntitlement_ids\x18\x02 \x03(\x03\x12@\n\x0c\x65ntitlements\x18\x03 \x03(\x0b\x32*.OakSave.RegisteredDownloadableEntitlement\"T\n\x19\x43hallengeStatSaveGameData\x12\x1a\n\x12\x63urrent_stat_value\x18\x01 \x01(\x05\x12\x1b\n\x13\x63hallenge_stat_path\x18\x02 \x01(\t\"B\n\x1eOakChallengeRewardSaveGameData\x12 \n\x18\x63hallenge_reward_claimed\x18\x01 \x01(\x08\"\xc3\x02\n\x15\x43hallengeSaveGameData\x12\x17\n\x0f\x63ompleted_count\x18\x01 \x01(\x05\x12\x11\n\tis_active\x18\x02 \x01(\x08\x12\x1b\n\x13\x63urrently_completed\x18\x03 \x01(\x08\x12 \n\x18\x63ompleted_progress_level\x18\x04 \x01(\x05\x12\x18\n\x10progress_counter\x18\x05 \x01(\x05\x12?\n\x13stat_instance_state\x18\x06 \x03(\x0b\x32\".OakSave.ChallengeStatSaveGameData\x12\x1c\n\x14\x63hallenge_class_path\x18\x07 \x01(\t\x12\x46\n\x15\x63hallenge_reward_info\x18\x08 \x03(\x0b\x32\'.OakSave.OakChallengeRewardSaveGameData\"\xeb\x01\n\x0bOakMailItem\x12\x16\n\x0email_item_type\x18\x01 \x01(\r\x12\x1b\n\x13sender_display_name\x18\x02 \x01(\t\x12\x0f\n\x07subject\x18\x03 \x01(\t\x12\x0c\n\x04\x62ody\x18\x04 \x01(\t\x12\x1a\n\x12gear_serial_number\x18\x05 \x01(\t\x12\x11\n\tmail_guid\x18\x06 \x01(\t\x12\x11\n\tdate_sent\x18\x07 \x01(\x03\x12\x17\n\x0f\x65xpiration_date\x18\x08 \x01(\x03\x12\x16\n\x0e\x66rom_player_id\x18\t \x01(\t\x12\x15\n\rhas_been_read\x18\n \x01(\x08\"P\n\x1cOakCustomizationSaveGameData\x12\x0e\n\x06is_new\x18\x01 \x01(\x08\x12 \n\x18\x63ustomization_asset_path\x18\x02 \x01(\t\"T\n!OakInventoryCustomizationPartInfo\x12\x1f\n\x17\x63ustomization_part_hash\x18\x01 \x01(\r\x12\x0e\n\x06is_new\x18\x02 \x01(\x08\"M\n\x1fOakProfileCustomizationLinkData\x12\x1a\n\x12\x63ustomization_name\x18\x01 \x01(\t\x12\x0e\n\x06\x61\x63tive\x18\x02 \x01(\x08\"\xf8\x01\n\'InventoryBalanceStateInitializationData\x12\x12\n\ngame_stage\x18\x01 \x01(\x05\x12\x16\n\x0einventory_data\x18\x02 \x01(\t\x12\x1e\n\x16inventory_balance_data\x18\x03 \x01(\t\x12\x19\n\x11manufacturer_data\x18\x04 \x01(\t\x12\x11\n\tpart_list\x18\x05 \x03(\t\x12\x19\n\x11generic_part_list\x18\x06 \x03(\t\x12\x17\n\x0f\x61\x64\x64itional_data\x18\x07 \x01(\x0c\x12\x1f\n\x17\x63ustomization_part_list\x18\x08 \x03(\t\"\xb6\x01\n\x1cOakInventoryItemSaveGameData\x12\x1a\n\x12item_serial_number\x18\x01 \x01(\x0c\x12\x1a\n\x12pickup_order_index\x18\x02 \x01(\x05\x12\r\n\x05\x66lags\x18\x03 \x01(\x05\x12O\n\x15\x64\x65velopment_save_data\x18\x05 \x01(\x0b\x32\x30.OakSave.InventoryBalanceStateInitializationDatab\x06proto3'
)


_VEC3 = DESCRIPTOR.message_types_by_name['Vec3']
_GAMESTATSAVEGAMEDATA = DESCRIPTOR.message_types_by_name['GameStatSaveGameData']
_INVENTORYCATEGORYSAVEDATA = DESCRIPTOR.message_types_by_name['InventoryCategorySaveData']
_OAKSDUSAVEGAMEDATA = DESCRIPTOR.message_types_by_name['OakSDUSaveGameData']
_REGISTEREDDOWNLOADABLEENTITLEMENT = DESCRIPTOR.message_types_by_name[
    'RegisteredDownloadableEntitlement']
_REGISTEREDDOWNLOADABLEENTITLEMENTS = DESCRIPTOR.message_types_by_name[
    'RegisteredDownloadableEntitlements']
_CHALLENGESTATSAVEGAMEDATA = DESCRIPTOR.message_types_by_name['ChallengeStatSaveGameData']
_OAKCHALLENGEREWARDSAVEGAMEDATA = DESCRIPTOR.message_types_by_name[
    'OakChallengeRewardSaveGameData']
_CHALLENGESAVEGAMEDATA = DESCRIPTOR.message_types_by_name['ChallengeSaveGameData']
_OAKMAILITEM = DESCRIPTOR.message_types_by_name['OakMailItem']
_OAKCUSTOMIZATIONSAVEGAMEDATA = DESCRIPTOR.message_types_by_name['OakCustomizationSaveGameData']
_OAKINVENTORYCUSTOMIZATIONPARTINFO = DESCRIPTOR.message_types_by_name[
    'OakInventoryCustomizationPartInfo']
_OAKPROFILECUSTOMIZATIONLINKDATA = DESCRIPTOR.message_types_by_name[
    'OakProfileCustomizationLinkData']
_INVENTORYBALANCESTATEINITIALIZATIONDATA = DESCRIPTOR.message_types_by_name[
    'InventoryBalanceStateInitializationData']
_OAKINVENTORYITEMSAVEGAMEDATA = DESCRIPTOR.message_types_by_name['OakInventoryItemSaveGameData']
Vec3 = _reflection.GeneratedProtocolMessageType('Vec3', (_message.Message,), {
    'DESCRIPTOR': _VEC3,
    '__module__': 'OakShared_pb2'
    # @@protoc_insertion_point(class_scope:OakSave.Vec3)
})
_sym_db.RegisterMessage(Vec3)

GameStatSaveGameData = _reflection.GeneratedProtocolMessageType('GameStatSaveGameData', (_message.Message,), {
    'DESCRIPTOR': _GAMESTATSAVEGAMEDATA,
    '__module__': 'OakShared_pb2'
    # @@protoc_insertion_point(class_scope:OakSave.GameStatSaveGameData)
})
_sym_db.RegisterMessage(GameStatSaveGameData)

InventoryCategorySaveData = _reflection.GeneratedProtocolMessageType('InventoryCategorySaveData', (_message.Message,), {
    'DESCRIPTOR': _INVENTORYCATEGORYSAVEDATA,
    '__module__': 'OakShared_pb2'
    # @@protoc_insertion_point(class_scope:OakSave.InventoryCategorySaveData)
})
_sym_db.RegisterMessage(InventoryCategorySaveData)

OakSDUSaveGameData = _reflection.GeneratedProtocolMessageType('OakSDUSaveGameData', (_message.Message,), {
    'DESCRIPTOR': _OAKSDUSAVEGAMEDATA,
    '__module__': 'OakShared_pb2'
    # @@protoc_insertion_point(class_scope:OakSave.OakSDUSaveGameData)
})
_sym_db.RegisterMessage(OakSDUSaveGameData)

RegisteredDownloadableEntitlement = _reflection.GeneratedProtocolMessageType('RegisteredDownloadableEntitlement', (_message.Message,), {
    'DESCRIPTOR': _REGISTEREDDOWNLOADABLEENTITLEMENT,
    '__module__': 'OakShared_pb2'
    # @@protoc_insertion_point(class_scope:OakSave.RegisteredDownloadableEntitlement)
})
_sym_db.RegisterMessage(RegisteredDownloadableEntitlement)

RegisteredDownloadableEntitlements = _reflection.GeneratedProtocolMessageType('RegisteredDownloadableEntitlements', (_message.Message,), {
    'DESCRIPTOR': _REGISTEREDDOWNLOADABLEENTITLEMENTS,
    '__module__': 'OakShared_pb2'
    # @@protoc_insertion_point(class_scope:OakSave.RegisteredDownloadableEntitlements)
})
_sym_db.RegisterMessage(RegisteredDownloadableEntitlements)

ChallengeStatSaveGameData = _reflection.GeneratedProtocolMessageType('ChallengeStatSaveGameData', (_message.Message,), {
    'DESCRIPTOR': _CHALLENGESTATSAVEGAMEDATA,
    '__module__': 'OakShared_pb2'
    # @@protoc_insertion_point(class_scope:OakSave.ChallengeStatSaveGameData)
})
_sym_db.RegisterMessage(ChallengeStatSaveGameData)

OakChallengeRewardSaveGameData = _reflection.GeneratedProtocolMessageType('OakChallengeRewardSaveGameData', (_message.Message,), {
    'DESCRIPTOR': _OAKCHALLENGEREWARDSAVEGAMEDATA,
    '__module__': 'OakShared_pb2'
    # @@protoc_insertion_point(class_scope:OakSave.OakChallengeRewardSaveGameData)
})
_sym_db.RegisterMessage(OakChallengeRewardSaveGameData)

ChallengeSaveGameData = _reflection.GeneratedProtocolMessageType('ChallengeSaveGameData', (_message.Message,), {
    'DESCRIPTOR': _CHALLENGESAVEGAMEDATA,
    '__module__': 'OakShared_pb2'
    # @@protoc_insertion_point(class_scope:OakSave.ChallengeSaveGameData)
})
_sym_db.RegisterMessage(ChallengeSaveGameData)

OakMailItem = _reflection.GeneratedProtocolMessageType('OakMailItem', (_message.Message,), {
    'DESCRIPTOR': _OAKMAILITEM,
    '__module__': 'OakShared_pb2'
    # @@protoc_insertion_point(class_scope:OakSave.OakMailItem)
})
_sym_db.RegisterMessage(OakMailItem)

OakCustomizationSaveGameData = _reflection.GeneratedProtocolMessageType('OakCustomizationSaveGameData', (_message.Message,), {
    'DESCRIPTOR': _OAKCUSTOMIZATIONSAVEGAMEDATA,
    '__module__': 'OakShared_pb2'
    # @@protoc_insertion_point(class_scope:OakSave.OakCustomizationSaveGameData)
})
_sym_db.RegisterMessage(OakCustomizationSaveGameData)

OakInventoryCustomizationPartInfo = _reflection.GeneratedProtocolMessageType('OakInventoryCustomizationPartInfo', (_message.Message,), {
    'DESCRIPTOR': _OAKINVENTORYCUSTOMIZATIONPARTINFO,
    '__module__': 'OakShared_pb2'
    # @@protoc_insertion_point(class_scope:OakSave.OakInventoryCustomizationPartInfo)
})
_sym_db.RegisterMessage(OakInventoryCustomizationPartInfo)

OakProfileCustomizationLinkData = _reflection.GeneratedProtocolMessageType('OakProfileCustomizationLinkData', (_message.Message,), {
    'DESCRIPTOR': _OAKPROFILECUSTOMIZATIONLINKDATA,
    '__module__': 'OakShared_pb2'
    # @@protoc_insertion_point(class_scope:OakSave.OakProfileCustomizationLinkData)
})
_sym_db.RegisterMessage(OakProfileCustomizationLinkData)

InventoryBalanceStateInitializationData = _reflection.GeneratedProtocolMessageType('InventoryBalanceStateInitializationData', (_message.Message,), {
    'DESCRIPTOR': _INVENTORYBALANCESTATEINITIALIZATIONDATA,
    '__module__': 'OakShared_pb2'
    # @@protoc_insertion_point(class_scope:OakSave.InventoryBalanceStateInitializationData)
})
_sym_db.RegisterMessage(InventoryBalanceStateInitializationData)

OakInventoryItemSaveGameData = _reflection.GeneratedProtocolMessageType('OakInventoryItemSaveGameData', (_message.Message,), {
    'DESCRIPTOR': _OAKINVENTORYITEMSAVEGAMEDATA,
    '__module__': 'OakShared_pb2'
    # @@protoc_insertion_point(class_scope:OakSave.OakInventoryItemSaveGameData)
})
_sym_db.RegisterMessage(OakInventoryItemSaveGameData)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _VEC3._serialized_start = 28
    _VEC3._serialized_end = 67
    _GAMESTATSAVEGAMEDATA._serialized_start = 69
    _GAMESTATSAVEGAMEDATA._serialized_end = 130
    _INVENTORYCATEGORYSAVEDATA._serialized_start = 132
    _INVENTORYCATEGORYSAVEDATA._serialized_end = 216
    _OAKSDUSAVEGAMEDATA._serialized_start = 218
    _OAKSDUSAVEGAMEDATA._serialized_end = 280
    _REGISTEREDDOWNLOADABLEENTITLEMENT._serialized_start = 282
    _REGISTEREDDOWNLOADABLEENTITLEMENT._serialized_end = 381
    _REGISTEREDDOWNLOADABLEENTITLEMENTS._serialized_start = 384
    _REGISTEREDDOWNLOADABLEENTITLEMENTS._serialized_end = 550
    _CHALLENGESTATSAVEGAMEDATA._serialized_start = 552
    _CHALLENGESTATSAVEGAMEDATA._serialized_end = 636
    _OAKCHALLENGEREWARDSAVEGAMEDATA._serialized_start = 638
    _OAKCHALLENGEREWARDSAVEGAMEDATA._serialized_end = 704
    _CHALLENGESAVEGAMEDATA._serialized_start = 707
    _CHALLENGESAVEGAMEDATA._serialized_end = 1030
    _OAKMAILITEM._serialized_start = 1033
    _OAKMAILITEM._serialized_end = 1268
    _OAKCUSTOMIZATIONSAVEGAMEDATA._serialized_start = 1270
    _OAKCUSTOMIZATIONSAVEGAMEDATA._serialized_end = 1350
    _OAKINVENTORYCUSTOMIZATIONPARTINFO._serialized_start = 1352
    _OAKINVENTORYCUSTOMIZATIONPARTINFO._serialized_end = 1436
    _OAKPROFILECUSTOMIZATIONLINKDATA._serialized_start = 1438
    _OAKPROFILECUSTOMIZATIONLINKDATA._serialized_end = 1515
    _INVENTORYBALANCESTATEINITIALIZATIONDATA._serialized_start = 1518
    _INVENTORYBALANCESTATEINITIALIZATIONDATA._serialized_end = 1766
    _OAKINVENTORYITEMSAVEGAMEDATA._serialized_start = 1769
    _OAKINVENTORYITEMSAVEGAMEDATA._serialized_end = 1951
# @@protoc_insertion_point(module_scope)
