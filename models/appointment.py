from odoo import models,fields

class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _description = "Patient Appointment"

    name = fields.Char(sting="Name", required=True)
    appointment_date = fields.Datetime(string="Date")
    doctor = fields.Many2one('hospital.doctor', string="Doctor")
    patient = fields.Many2one('hospital.patient',string="Patient")

