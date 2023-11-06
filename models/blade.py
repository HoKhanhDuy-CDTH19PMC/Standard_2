from odoo import models, fields


class Blade(models.Model):
    _name = 'standard.blade'
    _description = 'Blade'
    _order = 'name'
    _sql_constraints = [
        ('unique_blade_code', 'unique(blade_serial)', "Duplicated Blade Serial"),]

    name = fields.Char('name', required=True)
    blade_serial = fields.Char('Blade Serial', required=True, index=True)
    supplier = fields.Many2one(
        'res.partner', 'Supplier Name', required=True, index=True)
    check_form = fields.Char(
        'Check Form', required=True)  # select QC Form Mold
    import_date = fields.Datetime('Import Date', required=True)
    export_date = fields.Datetime('Export Date', required=True)
    line = fields.Many2one('standard.line',
                           'line', required=True, index=True)
    blade_status = fields.Selection(
        [('0', 'NOT YET CHECK'), ('1', 'STOCK'), ('2', 'USING'), ('3', 'HOLD'), ('4', 'NG'), ('5', 'SCRAP')], string='Blade Status', required=True, multiple=True)
    expire_number = fields.Integer('Expire Number', required=True)
    current_number = fields.Integer('Current Number', required=True)
    periodic_check = fields.Integer('Periodic Check', required=True)
    description = fields.Char('Description')
