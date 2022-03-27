
# Copyright (c) 2020-2021 CJ Kucera (cj@apocalyptech.com)
# 
# This software is provided 'as-is', without any express or implied warranty.
# In no event will the authors be held liable for any damages arising from
# the use of this software.
# 
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely, subject to the following restrictions:
# 
# 1. The origin of this software must not be misrepresented; you must not
#    claim that you wrote the original software. If you use this software in a
#    product, an acknowledgment in the product documentation would be
#    appreciated but is not required.
# 
# 2. Altered source versions must be plainly marked as such, and must not be
#    misrepresented as being the original software.
# 
# 3. This notice may not be removed or altered from any source distribution.

# Editor Version
__version__ = '1.16.1b1'

# Classes
(PLAYER) = range(1)
class_to_eng = {
        PLAYER: 'Player',
        }
classobj_to_class = {
        '/Game/PlayerCharacters/PlayerClassId_Player.PlayerClassId_Player': PLAYER,
        }

# Pets
# TODO (ish): Looks like there's currently no support for renaming your Loader
# pet.  Make sure to add that in, if they ever get that in the game.  (I did try
# just injecting some data even though there's no in-game UI, and couldn't
# find a string that worked.)
(JABBER, SPIDERANT, SKAG) = range(3)
pet_to_eng = {
        JABBER: 'Jabber',
        SPIDERANT: 'Spiderant',
        SKAG: 'Skag',
        }
petkey_to_pet = {
        'petmonkey': JABBER,
        'petspiderant': SPIDERANT,
        'petskag': SKAG,
        }
pet_to_petkey = {v: k for k, v in petkey_to_pet.items()}

# Currencies
(MONEY, ERIDIUM) = range(2)
currency_to_eng = {
        MONEY: 'Money',
        ERIDIUM: 'Eridium',
        }
currency_to_curhash = {
        MONEY: 618814354,
        ERIDIUM: 3679636065
        }
curhash_to_currency = {v: k for k, v in currency_to_curhash.items()}

# Inventory Slots
(WEAPON1, WEAPON2, WEAPON3, WEAPON4, SHIELD, GRENADE, COM, ARTIFACT) = range(8)
slot_to_eng = {
        WEAPON1: 'Weapon 1',
        WEAPON2: 'Weapon 2',
        WEAPON3: 'Weapon 3',
        WEAPON4: 'Weapon 4',
        SHIELD: 'Shield',
        GRENADE: 'Grenade',
        COM: 'COM',
        ARTIFACT: 'Artifact',
}
slotobj_to_slot = {
        '/Game/Gear/Weapons/_Shared/_Design/InventorySlots/BPInvSlot_Weapon1.BPInvSlot_Weapon1': WEAPON1,
        '/Game/Gear/Weapons/_Shared/_Design/InventorySlots/BPInvSlot_Weapon2.BPInvSlot_Weapon2': WEAPON2,
        '/Game/Gear/Weapons/_Shared/_Design/InventorySlots/BPInvSlot_Weapon3.BPInvSlot_Weapon3': WEAPON3,
        '/Game/Gear/Weapons/_Shared/_Design/InventorySlots/BPInvSlot_Weapon4.BPInvSlot_Weapon4': WEAPON4,
        '/Game/Gear/Shields/_Design/A_Data/BPInvSlot_Shield.BPInvSlot_Shield': SHIELD,
        '/Game/Gear/GrenadeMods/_Design/A_Data/BPInvSlot_GrenadeMod.BPInvSlot_GrenadeMod': GRENADE,
        '/Game/Gear/ClassMods/_Design/_Data/BPInvSlot_ClassMod.BPInvSlot_ClassMod': COM,
        '/Game/Gear/Artifacts/_Design/_Data/BPInvSlot_Artifact.BPInvSlot_Artifact': ARTIFACT,
        }
slot_to_slotobj = {v: k for k, v in slotobj_to_slot.items()}

# SDUs
(SDU_BACKPACK, SDU_AR, SDU_PISTOL, SDU_SNIPER, SDU_SHOTGUN, SDU_GRENADE, SDU_SMG, SDU_HEAVY) = range(8)
ammo_sdus = [SDU_AR, SDU_PISTOL, SDU_SNIPER, SDU_SHOTGUN, SDU_GRENADE, SDU_SMG, SDU_HEAVY]
sdu_to_eng = {
        SDU_BACKPACK: 'Backpack',
        SDU_AR: 'AR',
        SDU_PISTOL: 'Pistol',
        SDU_SNIPER: 'Sniper',
        SDU_SHOTGUN: 'Shotgun',
        SDU_GRENADE: 'Grenade',
        SDU_SMG: 'SMG',
        SDU_HEAVY: 'Heavy',
        }
sduobj_to_sdu = {
        '/Game/Pickups/SDU/SDU_Backpack.SDU_Backpack': SDU_BACKPACK,
        '/Game/Pickups/SDU/SDU_AssaultRifle.SDU_AssaultRifle': SDU_AR,
        '/Game/Pickups/SDU/SDU_Pistol.SDU_Pistol': SDU_PISTOL,
        '/Game/Pickups/SDU/SDU_SniperRifle.SDU_SniperRifle': SDU_SNIPER,
        '/Game/Pickups/SDU/SDU_Shotgun.SDU_Shotgun': SDU_SHOTGUN,
        '/Game/Pickups/SDU/SDU_Grenade.SDU_Grenade': SDU_GRENADE,
        '/Game/Pickups/SDU/SDU_SMG.SDU_SMG': SDU_SMG,
        '/Game/Pickups/SDU/SDU_Heavy.SDU_Heavy': SDU_HEAVY,
        }
sdu_to_sduobj = {v: k for k, v in sduobj_to_sdu.items()}
sdu_to_max = {
        SDU_BACKPACK: 13,
        SDU_AR: 10,
        SDU_PISTOL: 10,
        SDU_SNIPER: 13,
        SDU_SHOTGUN: 10,
        SDU_GRENADE: 10,
        SDU_SMG: 10,
        SDU_HEAVY: 13,
        }

# Profile SDUs
(PSDU_LOSTLOOT, PSDU_BANK) = range(2)
psdu_to_eng = {
        PSDU_LOSTLOOT: 'Lost Loot',
        PSDU_BANK: 'Bank',
        }
psduobj_to_psdu = {
        '/Game/Pickups/SDU/SDU_LostLoot.SDU_LostLoot': PSDU_LOSTLOOT,
        '/Game/Pickups/SDU/SDU_Bank.SDU_Bank': PSDU_BANK,
        }
psdu_to_psduobj = {v: k for k, v in psduobj_to_psdu.items()}
psdu_to_max = {
        PSDU_LOSTLOOT: 10,
        PSDU_BANK: 28,
        }

# Ammo
(AMMO_AR, AMMO_GRENADE, AMMO_HEAVY, AMMO_PISTOL, AMMO_SMG, AMMO_SHOTGUN, AMMO_SNIPER) = range(7)
ammo_to_eng = {
        AMMO_AR: 'AR',
        AMMO_GRENADE: 'Grenade',
        AMMO_HEAVY: 'Heavy',
        AMMO_PISTOL: 'Pistol',
        AMMO_SMG: 'SMG',
        AMMO_SHOTGUN: 'Shotgun',
        AMMO_SNIPER: 'Sniper',
        }
ammoobj_to_ammo = {
        '/Game/GameData/Weapons/Ammo/Resource_Ammo_AssaultRifle.Resource_Ammo_AssaultRifle': AMMO_AR,
        '/Game/GameData/Weapons/Ammo/Resource_Ammo_Grenade.Resource_Ammo_Grenade': AMMO_GRENADE,
        '/Game/GameData/Weapons/Ammo/Resource_Ammo_Heavy.Resource_Ammo_Heavy': AMMO_HEAVY,
        '/Game/GameData/Weapons/Ammo/Resource_Ammo_Pistol.Resource_Ammo_Pistol': AMMO_PISTOL,
        '/Game/GameData/Weapons/Ammo/Resource_Ammo_SMG.Resource_Ammo_SMG': AMMO_SMG,
        '/Game/GameData/Weapons/Ammo/Resource_Ammo_Shotgun.Resource_Ammo_Shotgun': AMMO_SHOTGUN,
        '/Game/GameData/Weapons/Ammo/Resource_Ammo_Sniper.Resource_Ammo_Sniper': AMMO_SNIPER,
        }
ammo_to_ammoobj = {v: k for k, v in ammoobj_to_ammo.items()}
ammo_to_max = {
        AMMO_AR: 1680,
        AMMO_GRENADE: 13,
        AMMO_HEAVY: 51,
        AMMO_PISTOL: 1200,
        AMMO_SMG: 2160,
        AMMO_SHOTGUN: 280,
        AMMO_SNIPER: 204,
        }

# Challenges
(ERIDIAN_ANALYZER,
        ERIDIAN_RESONATOR,
        MAYHEM,
        CHAL_ARTIFACT,
        COM_BEASTMASTER,
        COM_GUNNER,
        COM_OPERATIVE,
        COM_SIREN,
        ) = range(8)
