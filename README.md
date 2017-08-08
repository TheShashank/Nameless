# Nameless
An app that takes scans of pages of textbooks, extracts all highlighted text and creates questions with multiple choice answers to enable active recall. 

There are multiple approaches to the "extracts all highlighted text" part:
1. Fork and somehow use the logic in https://github.com/danielsnider/OCR-only-highlighted/blob/master/MyFuncs.cpp
2. Build my own dataset and teach it to recognise the text
3. Image segmentation using K-Means Clustering, extract the block(s) of highlighted text, and then input it as an image into the Tesseract. 

To know which color text to scrape, we could have the user select from a dropdown-ish thing. Otherwise, they could take a picture of that color on the highlighted section. 

Once the text has been extracted, it will be Googled, and two things will happen:
1. Using BeautifulSoup, the "Did you mean ____" portion will be extracted (easy peazy) - this will be the database entry. 
2. The part of the app with all the links and such will be derived from this page (maybe).

Quiz generation from the text/ 
