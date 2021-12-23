# Meme Generator

## Overview
### What the project is
> This projects is all about building a "meme generator" – a multimedia application to dynamically generate memes, including an image with an overlaid quote.

This project is the second and final project of Udacity's Intermediate Python nanodegree program.


### Project Requirements
- The project makes us demonstrate the following:
    - How to interact with a variety of complex filetypes. This emulates the kind of data one noramlly encounters in a data engineering role.
    - How to load quotes from a variety of filetypes (PDF, Word Documents, CSVs, Text files).
    - How to load, manipulate, and save images.
    - How to accept dynamic user input through a command-line tool and a web service. This emulates the kind of work you’ll encounter as a full stack developer.

### Key Learning Highlights
- The key learning highlight of the project are:
    - Object-oriented thinking in Python, including abstract classes, class methods, and static methods.
    - DRY (don’t repeat yourself) principles of class and method design.
    - Working with modules and packages in Python.
    - How to ensure the best coding practices for style and documentation.

## Instructions for setting up the program
- Install all dependencies as given in the `requirements.txt` file using:

```bash
    pip install -r requirements.txt
```

## Roles and Responsibilities of the Submodules
This project has three modules
1. Quote Engine Module
1. Ingestor Module
1. Meme Engine Module

### Quote Engine Module
This module includes QuoteModel, the single model class used in the project. The `QuoteModel` takes two parameters `body` and `author` and modifies `__repr__` method to print the model contents as
```
    "body text" - author
```

### Ingestor Module
The Ingestor Module parses quotes from the following four file formats:
1. `txt`, for which it uses the inbuilt python libraries and methods
1. `csv`, for which the app uses `pandas` library and its `res_csv` method.
1.  `docx`, for which it uses `python-docx` library.
1.  `pdf`. The implementation of reading `pdf` format is the most complicated of all the four file formats. For this the app uses an external library named `pdftotext`, which is written in `C++` and interacts with this library using command line interface (CLI) to convert the contents of `pdf` into `txt` format and then reads that `txt` file using inbuilt methods and libraries. 

All the above modules depend upon an Abstract base class `IngestorInterface` for homogenised way og dealing with reading file contents and then uses a `Ingestor` class, which is a unigied interface to read the contents of the various file formats. It's an example of strategy design pattern and its main purpose is simplification by encapsulation.

### Meme Module

This module is responsible for manipulating and drawing text onto images. For this purpose it uses an external library `pillow` to resize images and draw texts over images.
This class  takes an output directory path as an argument. Its main method is `make_meme`, which creates the meme image and saves it in the provided output directory (it creates the output directory if its not created already), and returns a `string` path to the created meme. This meme path can be used later by the various applications interfaces like CLI or Flask for getting the images with memes and showing to the users.

## Using the app
The app has two interfaces 
1. CLI based, created using `argparse`
1. Web based, created using `Flask`

- To use CLI based interface run the `meme.py` file using the following command

```
    python meme.py
```

- The web application can be started by running `app.py` as  follows:
```bash

    python app.py
```

The application can be accessed at http://127.0.0.1:5000

## Author
Nikhil Pandey



