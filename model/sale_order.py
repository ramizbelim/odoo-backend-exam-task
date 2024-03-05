from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    check_line_sol = fields.Boolean(compute='_compute_check_line', store=True)

    @api.depends('order_line')
    def _compute_check_line(self):
        for order in self.order_line:
            line_count = self.order_line.filtered(lambda line: line.product_id.id == order.product_id.id)
            if len(line_count.ids) > 1:
                 self.check_line_sol = True
            else:
                self.check_line_sol = False
    def order_line_merge(self):
        line_id = []
        uniq_id = []
        for order in self.order_line:
            line_count = self.order_line.filtered(lambda line: line.product_id.id == order.product_id.id)
            if len(line_count.ids) > 1:
                if line_count not in line_id:
                    line_id.append(line_count)
                    qty = 0
                    for rec in line_id:
                        qty = sum(res.product_uom_qty for res in rec)
                    line_count[0].update({
                        'product_uom_qty': qty
                    })
                    uniq_id.append(line_count[0].id)
        message = []
        for rec in line_id:
            for wo in rec.ids:
                if wo not in uniq_id:
                    product = self.env['sale.order.line'].browse(wo)
                    body = f"This {product.name} quantity {product.product_uom_qty} has been Merge"
                    message.append(body)
                    self.send_mail_merge_notificaton()
                    product.unlink()
        self.message_post(body="\n".join(message))

    def send_mail_merge_notificaton(self):
        mail_template = self.env.ref('ramiz_29022024.merge_notification_mail_template')
        responsible_person_id = int(self.env['ir.config_parameter'].get_param('ramiz_29022024.responsible_person'))
        values = [self.env['res.partner'].browse(responsible_person_id).email, self.partner_id.email]
        mail_template.send_mail(self.id, force_send=True, email_values=dict(email_to=values))

