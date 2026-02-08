from PIL import Image
filename = "test.jpg" #HERE PUT IN A NAME OF THE FILE
with Image.open(filename) as img:
    img.load()
type(img) 
isinstance(img, Image.Image)

palette = [(32, 1, 93, 255),     #HERE PUT YOUR PALETTE IN FORM OF RGBA, LAST PATAMETER IS ALWAYS 255
           (74, 29, 71, 255), 
           (131, 65, 41, 255), 
           (185, 101, 12, 255), 
           (206, 115, 0, 255), 
           (194, 100, 72, 255), 
           (239, 38, 150, 255), 
           (255, 0, 224, 255)]

resized_img = img.reduce(4) #ITERATIONS OF REDUCTION, BIGGER NUMBER = SMALER IMAGE

img_step1 = resized_img.convert(mode = "P", matrix = None, dither = None, palette = "JPEG", colors = 8)
img_finale = img_step1.convert("L").convert("RGBA")

w, h = img_finale.size

for i in range(w):
    for j in range(h):
        print(int(((i * h + j) / (w * h)) * 100), "%")
        temp = int(img_finale.getpixel((i, j))[0] // 31.875)
        if temp == 8:
            img_finale.putpixel((i, j), (255, 255, 255, 255))
        else:
            img_finale.putpixel((i, j), palette[temp])


print(f"Done!")
img_finale.show()
img_finale.save("output.png") #SHOWS NOT A SAVED IMAGE, IT IS SAVED IN THE FOLDER WITH THE CODE