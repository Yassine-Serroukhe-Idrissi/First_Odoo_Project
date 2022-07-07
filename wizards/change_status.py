from odoo import models, fields

class ChangeStatus(models.TransientModel):
    _name = "change.status"
    _description = "Change Status"

    status = fields.Many2one("hospital.patient.state", string='Status')

    def action_confirm(self):
        self.status = "confirm"

    def action_done(self):
        self.status = "done"

    def action_draft(self):
        self.status = "draft"

    def action_cancel(self):
        self.status = "cancel"



