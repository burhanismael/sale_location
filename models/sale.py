from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = 'sale.order.line'

    delivery_location_id = fields.Many2one('stock.location', string='Location')