challenge_to_eng = {
        ERIDIAN_ANALYZER: 'Eridian Analyzer',
        ERIDIAN_RESONATOR: 'Eridian Resonator',
        MAYHEM: 'Mayhem Mode',
        CHAL_ARTIFACT: 'Artifact Slot',
        COM_BEASTMASTER: 'Beastmaster COM Slot',
        COM_GUNNER: 'Gunner COM Slot',
        COM_OPERATIVE: 'Operative COM Slot',
        COM_SIREN: 'Siren COM Slot',
        }
challenge_char_lock = {
        COM_BEASTMASTER: BEASTMASTER,
        COM_GUNNER: GUNNER,
        COM_OPERATIVE: OPERATIVE,
        COM_SIREN: SIREN,
        }
challengeobj_to_challenge = {
        # '/Game/GameData/Challenges/Account/Challenge_VaultReward_Analyzer.Challenge_VaultReward_Analyzer_C': ERIDIAN_ANALYZER,
        # '/Game/GameData/Challenges/Account/Challenge_VaultReward_Resonator.Challenge_VaultReward_Resonator_C': ERIDIAN_RESONATOR,
        # '/Game/GameData/Challenges/Account/Challenge_VaultReward_Mayhem.Challenge_VaultReward_Mayhem_C': MAYHEM,
        # '/Game/GameData/Challenges/Account/Challenge_VaultReward_ArtifactSlot.Challenge_VaultReward_ArtifactSlot_C': CHAL_ARTIFACT,
        # '/Game/GameData/Challenges/Character/Beastmaster/BP_Challenge_Beastmaster_ClassMod.BP_Challenge_Beastmaster_ClassMod_C': COM_BEASTMASTER,
        # '/Game/GameData/Challenges/Character/Gunner/BP_Challenge_Gunner_ClassMod.BP_Challenge_Gunner_ClassMod_C': COM_GUNNER,
        # '/Game/GameData/Challenges/Character/Operative/BP_Challenge_Operative_ClassMod.BP_Challenge_Operative_ClassMod_C': COM_OPERATIVE,
        # '/Game/GameData/Challenges/Character/Siren/BP_Challenge_Siren_ClassMod.BP_Challenge_Siren_ClassMod_C': COM_SIREN,

        # This alone is not sufficient to unlock Sanctuary early
        #'/Game/GameData/Challenges/FastTravel/Challenge_FastTravel_Sanctuary3_2.Challenge_FastTravel_Sanctuary3_2_C': FOO,

        # Unlocking Fabricator really doesn't interest me; I think you'd need the item drop to go along with it, too.
        #'/Game/GameData/Challenges/Account/Challenge_VaultReward_Fabricator.Challenge_VaultReward_Fabricator_C': FOO,

        # Also, where are the other two gun slots?
        }
challenge_to_challengeobj = {v: k for k, v in challengeobj_to_challenge.items()}

# Level-based challenges (probably unimportant, but I've already started doing it,
# so here we go anyway)
level_stat = '/Game/PlayerCharacters/_Shared/_Design/Stats/Character/Stat_Character_Level.Stat_Character_Level'
level_challenges = [
        # (2, '/Game/GameData/Challenges/System/BP_Challenge_Console_1.BP_Challenge_Console_1_C'),
        # (10, '/Game/GameData/Challenges/System/BP_Challenge_Console_2.BP_Challenge_Console_2_C'),
        # (25, '/Game/GameData/Challenges/System/BP_Challenge_Console_3.BP_Challenge_Console_3_C'),
        # (50, '/Game/GameData/Challenges/System/BP_Challenge_Console_4.BP_Challenge_Console_4_C'),
        ]

# Borderlands Science
borderlands_science_levels = [
        #(5, "Claptrap"),
        ]

# Vehicle info.  We're not doing as much object-to-english mapping stuff here, 'cause
# I don't care enough to code it into the editor.  Just doing some more general
# "unlock all" type activity.
(OUTRUNNER, TECHNICAL, CYCLONE, JETBEAST) = range(4)
vehicle_to_eng = {
        OUTRUNNER: 'Outrunner',
        TECHNICAL: 'Technical',
        CYCLONE: 'Cyclone',
        JETBEAST: 'Jetbeast',
        }
