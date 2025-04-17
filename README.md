# AppOpener

An automation script. Given a specially-formatted CSV, opens a list of executables alongside any URLs as command-line arguments.

For example:

```
py ./app_opener.py example.csv
```

is the equivalent of running the following in a terminal:

```
exe0 A
exe0 B
exe0 C
exe0 D
exe0 E
exe0 F
exe1 G
exe1 H
exe1 I
exe1 J
exe2
```

# Setup

To run this app, you'll need to do 3 things:

1. Clone this repo.
2. Download dependencies.
3. Create a specially-formatted CSV

# Dependencies

```
pip install -r .\requirements.txt
```

For manual download, install pywinauto. Instructions [are provided on their website](https://pywinauto.readthedocs.io/en/latest/index.html).

# Formatting your CSV

Check [example.csv](/example.csv) for reference. As a summary, the following things are required for the program to open your executables

1. Two headers - Exe Paths and URLs - this program assumes you have headers and will skip the first line
2. Executable files as the first entry in each row - this program WILL exit prematurely if the first entry is blank or not a .exe file
3. If you have more than 1 url, it goes in a new cell/space to the RIGHT of the .exe file
4. Absolute paths only please.

# Running the file

```
py ./app_opener.py (csv_file_path)
```

Replace `(csv_file_path)` with your path to your csv

More instructions:

```
py ./app_opener -h
py ./app_opener --help
```

# Permissions

Don't use this for malware/ad-ware. Only install on your own machine. Otherwise go wild.
