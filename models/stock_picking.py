from odoo import api, fields, models, _


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def action_confirm(self):
        res = super(StockPicking, self).action_confirm()
        if self.sale_id.order_line:
            for data in self:
                for line in data.move_ids:
                    line.location_id = line.sale_line_id.delivery_location_id.id
        return res
