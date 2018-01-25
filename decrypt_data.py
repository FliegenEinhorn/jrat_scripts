# -*- coding:Utf-8 -*-

from Crypto.Cipher import AES
import os
import shutil



def decrypt_files() :
    # Clé secrète récupérée dans la classe Loader
    secret_key_str = "0123456789012345"
    cipher = AES.new(secret_key_str, AES.MODE_ECB)

    results ="./results_decrypted_2"
    # On tente de déchiffrer chaque fichier du genre qui n'est pas une classe avec la clé que l'on a récupérée
    for root, dirs, files in os.walk("./Facture"):
        for name in files:
            if not ".class" in name :
                with open(os.path.join(root,name),"rb") as f :
                    with open(os.path.join(results, name),"w") as fw :
                        try :
                            fw.write(cipher.decrypt(f.read()))
                        except :
                            # on enregistre tous les chemins des fichiers qui n'ont pas pu être déchiffrés
                            with open("errors_decrypted", "w") as fe :
                                fe.write(os.path.join(root,name))


def get_interesting_files() :
    results ="./results_decrypted_2"
    for root, dirs, files in os.walk(results):
        for file_ in files :
            with open(os.path.join(root,file_), "rb") as f :
                content = f.read()
                # on renomme tous les fichiers contenant com ou criminal en .data
                # criminal fait partie du chemin vers les fichiers déchiffrés
                # com est la racine de notre JAR
                if b"criminal" in content or b"com" in content :
                    shutil.copyfile(os.path.join(root,file_), os.path.join(root,file_)+".data")

decrypt_files()
get_interesting_files()