{
    'name': 'final_project_2',
    'version': '1.0',
    'description': 'Final Project 2',
    'author': 'Ari Cahyono',
    "depends": ['mail'],
    'data': [
        'data/member.class.csv',
        'data/author.class.csv',
        'data/publisher.class.csv',
        'data/book.class.csv',
        'data/borrowing.book.class.csv',
        'securitys/ir.model.access.csv',
        'sequences/sequence_returning_book.xml',
        'sequences/sequence_borrowing_book.xml',
        'reports/paperformat_member_borrowing_book.xml',
        'reports/action_member_borrowing_book.xml',
        'reports/report_member_borrowing_book.xml',
        'views/borrowing_book_view.xml',
        'views/returning_book_view.xml',
        'views/member_view.xml',
        'views/book_view.xml',
        'views/library_view.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True
}
