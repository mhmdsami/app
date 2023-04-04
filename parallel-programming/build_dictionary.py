import threading


class CharacterDictionaryThread(threading.Thread):
    def __init__(self, input_string):
        threading.Thread.__init__(self)
        self.input_string = input_string
        self.character_dict = {}

    def run(self):
        for char in self.input_string:
            if char in self.character_dict:
                self.character_dict[char] += 1
            else:
                self.character_dict[char] = 1

    def get_character_dict(self):
        return self.character_dict


if __name__ == '__main__':
    input_string = input("Enter a string: ")
    character_thread = CharacterDictionaryThread(input_string)
    character_thread.start()
    character_thread.join()

    character_dict = character_thread.get_character_dict()
    print(character_dict)
