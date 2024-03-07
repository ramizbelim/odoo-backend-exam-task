from odoo import models, api


class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        res = super()._name_search(name, args, operator, limit=limit, name_get_uid=None)
        args = args or []
        domain = []
        if self.env.context.get('check_condition'):
            domain = args + ['|', ('name', operator, name), ('barcode', operator, name)]
            return self._search(args + domain, limit=limit, access_rights_uid=name_get_uid)
        else:
            return res
