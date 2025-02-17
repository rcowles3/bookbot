# Main Function
def main():
  book_path = "books/frankenstein.txt"
  book_contents = read_book(book_path)
  book_words = count_words(book_contents)
  book_characters = count_characters(book_contents)
  report_dict = create_report_dict(book_characters)
  
  build_report(report_dict, book_words, book_path)  

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

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["num"]

# Create a list of dictionaries, sorting them in reverse to display
# in order of characters that appear the most
def create_report_dict(char_dict):
  char_list = []
  for char in char_dict:
    if char.isalpha():  
      temp_dict = {}
      temp_dict["key"] = char
      temp_dict["num"] = char_dict[char]
      temp_dict["string"] = f"The '{char}' character was found {char_dict[char]} times"
      char_list.append(temp_dict)

  # sort our char_list list in reverse on key = 'num'
  char_list.sort(reverse=True, key=sort_on)
  return char_list

# Build Formatted Report
def build_report(report_dict, word_count, path):
  print(f"--- Begin report of {path} ---")
  print(f"{word_count} words found in the document")
  print("\n")

  for i in report_dict:
    print(i['string'])

  print("--- End report ---")

# Call Main
main()