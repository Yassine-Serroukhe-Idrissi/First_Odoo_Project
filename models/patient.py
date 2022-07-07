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
    def action_confirm(self):
        self.state = "confirm"

    def action_done(self):
        self.state = "done"

    def action_draft(self):
        self.state = "draft"

    def action_cancel(self):
        self.state = "cancel"

    def test_name(self):
        return

    @api.model
    def create(self, vals):
        if not vals.get('note'):
            vals['note'] = 'New Patient'
        if vals.get('reference', ('New')) == ('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.patient') or ('New')
        res = super(HospitalPatient,self).create(vals)
        return res