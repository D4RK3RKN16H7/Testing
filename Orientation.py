import cv2
import math

pts = list()
dst = list()
ang = list()


def dist(a, b):
    d = 0
    if len(a) == len(b):
        for i in range(len(a)):
            d = d + (b[i] - a[i])**2
        d = math.sqrt(d)
    return d


def angle(a):
    x, y = a[0], a[1]
    if x in range(201) and y in range(201):
        slope = float((200 - y) / float(200 - x))
        return math.atan(slope) * 180.0 / math.pi + 90
    elif x in range(201, 401) and y in range(201):
        slope = float((200 - y) / float(x - 200))
        return math.atan(slope) * 180.0 / math.pi
    elif x in range(201) and y in range(201, 401):
        slope = float((y - 200) / float(200 - x))
        return math.atan(slope) * 180.0 / math.pi + 180
    elif x in range(201, 401) and y in range(201, 401):
        slope = float((y - 200) / float(x - 200))
        return math.atan(slope) * 180.0 / math.pi + 270



def find_pts(img, cam_pt):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 127, 255, 0)
    im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    c = max(contours, key=cv2.contourArea)
    contours.remove(c)
    #cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

    for c in contours:
        ((_, _), radius) = cv2.minEnclosingCircle(c)
        if radius > 10:
            m = cv2.moments(c)
            center = (int(m["m10"] / m["m00"]), int(m["m01"] / m["m00"]))
            cv2.line(img, center, (cam_pt[0], cam_pt[1]), (255, 255, 0), 2)
            cv2.circle(img, (center[0], center[1]), 5, (0, 0, 255), -1)
            center = (center[0], center[1], 0)
            center = list(center)
            ang.append(angle(center))
            pts.append(center)
            dst.append((dist(center, cam_pt)))

    cv2.circle(img, (cam_pt[0], cam_pt[1]), 5, (255, 0, 0), -1)


def main():
    img = cv2.imread('Image.jpg')
    #cap = cv2.VideoCapture('http://192.168.1.101:8080/videofeed')
    #ret, img = cap.read()
    img = img[0:400, 0:400]
    vertical_dist = 0
    camera_pt = (img.shape[1]/2, img.shape[0]/2, vertical_dist)
    cv2.imshow('original', img)
    find_pts(img, camera_pt)
    print camera_pt
    print pts
    print dst
    print ang
    cv2.imshow('distance', img)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
