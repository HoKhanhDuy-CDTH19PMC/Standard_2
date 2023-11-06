from odoo import models, fields


class Mold(models.Model):
    _name = 'standard.mold'
    _description = 'Mold'
    _order = 'mold_serial'
    _sql_constraints = [
        ('unique_mold_code', 'unique(mold_serial)', "Duplicated Mold Serial"),]

    name = fields.Char('Mold Name', required=True)
    mold_serial = fields.Char('Mold Serial', required=True, index=True)
    product = fields.Many2many('product.product', required=True, index=True)
    # model = fields.Char('Model', compute='compute_string')
    # Model = fields.Char('Model')
    line_type = fields.Many2many('standard.common.detail', required=True, index=True, domain=[
                                 ('master.code', '=', 'LineType')])
    check_form = fields.Char(
        'Check Form', required=True)  # select QC Form Mold
    mold_type = fields.Selection(
        [('1', 'Khuôn tròn'), ('0', 'Khuôn bằng')], string='Mold Type', required=True)
    production_date = fields.Datetime('Production Date', required=True)
    supplier = fields.Many2one(
        'res.partner', 'Supplier Name', required=True, index=True)
    mold_status = fields.Selection(
        [('0', 'NOT YET CHECK'), ('1', 'STOCK'), ('2', 'USING'), ('3', 'HOLD'), ('4', 'NG'), ('5', 'SCRAP')], string='Mold Status', required=True, multiple=True)
    max_number = fields.Integer('Max Number', required=True)
    current_number = fields.Integer('Current Number', required=True)
    period_number = fields.Integer('Period Number', required=True)
    remark = fields.Char('Remark')

    # def compute_string(self):
    #     b = ''
    #     for mold in self:
    #         for product in mold.product:
    #             if b != '':
    #                 b += ', '
    #             b += str(product.model.name)
    #     mold.model = b
