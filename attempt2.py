import chardet

# Open the input text file in binary mode
with open('.txt', 'rb') as f:
    data = f.read()

# Detect the encoding of the file
encoding = chardet.detect(data)['encoding']

# Open the file with the detected encoding
with open('.txt', 'r', encoding=encoding) as f:
    text = f.read()

# Divide the text into 30 parts
parts = [text[i:i+len(text)//30] for i in range(0, len(text), len(text)//30)]

# Save each part to a separate file
for i, part in enumerate(parts):
    with open(f'Day{i+1}.txt', 'w', encoding=encoding) as f:
        f.write(part)
