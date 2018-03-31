# -*- coding: utf-8 -*-
import top.api

def dayu_tt(number,sms_code): 
    req = top.api.AlibabaAliqinFcSmsNumSendRequest("gw.api.taobao.com",80)
    req.set_app_info(top.appinfo("23906242","836694ae369bb4d5b6091b48e0f383c2"))
 
    req.extend = ""
    req.sms_type = "normal"
    req.sms_free_sign_name = "实验室报警系统"
    req.sms_param = ""
    req.rec_num = number
    req.sms_template_code = sms_code
    try :
         resp = req.getResponse()
         print (resp)
    except Exception,e:
         print (e)

#dayu_tt("18256021703","SMS_70185251")
