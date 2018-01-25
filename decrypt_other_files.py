# -*- coding:Utf-8 -*-

import os
import string
from Crypto.Cipher import AES

files = [{"path" : "/com/vivandi/quashee/folksey/MacroGpad", "key" : "1e4o2746j5\0"+"1d9d1"},
         {"path" : "/com/zander/titania/quaeres/PensyDux", "key" : "bamv63c\0"+"9pf346dq"},
         {"path" : "/com/vivandi/quashee/overtimes/WhunAslant", "key" : "1h4l\0"+"4202c6d4623"},
         {"path" : "/com/zander/titania/LocZoons", "key" : "ab1\0"+"03b110137d3p"},
         {"path" : "/com/vivandi/ethnoses/LdgDrays", "key" : "8n02b1b6k\0"+"20gfk7"},
         {"path" : "/com/retrieving/trimnesses/thalthan/MuthThave", "key" : "h4\0"+"4e415i522\0"+"kcc"},
         {"path" : "/com/retrieving/trimnesses/niggard/GummedBrid", "key" : "1a8\0"+"6d0k3pdb8b35"},
         {"path" : "/com/zander/titania/costumire/ShirtsYrs", "key" : "p2021091\0"+"6ae6956"},
         {"path" : "/com/retrieving/trimnesses/niggard/FrateTng", "key": "65a3832\0"+"79g233b7"},
         {"path" : "/com/zander/donnybrook/louisa/BoxCanoed", "key" : "1\0"+"jb153cm85iq694"},
         {"path" : "/com/retrieving/trimnesses/niggard/MortonGuv", "key" : "\0"+"e0oa3e\0"+"2m7054a6"},
         {"path" : "/com/vivandi/honeybloom/husbander/BuzzedToher", "key" : "h3\0"+"f5662s51m4m12"},
         {"path" : "/com/zander/donnybrook/weeweeing/ColtsGrouf", "key" : "3\0"+"22b02agsro7124"},
         {"path" : "/com/zander/titania/costumire/UsuVite", "key":"\0"+"7f20ae1j1\0"+"e07qa"},
         {"path" : "/com/retrieving/macaasim/epizoa/OadHarmal", "key" : "031n251\0"+"62503nc0"},
         {"path" : "/com/zander/titania/SestonGail", "key" : "\0"+"030h201i188d43q"},
         {"path" : "/com/zander/titania/lucken/RazeCeptor", "key" : "r344n91440\0"+"iaj4a"},
         {"path" : "/com/retrieving/macaasim/blushless/JynxTanker", "key" : "2ijh4a20ok1q0\0"+"\0"+"4"},
         {"path" : "/com/zander/donnybrook/MoulviAgin", "key" : "3adf2j0\0"+"0429j200"},
         {"path" : "/com/retrieving/macaasim/InflCangia", "key" : "16f\0"+"f0e04a244en0"},
         {"path" : "/com/retrieving/regelation/philopater/BerobTags", "key" : "9i0n3ll2\0"+"3024212"},
         {"path" : "/com/zander/donnybrook/BipodPooty", "key" : "a225122f06r1p\0"+"42"},
         {"path" : "/com/vivandi/ethnoses/CuyaClift", "key" : "6dqh6a1110m06\0"+"14"},
         {"path" : "/com/zander/donnybrook/weeweeing/MoniedDorian", "key" : "d5326f\0"+"2i5a66egf"},
         {"path" : "/com/vivandi/quashee/PelfLimber", "key" : "2691\0"+"45000cb8242"},
         {"path" : "/com/retrieving/regelation/simous/SoySelety", "key" : "21gd825j274d\0"+"0b1"},
         {"path" : "/com/vivandi/FrimFlawed", "key" : "ho475p754\0"+"110j11"},
         {"path" : "/com/retrieving/regelation/RcptVim", "key" : "2bed1\0"+"006ah\0"+"8dos"},
         {"path" : "/com/zander/titania/lucken/BetoneHanap", "key" : "910\0"+"4fl6i20416e0"},
         {"path" : "/com/zander/titania/lucken/SweltPossy", "key" : "qd\0"+"265959\0"+"1k435c"},
         {"path" : "/com/retrieving/regelation/philopater/ReburnUstion", "key" : "5\0"+"e2g5c7f47a83h0"}
        ]

for elem in files :
    base_path = "./Facture"
    result = "./results_decrypted_4"
    try :
        cipher = AES.new(elem["key"], AES.MODE_ECB)
        with open(base_path + elem["path"], "rb") as f :
            with open(os.path.join(result,os.path.basename(elem["path"]))+".tar.gz", "w") as fbis :
                fbis.write(cipher.decrypt(f.read()))
    except Exception as e:
        print e
        print elem["path"], " : ", elem["key"], len(elem["key"])
