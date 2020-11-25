import cv2
import dropbox
import time
import random
start_time=time.time()
def takesnapshot():
    number=random.randint(0,100)
    capture=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=capture.read()
        img_name='img'+str(number)+'.jpg'
        cv2.imwrite(img_name,frame)
        start_time=time.time()
        result=False

    return img_name
    capture.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token='sl.AmNnM76kSvt_qbtTRplgeBGEunK0gt21mmWzH7tVQDU9vhTw7Ty3WkyM8eM0yoenxPFqHUVtu8Ld6SHZId_C49QXuq71h7SdRI0Dtrnf1WaQVdbOI6j9oqwHB2nIT0a_aeTNmcp-krg'
    file=img_counter
    file_from=file
    file_to='/test_dropbox/'+(img_name)
    dbx=dropbox.Dropbox(access_token)
    with open(file_from,'rb')as f:
        dbx.file_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
def main():
    while(True):
        if((time.time()-start_time)>=300):
            name=takesnapshot()
            upload_file(name)

main()