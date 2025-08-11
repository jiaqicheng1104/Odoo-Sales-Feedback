from odoo import fields, api, models, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    feedback_ids = fields.One2many('sale.feedback', 'sale_order_id', string='All Feedbacks')
