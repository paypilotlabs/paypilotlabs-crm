frappe.listview_settings["CRM Product"] = {
  onload(listview) {
    listview.page.set_primary_action(__("Add CRM Product"), () => {
      frappe.new_doc("CRM Product");
    });
  },
};
