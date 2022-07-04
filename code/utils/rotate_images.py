import os
import cv2

# start from top directory
os.chdir('../..')

# create output folders
if not os.path.exists('datasets/kaggle_augmented/training'):
    os.makedirs('datasets/kaggle_augmented/training')
if not os.path.exists('datasets/kaggle_augmented/training/images'):
    os.makedirs('datasets/kaggle_augmented/training/images')
if not os.path.exists('datasets/kaggle_augmented/training/groundtruth'):
    os.makedirs('datasets/kaggle_augmented/training/groundtruth')


# go through all the images
def produceRotated(sourcePath, destPath):
    for img_file in os.listdir(sourcePath):
        # careful: the ground truth images are single-channel!
        img_read = cv2.imread(sourcePath + '/' + img_file, cv2.IMREAD_UNCHANGED)
        # initial unrotated
        # filename ending indicates rotation amount
        cv2.imwrite(destPath + '/' + img_file.replace('.png', '') + '_0.png', img_read)
        for i in range(1, 4):
            img_read = cv2.rotate(img_read, cv2.ROTATE_90_CLOCKWISE)
            cv2.imwrite(destPath + '/' + img_file.replace('.png', '') + '_' + str(i * 90) + '.png', img_read)

produceRotated('datasets/kaggle_data/training/images', 'datasets/kaggle_augmented/training/images')
produceRotated('datasets/kaggle_data/training/groundtruth', 'datasets/kaggle_augmented/training/groundtruth')