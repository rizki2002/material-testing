# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class testprogram(models.Model):
#     _name = 'testprogram.testprogram'
#     _description = 'testprogram.testprogram'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
from odoo.exceptions import ValidationError

from odoo import api, fields, models

class Material(models.Model):

    _name = 'material'
    _description = 'Material'

    material_code = fields.Char(string='Material Code', required=True)
    material_name = fields.Char(string='Material Name', required=True)
    material_type = fields.Selection([
        ('fabric', 'Fabric'),
        ('jeans', 'Jeans'),
        ('cotton', 'Cotton')
    ], string='Material Type', required=True)
    material_buy_price = fields.Float(string='Material Buy Price', required=True)
    supplier_id = fields.Many2one(comodel_name="supplier", string="", required=True, )



    @api.constrains('material_buy_price')
    def _check_buy_price(self):
        for record in self:
            if record.material_buy_price < 100:
                raise ValidationError('Material Buy Price must be greater than or equal to 100.')

    # supplier_id = fields.Many2one('testprogram.supplier', string='Related Supplier', required=True)
