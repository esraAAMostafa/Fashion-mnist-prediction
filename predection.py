from keras.engine.saving import load_model
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array


def load_image(filename):
    # load the image
    img = load_img(filename, color_mode="grayscale", target_size=(28, 28))
    # convert to array
    img = img_to_array(img)
    # reshape into a single sample with 1 channel
    img = img.reshape(1, 28, 28, 1)
    # prepare pixel data
    img = img.astype('float32')
    img = img / 255.0
    return img


# load an image and predict the class
def run_example(data):
    # load the image
    img = load_image(data)
    # load model
    model = load_model('final_model.h5')
    # predict the class
    result = model.predict_classes(img)
    return result[0]


