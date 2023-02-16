import os

class FileService:

    def __init(self) -> None:
        pass

    def get_list_filenames(self, directory:str) -> list:
        result_list = list()
        for name in os.listdir(directory):
            abs_name = os.path.join(directory, name)
            # If it is a directory, call method recursevely to process all images            
            # Else, if it is an image, check the extensions
            if os.path.isdir(abs_name):
                result_list.extend(self.get_list_filenames(abs_name))
            else:
                # Check the extensions
                if os.path.splitext(name)[1] in ('.jpeg', '.png', '.jpg'):
                    result_list.append(abs_name)
                else:
                    # TODO add logger to proper error handlin
                    print('File not processed')
        return result_list
