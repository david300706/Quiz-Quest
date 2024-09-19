
def draw_scroll(scroll, display_surface, coordinates):
    """
    draw a scroll on the display_surface
    :param scroll: the image of scroll
    :param display_surface: the display_surface to draw on
    :param coordinates: x and y coordinates NOT index , if wou want to use index use the function convert_index_to_cords(index_x, index_y)
    """
    display_surface.blit(scroll, coordinates)
