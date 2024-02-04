
<h1 align="center">
    <img src="https://github.com/gabrielhamdan/2600-bitmapy/assets/74621925/6edf1924-ad28-4d9b-aeaa-47c2c6166c5e" alt="2600 bitmapy" width="40%"/>
    <p>Easily create async playfields for the Atari 2600</p>
</h1>

![Static Badge](https://img.shields.io/badge/license-MIT-blue) ![Python](https://img.shields.io/badge/built_with-python-blue)

<details open="open">
<summary><b>Table of Contents</b></summary>

- [About 2600 Bitmapy](#about-2600-bitmapy)
- [2600 Bitmapy Features](#2600-bitmapy-features)
- [Installation](#installation)
- [Usage](#usage)
    - [Example Input/Output](#example-inputoutput)
- [Contributing](#contributing)
- [Issues and Bug Reports](#issues-and-bug-reports)
- [Acknowledgements](#acknowledgements)

</details>

## About 2600 Bitmapy

Welcome to **2600 Bitmapy**, an open-source tool crafted with love and dedication for creating asynchronous playfield bitmaps for the classic Atari 2600. This project was inspired by the vibrant community of 2600 homebrew content creators and fueled by the need for more modern, multiplatform bitmap tools for the Atari 2600.

## 2600 Bitmapy Features

- Automatically convert any image to 2600 bitmap
- Optionally save converted image files
- Easily invert image colors

## Installation

Clone the repo:
```bash
$ git clone https://github.com/gabrielhamdan/2600-bitmapy.git
$ cd 2600-bitmapy
```

Make sure you have Python and Pipenv installed.

For POSIX terminal users, there's a Makefile in order to make things easier. Run ```make env```, then ```make init```. Finally ```make test``` and *voilà*! A ```test``` directory will be created with a black and white 40x192 image, resulting from the conversion of ```data/bitmapy_splash.png```. The good stuff is going to be there too: the bitmap text file*.

**For the time beign, it's only possible to output a bitmap with the* ```hex``` *directive. You can learn more about the technique for rendering async playfields at [8bitworkshop](https://8bitworkshop.com/v3.11.0/?file=examples%2Fbitmap.a&platform=vcs). Byte arrays are a next step.*

## Usage

**2600 Bitmap** is provided as a CLI tool.

```bash
$ 2600_bitma.py [-h] -i INPUT_IMAGE [-t THRSHLD] [-I] [-o OUTPUT_FILE] [-s SAVE] [-b] [-v]
```

- ```-h``` to show help message and exit
- ```-i INPUT_IMAGE``` to specify the input image file path
- ```-t THRSHLD``` to set the image conversion thresholding value*
- ```-I``` to invert the pixel colors in the image
- ```-o OUTPUT_FILE``` to specify the output file name for the converted image
- ```-s OUTPUT_IMAGE``` to save the converted image**
- ```-b``` to output byte arrays***
- ```-v``` to execute the tool in verbose mode, providing additional information during execution

**By default, it's 150.*

***If no path is provided, the program won't output the converted image, which can be helpful for further editing.*

****By default, it's in hexadecimal.*

By running the following command:

```bash
$ python3 2600_bitma.py -i my_img.png -t 100 -I -o my_bitmap -s my_converted_img.png -b -v
```

You should then see something similar to this:

```bash
                         ___  ____ ___   ___ 
                        |_  |/ __// _ \ / _ \
                       / __// _ \/ // // // /
         ___   _  __  /____/\___/\___/ \___/ 
        / _ ) (_)/ /_ __ _  ___ _ ___  __ __ 
       / _  |/ // __//  ' \/ _ `// _ \/ // / 
      /____//_/ \__//_/_/_/\_,_// .__/\_, /  
                               /_/   /___/   
      
                  developed by Gabriel Hamdan

> 2600 Bitmapy initialized.
> Image converted with success.
> Converted image saved as my_converted_img.png.
> Pixels parsed.
> Creating playfield as byte.
> Could not output image data to byte directive. Formatting data to hex...
> Success! Time of execution: 97.73 milliseconds.
> Happy coding!
```

### Example Input/Output

<details><summary>Input Image</summary>
    <div align="center">
        <img src="https://github.com/gabrielhamdan/2600-bitmapy/assets/74621925/01cc2571-21bd-4d5c-b8a1-61a96c12644e" alt="input image" width="30%"/>
    </div>
</details>

<details><summary>Output Image</summary>
    <div align="center">
        <img src="https://github.com/gabrielhamdan/2600-bitmapy/assets/74621925/c004c56a-ba88-48ca-8ff4-f913edcb4af7" alt="output image" height="40%"/>
    </div>
</details>

<details><summary>Bitmap</summary>
<pre>
<code>

    PFBitmap0
        hex 00
        hex f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0
        hex f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0
        hex f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0
        hex f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0
        hex f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0
        hex f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0
        hex f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0
        hex f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0
        hex f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0
        hex f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0
        hex f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0
        hex f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0

    PFBitmap1
        hex 00
        hex ffffffffffffffffffffffffffffffff
        hex ffffffffff692c9c9c9c6063ffffffff
        hex ffff6ca39393a368ffffffffffff6060
        hex 8d8d8d2470ffffffffffffffffffffff
        hex ffffffff1b0b0b0b0b0b2b2b2b2b2b2b
        hex 2b0b0b0b0b0b0b2b2b2b2b2b0b0b0b0b
        hex 1b1b1bffffffffffffffffffffffffff
        hex ffffffffffffffffffffffffffffffff
        hex ffffffffffffffffffffffffffffffff
        hex ffffffffffffffffffffffffffffffff
        hex ffffffffffffffffffffffffffffffff
        hex ffffffffffffffffffffffffffffffff

    PFBitmap2
        hex 00
        hex ffffffffffffffffffffffffffffffff
        hex ffffffffff99596363631999ffffffff
        hex ffff83686c6c6882ffffffffffffa626
        hex 717171648effffffffffffffffffffff
        hex ffffffffadacacacacacacacacacacac
        hex acacacacacacacacacacacacac080808
        hex 081858ffffffffffffffffffffffffff
        hex ffffffffffffffffffffffffffffffff
        hex ffc3c3c3c3c363776767676f6f4f4f4f
        hex 5fdfdfdfdfdfdbdbdbdbc3c3c3c7e7ef
        hex ffffffffffffffffffffffffffffffff
        hex ffffffffffffffffffffffffffffffff

    PFBitmap3
        hex 00
        hex f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0
        hex f0f0f0f0f09090b0b0b01010f0f0f0f0
        hex f0f0d01020201050f0f0f0f0f0f03010
        hex 90b0b09010f0f0f0f0f0f0f0f0f0f0f0
        hex f0f0f0f0202020202020202020202020
        hex 20202020202020202060606060606060
        hex e0e0f0f0f0f0f0f0f0f0f0f0f0f0f0f0
        hex f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0
        hex f0c0c0808080a0a0b0b0b0b0b0b0a0a0
        hex 808080c0c0e0e0e0e0e0e0e0c0c0c0d0
        hex f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0
        hex f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0

    PFBitmap4
        hex 00
        hex ffffffffffffffffffffffffffffffff
        hex ffffffffff71a18d8dad2070ffffffff
        hex ffff42ebefefeb40ffffffffffffe646
        hex 5898d84667ffffffffffffffffffffff
        hex ffffffffa7a7a7a7a7a7272727272323
        hex a3a1a1a1a5a5a5a5a5a5a5a5a5212121
        hex 232323ffffffffffffffffffffffffff
        hex ffffffffffffffffffffffffffffffff
        hex ffcfcf8e8686a6263434747575717171
        hex 717171717174743434368686868e8fcf
        hex ffffffffffffffffffffffffffffffff
        hex ffffffffffffffffffffffffffffffff

    PFBitmap5
        hex 00
        hex ffffffffffffffffffffffffffffffff
        hex fffffffffffbf9fcfcfcf9fbffffffff
        hex fffff8fcfcfcfcf8fffffffffffffcf8
        hex fbf3f3f8f8ffffffffffffffffffffff
        hex fffffffffdfdfdfdfdfdfdfdfdfdfdf9
        hex f9f8f8f8f8f2f2f2f2f2f2f2f2f2f2f2
        hex f2f2f2ffffffffffffffffffffffffff
        hex ffffffffffffffffffffffffffffffff
        hex fffcfcfcf8f8f8fbfbfbf3f3f3f3f7f7
        hex f7f7f7f3f3f3f3fbfbfbf8f8f8fcfcfc
        hex ffffffffffffffffffffffffffffffff
        hex ffffffffffffffffffffffffffffffff
</code>
</pre>
</details>

<details><summary>2600 Rendering</summary>
    <div align="center">
        <img src="https://github.com/gabrielhamdan/2600-bitmapy/assets/74621925/7cefc9f8-fda5-445e-b447-58278e283540" alt="2600 rendering" width="30%"/>
    </div>
</details>

## Contributing

Contributions are welcome! Fork the repository, make changes, and submit a pull request to help improve **2600 Bitmapy**.

## Issues and Bug Reports

If you encounter any issues or bugs, [open an issue](https://github.com/gabrielhamdan/2600-bitmapy/issues) on GitHub.

## Acknowledgements

 - ASCII banner made with [manytools.org](https://manytools.org/)
 - 2600 cartridge label used for this README cover made with [labelmaker2600.com](http://labelmaker2600.com/)