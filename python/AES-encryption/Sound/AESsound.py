import random
import pickle
import numpy as np
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def loadFile(fileName: str = ''):
    try:
        with open(fileName, "rb") as f:
            arrayValues = np.array(f.read().splitlines(), dtype='float32')
            f.close()
        return arrayValues
    except Exception as e:
        print(f"#Error#function loadFile: {e}")


def getKeyFromFile(filePath:str, encryptationLevel:int = 256):
    try:
        binaryKeys = np.array(loadFile(filePath), dtype='uint32')
        keyBin = binaryKeys[0:encryptationLevel]
        keyInt = np.packbits(keyBin, axis=-1)
        key = keyInt.tobytes()
        return key
    except Exception as e:
        print(f"#Error#function getKeyFromFile: {e}")


def encryptSound(soundBytes: bytes = b'',keyFilePath:str = '' ,encryptationLevel = 256):
    try:

        print("")

    except Exception as e:
        print(f"#Error#function encryptSound: {e}")


def decryptSound(soundBytes: bytes = b'',keyFilePath:str = '' ,encryptationLevel = 256):
    try:

        print("")

    except Exception as e:
        print(f"#Error#function decryptSound: {e}")


def soundEncryptDecrypt_TEST():
    try:

        print("")

    except Exception as e:
        print(f"#Error#function soundEncryptDecrypt_TEST: {e}")


soundEncryptDecrypt_TEST()