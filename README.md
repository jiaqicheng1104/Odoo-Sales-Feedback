# Odoo Sales Feedback

## Overview
The **Sales Feedback** module allows customers to submit feedback for sales orders directly from the Odoo customer portal.  
Feedback includes a star rating (1–5) and optional comments, which are linked to both the sales order and the responsible salesperson.  
Managers can view aggregated ratings and generate reports to monitor performance.

## Key Features
- **Portal Feedback Submission**
  - Customers can submit ratings and comments for sales orders from the portal.
  - Feedback form is only shown if no feedback exists for the order.
  - Input sanitization to prevent injection attacks.
  
- **Backend Integration**
  - Feedback records linked to related sales orders and salespersons.
  - Feedback list displayed in internal sales order form view.
  - Read-only display of feedback for submitted orders in the portal.

- **Reporting**
  - Bar chart view showing **average feedback rating per salesperson**.
  - Tree/list view for detailed feedback analysis.
  - Default sorting by most recent feedback.

## Technical Details
- **Models**
  - `sale.feedback`: Stores rating, comment, linked sales order, and feedback date.
  - `sale.order`: One-to-one relationship to feedback record via `feedback_ids`.

- **Security**
  - Portal authentication required for feedback submission.
  - CSRF token validation enabled for POST requests.
  - Input data sanitized before saving.

- **Views**
  - Portal: Feedback form and submitted feedback display.
  - Backend: Tree, form, and graph views for feedback data.

## Installation
Requires Odoo 18.0 Community Edition.

Place the module inside your custom_modules folder.

Update the Odoo start parameters:

--addons-path=addons,../custom_modules

Restart Odoo, update the apps list, and install Sales Feedback.
