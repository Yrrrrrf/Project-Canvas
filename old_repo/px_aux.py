
region_pixels = set()  # Store the coordinates of ALL the pixels that belong to the region
# region_pixels.add((x_pixel, y_pixel))
# print(region_pixels)
# print(type(region_pixels))

# If this method is excecuted means that the curren pixel is also in the region
def get_region(x, y):
    # roi_mask[x, y] = img[x, y]
    global region_pixels
    region_pixels.add((x, y))  # Add current pixel to the region

    # global temp_coord_list  # This variable will store all the coordinates that still needs to be ckecked
    temp_coord_list = set()
    temp_coord_list.update(region_pixels)
    global itered_coord
    itered_coord = set()
    while len(temp_coord_list) > 0:
        current_px = temp_coord_list.pop()
        print(current_px)
        if current_px not in itered_coord:
            itered_coord.add(current_px)
            print(current_px)
            temp_coord_list.update(get_neighbours(current_px[0], current_px[1]))
    region_pixels.update(itered_coord)
        # print(get_neighbours(current_px[0], current_px[1]))
        # region_pixels = set.union(region_pixels, get_neighbours(x, y))  # Get the neighbours of the current pixel


def get_neighbours(x, y):
    similar_nb = set()
    for i in range(-1, 2):  # [-1, 0, 1]
        for j in range(-1, 2):  # [-1:1]
            # if 0 <= x + i < roi_mask.shape[1] and 0 <= y + j < roi_mask.shape[0]:
            # Check if the neighbour is inside the image
                # if (x+i, y+j) not in itered_coord:
                    similar_nb.add((x+i, y+j))
    # print(type(similar_nb))
    print(similar_nb)
    return similar_nb
                # Check if the neighbour is not the pixel itself
            # shape -> [height, width]
                    # roi_mask[x + i][y + j] = img[x + i][y + j]
                # if (i != 0 or j != 0): # and px_is_similar(img[x, y], img[x + i][y + j]):
