import chardet
import os

# Open the input text file in binary mode
file_name = "Stardust - Neil Gaiman.txt"
first_5_letters = file_name[:5]
with open(file_name, 'rb') as f:
    data = f.read()

# Detect the encoding of the file
encoding = chardet.detect(data)['encoding']

# Open the file with the detected encoding
with open(file_name, 'r', encoding=encoding) as f:
    text = f.read()

# Divide the text into 30 parts
parts = [text[i:i+len(text)//30] for i in range(0, len(text), len(text)//30)]

# Save each part to a separate file
for i, part in enumerate(parts):
    with open(f'{first_5_letters}_Day{i+1}.txt', 'w', encoding=encoding) as f:
        f.write(part)
