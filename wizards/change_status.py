from odoo import models, fields,api


class ChangeStatus(models.TransientModel):
    _name = "change.status"
    _inherit = "hospital.patient"
    _description = "Change Status"

    id = fields.Many2one("hospital.patient",string='id')
    status = fields.Many2one("hospital.patient.state", string='Status')

    @api.multi
    def change_status_ac(self):
        st = self.env['hospital.patient'].browse(self._context.get('active_ids'))
        for s in st:
            s.state = "done"




