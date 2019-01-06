# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import, division, print_function, unicode_literals)
import datetime
from operator import itemgetter

mapping = {
    'has_header': True,
    'is_split': False,
#    'bank': 'Bank',
    'currency': 'EUR',
    'delimiter': ';',
    'account': 'Actif:Actifs actuels:Compte chèque',
# gnucash needs US date format for qif
    'date': lambda tr: datetime.datetime.strptime(tr['Date'],
                                       '%d/%m/%y').strftime('%m/%d/%y'),
    'amount': lambda tr: tr['Débit'] + tr['Crédit'],
    'payee': itemgetter('Libellé'),
#    'date_fmt': '%x',
#    'date_fmt': '%d/%m/%y',
#    'payee': itemgetter('Description'),
#    'notes': itemgetter('Notes'),
#    'check_num': itemgetter('Num'),
#    'id': itemgetter('Row'),
}
