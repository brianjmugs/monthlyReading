import ebooklib
from ebooklib import epub
from math import ceil

# Open the ePub file
book = epub.read_epub('book.epub')

# Extract the text from each chapter
chapters = []
for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
    chapters.append(item.get_content())

# Calculate the number of chapters per part
chapters_per_part = ceil(len(chapters) / 30)

# Iterate through the chapters and write each part to a separate text file
for i in range(30):
    start = i * chapters_per_part
    end = start + chapters_per_part
    # Use the 'utf-8' encoding when opening the file
    with open(f'part{i+1}.txt', 'w', encoding='utf-8') as f:
        for chapter in chapters[start:end]:
            # Decode the bytes object into a string
            chapter_text = chapter.decode('utf-8')
            f.write(chapter_text)
