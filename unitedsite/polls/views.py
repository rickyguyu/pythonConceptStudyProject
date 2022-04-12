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
    mblfile = request.FILES.get("mblfile", "")
    hblfiles = request.FILES.get("hblfiles", "")
    dp_voucher = request.FILES.get("dp_voucher", "")
    dp_invoice = request.FILES.get("dp_invoice", "")
    hp_voucher = request.FILES.get("hp_voucher", "")
    hp_invoice = request.FILES.get("hp_invoice", "")
    hbls_canjeados = request.FILES.get("hbls_canjeados", "")
    income_voucher = request.FILES.get("income_voucher", "")
    income_invoice = request.FILES.get("income_invoice", "")
    hbls_firmados = request.FILES.get("hbls_firmados", "")
    if vessel_voyage and pol and pod and numctrs and type_ctrs and booking_no and shipping_line and freeddday and \
    costhbl_dest_status and topaid_status and toinvoice_dest_status and hbl_canjeado_status and operation_status:
        if idbusinessinfo: # 修改保存
            businessinfo = Businessinfo.objects.get(idbusinessinfo = idbusinessinfo)
            businessinfo.clientname=clientname
            businessinfo.week=week
            businessinfo.estimated_load_date=estimated_load_date
            businessinfo.pre_etd=pre_etd
            businessinfo.etd=etd
            businessinfo.eta=eta
            businessinfo.vessel_voyage=vessel_voyage
            businessinfo.pol=pol
            businessinfo.pod=pod
            businessinfo.businessinfocol=businessinfocol
            businessinfo.numctrs=numctrs
            businessinfo.type_ctrs=type_ctrs
            businessinfo.booking_no=booking_no
            businessinfo.master_no=master_no
            businessinfo.num_hbls=num_hbls
            businessinfo.container_no=container_no
            businessinfo.shipping_line=shipping_line
            businessinfo.freeddday=freeddday
            businessinfo.cost_org=cost_org
            businessinfo.sale_org=sale_org
            businessinfo.set_org=set_org
            businessinfo.local_org=local_org
            businessinfo.venta_dest=venta_dest
            businessinfo.costhbl_dest_description=costhbl_dest_description
            businessinfo.costhbl_dest=costhbl_dest
            businessinfo.costhbl_dest_status=costhbl_dest_status
            businessinfo.topaid_org_description=topaid_org_description
            businessinfo.topaid_org=topaid_org
            businessinfo.topaid_status=topaid_status
            businessinfo.toinvoice_dest_description=toinvoice_dest_description
            businessinfo.toinvoice_dest=toinvoice_dest
            businessinfo.toinvoice_dest_status=toinvoice_dest_status
            businessinfo.profit=profit
            businessinfo.hbl_canjeado_status=hbl_canjeado_status
            businessinfo.devolution_ctrs_inidate=devolution_ctrs_inidate
            businessinfo.devolution_ctrs_findate=devolution_ctrs_findate
            businessinfo.operation_status=operation_status
            businessinfo.bl_type=bl_type
            businessinfo.release_type=release_type
            if mblfile:
                businessinfo.mblfile = mblfile
            if hblfiles:
                businessinfo.hblfiles = hblfiles
            if dp_voucher:
                businessinfo.dp_voucher = dp_voucher
            if dp_invoice:
                businessinfo.dp_invoice = dp_invoice
            if hp_voucher:
                businessinfo.hp_voucher = hp_voucher
            if hp_invoice:
                businessinfo.hp_invoice = hp_invoice
            if hbls_canjeados:
                businessinfo.hbls_canjeados = hbls_canjeados
            if income_voucher:
                businessinfo.income_voucher = income_voucher
            if income_invoice:
                businessinfo.income_invoice = income_invoice
            if hbls_firmados:
                businessinfo.hbls_firmados = hbls_firmados


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
                release_type=release_type,
                mblfile=mblfile,
                hblfiles=hblfiles,
                dp_voucher=dp_voucher,
                dp_invoice=dp_invoice,
                hp_voucher=hp_voucher,
                hp_invoice=hp_invoice,
                hbls_canjeados=hbls_canjeados,
                income_voucher = income_voucher,
                income_invoice = income_invoice,
                hbls_firmados = hbls_firmados,
            )

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