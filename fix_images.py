with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Fix spaced filenames (with backslash escape — invalid in browsers)
c = c.replace("pinchu\\ 2.jpg", "pinchu-2.jpg")
c = c.replace("pinchu\\ 3.jpg", "pinchu-3.jpg")
c = c.replace("pinchu\\ 4.jpg", "pinchu-4.jpg")

# Fix spaces in <img src> attributes (no backslash)
c = c.replace("pinchu 2.jpg", "pinchu-2.jpg")
c = c.replace("pinchu 3.jpg", "pinchu-3.jpg")
c = c.replace("pinchu 4.jpg", "pinchu-4.jpg")

# Fix .jfif extension
c = c.replace("velvet.jfif", "velvet.jpg")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("Done! All image references fixed.")
