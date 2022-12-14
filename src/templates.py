'''
    This file contains the templates for the images.
    The templates are used to create the image buffer's.
'''
templates = {
    # w -> width,   h -> height,   m -> margin
    'square': lambda w, h, m: [[m, m, (int)(w-m*2), (int)(h-m*2)]],  #  1 image: 1 full
    # ? 2 IMAGES ------------------------------------------------------------------------------------------------------------------------------------------
    'vertical': lambda w, h, m: [[m, m, (int)(w/2-m*1.5), (int)(h-m*2)], [(int)((w/2)+m/2), m, (int)(w/2-m*1.5), (int)(h-m*2)]],  # 2 images: 1 top 1 bottom
    'horizontal':  lambda w, h, m: [[m, m, (int)(w-m*2), (int)(h/2-m*1.5)], [m, (int)((h/2)+m/2), (int)(w-m*2), (int)(h/2-m*1.5)]],  # 3 images: 1 top 1 right 1 bottom
    # now set it in horizontal
    # ? 3 IMAGES ------------------------------------------------------------------------------------------------------------------------------------------
    # 3 images: 3 vertical
    '3v': lambda w, h, m: [[m, m, (int)((w/3)-m*1.5), (int)(h-m*2)], [(int)((w/3)+m/2), m, (int)((w/3)-m*1.5), (int)(h-m*2)], [(int)((w/3)*2+m/2), m, (int)((w/3)-m*1.5), (int)(h-m*2)]],  # 3 images: 3 vertical
    '3h': lambda w, h, m: [[m, m, (int)(w-m*2), (int)((h/3)-m*1.5)], [m, (int)((h/3)+m/2), (int)(w-m*2), (int)((h/3)-m)], [m, (int)((h/3)*2+m/2), (int)(w-m*2), (int)((h/3)-m*1.5)]],  # 3 images: 3 horizontal
    # ? T LAYOUT ------------------------------------------------------------------------------------------------------------------------------------------
    't':  lambda w, h, m: [[m, m, (int)(w-m*2), (int)(h/2-m*1.5)], [m, (int)((h/2)+m/2), (int)(w/2-m*1.5), (int)(h/2-m*1.5)], [(int)((w/2)+m/2), (int)((h/2)+m/2), (int)(w/2-m*1.5), (int)(h/2-m*1.5)]],  # 3 images: 1 top 1 left 1 right
    't_inv': lambda w, h, m: [[m, m, (int)(w/2-m*1.5), (int)(h/2-m*1.5)], [(int)((w/2)+m/2), m, (int)(w/2-m*1.5), (int)(h/2-m*1.5)], [m, (int)((h/2)+m/2), (int)(w-m*2), (int)(h/2-m*1.5)]],  # 3 images: 1 top 1 right 1 bottom
    'tl': lambda w, h, m: [[m, m, (int)(w/2-m*1.5), (int)(h/2-m*1.5)], [m, (int)((h/2)+m/2), (int)(w/2-m*1.5), (int)(h/2-m*1.5)], [(int)((w/2)+m/2), m, (int)(w/2-m*1.5), (int)(h-m*2)]],  # 3 images: 1 top left 1 bottom left 1 right
    'tr': lambda w, h, m: [[m, m, (int)(w/2-m*1.5), (int)(h-m*2)], [(int)((w/2)+m/2), m, (int)(w/2-m*1.5), (int)(h/2-m*1.5)], [(int)((w/2)+m/2), (int)((h/2)+m/2), (int)(w/2-m*1.5), (int)(h/2-m*1.5)]],  # 3 images: 1 top right 1 bottom right 1 left
    # # ? 4 IMAGES ------------------------------------------------------------------------------------------------------------------------------------------
    'cross': lambda w, h, m: [[m, m, (int)((w/2)-m*1.5), (int)((h/2)-m*1.5)], [(int)((w/2)+m/2), m, (int)((w/2)-m*1.5), (int)((h/2)-m*1.5)], [m, (int)((h/2)+m/2), (int)((w/2)-m*1.5), (int)((h/2)-m*1.5)], [(int)((w/2)+m/2), (int)((h/2)+m/2), (int)((w/2)-m*1.5), (int)((h/2)-m*1.5)]],  # 4 images: 2 top 2 bottom
    'trident': lambda w, h, m: [[m, m, (int)((w/3)-m*1.5), (int)((h/2)-m*1.5)], [(int)((w/3)+m/2), m, (int)((w/3)-m*1.5), (int)((h/2)-m*1.5)], [(int)((w/3)*2+m/2), m, (int)((w/3)-m*1.5), (int)((h/2)-m*1.5)], [m, (int)((h/2)+m/2), (int)(w-m*2), (int)((h/2)-m*1.5)]],  # 4 images: 1 top 3 bottom
    'inversed_trident': lambda w, h, m: [[m, m, (int)(w-m*2), (int)((h/2)-m*1.5)], [m, (int)((h/2)+m/2), (int)((w/3)-m*1.5), (int)((h/2)-m*1.5)], [(int)((w/3)+m/2), (int)((h/2)+m/2), (int)((w/3)-m*1.5), (int)((h/2)-m*1.5)], [(int)((w/3)*2+m/2), (int)((h/2)+m/2), (int)((w/3)-m*1.5), (int)((h/2)-m*1.5)]],  # 4 images: 1 bottom 3 top
    'lateral_trident': lambda w, h, m: [[m, m, (int)((w/2)-m*1.5), (int)(h-m*2)], [(int)((w/2)+m/2), m, (int)((w/2)-m*1.5), (int)((h/3)-m*1.5)], [(int)((w/2)+m/2), (int)((h/3)+m/2), (int)((w/2)-m*1.5), (int)((h/3)-m*1.5)], [(int)((w/2)+m/2), (int)((h/3)*2+m/2), (int)((w/2)-m*1.5), (int)((h/3)-m*1.5)]],  # 4 images: 1 left 3 right
    'inversed_lateral_trident': lambda w, h, m: [[(int)((w/2)+m/2), m, (int)((w/2)-m*1.5), (int)(h-m*2)], [m, m, (int)((w/2)-m*1.5), (int)((h/3)-m*1.5)], [m, (int)((h/3)+m/2), (int)((w/2)-m*1.5), (int)((h/3)-m*1.5)], [m, (int)((h/3)*2+m/2), (int)((w/2)-m*1.5), (int)((h/3)-m*1.5)]],  # 4 images: 1 right 3 left
}

