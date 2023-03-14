# Photo Organiser

This project aimed to be a personal tool for picture self-organization in order to avoid duplicate images.

Currently it detects duplicate images (both images are the same) and generate a file with the duplications in order to be able to clean them.

If a image if the same of another one but with other size, other colors and other possible variations, the program doesn't *still* detect they are duplicated.

## How to install

Before installing the package, it's highly recommended to generate a custom environment using `virtualenv` or `conda`. This new environment allows to isolate the dependencies for this project.

Execute the following command to install a dependency before launch the installation of the package:

```
pip install pyinstaller_setuptools
```

Now, you can install the module using `setuptools` using the following commands:

```
python setup.py build

pip install -r requirements.txt

pip install .
```

It's also possible to generate an executable for your OS using the following command:

```
python setup.py pyinstaller
```

# How to use

After install the package, it can be used through the command line by providing several parameters:

* `--input_path` must be an existing directory where images are stored. Only PNG, JPG and JPEG formats are supported right now. If another file extension is found in the directory, it's skipped and a messega will appear in the console.
* `--output_path` must be an existing directory where the output document file will be generated.