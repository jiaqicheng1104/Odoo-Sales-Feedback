# -*- coding: utf-8 -*-
{
    'name': 'Sales Feedback Management',
    'version': '1.0.0',
    'summary': 'End-to-end sales feedback system for Odoo with ratings, reviews, analytics, and portal integration.',
    'description': """
A production-ready Odoo module to collect, manage, and analyze sales feedback on sales orders.

🎯 Key Features:
- Sales reviews with star ratings and comments
- Portal page for secure feedback submission
- Automatic email invitations after order delivery
- Admin dashboard with list, kanban, graph, and calendar views
- Linked to products, customers, and sales orders
- Access control for public, portal, and internal users

Built for the Odoo Community 18.0 framework.
Use this module to track customer satisfaction, reduce churn, and empower your sales team with actionable insights.
    """,
    'author': 'Jiaqi Cheng',
    'website': 'https://github.com/jiaqicheng1104/Odoo-Sales-Feedback',
    'category': 'Sales',
    'version': '1.0.0',
    'application': False,
    'installable': True,
    'depends': [
        'website_sale',
        'sale_management',
        'portal',
        'mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_feedback_views.xml',
        'views/portal_sale_feedback_templates.xml',
    ],
}
