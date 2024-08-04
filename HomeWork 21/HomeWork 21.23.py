def word_count(text):
    return len(text.split())

def character_count(text):
    return len(text)

def find_word(text, word):
    return text.find(word)

def replace_word(text, old_word, new_word):
    return text.replace(old_word, new_word)

text_processing_functions = {
    'word_count': word_count,
    'character_count': character_count,
    'find_word': find_word,
    'replace_word': replace_word
}

def process_text(text, operation, **kwargs):
    if operation in text_processing_functions:
        return text_processing_functions[operation](text, **kwargs)
        

text = input("Write a something:\t")
print("Your sentence:", text)
word = input("Write a selected word:\t")
old_word = input("Old word:\t")
new_word = input("New word:\t")


print("Word Count:", process_text(text, 'word_count'))

print("Character Count:", process_text(text, 'character_count'))

if word not in text:
    print("There is no such word")
else:
    print(f"Find: '{word}' :", process_text(text, 'find_word', word=word))

print(f"Replace '{old_word}' with '{new_word}':", process_text(text, 'replace_word', old_word=old_word, new_word=new_word))