from odoo import api, fields, models


class Supllier(models.Model):
    _name = 'supplier'
    _description = 'Supplier'

    name = fields.Char(string='Supplier Name', required=True)


