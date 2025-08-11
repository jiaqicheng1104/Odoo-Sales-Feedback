import werkzeug

from odoo import http
from odoo.http import request

from odoo.addons.sale.controllers.portal import CustomerPortal


class PortalSalesFeedback(CustomerPortal):

    @http.route(['/my/orders/<int:order_id>/submit_feedback'], type='http', auth="user", website=True, methods=['POST'], csrf=True)
    def portal_feedback_submit(self, order_id, **post):
        print("Submitting feedback for order:", order_id, post)
        try:

            feedback = request.env['sale.feedback'].sudo().search([('sale_order_id', '=', order_id)])
            print(feedback)
            rating = int(post.get('rating')) if 1 <= int(post.get('rating', 0)) <= 5 else None
            # Odoo ORM layer prevents SQL injection, so we can safely use post.get()
            comment = post.get('comment')
            print(feedback, order_id, rating, comment)
            if order_id and rating and comment and not feedback:
                feedback = request.env['sale.feedback'].sudo().create({
                    'name': 'Feedback for Sale Order %s' % order_id,
                    'sale_order_id': order_id,
                    'rating': str(rating),
                    'comment': str(comment),
                })
        except Exception as e:
            no_exception = ""

        return request.redirect(('/my/orders/%s' % order_id))
