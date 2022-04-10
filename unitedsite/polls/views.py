import random

from django.http import HttpResponse
from django.shortcuts import render

from .models import Businessinfo
from .models import Userinfo


# Create your views here.

def toLogin_view(request):
    return render(request, "login.html")


def login_view(request):
    u = request.POST.get("user", "")
    p = request.POST.get("pwd", "")
    if u and p:
        c = Userinfo.objects.filter(user_name=u, user_pwd=p).count()
        if c == 1:
            businessinfos = Businessinfo.objects.order_by('idbusinessinfo')
            return render(request, "main.html", {"businessLists": businessinfos})
        else:
            return HttpResponse("用户名或密码错误")
    else:
        return HttpResponse("请输入用户名和密码")


def toregister_view(request):
    return render(request, "registry.html")


def register_view(request):
    u = request.POST.get("user", "")
    p = request.POST.get("pwd", "")
    if u and p:
        user = Userinfo(id=str(random.randrange(0000, 9999)), user_name=u, user_pwd=p)
        user.save()
        return HttpResponse("注册成功")
    else:
        return HttpResponse("请输入用户名和密码")


def main_view(request):
    businessinfos = Businessinfo.objects.order_by('idbusinessinfo')
    return render(request, "main.html", {"businessLists": businessinfos})

def new_business(request):
    userSelectUID= request.POST.get("userSelectBID", "")
    if userSelectUID == "": #新建
        return render(request, "newbusiness.html")
    else: # 修改
        businessinfo = Businessinfo.objects.get(idbusinessinfo=userSelectUID)
        return render(request, "modbusiness.html", {"businessinfo": businessinfo})

