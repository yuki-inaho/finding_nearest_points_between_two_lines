import colorsys


def label2color(label: int, color_shift_coefficient=50, color_start_coeff=30):
    if label < 0:
        return (60, 60, 60)  # Gray
    else:
        # Convert the label to a unique hue in the HSV color space
        hue = ((label + color_start_coeff) * color_shift_coefficient % 360.0) / 360.0
        # hue = float(label) / 10
        saturation = 1.0  # High saturation for bright colors
        value = 0.9  # Not too bright or too dark
        r, g, b = colorsys.hsv_to_rgb(hue, saturation, value)

        # Convert from range 0.0-1.0 to 0-255
        return [r, g, b]
