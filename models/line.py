# -*- coding: utf-8 -*-
from odoo import models, fields


class Line(models.Model):
    _name = 'standard.line'
    _description = 'Line'
    _order = 'name'
    _sql_constraints = [
        ('unique_line_code', 'unique(name)', "Duplicated Line Name"),]

    name = fields.Char('Line Name', required=True)
    description = fields.Char('Description')
    location_name = fields.Many2one('stock.location', 'Area', required=True)
