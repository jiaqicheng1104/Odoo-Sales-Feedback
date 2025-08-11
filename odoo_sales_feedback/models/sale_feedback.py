from odoo import models, fields, api


class SaleFeedback(models.Model):
    _name = 'sale.feedback'
    _description = 'Sales Feedback'

    name = fields.Char(string='Feedback Title', required=True)
    salesperson_id = fields.Many2one('res.users', string='Salesperson', related='sale_order_id.user_id', store=True, readonly=True)
    sale_order_id = fields.Many2one('sale.order', string='Sale Order', required=True, ondelete='cascade')
    rating = fields.Selection([
        ('1', '1 Star'), 
        ('2', '2 Stars'), 
        ('3', '3 Stars'), 
        ('4', '4 Stars'), 
        ('5', '5 Stars')
    ], string='Rating', required=True)
    comment = fields.Text(string='Comment')
    feedback_date = fields.Datetime(string='Feedback Date', default=fields.Datetime.now)
