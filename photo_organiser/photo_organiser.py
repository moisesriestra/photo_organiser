from photo_organiser.services.file_service import FileService
from PIL import Image, ImageChops
import numpy as np

class PhotoOrganiser:

    def __init__(self, input_directory:str, output_directory: str) -> None:
        self._id = input_directory
        self._od = output_directory
        self.fs = FileService()

    def process(self) -> None:

        # Get the list pf paths to process
        list_of_images = self.fs.get_list_filenames(self._id)

        # Process the list of images
        valid_imgs = list()
        not_valid_imags = list()
        for i, img_file in enumerate(list_of_images):
            print(valid_imgs)
            print(not_valid_imags)
            if img_file in not_valid_imags:
                # Move to other folder and continue with next image
                continue
            new_img = Image.open(img_file).convert('RGB')
            valid_imgs.append(img_file)
            for elem in range(i + 1,len(list_of_images)):
                to_comp_img = Image.open(list_of_images[elem]).convert('RGB')
                diff = np.sum(np.array(ImageChops.difference(new_img, to_comp_img).getdata()))

                if diff == 0:
                    print('Images are equal')
                    not_valid_imags.append(list_of_images[elem])