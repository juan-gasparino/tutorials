import random
import pickle
import cv2 as cv
import numpy as np
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


def loadFile(fileName: str):
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


def encryptImage(imgBytes: bytes, keyFilePath:str ,encryptationLevel = 256):
    try:

        key = getKeyFromFile(keyFilePath,encryptationLevel)
        iv = get_random_bytes(16)
        
        #Create cipher object
        cipher = AES.new(key, AES.MODE_CBC, iv)

        padded_imgBytes = pad(imgBytes, 16)
        cypher_imgBytes = cipher.encrypt(padded_imgBytes)

        return iv + cypher_imgBytes

    except Exception as e:
        print(f"#Error#function encryptImage: {e}")


def decryptImage(dataBytes: bytes, keyFilePath:str ,encryptationLevel = 256):
    try:

        #parse CypherFrame
        packed_iv = dataBytes[0:16]
        packed_cypher_imgBytes = dataBytes[16:]
        
        #Create cipher object
        key = getKeyFromFile(keyFilePath,encryptationLevel)
        cipher = AES.new(key, AES.MODE_CBC, packed_iv)
        
        #Decrypt image
        padded_imgBytes = cipher.decrypt(packed_cypher_imgBytes)

        return unpad(padded_imgBytes, 16)

    except Exception as e:
        print(f"#Error#function decodeStream: {e}")


def encrypted(filePath:str, keyPath:str):
    try:
        img = cv.imread(filePath)
        _, imgEncode = cv.imencode('.jpg', img)
        imgBytes = pickle.dumps(imgEncode)
        dataEncrypt = encryptImage(imgBytes, keyPath)
        return dataEncrypt
    except Exception as e:
        print(f"#Error#function imageEncrypted: {e}")


def decrypted(dataEncrypt:bytes, keyPath:str, newFilePath:str):
    try:
        imgBytes = decryptImage(dataEncrypt, keyPath)
        imgEncode = pickle.loads(imgBytes)
        img = cv.imdecode(imgEncode, cv.IMREAD_COLOR)
        cv.imwrite(newFilePath,img)
    except Exception as e:
        print(f"#Error#function imageDecrypted: {e}")


#Script
dataEncrypt = encrypted('./messi.jpg', './Alice.csv')
decrypted(dataEncrypt,'./Bob.csv','./messi2.jpg')