vehicle_chassis = {
        OUTRUNNER:  set([]),
        TECHNICAL:  set([]),
        CYCLONE:  set([]),
        JETBEAST:  set([])
# Chassis types to *not* unlock.  Added for DLC3 since the game is apparently hardcoded to
# unlock the main Jetbeast type, and will do so even if we've already unlocked it, which
# makes it show up in the list twice.  This doesn't actually seem to cause any problems, but
# it bothers me, so an `excluders` for unlocking it is.
jetbeast_main_chassis = '/Geranium/Vehicles/Horse/Design/WT_Horse_Biobeast.WT_Horse_Biobeast'
chassis_excluders = set([
    jetbeast_main_chassis,
    ])
chassis_to_vehicle = {}
for vehicle, chassislist in vehicle_chassis.items():
    for chassis in chassislist:
        chassis_to_vehicle[chassis] = vehicle
vehicle_parts = {
        OUTRUNNER:  set([]),
        TECHNICAL:  set([]),
        CYCLONE:  set([]),
        JETBEAST: set([]),
        }
part_to_vehicle = {}
for vehicle, parts in vehicle_parts.items():
    for part in parts:
        part_to_vehicle[part] = vehicle
vehicle_skins = {
        OUTRUNNER: set([]),
        TECHNICAL: set([]),
        CYCLONE: set([]),
        JETBEAST: set([]),
        }
skin_to_vehicle = {}
for vehicle, skins in vehicle_skins.items():
    for skin in skins:
        skin_to_vehicle[skin] = vehicle

# Profile customizations - Skins
# (all these customization sections omit the ones unlocked by default,
# which don't seem to show up in the profile usually)
profile_skins = set([
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_18_Primary.ArmorColor_18_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_19_Primary.ArmorColor_19_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_20_Primary.ArmorColor_20_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_21_Primary.ArmorColor_21_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_22_Primary.ArmorColor_22_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_23_Primary.ArmorColor_23_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_24_Primary.ArmorColor_24_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_25_Primary.ArmorColor_25_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_26_Primary.ArmorColor_26_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_27_Primary.ArmorColor_27_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_28_Primary.ArmorColor_28_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_29_Primary.ArmorColor_29_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_30_Primary.ArmorColor_30_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_31_Primary.ArmorColor_31_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_32_Primary.ArmorColor_32_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_33_Primary.ArmorColor_33_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_34_Primary.ArmorColor_34_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_35_Primary.ArmorColor_35_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_36_Primary.ArmorColor_36_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_37_Primary.ArmorColor_37_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_38_Primary.ArmorColor_38_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_39_Primary.ArmorColor_39_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_40_Primary.ArmorColor_40_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_41_Primary.ArmorColor_41_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_42_Primary.ArmorColor_42_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_43_Primary.ArmorColor_43_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_44_Primary.ArmorColor_44_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_45_Primary.ArmorColor_45_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_46_Primary.ArmorColor_46_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_47_Primary.ArmorColor_47_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_48_Primary.ArmorColor_48_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_49_Primary.ArmorColor_49_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_50_Primary.ArmorColor_50_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_51_Primary.ArmorColor_51_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_52_Primary.ArmorColor_52_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_53_Primary.ArmorColor_53_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_54_Primary.ArmorColor_54_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_55_Primary.ArmorColor_55_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_56_Primary.ArmorColor_56_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_57_Primary.ArmorColor_57_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_58_Primary.ArmorColor_58_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_59_Primary.ArmorColor_59_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_60_Primary.ArmorColor_60_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_61_Primary.ArmorColor_61_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_62_Primary.ArmorColor_62_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_63_Primary.ArmorColor_63_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_64_Primary.ArmorColor_64_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_65_Primary.ArmorColor_65_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_66_Primary.ArmorColor_66_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_67_Primary.ArmorColor_67_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_68_Primary.ArmorColor_68_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_69_Primary.ArmorColor_69_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_70_Primary.ArmorColor_70_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_71_Primary.ArmorColor_71_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorPrimary/ArmorColor_72_Primary.ArmorColor_72_Primary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_18_Secondary.ArmorColor_18_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_19_Secondary.ArmorColor_19_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_20_Secondary.ArmorColor_20_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_21_Secondary.ArmorColor_21_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_22_Secondary.ArmorColor_22_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_23_Secondary.ArmorColor_23_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_24_Secondary.ArmorColor_24_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_25_Secondary.ArmorColor_25_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_26_Secondary.ArmorColor_26_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_27_Secondary.ArmorColor_27_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_28_Secondary.ArmorColor_28_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_29_Secondary.ArmorColor_29_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_30_Secondary.ArmorColor_30_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_31_Secondary.ArmorColor_31_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_32_Secondary.ArmorColor_32_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_33_Secondary.ArmorColor_33_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_34_Secondary.ArmorColor_34_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_35_Secondary.ArmorColor_35_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_36_Secondary.ArmorColor_36_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_37_Secondary.ArmorColor_37_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_38_Secondary.ArmorColor_38_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_39_Secondary.ArmorColor_39_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_40_Secondary.ArmorColor_40_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_41_Secondary.ArmorColor_41_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_42_Secondary.ArmorColor_42_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_43_Secondary.ArmorColor_43_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_44_Secondary.ArmorColor_44_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_45_Secondary.ArmorColor_45_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_46_Secondary.ArmorColor_46_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_47_Secondary.ArmorColor_47_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_48_Secondary.ArmorColor_48_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_49_Secondary.ArmorColor_49_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_50_Secondary.ArmorColor_50_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_51_Secondary.ArmorColor_51_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_52_Secondary.ArmorColor_52_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_53_Secondary.ArmorColor_53_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_54_Secondary.ArmorColor_54_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_55_Secondary.ArmorColor_55_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_56_Secondary.ArmorColor_56_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_57_Secondary.ArmorColor_57_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_58_Secondary.ArmorColor_58_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_59_Secondary.ArmorColor_59_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_60_Secondary.ArmorColor_60_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_61_Secondary.ArmorColor_61_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_62_Secondary.ArmorColor_62_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_63_Secondary.ArmorColor_63_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_64_Secondary.ArmorColor_64_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_65_Secondary.ArmorColor_65_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_66_Secondary.ArmorColor_66_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_67_Secondary.ArmorColor_67_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_68_Secondary.ArmorColor_68_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_69_Secondary.ArmorColor_69_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_70_Secondary.ArmorColor_70_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_71_Secondary.ArmorColor_71_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorSecondary/ArmorColor_72_Secondary.ArmorColor_72_Secondary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_18_Tertiary.ArmorColor_18_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_19_Tertiary.ArmorColor_19_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_20_Tertiary.ArmorColor_20_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_21_Tertiary.ArmorColor_21_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_22_Tertiary.ArmorColor_22_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_23_Tertiary.ArmorColor_23_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_24_Tertiary.ArmorColor_24_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_25_Tertiary.ArmorColor_25_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_26_Tertiary.ArmorColor_26_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_27_Tertiary.ArmorColor_27_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_28_Tertiary.ArmorColor_28_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_29_Tertiary.ArmorColor_29_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_30_Tertiary.ArmorColor_30_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_31_Tertiary.ArmorColor_31_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_32_Tertiary.ArmorColor_32_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_33_Tertiary.ArmorColor_33_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_34_Tertiary.ArmorColor_34_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_35_Tertiary.ArmorColor_35_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_36_Tertiary.ArmorColor_36_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_37_Tertiary.ArmorColor_37_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_38_Tertiary.ArmorColor_38_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_39_Tertiary.ArmorColor_39_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_40_Tertiary.ArmorColor_40_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_41_Tertiary.ArmorColor_41_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_42_Tertiary.ArmorColor_42_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_43_Tertiary.ArmorColor_43_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_44_Tertiary.ArmorColor_44_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_45_Tertiary.ArmorColor_45_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_46_Tertiary.ArmorColor_46_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_47_Tertiary.ArmorColor_47_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_48_Tertiary.ArmorColor_48_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_49_Tertiary.ArmorColor_49_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_50_Tertiary.ArmorColor_50_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_51_Tertiary.ArmorColor_51_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_52_Tertiary.ArmorColor_52_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_53_Tertiary.ArmorColor_53_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_54_Tertiary.ArmorColor_54_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_55_Tertiary.ArmorColor_55_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_56_Tertiary.ArmorColor_56_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_57_Tertiary.ArmorColor_57_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_58_Tertiary.ArmorColor_58_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_59_Tertiary.ArmorColor_59_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_60_Tertiary.ArmorColor_60_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_61_Tertiary.ArmorColor_61_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_62_Tertiary.ArmorColor_62_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_63_Tertiary.ArmorColor_63_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_64_Tertiary.ArmorColor_64_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_65_Tertiary.ArmorColor_65_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_66_Tertiary.ArmorColor_66_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_67_Tertiary.ArmorColor_67_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_68_Tertiary.ArmorColor_68_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_69_Tertiary.ArmorColor_69_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_70_Tertiary.ArmorColor_70_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_71_Tertiary.ArmorColor_71_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/ColorTertiary/ArmorColor_72_Tertiary.ArmorColor_72_Tertiary',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/Pattern/ArmorPattern_03.ArmorPattern_03',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/Pattern/ArmorPattern_04.ArmorPattern_04',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/Pattern/ArmorPattern_05.ArmorPattern_05',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/Pattern/ArmorPattern_06.ArmorPattern_06',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/Pattern/ArmorPattern_07.ArmorPattern_07',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/Pattern/ArmorPattern_09.ArmorPattern_09',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/Pattern/ArmorPattern_10.ArmorPattern_10',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/Pattern/ArmorPattern_11.ArmorPattern_11',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/Pattern/ArmorPattern_12.ArmorPattern_12',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/Pattern/ArmorPattern_13.ArmorPattern_13',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/Pattern/ArmorPattern_15.ArmorPattern_15',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/Pattern/ArmorPattern_16.ArmorPattern_16',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/Pattern/ArmorPattern_18.ArmorPattern_18',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/Pattern/ArmorPattern_19.ArmorPattern_19',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/Pattern/ArmorPattern_21.ArmorPattern_21',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/Pattern/ArmorPattern_22.ArmorPattern_22',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/Pattern/ArmorPattern_23.ArmorPattern_23',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/Pattern/ArmorPattern_24.ArmorPattern_24',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/Pattern/ArmorPattern_25.ArmorPattern_25',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/UnderPattern/UnderArmorPattern_03.UnderArmorPattern_03',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/UnderPattern/UnderArmorPattern_05.UnderArmorPattern_05',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/UnderPattern/UnderArmorPattern_08.UnderArmorPattern_08',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/UnderPattern/UnderArmorPattern_10.UnderArmorPattern_10',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/UnderPattern/UnderArmorPattern_11.UnderArmorPattern_11',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/UnderPattern/UnderArmorPattern_12.UnderArmorPattern_12',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/UnderPattern/UnderArmorPattern_13.UnderArmorPattern_13',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/UnderPattern/UnderArmorPattern_14.UnderArmorPattern_14',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/UnderPattern/UnderArmorPattern_17.UnderArmorPattern_17',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/UnderPattern/UnderArmorPattern_18.UnderArmorPattern_18',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/UnderPattern/UnderArmorPattern_19.UnderArmorPattern_19',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/UnderPattern/UnderArmorPattern_20.UnderArmorPattern_20',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/UnderPattern/UnderArmorPattern_21.UnderArmorPattern_21',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/UnderPattern/UnderArmorPattern_22.UnderArmorPattern_22',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/UnderPattern/UnderArmorPattern_23.UnderArmorPattern_23',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Armor/UnderPattern/UnderArmorPattern_24.UnderArmorPattern_24',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Background/BannerShape_02.BannerShape_02',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Background/BannerShape_04.BannerShape_04',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Background/BannerShape_05.BannerShape_05',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Background/BannerShape_07.BannerShape_07',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Background/BannerShape_08.BannerShape_08',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Background/BannerShape_09.BannerShape_09',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Background/BannerShape_10.BannerShape_10',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Background/BannerShape_11.BannerShape_11',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Background/BannerShape_13.BannerShape_13',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Background/BannerShape_14.BannerShape_14',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Background/BannerShape_16.BannerShape_16',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Background/BannerShape_17.BannerShape_17',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Background/BannerShape_18.BannerShape_18',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Background/BannerShape_19.BannerShape_19',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Background/BannerShape_20.BannerShape_20',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/BackgroundColor/BannerColor_09_Shape.BannerColor_09_Shape',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/BackgroundColor/BannerColor_10_Shape.BannerColor_10_Shape',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/BackgroundColor/BannerColor_11_Shape.BannerColor_11_Shape',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/BackgroundColor/BannerColor_12_Shape.BannerColor_12_Shape',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/BackgroundColor/BannerColor_13_Shape.BannerColor_13_Shape',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/BackgroundColor/BannerColor_14_Shape.BannerColor_14_Shape',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/BackgroundColor/BannerColor_15_Shape.BannerColor_15_Shape',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/BackgroundColor/BannerColor_16_Shape.BannerColor_16_Shape',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/BackgroundColor/BannerColor_17_Shape.BannerColor_17_Shape',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/BackgroundColor/BannerColor_18_Shape.BannerColor_18_Shape',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/BackgroundColor/BannerColor_19_Shape.BannerColor_19_Shape',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/BackgroundColor/BannerColor_20_Shape.BannerColor_20_Shape',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/BackgroundColor/BannerColor_21_Shape.BannerColor_21_Shape',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/BackgroundColor/BannerColor_22_Shape.BannerColor_22_Shape',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/BackgroundColor/BannerColor_23_Shape.BannerColor_23_Shape',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/BackgroundColor/BannerColor_24_Shape.BannerColor_24_Shape',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/BackgroundColor/BannerColor_25_Shape.BannerColor_25_Shape',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/BackgroundColor/BannerColor_26_Shape.BannerColor_26_Shape',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/BackgroundColor/BannerColor_27_Shape.BannerColor_27_Shape',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/BackgroundColor/BannerColor_28_Shape.BannerColor_28_Shape',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/BackgroundColor/BannerColor_29_Shape.BannerColor_29_Shape',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/BackgroundColor/BannerColor_30_Shape.BannerColor_30_Shape',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/BackgroundColor/BannerColor_31_Shape.BannerColor_31_Shape',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/BackgroundColor/BannerColor_32_Shape.BannerColor_32_Shape',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Icon/BannerIcon_01.BannerIcon_01',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Icon/BannerIcon_03.BannerIcon_03',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Icon/BannerIcon_04.BannerIcon_04',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Icon/BannerIcon_06.BannerIcon_06',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Icon/BannerIcon_07.BannerIcon_07',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Icon/BannerIcon_08.BannerIcon_08',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Icon/BannerIcon_09.BannerIcon_09',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Icon/BannerIcon_10.BannerIcon_10',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Icon/BannerIcon_12.BannerIcon_12',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Icon/BannerIcon_13.BannerIcon_13',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Icon/BannerIcon_14.BannerIcon_14',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Icon/BannerIcon_15.BannerIcon_15',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Icon/BannerIcon_16.BannerIcon_16',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Icon/BannerIcon_25.BannerIcon_25',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Icon/BannerIcon_26.BannerIcon_26',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Icon/BannerIcon_27.BannerIcon_27',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Icon/BannerIcon_28.BannerIcon_28',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Icon/BannerIcon_29.BannerIcon_29',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Icon/BannerIcon_30.BannerIcon_30',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Icon/BannerIcon_31.BannerIcon_31',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Icon/BannerIcon_32.BannerIcon_32',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Icon/BannerIcon_33.BannerIcon_33',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Icon/BannerIcon_34.BannerIcon_34',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Icon/BannerIcon_35.BannerIcon_35',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Icon/BannerIcon_36.BannerIcon_36',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Icon/BannerIcon_37.BannerIcon_37',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Icon/BannerIcon_38.BannerIcon_38',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Icon/BannerIcon_39.BannerIcon_39',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Icon/BannerIcon_40.BannerIcon_40',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Icon/BannerIcon_41.BannerIcon_41',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/IconColor/BannerColor_09_Icon.BannerColor_09_Icon',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/IconColor/BannerColor_10_Icon.BannerColor_10_Icon',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/IconColor/BannerColor_11_Icon.BannerColor_11_Icon',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/IconColor/BannerColor_12_Icon.BannerColor_12_Icon',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/IconColor/BannerColor_13_Icon.BannerColor_13_Icon',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/IconColor/BannerColor_14_Icon.BannerColor_14_Icon',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/IconColor/BannerColor_15_Icon.BannerColor_15_Icon',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/IconColor/BannerColor_16_Icon.BannerColor_16_Icon',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/IconColor/BannerColor_17_Icon.BannerColor_17_Icon',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/IconColor/BannerColor_18_Icon.BannerColor_18_Icon',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/IconColor/BannerColor_19_Icon.BannerColor_19_Icon',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/IconColor/BannerColor_20_Icon.BannerColor_20_Icon',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/IconColor/BannerColor_21_Icon.BannerColor_21_Icon',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/IconColor/BannerColor_22_Icon.BannerColor_22_Icon',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/IconColor/BannerColor_23_Icon.BannerColor_23_Icon',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/IconColor/BannerColor_24_Icon.BannerColor_24_Icon',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/IconColor/BannerColor_25_Icon.BannerColor_25_Icon',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/IconColor/BannerColor_26_Icon.BannerColor_26_Icon',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/IconColor/BannerColor_27_Icon.BannerColor_27_Icon',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/IconColor/BannerColor_28_Icon.BannerColor_28_Icon',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/IconColor/BannerColor_29_Icon.BannerColor_29_Icon',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/IconColor/BannerColor_30_Icon.BannerColor_30_Icon',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/IconColor/BannerColor_31_Icon.BannerColor_31_Icon',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/IconColor/BannerColor_32_Icon.BannerColor_32_Icon',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/PatternColor/BannerColor_09_Pattern.BannerColor_09_Pattern',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/PatternColor/BannerColor_10_Pattern.BannerColor_10_Pattern',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/PatternColor/BannerColor_11_Pattern.BannerColor_11_Pattern',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/PatternColor/BannerColor_12_Pattern.BannerColor_12_Pattern',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/PatternColor/BannerColor_13_Pattern.BannerColor_13_Pattern',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/PatternColor/BannerColor_14_Pattern.BannerColor_14_Pattern',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/PatternColor/BannerColor_15_Pattern.BannerColor_15_Pattern',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/PatternColor/BannerColor_16_Pattern.BannerColor_16_Pattern',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/PatternColor/BannerColor_17_Pattern.BannerColor_17_Pattern',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/PatternColor/BannerColor_18_Pattern.BannerColor_18_Pattern',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/PatternColor/BannerColor_19_Pattern.BannerColor_19_Pattern',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/PatternColor/BannerColor_20_Pattern.BannerColor_20_Pattern',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/PatternColor/BannerColor_21_Pattern.BannerColor_21_Pattern',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/PatternColor/BannerColor_22_Pattern.BannerColor_22_Pattern',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/PatternColor/BannerColor_23_Pattern.BannerColor_23_Pattern',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/PatternColor/BannerColor_24_Pattern.BannerColor_24_Pattern',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/PatternColor/BannerColor_25_Pattern.BannerColor_25_Pattern',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/PatternColor/BannerColor_26_Pattern.BannerColor_26_Pattern',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/PatternColor/BannerColor_27_Pattern.BannerColor_27_Pattern',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/PatternColor/BannerColor_28_Pattern.BannerColor_28_Pattern',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/PatternColor/BannerColor_29_Pattern.BannerColor_29_Pattern',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/PatternColor/BannerColor_30_Pattern.BannerColor_30_Pattern',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/PatternColor/BannerColor_31_Pattern.BannerColor_31_Pattern',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/PatternColor/BannerColor_32_Pattern.BannerColor_32_Pattern',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Emotes/Emote_01.Emote_01',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Emotes/Emote_02.Emote_02',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Emotes/Emote_03.Emote_03',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Emotes/Emote_04.Emote_04',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Emotes/Emote_05.Emote_05',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Emotes/Emote_06.Emote_06',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Emotes/Emote_08.Emote_08',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Emotes/Emote_12.Emote_12',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Emotes/Emote_13.Emote_13',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Emotes/Emote_14.Emote_14',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Emotes/Emote_15.Emote_15',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Emotes/Emote_18.Emote_18',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/EyeColor/EyeColor_05.EyeColor_05',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/EyeColor/EyeColor_06.EyeColor_06',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/EyeColor/EyeColor_08.EyeColor_08',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/EyeColor/EyeColor_09.EyeColor_09',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/EyeColor/EyeColor_10.EyeColor_10',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/EyeColor/EyeColor_11.EyeColor_11',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/EyeColor/EyeColor_12.EyeColor_12',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/EyeColor/EyeColor_14.EyeColor_14',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/EyeColor/EyeColor_15.EyeColor_15',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/EyeColor/EyeColor_16.EyeColor_16',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/FaceAcc/FaceAccessory_10.FaceAccessory_10',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/FaceAcc/FaceAccessory_12.FaceAccessory_12',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/FaceAcc/FaceAccessory_13.FaceAccessory_13',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/FaceAcc/FaceAccessory_14.FaceAccessory_14',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HairColor/HairColor_12.HairColor_12',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HairColor/HairColor_14.HairColor_14',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HairColor/HairColor_15.HairColor_15',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HairColor/HairColor_16.HairColor_16',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HairColor/HairColor_17.HairColor_17',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HairColor/HairColor_19.HairColor_19',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HairColor/HairColor_20.HairColor_20',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HairColor/HairColor_21.HairColor_21',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HairColor/HairColor_22.HairColor_22',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HairColor/HairColor_23.HairColor_23',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HairColor/HairColor_24.HairColor_24',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HairColor/HairColor_25.HairColor_25',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HairColor/HairColor_26.HairColor_26',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HairColor/HairColor_28.HairColor_28',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HairColor/HairColor_29.HairColor_29',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HeadAcc/HeadAccessory_01.HeadAccessory_01',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HeadAcc/HeadAccessory_02.HeadAccessory_02',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HeadAcc/HeadAccessory_03.HeadAccessory_03',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HeadAcc/HeadAccessory_04.HeadAccessory_04',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HeadAcc/HeadAccessory_05.HeadAccessory_05',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HeadAcc/HeadAccessory_06.HeadAccessory_06',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HeadAcc/HeadAccessory_07.HeadAccessory_07',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HeadAcc/HeadAccessory_08.HeadAccessory_08',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HeadAcc/HeadAccessory_09.HeadAccessory_09',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HeadAcc/HeadAccessory_10.HeadAccessory_10',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HeadAcc/HeadAccessory_15.HeadAccessory_15',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HeadAcc/HeadAccessory_20.HeadAccessory_20',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HeadAcc/HeadAccessory_25.HeadAccessory_25',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HeroStatue/Material/HeroStatueMaterial_03.HeroStatueMaterial_03',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HeroStatue/Material/HeroStatueMaterial_05.HeroStatueMaterial_05',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HeroStatue/Material/HeroStatueMaterial_06.HeroStatueMaterial_06',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HeroStatue/Material/HeroStatueMaterial_07.HeroStatueMaterial_07',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HeroStatue/Material/HeroStatueMaterial_08.HeroStatueMaterial_08',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HeroStatue/Material/HeroStatueMaterial_09.HeroStatueMaterial_09',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HeroStatue/Material/HeroStatueMaterial_10.HeroStatueMaterial_10',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HeroStatue/Material/HeroStatueMaterial_11.HeroStatueMaterial_11',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HeroStatue/Material/HeroStatueMaterial_12.HeroStatueMaterial_12',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HeroStatue/Material/HeroStatueMaterial_14.HeroStatueMaterial_14',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HeroStatue/Material/HeroStatueMaterial_15.HeroStatueMaterial_15',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HeroStatue/Material/HeroStatueMaterial_16.HeroStatueMaterial_16',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HeroStatue/Material/HeroStatueMaterial_18.HeroStatueMaterial_18',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HeroStatue/Material/HeroStatueMaterial_19.HeroStatueMaterial_19',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HeroStatue/Material/HeroStatueMaterial_20.HeroStatueMaterial_20',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HeroStatue/Material/HeroStatueMaterial_21.HeroStatueMaterial_21',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HeroStatue/Pose/HeroStatuePose_01.HeroStatuePose_01',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HeroStatue/Pose/HeroStatuePose_02.HeroStatuePose_02',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HeroStatue/Pose/HeroStatuePose_04.HeroStatuePose_04',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HeroStatue/Pose/HeroStatuePose_05.HeroStatuePose_05',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HeroStatue/Pose/HeroStatuePose_06.HeroStatuePose_06',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HeroStatue/Pose/HeroStatuePose_08.HeroStatuePose_08',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HeroStatue/Pose/HeroStatuePose_10.HeroStatuePose_10',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HeroStatue/Pose/HeroStatuePose_11.HeroStatuePose_11',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HeroStatue/Pose/HeroStatuePose_12.HeroStatuePose_12',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HeroStatue/Pose/HeroStatuePose_13.HeroStatuePose_13',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HeroStatue/Pose/HeroStatuePose_14.HeroStatuePose_14',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HeroStatue/Pose/HeroStatuePose_15.HeroStatuePose_15',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HeroStatue/Pose/HeroStatuePose_17.HeroStatuePose_17',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HeroStatue/Pose/HeroStatuePose_18.HeroStatuePose_18',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HeroStatue/Pose/HeroStatuePose_19.HeroStatuePose_19',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/HeroStatue/Pose/HeroStatuePose_20.HeroStatuePose_20',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/Blush/BlushShape_02.BlushShape_02',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/Blush/BlushShape_10.BlushShape_10',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/Blush/BlushShape_11.BlushShape_11',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/Blush/BlushShape_12.BlushShape_12',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/Blush/BlushShape_13.BlushShape_13',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/Blush/BlushShape_14.BlushShape_14',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/Blush/BlushShape_15.BlushShape_15',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/Blush/BlushShape_16.BlushShape_16',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/Blush/BlushShape_17.BlushShape_17',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/Blush/BlushShape_18.BlushShape_18',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/Blush/BlushShape_19.BlushShape_19',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/Blush/BlushShape_20.BlushShape_20',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/Blush/BlushShape_21.BlushShape_21',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/BlushColor/MakeupColor_15_Blush.MakeupColor_15_Blush',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/BlushColor/MakeupColor_16_Blush.MakeupColor_16_Blush',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/BlushColor/MakeupColor_17_Blush.MakeupColor_17_Blush',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/BlushColor/MakeupColor_18_Blush.MakeupColor_18_Blush',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/BlushColor/MakeupColor_19_Blush.MakeupColor_19_Blush',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/BlushColor/MakeupColor_20_Blush.MakeupColor_20_Blush',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/BlushColor/MakeupColor_21_Blush.MakeupColor_21_Blush',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/BlushColor/MakeupColor_22_Blush.MakeupColor_22_Blush',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/BlushColor/MakeupColor_23_Blush.MakeupColor_23_Blush',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/BlushColor/MakeupColor_25_Blush.MakeupColor_25_Blush',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/BlushColor/MakeupColor_26_Blush.MakeupColor_26_Blush',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/BlushColor/MakeupColor_28_Blush.MakeupColor_28_Blush',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/BlushColor/MakeupColor_29_Blush.MakeupColor_29_Blush',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/BlushColor/MakeupColor_30_Blush.MakeupColor_30_Blush',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeLiner/EyelinerShape_04.EyelinerShape_04',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeLiner/EyelinerShape_08.EyelinerShape_08',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeLiner/EyelinerShape_09.EyelinerShape_09',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeLiner/EyelinerShape_11.EyelinerShape_11',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeLiner/EyelinerShape_12.EyelinerShape_12',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeLiner/EyelinerShape_13.EyelinerShape_13',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeLiner/EyelinerShape_14.EyelinerShape_14',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeLiner/EyelinerShape_15.EyelinerShape_15',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeLiner/EyelinerShape_16.EyelinerShape_16',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeLiner/EyelinerShape_17.EyelinerShape_17',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeLiner/EyelinerShape_18.EyelinerShape_18',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeLiner/EyelinerShape_20.EyelinerShape_20',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeLiner/EyelinerShape_21.EyelinerShape_21',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeLinerColor/MakeupColor_15_Eyeliner.MakeupColor_15_Eyeliner',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeLinerColor/MakeupColor_16_Eyeliner.MakeupColor_16_Eyeliner',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeLinerColor/MakeupColor_17_Eyeliner.MakeupColor_17_Eyeliner',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeLinerColor/MakeupColor_18_Eyeliner.MakeupColor_18_Eyeliner',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeLinerColor/MakeupColor_19_Eyeliner.MakeupColor_19_Eyeliner',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeLinerColor/MakeupColor_20_Eyeliner.MakeupColor_20_Eyeliner',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeLinerColor/MakeupColor_21_Eyeliner.MakeupColor_21_Eyeliner',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeLinerColor/MakeupColor_22_Eyeliner.MakeupColor_22_Eyeliner',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeLinerColor/MakeupColor_23_Eyeliner.MakeupColor_23_Eyeliner',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeLinerColor/MakeupColor_25_Eyeliner.MakeupColor_25_Eyeliner',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeLinerColor/MakeupColor_26_Eyeliner.MakeupColor_26_Eyeliner',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeLinerColor/MakeupColor_28_Eyeliner.MakeupColor_28_Eyeliner',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeLinerColor/MakeupColor_29_Eyeliner.MakeupColor_29_Eyeliner',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeLinerColor/MakeupColor_30_Eyeliner.MakeupColor_30_Eyeliner',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeShadow/EyeShadow_07.EyeShadow_07',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeShadow/EyeShadow_09.EyeShadow_09',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeShadow/EyeShadow_10.EyeShadow_10',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeShadow/EyeShadow_12.EyeShadow_12',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeShadow/EyeShadow_13.EyeShadow_13',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeShadow/EyeShadow_14.EyeShadow_14',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeShadow/EyeShadow_15.EyeShadow_15',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeShadow/EyeShadow_16.EyeShadow_16',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeShadow/EyeShadow_17.EyeShadow_17',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeShadow/EyeShadow_18.EyeShadow_18',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeShadow/EyeShadow_19.EyeShadow_19',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeShadow/EyeShadow_20.EyeShadow_20',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeShadow/EyeShadow_21.EyeShadow_21',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeShadowColor/MakeupColor_15_Eyeshadow.MakeupColor_15_Eyeshadow',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeShadowColor/MakeupColor_16_Eyeshadow.MakeupColor_16_Eyeshadow',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeShadowColor/MakeupColor_17_Eyeshadow.MakeupColor_17_Eyeshadow',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeShadowColor/MakeupColor_18_Eyeshadow.MakeupColor_18_Eyeshadow',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeShadowColor/MakeupColor_19_Eyeshadow.MakeupColor_19_Eyeshadow',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeShadowColor/MakeupColor_20_Eyeshadow.MakeupColor_20_Eyeshadow',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeShadowColor/MakeupColor_21_Eyeshadow.MakeupColor_21_Eyeshadow',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeShadowColor/MakeupColor_22_Eyeshadow.MakeupColor_22_Eyeshadow',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeShadowColor/MakeupColor_23_Eyeshadow.MakeupColor_23_Eyeshadow',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeShadowColor/MakeupColor_25_Eyeshadow.MakeupColor_25_Eyeshadow',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeShadowColor/MakeupColor_26_Eyeshadow.MakeupColor_26_Eyeshadow',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeShadowColor/MakeupColor_28_Eyeshadow.MakeupColor_28_Eyeshadow',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeShadowColor/MakeupColor_29_Eyeshadow.MakeupColor_29_Eyeshadow',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/EyeShadowColor/MakeupColor_30_Eyeshadow.MakeupColor_30_Eyeshadow',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/Lipstick/Lipstick_06.Lipstick_06',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/Lipstick/Lipstick_07.Lipstick_07',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/Lipstick/Lipstick_08.Lipstick_08',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/Lipstick/Lipstick_10.Lipstick_10',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/Lipstick/Lipstick_11.Lipstick_11',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/Lipstick/Lipstick_12.Lipstick_12',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/Lipstick/Lipstick_13.Lipstick_13',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/Lipstick/Lipstick_14.Lipstick_14',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/Lipstick/Lipstick_15.Lipstick_15',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/Lipstick/Lipstick_16.Lipstick_16',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/Lipstick/Lipstick_17.Lipstick_17',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/Lipstick/Lipstick_18.Lipstick_18',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/Lipstick/Lipstick_19.Lipstick_19',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/Lipstick/Lipstick_21.Lipstick_21',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/LipstickColor/MakeupColor_15_Lipstick.MakeupColor_15_Lipstick',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/LipstickColor/MakeupColor_16_Lipstick.MakeupColor_16_Lipstick',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/LipstickColor/MakeupColor_17_Lipstick.MakeupColor_17_Lipstick',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/LipstickColor/MakeupColor_18_Lipstick.MakeupColor_18_Lipstick',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/LipstickColor/MakeupColor_19_Lipstick.MakeupColor_19_Lipstick',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/LipstickColor/MakeupColor_20_Lipstick.MakeupColor_20_Lipstick',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/LipstickColor/MakeupColor_21_Lipstick.MakeupColor_21_Lipstick',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/LipstickColor/MakeupColor_22_Lipstick.MakeupColor_22_Lipstick',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/LipstickColor/MakeupColor_23_Lipstick.MakeupColor_23_Lipstick',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/LipstickColor/MakeupColor_25_Lipstick.MakeupColor_25_Lipstick',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/LipstickColor/MakeupColor_26_Lipstick.MakeupColor_26_Lipstick',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/LipstickColor/MakeupColor_28_Lipstick.MakeupColor_28_Lipstick',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/LipstickColor/MakeupColor_29_Lipstick.MakeupColor_29_Lipstick',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Makeup/LipstickColor/MakeupColor_30_Lipstick.MakeupColor_30_Lipstick',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/PupilShape/Pupil_03.Pupil_03',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/PupilShape/Pupil_04.Pupil_04',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/PupilShape/Pupil_05.Pupil_05',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/PupilShape/Pupil_07.Pupil_07',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/PupilShape/Pupil_09.Pupil_09',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/PupilShape/Pupil_10.Pupil_10',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/PupilShape/Pupil_11.Pupil_11',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/PupilShape/Pupil_12.Pupil_12',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/PupilShape/Pupil_13.Pupil_13',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/PupilShape/Pupil_15.Pupil_15',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Scar/Scars_02.Scars_02',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Scar/Scars_03.Scars_03',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Scar/Scars_07.Scars_07',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Scar/Scars_12.Scars_12',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Scar/Scars_17.Scars_17',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/SkinTone/SkinToneColor_16.SkinToneColor_16',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/SkinTone/SkinToneColor_26.SkinToneColor_26',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/SkinTone/SkinToneColor_27.SkinToneColor_27',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/SkinTone/SkinToneColor_28.SkinToneColor_28',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/SkinTone/SkinToneColor_29.SkinToneColor_29',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/SkinTone/SkinToneColor_30.SkinToneColor_30',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/SkinTone/SkinToneColor_36.SkinToneColor_36',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/SkinTone/SkinToneColor_37.SkinToneColor_37',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/SkinTone/SkinToneColor_38.SkinToneColor_38',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/SkinTone/SkinToneColor_39.SkinToneColor_39',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/SkinTone/SkinToneColor_40.SkinToneColor_40',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/SkinTone/SkinToneColor_41.SkinToneColor_41',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/SkinTone/SkinToneColor_42.SkinToneColor_42',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/SkinTone/SkinToneColor_43.SkinToneColor_43',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/SkinTone/SkinToneColor_44.SkinToneColor_44',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Tattoo/Tattoos_01.Tattoos_01',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Tattoo/Tattoos_02.Tattoos_02',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Tattoo/Tattoos_03.Tattoos_03',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Tattoo/Tattoos_04.Tattoos_04',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Tattoo/Tattoos_05.Tattoos_05',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Tattoo/Tattoos_09.Tattoos_09',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Tattoo/Tattoos_10.Tattoos_10',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Tattoo/Tattoos_11.Tattoos_11',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Tattoo/Tattoos_12.Tattoos_12',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Tattoo/Tattoos_13.Tattoos_13',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Tattoo/Tattoos_15.Tattoos_15',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Tattoo/Tattoos_16.Tattoos_16',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/TattooColor/TattooColor_15.TattooColor_15',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/TattooColor/TattooColor_16.TattooColor_16',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/TattooColor/TattooColor_17.TattooColor_17',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/TattooColor/TattooColor_18.TattooColor_18',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/TattooColor/TattooColor_19.TattooColor_19',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/TattooColor/TattooColor_20.TattooColor_20',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/TattooColor/TattooColor_21.TattooColor_21',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/TattooColor/TattooColor_22.TattooColor_22',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/TattooColor/TattooColor_23.TattooColor_23',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/TattooColor/TattooColor_25.TattooColor_25',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/TattooColor/TattooColor_26.TattooColor_26',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/TattooColor/TattooColor_28.TattooColor_28',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/TattooColor/TattooColor_29.TattooColor_29',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/TattooColor/TattooColor_30.TattooColor_30',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Pattern/BannerPattern_26.BannerPattern_26',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Pattern/BannerPattern_21.BannerPattern_21',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Pattern/BannerPattern_05.BannerPattern_05',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Pattern/BannerPattern_13.BannerPattern_13',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Pattern/BannerPattern_23.BannerPattern_23',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Pattern/BannerPattern_19.BannerPattern_19',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Pattern/BannerPattern_09.BannerPattern_09',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Pattern/BannerPattern_08.BannerPattern_08',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Pattern/BannerPattern_24.BannerPattern_24',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Pattern/BannerPattern_03.BannerPattern_03',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Pattern/BannerPattern_14.BannerPattern_14',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Pattern/BannerPattern_15.BannerPattern_15',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Pattern/BannerPattern_18.BannerPattern_18',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Pattern/BannerPattern_22.BannerPattern_22',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Pattern/BannerPattern_20.BannerPattern_20',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Pattern/BannerPattern_11.BannerPattern_11',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Pattern/BannerPattern_04.BannerPattern_04',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Pattern/BannerPattern_12.BannerPattern_12',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Pattern/BannerPattern_10.BannerPattern_10',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Pattern/BannerPattern_06.BannerPattern_06',
        '/Game/PlayerCharacters/_Shared/_Design/Customization/Banner/Pattern/BannerPattern_07.BannerPattern_07'
    ])
profile_skins_defaults = set([
    '/Game/PlayerCharacters/_Customizations/Beastmaster/Skins/CustomSkin_Beastmaster_Default.CustomSkin_Beastmaster_Default',
    '/Game/PlayerCharacters/_Customizations/Gunner/Skins/CustomSkin_Gunner_Default.CustomSkin_Gunner_Default',
    '/Game/PlayerCharacters/_Customizations/Operative/Skins/CustomSkin_Operative_Default.CustomSkin_Operative_Default',
    '/Game/PlayerCharacters/_Customizations/SirenBrawler/Skins/CustomSkin_Siren_Default.CustomSkin_Siren_Default',
    ])

# Profile customizations - Heads
profile_heads = set([])
profile_heads_defaults = set([])

# Profile customizations - ECHO themes
profile_echothemes = set([])
profile_echothemes_defaults = set([])

# Profile customizations - Emotes
profile_emotes = set([])
profile_emotes_defaults = set([])

# Profile customizations - Room Decorations
# We're handling these a bit differently so that our util can re-order them in
# alphabetical order.
profile_roomdeco_obj_to_eng = {}
profile_roomdeco_eng_to_obj = {v: k for k, v in profile_roomdeco_obj_to_eng.items()}

# CRC32 table used to compute weapon customization hashes in the profile.  Many
# thanks to Gibbed, yet again, for supplying this!
_weapon_cust_crc32_table = [
        0x00000000, 0x04C11DB7, 0x09823B6E, 0x0D4326D9, 0x130476DC, 0x17C56B6B, 0x1A864DB2, 0x1E475005,
        0x2608EDB8, 0x22C9F00F, 0x2F8AD6D6, 0x2B4BCB61, 0x350C9B64, 0x31CD86D3, 0x3C8EA00A, 0x384FBDBD,
        0x4C11DB70, 0x48D0C6C7, 0x4593E01E, 0x4152FDA9, 0x5F15ADAC, 0x5BD4B01B, 0x569796C2, 0x52568B75,
        0x6A1936C8, 0x6ED82B7F, 0x639B0DA6, 0x675A1011, 0x791D4014, 0x7DDC5DA3, 0x709F7B7A, 0x745E66CD,
        0x9823B6E0, 0x9CE2AB57, 0x91A18D8E, 0x95609039, 0x8B27C03C, 0x8FE6DD8B, 0x82A5FB52, 0x8664E6E5,
        0xBE2B5B58, 0xBAEA46EF, 0xB7A96036, 0xB3687D81, 0xAD2F2D84, 0xA9EE3033, 0xA4AD16EA, 0xA06C0B5D,
        0xD4326D90, 0xD0F37027, 0xDDB056FE, 0xD9714B49, 0xC7361B4C, 0xC3F706FB, 0xCEB42022, 0xCA753D95,
        0xF23A8028, 0xF6FB9D9F, 0xFBB8BB46, 0xFF79A6F1, 0xE13EF6F4, 0xE5FFEB43, 0xE8BCCD9A, 0xEC7DD02D,
        0x34867077, 0x30476DC0, 0x3D044B19, 0x39C556AE, 0x278206AB, 0x23431B1C, 0x2E003DC5, 0x2AC12072,
        0x128E9DCF, 0x164F8078, 0x1B0CA6A1, 0x1FCDBB16, 0x018AEB13, 0x054BF6A4, 0x0808D07D, 0x0CC9CDCA,
        0x7897AB07, 0x7C56B6B0, 0x71159069, 0x75D48DDE, 0x6B93DDDB, 0x6F52C06C, 0x6211E6B5, 0x66D0FB02,
        0x5E9F46BF, 0x5A5E5B08, 0x571D7DD1, 0x53DC6066, 0x4D9B3063, 0x495A2DD4, 0x44190B0D, 0x40D816BA,
        0xACA5C697, 0xA864DB20, 0xA527FDF9, 0xA1E6E04E, 0xBFA1B04B, 0xBB60ADFC, 0xB6238B25, 0xB2E29692,
        0x8AAD2B2F, 0x8E6C3698, 0x832F1041, 0x87EE0DF6, 0x99A95DF3, 0x9D684044, 0x902B669D, 0x94EA7B2A,
        0xE0B41DE7, 0xE4750050, 0xE9362689, 0xEDF73B3E, 0xF3B06B3B, 0xF771768C, 0xFA325055, 0xFEF34DE2,
        0xC6BCF05F, 0xC27DEDE8, 0xCF3ECB31, 0xCBFFD686, 0xD5B88683, 0xD1799B34, 0xDC3ABDED, 0xD8FBA05A,
        0x690CE0EE, 0x6DCDFD59, 0x608EDB80, 0x644FC637, 0x7A089632, 0x7EC98B85, 0x738AAD5C, 0x774BB0EB,
        0x4F040D56, 0x4BC510E1, 0x46863638, 0x42472B8F, 0x5C007B8A, 0x58C1663D, 0x558240E4, 0x51435D53,
        0x251D3B9E, 0x21DC2629, 0x2C9F00F0, 0x285E1D47, 0x36194D42, 0x32D850F5, 0x3F9B762C, 0x3B5A6B9B,
        0x0315D626, 0x07D4CB91, 0x0A97ED48, 0x0E56F0FF, 0x1011A0FA, 0x14D0BD4D, 0x19939B94, 0x1D528623,
        0xF12F560E, 0xF5EE4BB9, 0xF8AD6D60, 0xFC6C70D7, 0xE22B20D2, 0xE6EA3D65, 0xEBA91BBC, 0xEF68060B,
        0xD727BBB6, 0xD3E6A601, 0xDEA580D8, 0xDA649D6F, 0xC423CD6A, 0xC0E2D0DD, 0xCDA1F604, 0xC960EBB3,
        0xBD3E8D7E, 0xB9FF90C9, 0xB4BCB610, 0xB07DABA7, 0xAE3AFBA2, 0xAAFBE615, 0xA7B8C0CC, 0xA379DD7B,
        0x9B3660C6, 0x9FF77D71, 0x92B45BA8, 0x9675461F, 0x8832161A, 0x8CF30BAD, 0x81B02D74, 0x857130C3,
        0x5D8A9099, 0x594B8D2E, 0x5408ABF7, 0x50C9B640, 0x4E8EE645, 0x4A4FFBF2, 0x470CDD2B, 0x43CDC09C,
        0x7B827D21, 0x7F436096, 0x7200464F, 0x76C15BF8, 0x68860BFD, 0x6C47164A, 0x61043093, 0x65C52D24,
        0x119B4BE9, 0x155A565E, 0x18197087, 0x1CD86D30, 0x029F3D35, 0x065E2082, 0x0B1D065B, 0x0FDC1BEC,
        0x3793A651, 0x3352BBE6, 0x3E119D3F, 0x3AD08088, 0x2497D08D, 0x2056CD3A, 0x2D15EBE3, 0x29D4F654,
        0xC5A92679, 0xC1683BCE, 0xCC2B1D17, 0xC8EA00A0, 0xD6AD50A5, 0xD26C4D12, 0xDF2F6BCB, 0xDBEE767C,
        0xE3A1CBC1, 0xE760D676, 0xEA23F0AF, 0xEEE2ED18, 0xF0A5BD1D, 0xF464A0AA, 0xF9278673, 0xFDE69BC4,
        0x89B8FD09, 0x8D79E0BE, 0x803AC667, 0x84FBDBD0, 0x9ABC8BD5, 0x9E7D9662, 0x933EB0BB, 0x97FFAD0C,
        0xAFB010B1, 0xAB710D06, 0xA6322BDF, 0xA2F33668, 0xBCB4666D, 0xB8757BDA, 0xB5365D03, 0xB1F740B4,
        ]

def inventory_path_hash(object_path):
    """
    Computes the hashes used in the profile for weapon customizations and the golden key
    count.  Possibly used for other things, too.  Many thanks to Gibbed, yet again, for this!
    """
    global _weapon_cust_crc32_table
    if '.' not in object_path:
        object_path = '{}.{}'.format(object_path, object_path.split('/')[-1])

    # TODO: Gibbed was under the impression that these were checksummed in
    # UTF-16, but the hashes all match for me when using latin1/utf-8.
    object_full = object_path.upper().encode('latin1')
    crc32 = 0
    for char in object_full:
        crc32 = (_weapon_cust_crc32_table[(crc32 ^ (char >> 0)) & 0xFF] ^ (crc32 >> 8)) & 0xFFFFFFFF
        crc32 = (_weapon_cust_crc32_table[(crc32 ^ (char >> 8)) & 0xFF] ^ (crc32 >> 8)) & 0xFFFFFFFF
    return crc32

def weapon_cust_paths_to_hash(obj_to_eng):
    """
    Computes the hashes used in the profile, for weapon customizations (skins+trinkets).
    """
    to_ret = {}
    for (object_path, eng) in obj_to_eng.items():
        to_ret[inventory_path_hash(object_path)] = eng
    return to_ret

# Profile customizations - Weapon Skins
profile_weaponskins_obj_to_eng = {}
profile_weaponskins_hash_to_eng = weapon_cust_paths_to_hash(profile_weaponskins_obj_to_eng)
profile_weaponskins_eng_to_hash = {v: k for k, v in profile_weaponskins_hash_to_eng.items()}

# Profile customizations - Weapon Trinkets
profile_weapontrinkets_obj_to_eng = {}
profile_weapontrinkets_hash_to_eng = weapon_cust_paths_to_hash(profile_weapontrinkets_obj_to_eng)
profile_weapontrinkets_eng_to_hash = {v: k for k, v in profile_weapontrinkets_hash_to_eng.items()}

# Golden Keys
goldenkey_category = '/Game/Gear/_Shared/_Design/InventoryCategories/InventoryCategory_GoldenKey'
goldenkey_hash = inventory_path_hash(goldenkey_category)

# Vault Card #1 Keys
vaultcard1key_category = '/Game/Gear/_Shared/_Design/InventoryCategories/InventoryCategory_VaultCard1Key'
vaultcard1key_hash = inventory_path_hash(vaultcard1key_category)

# Vault Card #2 Keys
vaultcard2key_category = '/Game/Gear/_Shared/_Design/InventoryCategories/InventoryCategory_VaultCard2Key'
vaultcard2key_hash = inventory_path_hash(vaultcard2key_category)

# Vault Card #3 Keys
vaultcard3key_category = '/Game/Gear/_Shared/_Design/InventoryCategories/InventoryCategory_VaultCard3Key'
vaultcard3key_hash = inventory_path_hash(vaultcard3key_category)

# Diamond Keys
diamondkey_category = '/Game/Gear/_Shared/_Design/InventoryCategories/InventoryCategory_DiamondKey'
diamondkey_hash = inventory_path_hash(diamondkey_category)

# XP
max_level = 72
required_xp_list = [
    0,          # lvl 1
    358,        # lvl 2
    1241,       # lvl 3
    2850,       # lvl 4
    5376,       # lvl 5
    8997,       # lvl 6
    13886,      # lvl 7
    20208,      # lvl 8
    28126,      # lvl 9
    37798,      # lvl 10
    49377,      # lvl 11
    63016,      # lvl 12
    78861,      # lvl 13
    97061,      # lvl 14
    117757,     # lvl 15
    141092,     # lvl 16
    167206,     # lvl 17
    196238,     # lvl 18
    228322,     # lvl 19
    263595,     # lvl 20
    302190,     # lvl 21
    344238,     # lvl 22
    389873,     # lvl 23
    439222,     # lvl 24
    492414,     # lvl 25
    549578,     # lvl 26
    610840,     # lvl 27
    676325,     # lvl 28
    746158,     # lvl 29
    820463,     # lvl 30
    899363,     # lvl 31
    982980,     # lvl 32
    1071435,    # lvl 33
    1164850,    # lvl 34
    1263343,    # lvl 35
    1367034,    # lvl 36
    1476041,    # lvl 37
    1590483,    # lvl 38
    1710476,    # lvl 39
    1836137,    # lvl 40
    # 1967582,    # lvl 41
    # 2104926,    # lvl 42
    # 2248285,    # lvl 43
    # 2397772,    # lvl 44
    # 2553501,    # lvl 45
    # 2715586,    # lvl 46
    # 2884139,    # lvl 47
    # 3059273,    # lvl 48
    # 3241098,    # lvl 49
    # 3429728,    # lvl 50
    # 3625271,    # lvl 51
    # 3827840,    # lvl 52
    # 4037543,    # lvl 53
    # 4254491,    # lvl 54
    # 4478792,    # lvl 55
    # 4710556,    # lvl 56
    # 4949890,    # lvl 57
    # 5196902,    # lvl 58
    # 5451701,    # lvl 59
    # 5714393,    # lvl 60
    # 5985086,    # lvl 61
    # 6263885,    # lvl 62
    # 6550897,    # lvl 63
    # 6846227,    # lvl 64
    # 7149982,    # lvl 65
    # 7462266,    # lvl 66
    # 7783184,    # lvl 67
    # 8112840,    # lvl 68
    # 8451340,    # lvl 69
    # 8798786,    # lvl 70
    # 9155282,    # lvl 71
    # 9520932,    # lvl 72
    # 9895837,    # lvl 73
    # 10280103,    # lvl 74
    # 10673830,    # lvl 75
    # 11077120,    # lvl 76
    # 11490077,    # lvl 77
    # 11912801,    # lvl 78
    # 12345393,    # lvl 79
    # 12787955,    # lvl 80
]
max_supported_level = len(required_xp_list)

# Mayhem parts
mayhem_part_to_lvl = {
        # '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Design/MayhemParts/Part_WeaponMayhemLevel_01.Part_WeaponMayhemLevel_01': 1,
        # '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Design/MayhemParts/Part_WeaponMayhemLevel_02.Part_WeaponMayhemLevel_02': 2,
        # '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Design/MayhemParts/Part_WeaponMayhemLevel_03.Part_WeaponMayhemLevel_03': 3,
        # '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Design/MayhemParts/Part_WeaponMayhemLevel_04.Part_WeaponMayhemLevel_04': 4,
        # '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Design/MayhemParts/Part_WeaponMayhemLevel_05.Part_WeaponMayhemLevel_05': 5,
        # '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Design/MayhemParts/Part_WeaponMayhemLevel_06.Part_WeaponMayhemLevel_06': 6,
        # '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Design/MayhemParts/Part_WeaponMayhemLevel_07.Part_WeaponMayhemLevel_07': 7,
        # '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Design/MayhemParts/Part_WeaponMayhemLevel_08.Part_WeaponMayhemLevel_08': 8,
        # '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Design/MayhemParts/Part_WeaponMayhemLevel_09.Part_WeaponMayhemLevel_09': 9,
        # '/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Design/MayhemParts/Part_WeaponMayhemLevel_10.Part_WeaponMayhemLevel_10': 10,
        }
mayhem_part_lower_to_lvl = {k.lower(): v for k, v in mayhem_part_to_lvl.items()}
mayhem_lvl_to_part = {v: k for k, v in mayhem_part_to_lvl.items()}
mayhem_max = max(mayhem_part_to_lvl.values())

# InvData types which can accept Mayhem parts
# (may have to be more clever about this if non-guns start accepting *different* Mayhem parts)
mayhem_invdata_types = set([])
mayhem_invdata_lower_types = set([t.lower() for t in mayhem_invdata_types])

# Anointable InvData types - will be identical to Mayhemable list, plus shields
anointable_invdata_types = mayhem_invdata_types | set(['/Game/Gear/Shields/_Design/A_Data/Shield_Default.Shield_Default'])
anointable_invdata_lower_types = set([t.lower() for t in anointable_invdata_types])

# Guardian Rank Rewards
guardian_rank_rewards = set([])

# Eridian Cube Puzzle stat
cube_puzzle_stat = '/Game/PlayerCharacters/_Shared/_Design/Stats/GameSystem/Stat_GameSystem_BeachCubeSolved.Stat_GameSystem_BeachCubeSolved'

# Takedown Discovery missions
takedown_missions = {}

# Mission names
#
# For most missions, the following find statement will generate this list:
#
#    for file in $(find Game/Missions Game/PatchDLC/Dandelion/Missions Game/PatchDLC/Hibiscus/Missions Game/PatchDLC/Raid1/Missions Game/PatchDLC/BloodyHarvest/Missions Game/PatchDLC/CitizenScience/Missions Game/PatchDLC/Event2/Missions Game/PatchDLC/Takedown2/Missions Game/PatchDLC/Geranium/Missions Game/PatchDLC/Alisma/Missions Game/PatchDLC/Ixora/Missions Game/PatchDLC/Ixora2/Missions \( -iname "Mission_*.uexp" -o -name "SideMission_*.uexp" -o -name "EP*_DLC2.uexp" -o -name "ALI_EP*.uexp" -o -name "ALI_SM_*.uexp" \) -print); do echo -n "'/$(dirname $file)/$(basename $file .uexp)': \""; echo $(strings $file | head -n 2 | tail -n 1)\",; done
#
# Various plot missions, though, from both the main game and DLC1, will need
# some edits by hand (they use a UIName_*_MissionTitle object instead.)  Also,
# the Rare Spawn missions need the second string, not the first, so you'll
# want to run this to grab those:
#
#    for file in $(find Game/Missions/Side/RareSpawn Game/PatchDLC/Hibiscus/Missions/Side/RareSpawn -iname "Mission_*.uexp" -print); do echo -n "'/$(dirname $file)/$(basename $file .uexp)': \""; echo $(strings $file | head -n 4 | tail -n 1)\",; done
#    
# Keep in mind that the El Dragon Jr one will need a hand edit, since `strings`
# only matches on latin1 by default (at least on the GNU/Linux version).
mission_to_name = {
        # '/Game/Missions/Plot/Mission_Ep01_ChildrenOfTheVault': "Children of the Vault",
        # '/Game/Missions/Plot/Mission_Ep02_Sacrifice': "From the Ground Up",
        # '/Game/Missions/Plot/Mission_Ep03_GetVaultMap': "Cult Following",
        }
for k, v in list(mission_to_name.items()):
    lower = k.lower()
    last_bit = lower.split('/')[-1]
    new_k = '{}.{}_c'.format(lower, last_bit)
    mission_to_name[new_k] = v

# Plot missions (of the sort that we don't want to allow removing, since you'd
# probably be locked out of the plot missions).  These were just copy+pasted
# from the mission_to_name structure above and pruned manually.
plot_missions = set()
for mission_name in [
        # '/Game/Missions/Plot/Mission_Ep01_ChildrenOfTheVault',
        ]:
    lower = mission_name.lower()
    last_bit = lower.split('/')[-1]
    plot_missions.add('{}.{}_c'.format(lower, last_bit))

# Map-to-eng
map_to_eng = {
     #   'Anger_P': "Castle Crimson",
 
        }

# Autogenerated by gen_fts_mappings.py, in my bl3hotfixmodding project (in dataprocessing)
fts_to_map = {
 #       '/game/gamedata/fasttravel/fts_atlashq.fts_atlashq': 'AtlasHQ_P',
        }

