import pytest

from api.address import Address


class TestAddress:
    def setup(self):
        self.address=Address()

    @pytest.mark.parametrize("userid,mobile",[("wangzi01","12112345678"),
                                              ("wangzi02", "12112345679"),
                                              ("wangzi03", "12112345677")
                                              ]
                             )
    def test_add_member(self,userid,mobile):
        name = "今天早下班"
        department =[2]
        r = self.address.delete_member(userid)
        print(r)
        r = self.address.add_member(userid=userid,name=name,mobile=mobile,department=department)
        print(r)
        r = self.address.get_member(userid)
        print(r)
        assert r.get("name","userid 添加失败") == name