{
    'name': 'Tts Credit Note Stock Receipt',
    'version': '19.0.1.0.0',
    'category': 'Accounting/Inventory',
    'summary': 'Create Stock Return Picking from Credit Note and View Receipts',
    'description': """
        This module allows selecting a return warehouse on Customer Credit Notes.
        When the Credit Note is posted, it automatically creates a generic Incoming Shipment (Receipt)
        in the selected warehouse for the products in the credit note.

        Features:
        - Return Warehouse selection on Credit Note.
        - Auto-create Stock Receipt on Post.
        - Smart Button "Receipts" to view linked stock moves.

        Our Services:
        - Odoo Customer development for all modules
        - Odoo Based Mobile APP
        - GCC Based Support
        - Saudi E Invoice Zatca Integration Service

        Author: Truetstech solutions Private limited
        Email: info@truetstech.com
        Whatsapp: +918304873145
        Website: truets.odoo.com
    """,
    'author': 'Truetstech solutions Private limited',
    'website': 'https://truets.odoo.com',
    'depends': ['account', 'stock'],
    'data': [
        'views/account_move_views.xml',
    ],
    'images': ['static/description/main_screenshot.png'],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
