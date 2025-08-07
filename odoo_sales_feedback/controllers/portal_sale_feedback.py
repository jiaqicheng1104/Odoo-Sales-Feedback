import werkzeug

from odoo import http
from odoo.http import request

from odoo.addons.sale.controllers.portal import CustomerPortal

class PortalSalesFeedback(CustomerPortal):

    @http.route(['/my/orders/<int:order_id>/feedback'], type='http', auth="user", website=True)
    def portal_feedback_form(self, order_id, **kwargs):
        order = request.env['sale.order'].sudo().browse(order_id)
        return request.render("odoo_sales_feedback.portal_feedback_form", {
            'order': order,
        })

    @http.route(['/my/orders/<int:order_id>/submit_feedback'], type='http', auth="user", website=True, methods=['POST'], csrf=True)
    def portal_feedback_submit(self, order_id, **post):
        print("Controller HIT!")

        return request.redirect(('/my/orders/%s' % order_id))
