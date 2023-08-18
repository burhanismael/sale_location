from odoo import api, fields, models, _


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def action_confirm(self):
        res = super(StockPicking, self).action_confirm()
        if self.sale_id:
            self.location_id = self.sale_id.delivery_location_id
        return res