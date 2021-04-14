import requests,json,math

class Wufachuli():
    def __init__(self):
        #请求头信息
        self.her = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Content-Type": "application/json;charset=UTF-8"

        }
    def login(self):
        #登录链接
        url = "http://9.23.66.143:8759/api/user/saveRoleUsed"

        d = {"userId": 1, "roleType": 6}
        d = json.dumps(d)
        self.r = requests.session()
        rd = self.r.post(url= url,data=d,headers = self.her)
        return rd
    def tijiao(self):
        url2 = "http://9.23.66.143:8759/api//openApi/common/manage/errorCrrectionForTag"
        d2 = {
            "id": self.id,
            "errorTxt": "",
            "rightTxt": "",
            "signTxt": "无法处理"
        }
        rd2 = self.r.post(url=url2, json=d2, headers=self.her)
        print(rd2.json())
    def biaozhu(self):
        #录音标注链接
        self.login()
        url1 = "http://9.23.66.143:8759/api/openApi/common/manage/queryTagList"
        d1 = {
            "pageSize":30,
            "pageNum":1,
            "startTime":"2021-03-31",   #开始时间
            "signTxt":"",
            "endTime":"2021-03-31",     #结束时间
            "policyNo":"",
            "qualityInspectionLabel":"",
            "signName":"",
            "businessType":"",
            "qualityTypeId":"",
            "branchCompanyCode":""
        }
        rd1 = self.r.post(url= url1,json = d1,headers = self.her)
        j = rd1.json()
        total = j["data"]["total"] #提取该天的总数据值
        # print(total)
        e = math.ceil(total/30)   #按照每页30条，向上取整
        # print(e)
        for m in range(13,e+1):
            d1 = {
                "pageSize": 30,
                "pageNum": m,
                "startTime": "2021-04-02",  # 开始时间
                "signTxt": "",
                "endTime": "2021-04-02",  # 结束时间
                "policyNo": "",
                "qualityInspectionLabel": "",
                "signName": "",
                "businessType": "",
                "qualityTypeId": "",
                "branchCompanyCode": ""
            }
            rd12 = self.r.post(url=url1, json=d1, headers=self.her)
            j = rd12.json()
            try:
                for i in range(0,30):
                    a = j["data"]["list"][i]   #获取每一单录音的数据
                    # global id
                    self.id = a["id"]
                    zj_name = a["qualityCheckNape"]   #质检项名称
                    c = a["remark"]             #录音备注
                    z = a["qualityInspectionLabel"]   #质检标签
                    yw_type = a["businessTypeName"]    #业务类型
                    if c != None or "结束语" in zj_name or "其他需备注告知项" in zj_name or "语音识别丢失句子" in z or "说话人识别错误" in z or "咨询类" in yw_type:
                        #提交操作
                        self.tijiao()
            except Exception as msg:
                print(msg)
if __name__ == '__main__':
    a = Wufachuli()
    a.biaozhu()











