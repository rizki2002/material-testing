from odoo.tests import TransactionCase
from odoo.exceptions import ValidationError
import logging

_logger = logging.getLogger(__name__)

class TestMaterialModel(TransactionCase):

    def setUp(self):
        super(TestMaterialModel, self).setUp()
        self.supplier = self.env['supplier'].create({'name': 'Supplier 1'})

        Material = self.env['material']
        # Test case for valid buy price
        self.material = Material.create({
            'material_name': 'Valid Material',
            'material_code': 'VAL001',
            'material_type': 'fabric',
            'material_buy_price': 50,
            'supplier_id' : self.supplier.id
            # Testing validation with a valid price
        })
        _logger.info("Valid Material: %s", self.material.material_buy_price)
        # self.assertTrue(valid_material)

        # Test case for invalid buy price
        # with self.assertRaises(ValidationError):
        # self.material = Material.create({
        #     'material_name': 'Invalid Material',
        #     'material_code': 'INV001',
        #     'material_type': 'cotton',
        #     'material_buy_price': 50,
        #     'supplier_id' : self.supplier.id
        #     # Testing validation with a price less than 100
        # })
        # _logger.info("Invalid Material: %s", self.material)
            # self.assertTrue(invalid_material

    def test_material_update(self):
        new_buy_price = 200

        self.material.write({'material_buy_price': new_buy_price})
        updated_material = self.env['material'].browse(self.material.id)
        self.assertEqual(updated_material.material_buy_price, new_buy_price)
        _logger.info("update price: %s", new_buy_price)

    def test_material_delete(self):
        # with self.assertRaises(ValidationError):
        self.material.unlink()
        _logger.info("Delete Material")