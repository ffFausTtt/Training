# Задача: "Менеджер заметок"

from pathlib import Path
import json
from datetime import date

class Note:
    def __init__(self, content, title = 'Без названия'):
        self.title = title
        self.content = content
        self.created_at = str(date.today())
        self.tags = []

    def add_tag(self, tag):
        ''' Добавление тега в список tags '''
        self.tags.append(tag)

    def word_count(self):
        ''' Возвращает количество слов '''
        word = self.content.split(' ')
        count = 0
        for cont in word:
            count += 1
        print(f"В content: {count} слов")
        print(f"Всего в content: {len(self.content)} символов")
        return count

    def display_info(self):
        ''' Возвращает строку с заголовком, датой, первыми 30 символами содержания '''
        new_content = []
        for i in self.content:
            if len(new_content) <= 30:
                new_content.append(i)
           
        result_content = ''.join(new_content)
        all_string = f"{self.title} {self.created_at} {result_content}"
        print(all_string + '...')

    def to_dict(self):
        ''' Собирает словарь '''
        return {
            'tag': self.tags,
            'date': self.created_at,
            'title': self.title,
            'content': self.content
        }


def find_notes_by_tag(notes, tag):
    ''' Возвращает новый список с теми заметками, у которых есть этот тег '''
    notes_by_tag = []
    for note in notes:
        if tag in note.tags:
            notes_by_tag.append(note)
    print (notes_by_tag)

def longest_note(notes):
    ''' Возвращает объект заметки с самым большим количеством слов '''
    if not notes:
        return None

    long = notes[0]
    for note in notes[1:]:
        if note.word_count() > long.word_count():
             long = note
    return long
    
def save_notes_to_file(notes, filename):
    ''' Сохранение заметок в файл '''
    notes_dict = []
    for note in notes: 
        notes_dict.append(note.to_dict())
    path = Path(filename)
    content = json.dumps(notes_dict)
    path.write_text(content)
    print(f"✅ Сохранено {len(notes)} заметок в файл {filename}")

def load_notes_from_file(filename):
    ''' Чтение заметок из файла '''
    path = Path(filename)
    content = path.read_text()
    notes_dict = json.loads(content)

    notes = []
    for note_dict in notes_dict:
        note = Note(note_dict['content'], note_dict['title'])
        note.created_at = note_dict['date'] 
        for tag in note_dict['tag']:
            note.add_tag(tag)
        notes.append(note)
    print("✅ Прочитано")
    return notes


if __name__ == '__main__':
    note1 = Note("Молоко, хлеб, яйца, сыр, помидоры", "Купить продукты")
    note1.add_tag("покупки")
    note1.add_tag("важно")

    note2 = Note("Сделать приложение для заметок с тегами и поиском", "Идея для проекта")
    note2.add_tag("идеи")
    note2.add_tag("программирование")

    note3 = Note("Омлет: взбить яйца с молоком, посолить, жарить на сковороде", "Рецепт")
    note3.add_tag("рецепты")
    note3.add_tag("еда")

    notes_list = [note1, note2, note3]

    note1.word_count()
    note1.display_info()

    longest_note(notes_list)

    save_notes_to_file(notes_list, 'notes.json')
    load_notes_from_file('notes.json')