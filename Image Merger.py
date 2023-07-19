import sys
from PIL import Image

print("Entre image paths \n exapmle: /storage/emulated/0/Download/20230704.jpg \n (when you done type letter V (for vertical)  or  H (for horizontal): ")

methode = ["h", "H", "v", "V"]
imglist = []
img = input("Entre image path: ")
imglist.append(img)
while img not in methode:
    print(img not in methode)
    img = input("Entre image path: ")
    imglist.append(img)

images = [Image.open(x) for x in imglist[:-1]]
widths, heights = zip(*(i.size for i in images))

name = input("New image name (example: FinalImg): ")

def get_concat_h_cut_center(images, widths, heights):
    total_width = sum(widths)
    max_height = max(heights)
    dst = Image.new('RGB', (total_width, max_height))  
    x_offset = 0
    for im in images:
        dst.paste(im, (x_offset,0))
        x_offset += im.size[0]
    dst = dst.resize((int(dst.size[0]), int(dst.size[1])))
    return dst



  
  
  
def get_concat_v_cut_center(images, widths, heights):
    max_width = max(widths)
    total_height = sum(heights)
    dst = Image.new('RGB', (max_width, total_height)) 
    y_offset = 0
    for im in images:
        dst.paste(im, (0, y_offset))
        y_offset += im.size[1]
    dst = dst.resize((int(dst.size[0]), int(dst.size[1])))
    return dst
    

if (img == "v" or img == "V"):
    get_concat_v_cut_center(images, widths, heights).save('/storage/emulated/0/Download/' + name + '.jpg')
    
elif (img == "h" or img == "H"):
    get_concat_h_cut_center(images, widths, heights).save('/storage/emulated/0/Download/' + name + '.jpg')