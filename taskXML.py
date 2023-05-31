import xml.etree.ElementTree as ET

# Read in the XML file
tree = ET.parse('Examples/movie.xml')
root = tree.getroot()

# List all the child tags of the movie element
for child in root.iter('movie'):
    print(child.tag)

# Print out the movie descriptions
for description in root.iter('description'):
    print(description.text)

# Find the number of movies that are favorites and the number of movies that are not
favorites = 0
not_favorites = 0

for movie in root.findall('movie'):
    if movie.attrib['favorite'] == 'yes':
        favorites += 1
    else:
        not_favorites += 1

print("Number of favorite movies:", favorites)
print("Number of non-favorite movies:", not_favorites)

#reference - https://docs.python.org/3/library/xml.etree.elementtree.html