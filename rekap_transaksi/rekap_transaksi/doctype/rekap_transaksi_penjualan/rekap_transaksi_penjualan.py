# -*- coding: utf-8 -*-
# Copyright (c) 2018, setyo and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

# from frappe import throw, _
# from frappe.utils import cstr

from frappe.model.document import Document
# from jinja2 import TemplateSyntaxError
# from frappe.utils.user import is_website_user
# from frappe.model.naming import make_autoname
# from frappe.core.doctype.dynamic_link.dynamic_link import deduplicate_dynamic_links
# from six import iteritems, string_types
#
# from frappe.website.website_generator import WebsiteGenerator

class RekapTransaksiPenjualan(Document):
	pass

# class RekapTransaksiPenjualan(WebsiteGenerator):
# 	pass

# def get_list_context(context=None):
# 	return {
# 		"title": _("Rekap Transaksi Penjualan"),
# 		"get_list": get_rekap_transaksi_penjualan_list,
# 		"row_template": "templates/includes/rekap_transaksi_penjualan_row.html",
# 		'no_breadcrumbs': True,
# 	}

# def get_rekap_transaksi_penjualan_list(doctype, txt, filters, limit_start, limit_page_length = 20, order_by = None):
#     from frappe.www.list import get_list
#     user = frappe.session.user
#     ignore_permissions = False
#
#     return get_list(doctype, txt, filters, limit_start, limit_page_length, ignore_permissions=ignore_permissions)
