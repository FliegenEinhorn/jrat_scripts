# -*- coding:Utf-8 -*-

from Crypto.Cipher import AES
import os

secret_key = "f32d22ce00621c1\0"

cipher = AES.new(secret_key, AES.MODE_ECB)
path = "./Facture/com/vivandi/quashee/terraquean/DrierEyen"

with open(path, "rb") as f:
    with open(os.path.basename(path), "wb") as fbis:
        fbis.write(cipher.decrypt(f.read()))