# Найдите скрытый текст.
# Дан отрывок текста. Соберите все заглавные буквы в одно слово
# Например: текст = "How are you? Eh, ok. Low or Lower? Ohhh.",
# если мы соберем все заглавные буквы, то получим сообщение "HELLO".

def show_mesage(text: str) -> str:
  letters = []
  for letter in text:
    if letter.isupper():
      letters.append(letter)
      text = ''.join(letters)
    if text.islower():
      text = ''
  if text.isupper():
    t = []
    t.append(text.replace("!", ""))
    text = ''.join(t).replace(" ", "")
  return text

if __name__ == '__main__':
    print('Example:')
    print(show_mesage("How are you? Eh, ok. Low or Lower? Ohhh."))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert show_mesage("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert show_mesage("hello world!") == "", "Nothing"
    assert show_mesage("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
    print("Cool")
