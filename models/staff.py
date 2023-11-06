from odoo import models, fields, api


class Staff(models.Model):
    _inherit = 'hr.employee'
    _sql_constraints = [
        ('unique_code', 'unique(code)', "Duplicated Code"),]

    code = fields.Char(string='Code', required=True)
