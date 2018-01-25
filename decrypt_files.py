# -*- coding:Utf-8 -*-

import os
import string
from Crypto.Cipher import AES

# Récupère pour chaque fichier du jar, son chemin et la clé qui lui est associée
def get_file_key():
    path = os.path.join(os.getcwd(), "results_decrypted_2/all_data_strings.txt")
    res = {}
    with open(path, "r") as f:
        content = f.readlines()
        for i, line in enumerate(content):
            try:
                # Vérifie que la ligne n'est pas une classe, est potentiellement un chemin et que la ligne suivante est une clé
                # Extrait du fichier :
                #./com/retrieving/regelation/ratooner/DortHuzoornintheskymanintheskymanintheskymanintheskyanintheskyn.class
                #(/com/zander/tachist/metastasis/DwineTickt
                #61612574a1r63kcdt
                if not "/" in content[i + 1] and "/" in content[i] and not ".class" in content[i]:
                    if len(content[i + 1].strip()) == 17:
                        # supprime le dernier caractère de la clé (souvent t) et l'associe au chemin du fichier
                        res[content[i].strip()[0:len(content[i].strip()) - 1]] = content[i + 1][0:16]
                    else:
                        # gestion du cas où la clé est sur 2 lignes
                        value = content[i + 1].strip() + content[i + 2].strip()
                        if len(value) != 16:
                            # suppression du caractère en trop sur la deuxième ligne
                            res[content[i].strip()[0:len(content[i].strip()) - 1]] = value[
                                                                                     0:len(content[i + 2].strip()) - 1]
                        else:
                            # la clé est associée au fichier
                            res[content[i].strip()[0:len(content[i].strip()) - 1]] = value
            except:
                print "ERROR : ", content[i]
    return res

# Déchiffrement de chaque fichier avec sa clé
def decrypt_file(file_path, key):
    base_path = "./Facture"
    result = "./results_decrypted_3"
    cipher = AES.new(key, AES.MODE_ECB)
    try:
        with open(base_path + file_path, "rb") as f:
            with open(os.path.join(result, os.path.basename(file_path)), "w") as fbis:
                fbis.write(cipher.decrypt(f.read()))
    except Exception as e:
        print e

# Nettoyage des chemins de fichiers qui commencent par un caractère aléatoire
def clean_path(res):
    for path, secret_key in res.items():
        if len(secret_key) == 16:
            if path[0] != "/" or (path[0] == "/" and path[1] == "/"):
                res[path[1:len(path)]] = res.pop(path)
    return res


res = get_file_key()
res = clean_path(res)

for path,secret_key in res.items():
    if len(secret_key) == 16 :
        decrypt_file(path,secret_key)

# Affiche tous les chemins vers les fichiers dont la clé n'a pas la bonne taille
for path, secret_key in res.items():
    if len(secret_key) != 16:
        print path, secret_key