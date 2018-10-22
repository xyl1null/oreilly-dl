# SafariBooks
This is a fork from lorenzodifuccia's [repo](https://github.com/lorenzodifuccia/safaribooks).

Download and generate *EPUB* of your favourite books from [*Safari Books Online*](https://www.safaribooksonline.com).  
I'm not responsible for the use of this program, which is for *personal* and *educational* purposes only.  

## Overview:
  * [EPUB Format](#epub-format)
    - META-INT
    - mimetype
    - content.opf
  * [Usage](#usage)
    - [Program options](#program-options)
## EPUB FORMAT:

The EPUB® format provides a means of representing, packaging and encoding structured and semantically enhanced Web content — including HTML, CSS, SVG and other resources — for distribution in a single-file container.
  * META-INF _(container.xml)_
  ```
    <?xml version="1.0" encoding="UTF-8"?>
    <container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
      <rootfiles>
        <rootfile full-path="content.opf" media-type="application/oebps-package+xml"/>
      </rootfiles>
    </container>
  ```
  * mimetype
  ```
   application/epub+zip
  ```
  * content.opf
  ```
    <?xml version="1.0" encoding="UTF-8"?>
    <package xmlns="http://www.idpf.org/2007/opf"
           xmlns:redirect="http://xml.apache.org/xalan/redirect"
           version="3.1"
           unique-identifier="bookid">
     <metadata xmlns:opf="http://www.idpf.org/2007/opf"
               xmlns:dc="http://purl.org/dc/elements/1.1/">
        <dc:identifier id="bookid">XXXXXXXXXXXXX</dc:identifier>
        ...
        <meta name="cover" content="cover-image"/>
        ...
     </metadata>
     <manifest>
        <item id="css" href="../css" media-type="text/css"/>
        <item id="cover" href="cover.xhtml" media-type="application/xhtml+xml"/>
        <item id="cover-image"
              href="images/cover.jpg"
              media-type="image/jpeg"
              properties="cover-image"/>
        ...
     </manifest>
     <spine toc="ncx">
      <itemref idref="f_0077" />
      ...
     </spine>
     <guide>
        <reference type="cover" title="Cover" href="cover.xhtml"/>
     </guide>
    </package>
  ```
And EPUB is basically a compressed combination of all files above plus other meta-data collections, however here comes another problem where python's `shutil.make_archive(zip)` works in apple's Books whilst unix's zip system doesn't. (~~There has to be some connections between there two, very peculiar yet I'm curious to know, gotta dig it deeper). ~~

For more info on EPUB, please check [here](http://www.idpf.org/epub3/latest/packages)

## Usage:
```
$ git clone https://github.com/lorenzodifuccia/safaribooks.git or
$ git clone https://github.com/shawneau/safaribooks.git
Cloning into 'safaribooks'...

$ cd safaribooks
$ pip3 install -r requirements.txt

```
#### Program options:
```
$ python3 safaribooks.py --help
usage: safaribooks.py [--cred <EMAIL:PASS>] [--no-cookies] [--no-kindle]
                      [--preserve-log] [--help]
                      <BOOK ID>

Download and generate EPUB of your favorite books from Safari Books Online.

positional arguments:
  <BOOK ID>            Book digits ID that you want to download.
                       You can find it in the URL (X-es):
                       `https://www.safaribooksonline.com/library/view/book-
                       name/XXXXXXXXXXXXX/`

optional arguments:
  --cred <EMAIL:PASS>  Credentials used to perform the auth login on Safari
                       Books Online.
                       Es. ` --cred "account_mail@mail.com:password01" `.
  --no-cookies         Prevent your session data to be saved into
                       `cookies.json` file.
  --no-kindle          Remove some CSS rules that block overflow on `table`
                       and `pre` elements. Use this option if you're not going
                       to export the EPUB to E-Readers like Amazon Kindle.
  --preserve-log       Leave the `info_XXXXXXXXXXXXX.log` file even if there 
                       isn't any error.
  --help               Show this help message.
```

For the first time users, you'll have to specify your SafariBooksOnline account credentials, which is in the format of   
```
$ python3 safaribooks.py --cred "account@email.com:password" XXXXXXXXXXXXX
```
  * Xs indicate the 13-digit ISBN number, which is available in the Book url, e.g.
       `https://www.safaribooksonline.com/library/view/how_to_build_a_harem/6666666666666/`
    *Notice* Sometimes ISBN in the book description page doesn't correspond to the url, so always trust the latter.
  * `email:password` with your own. 
    *Notice* Use a combination of alphanumerical characters. 
 
Later, you're free to omit the --cred inputs using:
```
$ python3 safaribooks.py XXXXXXXXXXXXX
```
---  
  
## Cheers!
