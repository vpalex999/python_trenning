# -*- coding: utf-8 -*-

from model.address import Address

class AddressHelper(object):

    def __init__(self, app):
        self.app = app

    def new_address_page(self):
        """Open new address page"""
        wd = self.app.wd
        if not(wd.current_url.endswith("/edit.php")):
            wd.find_element_by_link_text("add new").click()

    def del_first_address(self):
        """Delete first contact"""
        self.del_address_by_index(0)

    def del_address_by_index(self, index):
        """Delete first contact"""
        wd = self.app.wd
        self.return_home_page()
        wd.find_elements_by_name("selected[]")[index].click()
        # submit deletions
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.address_chace = None

    def return_home_page(self):
        """Return home page"""
        wd = self.app.wd
        if not(wd.current_url.endswith("/addressbook/") and wd.find_element_by_name("searchstring")):
            wd.find_element_by_link_text("home").click()

    def create(self, addr):
        """Create new address"""
        wd = self.app.wd
        self.new_address_page()
        self.input_fields(addr)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.address_chace = None

    def update_first_address(self, addr):
        """Update firs address"""
        self.update_address_by_index(addr, 0)

    def update_address_by_index(self, addr, index):
        """Update firs address"""
        wd = self.app.wd
        self.return_home_page()
        wd.find_elements_by_name("entry")[index].find_element_by_xpath("td[8]/a/img").click()
        self.input_fields(addr)
        # submit Update
        wd.find_element_by_name("update").click()
        self.address_chace = None

    def input_fields(self, addr):
        """Input fields for address"""
        wd = self.app.wd
        if addr.name is not None:
            wd.find_element_by_name("firstname").click()
            wd.find_element_by_name("firstname").clear()
            wd.find_element_by_name("firstname").send_keys(addr.name)
        if addr.mname is not None:
            wd.find_element_by_name("middlename").click()
            wd.find_element_by_name("middlename").clear()
            wd.find_element_by_name("middlename").send_keys(addr.mname)
        if addr.lname is not None:
            wd.find_element_by_name("lastname").click()
            wd.find_element_by_name("lastname").clear()
            wd.find_element_by_name("lastname").send_keys(addr.lname)
        if addr.nickname is not None:
            wd.find_element_by_name("nickname").click()
            wd.find_element_by_name("nickname").clear()
            wd.find_element_by_name("nickname").send_keys(addr.nickname)
        if addr.title is not None:
            wd.find_element_by_name("title").click()
            wd.find_element_by_name("title").clear()
            wd.find_element_by_name("title").send_keys(addr.title)
        if addr.company is not None:
            wd.find_element_by_name("company").click()
            wd.find_element_by_name("company").clear()
            wd.find_element_by_name("company").send_keys(addr.company)
        if addr.address is not None:
            wd.find_element_by_name("address").click()
            wd.find_element_by_name("address").clear()
            wd.find_element_by_name("address").send_keys(addr.address)
        if addr.phone is not None:
            wd.find_element_by_name("home").click()
            wd.find_element_by_name("home").clear()
            wd.find_element_by_name("home").send_keys(addr.phone)
        if addr.mobile is not None:
            wd.find_element_by_name("mobile").click()
            wd.find_element_by_name("mobile").clear()
            wd.find_element_by_name("mobile").send_keys(addr.mobile)
        if addr.workphone is not None:
            wd.find_element_by_name("work").click()
            wd.find_element_by_name("work").clear()
            wd.find_element_by_name("work").send_keys(addr.workphone)
        if addr.fax is not None:
            wd.find_element_by_name("fax").click()
            wd.find_element_by_name("fax").clear()
            wd.find_element_by_name("fax").send_keys(addr.fax)
        if addr.email is not None:
            wd.find_element_by_name("email").click()
            wd.find_element_by_name("email").clear()
            wd.find_element_by_name("email").send_keys(addr.email)
        if addr.email2 is not None:
            wd.find_element_by_name("email2").click()
            wd.find_element_by_name("email2").clear()
            wd.find_element_by_name("email2").send_keys(addr.email2)
        if addr.email3 is not None:
            wd.find_element_by_name("email3").click()
            wd.find_element_by_name("email3").clear()
            wd.find_element_by_name("email3").send_keys(addr.email3)
        if addr.homepage is not None:
            wd.find_element_by_name("homepage").click()
            wd.find_element_by_name("homepage").clear()
            wd.find_element_by_name("homepage").send_keys(addr.homepage)
        # Birthday
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[16]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[16]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[4]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[4]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1991")
        # Anniversary
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[6]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[6]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[3]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[3]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("2017")
        # select Group
        # if not wd.find_element_by_xpath("//div[@id='content']/form/select[5]//option[1]").is_selected():
        #     wd.find_element_by_xpath("//div[@id='content']/form/select[5]//option[1]").click()
        # Secondary
        if addr.address2 is not None:
            wd.find_element_by_name("address2").click()
            wd.find_element_by_name("address2").clear()
            wd.find_element_by_name("address2").send_keys(addr.address2)
        if addr.phone2 is not None:
            wd.find_element_by_name("phone2").click()
            wd.find_element_by_name("phone2").clear()
            wd.find_element_by_name("phone2").send_keys(addr.phone2)
        if addr.notes is not None:
            wd.find_element_by_name("notes").click()
            wd.find_element_by_name("notes").clear()
            wd.find_element_by_name("notes").send_keys(addr.notes)

    def count(self):
        """Check count address"""
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    address_chace = None

    def get_addresses_list(self):
        """Great list with addresses"""
        if self.address_chace is None:
            wd = self.app.wd
            self.return_home_page()
            self.address_chace = []
            for element in wd.find_elements_by_name("entry"):
                td = element.find_elements_by_tag_name("td")
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.address_chace.append(Address(name=td[2].text, lname=td[1].text, id=id))
        return list(self.address_chace)





