# import matplotlib
import cv2
import numpy as np
import colorsys

img = cv2.imread('resources/img/guardians450.jpg')
# img = cv2.imread('resources/img/eye64.png')
# cv2.imshow('original', img)
# Interest pixel (just for testing)

x_pixel = 127
y_pixel = 127

def set_pixel(x = 127, y = 127):    
    global x_pixel
    x_pixel = x
    global y_pixel
    y_pixel = y

# return list with each rgb value as an integer [r, g, b]
def get_pixel_rgb_values(x, y):
    px = img[x, y]
    return [px[0], px[1], px[2]]


# Function only for testing purposes
def create_px_img(x=int, y=int, width=int, height=int):
    matrix = []
    for i in range(width):
        matrix.append([get_pixel_rgb_values(x, y) for j in range(height)])
    return np.array(matrix)


# TODO: Research about closures
def print_img(format):
    counter = 0

    def print_rgb(rgb, width=32, height=32):
        nonlocal counter
        counter += 1
        matrix = []
        for i in range(width):
            matrix.append([np.array(rgb, dtype=np.uint8) for j in range(height)])
        cv2.imshow(f'pixel {counter}', np.array(matrix))

    def print_hsv(hsv, width=32, height=32):
        nonlocal counter
        counter += 1
        hsv_out = [0, 0, 0]
        hsv_out[0] = (hsv[0] % 360) / 360  # h: 0 < 360 [degrees]
        hsv_out[1] = (hsv[1] % 100) / 100  # s: 0 < 100 [%]
        hsv_out[2] = ((hsv[2] % 100) * 255) / 100  # b: 0 < 100 [%]
        print_rgb(colorsys.hsv_to_rgb(hsv_out[0], hsv_out[1], hsv_out[2]), width, height)

    if format == 'rgb':
        return print_rgb
    elif format == 'hsv':
        return print_hsv


rgb_print = print_img('rgb')
hsv_print = print_img('hsv')


def rgb_matrix(rgb, width=img.shape[0], height=img.shape[1]):
    matrix = []
    for i in range(width):
        matrix.append([np.array(rgb, dtype=np.uint8) for j in range(height)])
    return np.array(matrix)


roi_mask = rgb_matrix([0, 0, 0])


# STEPS:
# 0. Global list of pixel coordinates
# 1. Evaluate similarity %
# 2. Get similar neighbors list
# 3. Recurse over similar neighbors with the reference pixel's value

# # Check similarity between two pixels
# Get 8N neighbours of the pixel
# Iterate over the neighbours

# print([round(re_px[0]), round(re_px[1]), round(re_px[2])])
hsv_img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2HSV)  # Convert the image to a numpy array [B G R]
#print(hsv_img)
# cv2.imshow('hsv_img', hsv_img)


def hsv_std(hsv):
    hsv_standard = [0, 0, 0]
    hsv_standard[0] = round((hsv[0] / 255) * 360)
    hsv_standard[1] = round((hsv[1] / 255) * 100)
    hsv_standard[2] = round((hsv[2] / 255) * 100)
    return hsv_standard


def hsv_cv2(hsv):
    # print(hsv)
    hsv_cv2_standard = [0, 0, 0]
    hsv_cv2_standard[0] = round((hsv[0] / 360) * 100)
    hsv_cv2_standard[1] = round(hsv[1])
    hsv_cv2_standard[2] = round((hsv[2] * 255) / 100)
    return hsv_cv2_standard


def set_resem_range(x, y, resemblance):
    hsv = hsv_std(hsv_img[x, y])
    print(hsv)
    # Add a range of resemblance
    h_range = (hsv[0] - round(360*(1-resemblance)), hsv[0] + round(360*(1-resemblance)))
    s_range = (hsv[1] - round(100*(1-resemblance)), hsv[1] + round(100*(1-resemblance)))
    v_range = (hsv[2] - round(100*(1-resemblance)), hsv[2] + round(100*(1-resemblance)))
    hsv_ranges = [h_range, s_range, v_range]
    print(hsv_ranges)
    return hsv_ranges


resem_ranges = set_resem_range(x_pixel, y_pixel, 0.85)


# TODO: Optimize & 
def is_similar_at_coor(x, y):
    hsv = hsv_std(hsv_img[x, y])
    print(hsv)
    if resem_ranges[0][0] < hsv[0] < resem_ranges[0][1] \
    and resem_ranges[1][0] < hsv[1] < resem_ranges[1][1] \
    and resem_ranges[2][0] < hsv[2] < resem_ranges[2][1]:
        return True


def get_neighbours(x, y):
    neighbours = []
    for i in range(-1, 2):  # [-1, 0, 1]
        for j in range(-1, 2):  # [-1:1]
            # shape -> [width, height]
            if 0 <= x + i < roi_mask.shape[1] and 0 <= y + j < roi_mask.shape[0]:
            # Check if the neighbour is inside the image
                if is_similar_at_coor(x+i, y+j):
                    neighbours.append([(x+i, y+j), 0, 1])
                else:
                    neighbours.append([(x+i, y+j), 0, 0])
    return neighbours
    

print(get_neighbours(x_pixel, y_pixel))


glob_pixels = []


def get_region(x, y):
    unitered_idx = 0
    glob_pixels.append([(x, y), 1, 1])
    unitered_idx += 1
    # (x, y), isItered, isInRegion
    glob_pixels.append(get_neighbours(x, y))
    

def recursive_similar_px(x, y):
    for i in range(x-1, x+1):
        
        for i in range(y-1, y+1):
            continue
#     # global temp_coord_list  # This variable will store all the coordinates that still needs to be ckecked
#     temp_coord_list = set()
#     temp_coord_list.update(region_pixels)
#     global itered_coord
#     itered_coord = set()
#         current_px = temp_coord_list.pop()
#         print(current_px)
#         if current_px not in itered_coord:

# region_pixels = set()  # Store the coordinates of ALL the pixels that belong to the region
# region_pixels.add((x_pixel, y_pixel))
# # print(region_pixels)
# # print(type(region_pixels))

#             itered_coord.add(current_px)
#             print(current_px)
#             temp_coord_list.update(get_neighbours(current_px[0], current_px[1]))
#     region_pixels.update(itered_coord)
        # print(get_neighbours(current_px[0], current_px[1]))
        # region_pixels = set.union(region_pixels, get_neighbours(x, y))  # Get the neighbours of the current pixel


for i in glob_pixels:
    roi_mask[i[0], i[1]] = img[i[0], i[1]]


# cv2.imshow('mask', roi_mask)

cv2.waitKey(0)
cv2.destroyAllWindows()
