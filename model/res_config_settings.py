from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    responsible_person = fields.Many2one(string="Responsible Person", comodel_name="res.partner",
                                          config_parameter='ramiz_29022024.responsible_person')



