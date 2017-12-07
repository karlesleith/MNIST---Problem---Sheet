# MNIST---Problem---Sheet
CA Relating to Emerging Technologies 

## Problem set: Read the MNIST data files

These problems relate to the famous MNIST data set. Save your work as a Python file, or a collection of Python files. Place them in a single repository on GitHub, complete with a README. The files are in a bespoke format, as described on the website.

### 1. Read the data files

Download the image and label files. Have Python decompress and read them byte by byte into appropriate data structures in memory.

### 2. Output an image to the console

Output the third image in the training set to the console. Do this by representing any pixel value less than 128 as a full stop and any other pixel value as a hash symbol.

### 3. Output the image files as PNGs

Use Python to output the image files as PNGs, saving them in a subfolder in your repository. Name the images in the format train-XXXXX-Y.png or test-XXXXX-Y.png where XXXXX is the image number (where it occurs in the data file) and Y is its label. For instance, the five-thousandth training image is labelled 2, so its file name should be train-04999-2.png. Note the images are indexed from 0, so the five-thousandth image is indexed as 4999. See below for an example of it. Commit these image files to GitHub.

Solutions to the [MNIST Problem sheet](https://emerging-technologies.github.io/problems/mnist.html) 

## What is the MNIST Data Set?
The MNIST database (Modified National Institute of Standards and Technology database) is a large database of handwritten digits that is commonly used for training various image processing systems. The database is also widely used for training and testing in the field of machine learning. It was created by "re-mixing" the samples from NIST's original datasets. The creators felt that since NIST's training dataset was taken from American Census Bureau employees, while the testing dataset was taken from American high school students, it was not well-suited for machine learning experiments. Furthermore, the black and white images from NIST were normalized to fit into a 28x28 pixel bounding box and anti-aliased, which introduced grayscale levels..


**REF**: [http://yann.lecun.com/exdb/mnist/](http://yann.lecun.com/exdb/mnist/)


# How to clone the repository
1. Download and install Anaconda [https://anaconda.org/] <br/>
2.Under the repository name of the repo you want to clone, click "clone or download"<br/>
3.Open Git Bash <br/>
4.Type "Git Clone" the the URL of the Repository <br/>

# Overview
In this problem sheet we read in a decompressed files from a bespoke format byte by byte, and then outputed the images files to PNGs, I zipped the images so it would be easier to upload.

# To run the application
1.Open Cmd. <br/>
2.Go to the directory of the cloned repo. <br/>
3. Type Python "MINST-Test.py"
