from photo_organiser.services.file_service import FileService

class PhotoOrganiser:

    def __init__(self, input_directory:str, output_directory: str) -> None:
        self._id = input_directory
        self._od = output_directory
        self.fs = FileService()

    def process(self) -> None:

        # Get the list pf paths to process
        list_of_images = self.fs.get_list_filenames(self._id)
        print(list_of_images)