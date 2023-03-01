Photo Album Viewer
==================

This is a command-line tool for displaying photo ids and titles in an album. The photos are retrieved from the online web service [https://jsonplaceholder.typicode.com/photos](https://jsonplaceholder.typicode.com/photos), which provides a JSON file with the necessary information.

Requirements
------------

To run this tool, you will need to have Python 3 installed on your system. You can download Python 3 from the official website at [https://www.python.org/downloads/](https://www.python.org/downloads/).

Installation
------------

To install the dependencies required by this tool, run the following command in your terminal:

`pip install requests`

Usage
-----

To use this tool, open your terminal and navigate to the directory where you have saved the `photo_album.py` file. Then, run the following command:

css

```css
python photo_album.py [album_number]
```

Replace `[album_number]` with the number of the album you want to view. The tool will retrieve the photos for that album from the JSON file and display the photo IDs and titles in the terminal.

Example
-------

Here is an example of how to use the tool:

`python photo_album.py 2`

This command will retrieve the photos for album number 2 and display the photo IDs and titles in the terminal.

Tests
-----

To run the unit tests for this tool, open your terminal and navigate to the directory where you have saved the `test_photo_album.py` file. Then, run the following command:

`python -m unittest`

This command will run the unit tests and display the results in the terminal.

---