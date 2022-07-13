from odoo import models, fields,api


class ChangeStatus(models.TransientModel):
    _name = "change.status"
    _description = "Change Status"

    state = fields.Selection([('draft','Draft'),('confirm','Confirmed'),
                              ('done','Done'),('cancel','Cancelled')],default='draft', string="Status", tracking=True,track_visibility='onchange')

    def change_status_ac(self):
        self.env['hospital.patient'].browse(self._context.get("active_ids")).update({'state':self.state})
        return True





