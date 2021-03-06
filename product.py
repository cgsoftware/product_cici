# -*- encoding: utf-8 -*-

import netsvc
import pooler, tools
import math

from tools.translate import _

from osv import fields, osv


class product_product(osv.osv):
    _inherit='product.product'
    
    _columns = {
                'marchio_ids':fields.many2one('marchio.marchio','Marchio'),
                'composizione':fields.char('Composizione',size = 50,translate=True),
                'formato':fields.char('Formato Dimensioni',size= 50,translate=True),
                'tipologia':fields.char('Tipologia',size = 50,translate=True),
                'conf_collo_num_pezzi':fields.integer('Pezzi x Collo'),
                'conf_collo_num_mq': fields.float('Metri Quadri x Collo', digits=(10, 2)),
                'conf_collo_peso':fields.float('Peso x Collo', digits=(10, 2)),
                'conf_pallet_num_colli':fields.integer('Colli x Pallet'),
                'conf_pallet_num_mq':fields.float('Metri Quadri x Pallet', digits=(10, 2)),
                'categoria_prezzo':fields.char("Categoria Prezzo",size = 30),
                'prezzo_spallettizzato':fields.float('Prezzo Spallettizzato', digits=(16,2)),
                }

product_product()