# -*- coding: utf-8 -*-
from odoo import models, fields


class AccountMove(models.Model):

    _inherit = "account.move"

    def categ_exist(self, categ, dict_categ):
        return categ in dict_categ.keys()

    def get_parent_category(self, category):
        """This is a recursive function
        to find the parent of an category"""
        if not category.parent_id:
            return category
        else:
            return self.get_parent_category(category.parent_id)

    def get_lines_groupby_category(self):
        dict_categ = {}
        lines = self.invoice_line_ids.filtered(lambda x: not x.display_type)
        for line in lines:
            categ = self.get_parent_category(line.product_id.categ_id)
            result = self.categ_exist(categ.name, dict_categ)
            subtotal = line.price_subtotal
            if result:
                subtotal += dict_categ[categ.name]['subtotal']
            dict_categ[categ.name] = {
                'subtotal': round(subtotal, 2),
            }
        return dict_categ
