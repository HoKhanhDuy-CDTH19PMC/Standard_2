from odoo import models, fields


class Common(models.Model):
    _name = 'standard.common'
    _description = 'Common'
    _order = 'name'
    _sql_constraints = [
        ('unique_common_code', 'unique(code)', "Duplicated Common Code"),]

    code = fields.Char('code', required=True, index=True)
    name = fields.Char('name', required=True, index=True)
    detail = fields.One2many(
        'standard.common.detail', 'master', required=True, index=True)


class CommonDetail(models.Model):
    _name = 'standard.common.detail'
    _description = 'CommonDetail'
    _order = 'code'
    _sql_constraints = [('unique_commondetail_code',
                         'unique(code, master)', "Duplicated Detail Code"),]

    code = fields.Char('code', required=True, index=True)
    name = fields.Char('name', required=True, index=True)
    master = fields.Many2one('standard.common',
                             'master', required=True, index=True)
