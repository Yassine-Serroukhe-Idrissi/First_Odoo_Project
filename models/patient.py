from odoo import models, fields, api

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital patient"

    name = fields.Char(string='Name', required=True)
    reference = fields.Char(string='Order Reference', required=True, copy = False, readonly = True,
                            default=lambda self: ('New'))
    age = fields.Integer(string='Age', tracking=True)
    gender = fields.Selection([
        ('male','Male'),
        ('female','Female'),
        ('other','Other'),
    ], required=True, default='male', tracking=True)
    note = fields.Text(string='Description')
    state = fields.Selection([('draft','Draft'),('confirm','Confirmed'),
                              ('done','Done'),('cancel','Cancelled')],default='draft', string="Status", tracking=True)
    image = fields.Binary("Image",help="select image")
    doctor = fields.Many2one('hospital.doctor',string="Doctor")
    #appointment_count = fields.Integer(string='Appointment', compute='get_appointment_count')

    """def action_confirm(self):
        self.state = "confirm"

    def action_done(self):
        self.state = "done"

    def action_draft(self):
        self.state = "draft"

    def action_cancel(self):
        self.state = "cancel"

    def test_name(self):
        return"""

    def print_info(self):
        return self.env.ref('om_hospital.report_patient_cards').report_action(self)


    @api.model
    def create(self, vals):
        if not vals.get('note'):
            vals['note'] = 'New Patient'
        if vals.get('reference', ('New')) == ('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.patient') or ('New')
        res = super(HospitalPatient,self).create(vals)
        return res

    """def get_appointment_count(self):
        count = self.env['hospital.appointment'].search_count([('patient', '=', self.id)])
        self.appointment_count = count"""

