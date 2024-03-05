from odoo import models,api


class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        domain = []
        if name:
            domain = args + ['|',('name', operator, name),('barcode',operator,name)]
        return self._search(domain + args, limit=limit, access_rights_uid=name_get_uid)




