LEXICON: dict[str, str] = {
    'forward': '>>',
    'backward': '<<',
    '/start': '<b>Hello, reader</b>\n\nThis is a bot,'
              'where you can read The Martian Chronicles\n\n'
              'To see a list of available commands, type /help',
    '/hepl': '<b>This is a reader-bot</b>\n\nAvailable commands\n\n'
             '/beginning - go to the begining of the book\n'
             '/continue - continue to read\n/bookmarks - to see the list'
             'of bookmarks\n/help - help with the bot\n\nTo save a bookmark - '
             'type the page button\n\nGood reading',
    '/bookmarks': '<b>This the list of your bookmarks:</b>',
    'edit_bookmarks': '<b>Edit bookmarks</b>',
    'edit_bookmarks_button': '❌ EDIT',
    'del': '❌',
    'cancel': 'CANCEL',
    'no_bookmarks': 'You don`t have any bookmark.\n\nTo add page to'
                    'bookmark - during a reading a book type the page'
                    'button\n\n/continue - continue to read',
    'cancel_text': '/continue - continue to read',
}

LEXICON_COMMANDS: dict[str, str] = {
    '/beginning': 'Go to the beginning of the book',
    '/continue': 'Continue - to read',
    '/bookmarks': 'My bookmarks',
    '/help': 'Help with the bot'
}
