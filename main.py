# Main Function
def main():
  book_path = "books/frankenstein.txt"
  book_contents = read_book(book_path)
  book_words = count_words(book_contents)
  book_characters = count_characters(book_contents)

  print(book_characters)

# Returns the contents of a given book
def read_book(book_path):
  with open(book_path) as f:    
    return f.read()

# Returns the number of words in a given book
def count_words(book_contents):
  return len(book_contents.split())

# Count how many times characters are found in book
def count_characters(book_contents):
  characters = {}
  for word in book_contents:
    lower = word.lower()
    if lower in characters:
      characters[lower] += 1
    else:
      characters[lower] = 1
  return characters

# Call Main
main()