def savebusiness(request):
    idbusinessinfo = request.POST.get("idbusinessinfo", "")
    clientname = request.POST.get("clientname", "")
    week = request.POST.get("week", "")
    estimated_load_date = request.POST.get("estimated_load_date", None)
    if estimated_load_date=="":
        estimated_load_date=None
    pre_etd = request.POST.get("pre_etd", None)
    if pre_etd=="":
        pre_etd=None
    etd = request.POST.get("etd", None)
    if etd == "":
        etd = None
    eta = request.POST.get("eta", None)
    if eta == "":
        eta = None
    vessel_voyage = request.POST.get("vessel_voyage", "")
    pol = request.POST.get("pol", "")
    pod = request.POST.get("pod", "")
    businessinfocol = request.POST.get("businessinfocol", "")
    numctrs = request.POST.get("numctrs", "")
    type_ctrs = request.POST.get("type_ctrs", "")
    booking_no = request.POST.get("booking_no", "")
    master_no = request.POST.get("master_no", "")
    num_hbls = request.POST.get("num_hbls", None)
    if num_hbls == "":
        num_hbls = None
    container_no = request.POST.get("container_no", "")
    shipping_line = request.POST.get("shipping_line", "")
    freeddday = request.POST.get("freeddday", None)
    cost_org = request.POST.get("cost_org", None)
    if cost_org == "":
        cost_org = None
    sale_org = request.POST.get("sale_org", None)
    if sale_org == "":
        sale_org = None
    set_org = request.POST.get("set_org", None)
    if set_org == "":
        set_org = None
    local_org = request.POST.get("local_org", None)
    if local_org == "":
        local_org = None
    venta_dest = request.POST.get("venta_dest", None)
    if venta_dest == "":
        venta_dest = None
    costhbl_dest_description = request.POST.get("costhbl_dest_description", "")
    costhbl_dest = request.POST.get("costhbl_dest", None)
    if costhbl_dest == "":
        costhbl_dest = None
    costhbl_dest_status = request.POST.get("costhbl_dest_status", "NOT")
    topaid_org_description = request.POST.get("topaid_org_description", "")
    topaid_org = request.POST.get("topaid_org", None)
    if topaid_org == "":
        topaid_org = None
    topaid_status = request.POST.get("topaid_status", "NOT")
    toinvoice_dest_description = request.POST.get("toinvoice_dest_description", "")
    toinvoice_dest = request.POST.get("toinvoice_dest", None)
    if toinvoice_dest == "":
        toinvoice_dest = None
    toinvoice_dest_status = request.POST.get("toinvoice_dest_status", "NOT")
    profit = request.POST.get("profit", None)
    if profit == "":
        profit = None
    hbl_canjeado_status = request.POST.get("hbl_canjeado_status", "NOT")
    devolution_ctrs_inidate = request.POST.get("devolution_ctrs_inidate", None)
    if devolution_ctrs_inidate == "":
        devolution_ctrs_inidate = None
    devolution_ctrs_findate = request.POST.get("devolution_ctrs_findate", None)
    if devolution_ctrs_findate == "":
        devolution_ctrs_findate = None
    operation_status = request.POST.get("operation_status", "NOT")
    bl_type = request.POST.get("bl_type", "")
    release_type = request.POST.get("release_type", "")

    if vessel_voyage and pol and pod and numctrs and type_ctrs and booking_no and shipping_line and freeddday and \
    costhbl_dest_status and topaid_status and toinvoice_dest_status and hbl_canjeado_status and operation_status:
        if idbusinessinfo: # 修改保存
            businessinfo = Businessinfo( \
                idbusinessinfo = idbusinessinfo,
                clientname=clientname,
                week=week,
                estimated_load_date=estimated_load_date,
                pre_etd=pre_etd,
                etd=etd,
                eta=eta,
                vessel_voyage=vessel_voyage,
                pol=pol,
                pod=pod,
                businessinfocol=businessinfocol,
                numctrs=numctrs,
                type_ctrs=type_ctrs,
                booking_no=booking_no,
                master_no=master_no,
                num_hbls=num_hbls,
                container_no=container_no,
                shipping_line=shipping_line,
                freeddday=freeddday,
                cost_org=cost_org,
                sale_org=sale_org,
                set_org=set_org,
                local_org=local_org,
                venta_dest=venta_dest,
                costhbl_dest_description=costhbl_dest_description,
                costhbl_dest=costhbl_dest,
                costhbl_dest_status=costhbl_dest_status,
                topaid_org_description=topaid_org_description,
                topaid_org=topaid_org,
                topaid_status=topaid_status,
                toinvoice_dest_description=toinvoice_dest_description,
                toinvoice_dest=toinvoice_dest,
                toinvoice_dest_status=toinvoice_dest_status,
                profit=profit,
                hbl_canjeado_status=hbl_canjeado_status,
                devolution_ctrs_inidate=devolution_ctrs_inidate,
                devolution_ctrs_findate=devolution_ctrs_findate,
                operation_status=operation_status,
                bl_type=bl_type,
                release_type=release_type)
        else: # 新增保存
            businessinfo = Businessinfo( \
                # idbusinessinfo = idbusinessinfo,
                clientname=clientname,
                week=week,
                estimated_load_date=estimated_load_date,
                pre_etd=pre_etd,
                etd=etd,
                eta=eta,
                vessel_voyage=vessel_voyage,
                pol=pol,
                pod=pod,
                businessinfocol=businessinfocol,
                numctrs=numctrs,
                type_ctrs=type_ctrs,
                booking_no=booking_no,
                master_no=master_no,
                num_hbls=num_hbls,
                container_no=container_no,
                shipping_line=shipping_line,
                freeddday=freeddday,
                cost_org=cost_org,
                sale_org=sale_org,
                set_org=set_org,
                local_org=local_org,
                venta_dest=venta_dest,
                costhbl_dest_description=costhbl_dest_description,
                costhbl_dest=costhbl_dest,
                costhbl_dest_status=costhbl_dest_status,
                topaid_org_description=topaid_org_description,
                topaid_org=topaid_org,
                topaid_status=topaid_status,
                toinvoice_dest_description=toinvoice_dest_description,
                toinvoice_dest=toinvoice_dest,
                toinvoice_dest_status=toinvoice_dest_status,
                profit=profit,
                hbl_canjeado_status=hbl_canjeado_status,
                devolution_ctrs_inidate=devolution_ctrs_inidate,
                devolution_ctrs_findate=devolution_ctrs_findate,
                operation_status=operation_status,
                bl_type=bl_type,
                release_type=release_type)

        businessinfo.save()
        businessinfos = Businessinfo.objects.order_by('idbusinessinfo')
        return render(request, "main.html", {"businessLists": businessinfos})
    else: # 必填数据为空
        return HttpResponse("请输入数据")

def delbusiness(request):
    idbusinessfordelete = request.POST.get("idbusinessfordelete", "")
    if idbusinessfordelete:
        businessinfo = Businessinfo.objects.get(idbusinessinfo=idbusinessfordelete)
        businessinfo.delete()
        businessinfos = Businessinfo.objects.order_by('idbusinessinfo')
        return render(request, "main.html", {"businessLists": businessinfos})