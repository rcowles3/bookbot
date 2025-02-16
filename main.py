# Main Function
def main():
  book_path = "books/frankenstein.txt"
  book_contents = read_book(book_path)
  book_words = count_words(book_contents)

  print(book_words)

# Returns the contents of a given book
def read_book(book_path):
  with open(book_path) as f:    
    return f.read()

# Returns the number of words in a given book
def count_words(book_contents):
  return len(book_contents.split())

# Call Main
main()