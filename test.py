import cv2



def get_frames_from_videos(filename,lot_num):
    vidcap = cv2.VideoCapture(filename)
    success, image = vidcap.read()
    count = 0
    print(image)
    while vidcap. isOpened():
        success,image = vidcap.read()
        if(count > 9800):
            break
        cv2.imwrite("/Users/dwijvijaykumarpatel/tensorflow-test/env/parking_space_detection/extracted_images/{}/{}.png".format(lot_num,count),image) 
        count+=1
        



#get_frames_from_videos("/Users/dwijvijaykumarpatel/tensorflow-test/env/parking_space_detection/parking_lot_videos/BLK-HDPTZ12 Security Camera Parkng Lot Surveillance Video.mp4","lot_1")
#get_frames_from_videos("/Users/dwijvijaykumarpatel/tensorflow-test/env/parking_space_detection/parking_lot_videos/DOTS Parking Cameras Live Stream-2.mp4","lot_2")
get_frames_from_videos("/Users/dwijvijaykumarpatel/tensorflow-test/env/parking_space_detection/parking_lot_videos/DOTS Parking Cameras Live Stream-3.mp4","lot_3")