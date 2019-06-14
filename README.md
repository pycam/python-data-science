# Data science in Python - course materials

[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/pycam/Lobby?utm_source=share-link&utm_medium=link&utm_campaign=share-link)

New course based on 'Working with Python: functions and modules' course

Materials for the course run by the Graduate School of Life Sciences, University of Cambridge.

- Course website: http://pycam.github.io/
- Booking website: http://www.training.cam.ac.uk/

If you wish to run the course on your personal computer, here are the steps to follow to get up and running.

## Clone this github project

```bash
git clone https://github.com/pycam/python-data-science.git
cd python-data-science
```

## Dependencies

Install Python 3 by downloading the latest version from https://www.python.org/. For Mac OSX, just run `brew install python3`.

Python 2.x is legacy, Python 3.x is the present and future of the language.

Create first a virtual environment using the [`venv` library](https://docs.python.org/3/library/venv.html). Update pip if needed, install [jupyter](http://jupyter.org/) and [RISE](https://github.com/damianavila/RISE) to get a slideshow extension into jupyter.

***Note*** A virtual environment is a Python environment such that the Python interpreter, libraries and scripts installed into it are isolated from those installed in other virtual environments.

```bash
python3 -m venv venv
# activate your virtual environment
source venv/bin/activate
# update pip if needed
pip install --upgrade pip
# install package dependencies
pip install jupyter pandas matplotlib seaborn biopython

# slideshow extension
pip install rise
jupyter-nbextension install rise --py --sys-prefix
jupyter nbextension enable rise --py --sys-prefix

```

On mac OSX you may need to run this command to accept the XCode license, before installing biopython:

```bash
sudo xcodebuild -license
```

## Usage

Go to the directory where you've cloned this repository, activate your virtual environment and run jupyter.

Your web browser should automatically open with this url http://localhost:8888/tree where you see the directory tree of the course with all the jupyter notebooks.

```bash
cd python-data-science
source venv/bin/activate
jupyter notebook
```

To shutdown jupyter, type ctrl-C into the terminal you've ran `jupyter notebook`, answer `y` and press `enter`.

You may wish to deactivate the virtual environment, by entering into the terminal:
```
deactivate
```

## Resources used

- [Data Carpentry lesson](https://datacarpentry.org/python-ecology-lesson/)
- [Software Carpentry lesson](http://swcarpentry.github.io/python-novice-gapminder/)
- [Biopython tutorial on sickle cell](https://krother.gitbooks.io/biopython-tutorial/content/sicklecell.html)
- [Python tutorial](https://docs.python.org/3/tutorial/index.html)
- [Pandas tutorials](http://pandas.pydata.org/pandas-docs/stable/tutorials.html)
- [Matplotlib tutorials](https://matplotlib.org/tutorials/index.html)
- [Biopython tutorial](http://biopython.org/DIST/docs/tutorial/Tutorial.html)

## Contributing

- See [contributing.md](contributing.md)
