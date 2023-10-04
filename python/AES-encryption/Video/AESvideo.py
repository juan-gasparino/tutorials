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


def videoEncryptedDecrypted_TEST():
    try:

        cam = cv.VideoCapture(0)
        cam.set(3, 320)
        cam.set(4, 240)

        while cam.isOpened():
            ret, frame = cam.read()
            if not ret:
                print("Can't retrive frame")
                break
            elif cv.waitKey(25) & 0xFF == ord('q'):
                break
            else:
                #Tx
                _, frame = cv.imencode('.jpg', frame)
                frame1 = pickle.dumps(frame)
                frameEncrypt = encryptImage(frame1,'./Alice.csv')
                
                #Rx
                frameDecrypt = decryptImage(frameEncrypt,'./Bob.csv')
                frame2 = pickle.loads(frameDecrypt)
                frame2 = cv.imdecode(frame2, cv.IMREAD_COLOR)
                
                cv.imshow("Server", frame2)

        cam.release()
        cv.destroyAllWindows()

    except Exception as e:
        print(f"#Error#function start_Video_TEST: {e}")


videoEncryptedDecrypted_TEST()