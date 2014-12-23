from numpy import uint8
from matplotlib.pyplot import imread


def load_image_uint8(file_name):
    img_float = imread(file_name)
    img = (img_float * 256).astype(uint8)
    return img


if __name__ == "__main__":
    file_name = "char1.png"
    img = load_image_uint8(file_name)
    print(img)
    import matplotlib.pyplot as plt
    plt.imshow(img, interpolation="none")
    plt.show()