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
        not_valid_imags = dict()
        global_not_valid = list()
        for i, img_file in enumerate(list_of_images):
            if img_file in global_not_valid:
                # TODO Save to other folder and continue with next image
                continue
            # This is a valid image to check
            not_valid_imags[img_file] = list()
            new_img = Image.open(img_file).convert('RGB')
            valid_imgs.append(img_file)
            # TODO Save to common folder
            # Loop over the rest of images
            for elem in range(i + 1,len(list_of_images)):
                to_comp_img = Image.open(list_of_images[elem]).convert('RGB')
                diff = np.sum(np.array(ImageChops.difference(new_img, to_comp_img).getdata()))
                # If images are equal, append to not_valid list
                if diff == 0:
                    not_valid_imags[img_file].append(list_of_images[elem])
                    global_not_valid.append(list_of_images[elem])
        # Save files with duplicated images
        self.fs.save_dictionary(self._od, not_valid_imags)
        