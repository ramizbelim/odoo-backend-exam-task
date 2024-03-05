from odoo import models, fields, api
from odoo.fields import Command
from odoo.exceptions import ValidationError


class QuotationBulkUpload(models.TransientModel):
    _name = 'quotation.bulk.upload'

    product_bulk_ids = fields.Many2many('bulk.upload', string="Product")


    @api.constrains('product_bulk_ids.quantity')
    def upload_products(self):
        sale_order_id = self.env["sale.order"].browse(self.env.context.get('active_id'))
        for rec in self.product_bulk_ids:
            for prod_id in rec.product_ids:
                if rec.quantity == 0.0:
                    raise ValidationError("Quantity is zero not allowed")
                sale_order_id.sudo().update({
                    # 'order_line': [(fields.Command.create(values))]
                    'order_line': [
                        Command.create({
                            'product_id': prod_id.id,
                            'product_uom_qty': rec.quantity
                        })]
                })
