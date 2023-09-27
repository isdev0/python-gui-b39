from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app
        self.group_editor = None

    def open_group_editor(self):
        self.app.main_window.window(auto_id="groupButton").click()
        self.group_editor = self.app.application.window(title="Group editor")
        self.group_editor.wait("visible")

    def close_group_editor(self):
        self.group_editor.close()

    def create(self, group):
        self.open_group_editor()

        self.group_editor.window(auto_id="uxNewAddressButton").click()
        input = self.group_editor.window(class_name="Edit")
        input.set_text(group.name)
        input.type_keys("\n")

        self.close_group_editor()

    def get_all(self):
        self.open_group_editor()

        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        groups_list = [Group(node.text()) for node in root.children()]

        self.close_group_editor()
        return groups_list

    def delete_by_name(self, name):
        self.open_group_editor()

        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        for children in root.children():
            if children.text() == name:
                children.click()
                self.group_editor.window(auto_id="uxDeleteAddressButton").click()
                group_deleting = self.app.application.window(title="Delete group")
                group_deleting.wait("visible")
                group_deleting.window(auto_id="uxDeleteAllRadioButton").click()
                group_deleting.window(auto_id="uxOKAddressButton").click()


