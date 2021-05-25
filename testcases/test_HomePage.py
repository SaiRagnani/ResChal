from io import StringIO
from pageobjects.HomePage import HomePage
import sys
import time
class Test_HomePage:

    temp_out = StringIO()
    sys.stdout = temp_out
    name = "raghav"
    city = "hyderabad"

    # test1
    def test_modaldetails(self,setup):
        self.driver=setup
        hp=HomePage(self.driver)
        hp.getframe()
        hp.modalclick()
        hp.entername(self.name)
        hp.entercity(self.city)
        hp.save()
        self.driver=hp.closebutton()
        assert self.name==hp.getnamevalue() and self.city==hp.getcityvalue()


    #test2
    def test_combobox(self,setup):
        self.driver = setup
        hp=HomePage(self.driver)
        hp.clickmebutton()
        # to check the list for Angular
        enteredvalues = hp.enterfiltertext("Angular")
        for val in enteredvalues:
            assert "Angular" or "Angular2" in val.text
        hp.filterclear()
        time.sleep(1)
        #to check the list for reactjs
        num=len(hp.enterfiltertext("ReactJs"))
        assert num==0
        #
        # self.temp_out.write("nothing")
        # sys.stdout = sys.__stdout__
        # sys.stdout.write(self.temp_out.getvalue())

    # test3
    def test_SearchTable(self,setup):
        self.driver = setup
        hp = HomePage(self.driver)
        # to check the table for USA records
        hp.entersearchtext("USA")
        time.sleep(1)
        rows=len(hp.getnamerows())
        assert rows==2
        hp.searchclear()
        # to check table has four rows
        allrows=len(hp.getallrows())
        assert allrows==4

    # test4
    def test_dragelement(self,setup):
        self.driver = setup
        hp = HomePage(self.driver)
        time.sleep(2)
        hp.draganddrop()



