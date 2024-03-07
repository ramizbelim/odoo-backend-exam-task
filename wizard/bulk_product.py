from odoo import models, fields

class QuotationBulkUpload(models.TransientModel):
    _name = 'bulk.upload'

    bulk_product_id = fields.Many2one('quotation.bulk.upload')
    product_ids = fields.Many2many('product.product',string="Product")
    quantity = fields.Float(string="Quantity", default=1)
