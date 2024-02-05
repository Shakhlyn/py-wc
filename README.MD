# wc

## Description

A word counter tool similar to [wc<sup>1</sup>](<https://en.wikipedia.org/wiki/Wc_(Unix)>) in **UNIX**. It counts the number of lines, words, file size, and characters in a given file or input stream.

Currently, **wc** can count only from _.txt_ files. In the next version, it will count from other types of files too.

### Prerequisites:

- > Ensure you have Python 3 installed.
- > Make sure you have [**pip**<sup>2</sup>](https://pip.pypa.io/en/stable/installation/) installed. If your machine doesn't have _pip_, see [here<sup>2</sup>](https://pip.pypa.io/en/stable/installation/) to know how to install and upgrade.

## Installation

- clone the repository:

```bash
git clone https://github.com/Shakhlyn/py-wc.git
```

- Navigate into the project

```bash
cd py-wc
```

- Update _**pip**_ to the latest version if _pip_ is not the lates one. If your machine doesn't have pip, see the _installation requirements_ section.

```python
python -m pip install --upgrade pip
```

- Create a virtual environment.  
  (Optional) It is good to install the package in the virtual environment. However, you don't need to be in the virtual environment to run and use this package.

```python
python -m venv venv
```

- Activate the virtual environment:  
  (Optional) Needed if you want to install in the virtual environment

> For Linux/macOS or _git bash_ in windows machine

```bash
source venv/Scripts/activate.
```

> For windows

```bash
./venv/Scripts/activate.
```

- Install the package  
  It is good to install in the **editable mode**. Installing in the editable mode ,i.e., **-e**, will let you see changes right after changing/updating the code.

```python
python -m pip install -e .
```

## Usage

```bash
ccwc [options] [file]
```

or

```bash
ccwc [file] [options]
```

or **with piping functionality**

```bash
cat test.txt | ccwc [options]
```

### Options

> -l: Count lines  
> -w: Count words  
> -c: Count byte-size  
> -m: Count in characters

Examples:

- **Count lines in a file:**

```bash
ccwc -l test.txt
```

- **Count words in a file:**

```bash
ccwc -w test.txt
```

- **Count characters in a file:**

```bash
ccwc -c file.txt
```

- _If no argument is provided, it will count for all the options_

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

MIT

## External Links

> 1. https://en.wikipedia.org/wiki/Wc_(Unix)
> 2. https://pip.pypa.io/en/stable/installation/
