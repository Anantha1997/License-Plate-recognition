
import cv2
import imutils
import pytesseract
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Read the image file
image = cv2.imread("C:\\Users\\per\\PycharmProjects\\pycharmtest\\car images\\img2.png")

# Resize the image - change width to 500
image = imutils.resize(image, width=500)

# Display the original image
cv2.imshow("Original Image", image)
cv2.waitKey(0)

# RGB to gray scale conversion
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("1 - Grayscale Conversion", gray)
cv2.waitKey(0)

# Noise removal with iterative bilateral filter(Remove noise while preserving edges)
gray = cv2.bilateralFilter(gray, 11, 17, 17)
cv2.imshow("2 - Bilateral Filter", gray)
cv2.waitKey(0)

# Find edges of the grayscale image
edged = cv2.Canny(gray, 170, 200)
cv2.imshow("3 - Canny Edges", edged)
cv2.waitKey(0)

# Find contours based on Edges
cnts, new = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# Create copy of original image to draw all contours
img1 = image.copy()
cv2.drawContours(img1, cnts, -1, (0,255,0), 3)
cv2.imshow("4- All Contours", img1)
cv2.waitKey(0)

# Sort contours based on their area keeping minimum required area as '30' (Anything smaller than this will not be considered)
cnts=sorted(cnts, key = cv2.contourArea, reverse = True)[:30]
NumberPlateCnt = None

# Top 30 contours
img2 = image.copy()
cv2.drawContours(img2, cnts, -1, (0,255,0), 3)
cv2.imshow("5- Top 30 Contours", img2)
cv2.waitKey(0)

# loop over our contours to find the best possible approximate contour of number plate
count = 0
idx =7
for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        # print ("approx = ",approx)
        if len(approx) == 4:   # select the contour with 4 corners
            NumberPlateCnt = approx  # This is our approx number plate contour

            # Crop those contours and store it in car images folder
            x, y, w, h = cv2.boundingRect(c) #This will find out co-ord for plate
            new_img = image[y:y + h, x:x + w] # create new image
            cv2.imwrite('Cropped Image-Text/' + str(idx) + '.png', new_img)
            idx+=1

            break

# Drawing the selected contour on the original image
#print(NumberPlateCnt)
cv2.drawContours(image, [NumberPlateCnt], -1, (0,255,0), 3)
cv2.imshow("Final Image with Number Plate Detected", image)
cv2.waitKey(0)

Cropped_img_loc = 'car images/img3.png'
cv2.imshow("Cropped Image ", cv2.imread(Cropped_img_loc))

# use tesseract to convert image into string
text = pytesseract.image_to_string(Cropped_img_loc, lang='eng')
print("Number is :", text)

cv2.waitKey(0) #Wait for user input before closing the image displayed