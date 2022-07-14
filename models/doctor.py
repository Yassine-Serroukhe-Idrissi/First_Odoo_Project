from odoo import models,fields,api

class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Doctor"

    name = fields.Char(string='Name', required=True)
    specialite = fields.Selection([("genraliste","Generaliste"),("pediatre","Pediatre"),("chirurgien","Chirurgien"),
                                   ("ophtalmologue","Ophtalmologue"),("dermatologues","Dermatologue")],
                                  default='generaliste', string="Specialite", tracking=True)

    appointment_count = fields.Integer(string='Appointment', compute='get_appointment_count')

    def get_appointment_count(self):
        count = self.env['hospital.appointment'].search_count([('doctor', '=', self.id)])
        self.appointment_count = count

