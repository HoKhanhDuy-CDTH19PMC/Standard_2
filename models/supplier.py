from odoo import models, fields, api


class Supplier(models.Model):
    _inherit = 'res.partner'
    _sql_constraints = [
        ('uniquer_code', 'unique(code)', "Duplicated Code"),]

    code = fields.Char(string='Code', required=True)
