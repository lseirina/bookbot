import os
import sys

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


def _get_part_text(text: str, start: int, size: int):
    new_text = text[start:]
    pnct = ['.', ',', '?', '!', ':', ';']
    while size > 0:
        try:
            if new_text[size-1] in pnct and new_text[size-2] in pnct:
                size -= 3
            elif new_text[size-1] in pnct:
                return new_text[:size], len(new_text[:size])

            else:
                size -= 1
        except Exception:
            size = len(new_text)
    return new_text, len(new_text)


def prepare_book(path: str) -> None:
    with open(path, 'r', encoding='utf-8') as file:
        text = file.read()

    start = 0
    i = 1
    while start < len(text):
        page, len_page = _get_part_text(text, start, PAGE_SIZE)
        book[i] = page.lstrip()
        i += 1
        start += (PAGE_SIZE - (PAGE_SIZE - len_page))


prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))
