from odoo import api, models, fields


class ResUsers(models.Model):
    _inherit = 'res.users'

    feedback_ids = fields.One2many('sale.feedback', 'salesperson_id', string='All Feedbacks')
    average_rating = fields.Float(string='Average Rating', compute='_compute_average_rating', store=True)

    @api.depends('feedback_ids')
    def _compute_average_rating(self):
        for user in self:
            ratings = user.feedback_ids.mapped('rating')
            if ratings:
                user.average_rating = sum(int(r) for r in ratings) / len(ratings)
            else:
                user.average_rating = 0.0
