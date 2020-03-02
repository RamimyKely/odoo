# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    many2one_limit_param = fields.Integer(string='Many2one item limit')

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res.update(
            many2one_limit_param=int(self.env['ir.config_parameter'].sudo().get_param('many2one.limit')),
        )
        return res

    @api.multi
    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('many2one.limit', self.many2one_limit_param)
