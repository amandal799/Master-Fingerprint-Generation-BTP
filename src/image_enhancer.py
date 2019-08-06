import numpy as np
from matplotlib import pyplot as plt

class ImageEnhancer(object):

    def __init__(self, image, block_size, variance_thresh):
        self.original_image = image
        self.image = image
        self.block_size = int(block_size)
        self.variance_thresh = variance_thresh
        self.enhance()

    def enhance(self):
        self.segment()
        '''
        self.normalize()
        self.create_orientation_image()
        self.create_frequency_image()
        self.create_region_mask()
        self.apply_gabor_filter()
        self.create_binary_image()
        self.create_thinned_image()
        '''

    def segment(self):
        self.plot(self.original_image, 'original image')
        rows, cols = self.image.shape
        self.image = self.normalize(d_mean = 0, d_std = 1)
        self.plot(self.image, 'normalize image')

        new_rows = np.int(self.block_size * \
                np.ceil((np.float(rows))/(np.float(self.block_size))))

        new_cols = np.int(self.block_size * \
                np.ceil((np.float(cols))/(np.float(self.block_size))))

        padded_image = np.zeros((new_rows, new_cols))
        std_dev_image = np.zeros((new_rows, new_cols))

        padded_image[0:rows, 0:cols] = self.image

        for i in range(0, new_rows, self.block_size):
            for j in range(0, new_cols, self.block_size):
                block = padded_image[i:i+self.block_size, j:j+self.block_size]
                std_dev_image[i:i+self.block_size, j:j+self.block_size] = np.std(block)


        std_dev_image = std_dev_image[0:rows, 0:cols]

        mask = std_dev_image > self.variance_thresh
        print(mask)
        print("Image : \n ", self.image)
        print("Masked Image : \n", self.image[mask])
        #self.plot(self.image[mask], 'segmented image')
        '''
        mean_val = np.mean(self.image[mask])

        std_val = np.std(self.image[mask])
        '''
    def normalize(self, d_mean, d_std):
        return (self.image - np.mean(self.image)) / np.std(self.image)
        mean = np.mean(self.image)
        std = np.std(self.image)

        temp = np.where( self.image > mean, 1, -1) * \
                ( (self.image - mean) * np.sqrt( d_std/std ) )

        return d_mean + temp

    def create_orientation_image(self):
        pass

    def create_frequency_image(self):
        pass

    def create_region_mask(self):
        pass

    def apply_gabor_filter(self):
        pass

    def create_binary_image(self):
        pass

    def create_thinned_image(self):
        pass

    def plot(self, img, label='Image'):
        plt.imshow(img, cmap='gray')
        plt.title(label)
        plt.show()
