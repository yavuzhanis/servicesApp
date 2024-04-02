from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Drıver
from .models import Vehicle, Admın, Atama, puanTable, Drıver
import json
from .models import Plate
from .utils import calculate_monthly_data

def Index(request):
    if not request.user.is_staff:
        return redirect("login")
    vehicle = Vehicle.objects.all()
    driver = Drıver.objects.all()
    ata = Atama.objects.all()
    v = 0
    d = 0
    a = 0
    for i in vehicle:
        v += 1
    for i in driver:
        d += 1
    for i in ata:
        a += 1
    v1 = {"v": v, "d": d, "a": a}

    return render(request, "index.html", v1)


def Login(request):
    error = ""
    if request.method == "POST":
        u = request.POST["uname"]
        p = request.POST["pwd"]
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {"error": error}
    return render(request, "login.html", d)


def logOut_admin(request):
    if not request.user.is_staff:
        return redirect("login")
    logout(request)
    return redirect("admin_login")


def sofor_goruntule(request):
    if not request.user.is_staff:
        return redirect("login")
    sofor = Drıver.objects.all()
    s = {"sofor": sofor}
    return render(request, "sofor_goruntule.html", s)


def sofor_sil(request, pid):
    if not request.user.is_staff:
        return redirect("login")
    sof = Drıver.objects.get(id=pid)
    sof.delete()
    return redirect("sofor_goruntule")


def soforEkle(request):
    error = ""
    if not request.user.is_staff:
        return redirect("login")
    if request.method == "POST":
        name = request.POST["name"]
        mobile = request.POST["mobile"]
        surname = request.POST["surname"]
        try:
            Drıver.objects.create(name=name, mobile=mobile, surname=surname)
            error = "no"
        except:
            error = "yes"
    d = {"error": error}
    return render(request, "soforEkle.html", d)


def arac_goruntule(request):
    if not request.user.is_staff:
        return redirect("login")
    arac = Vehicle.objects.all()
    a = {"arac": arac}
    return render(request, "arac_goruntule.html", a)


def aracEkle(request):
    if not request.user.is_staff:
        return redirect("login")

    if request.method == "POST":
        try:
            Vehicle.objects.create(
                vehicle_model=request.POST.get("vehicleModel"),
                car_plaka=request.POST.get("car_plaka"),
                adress=request.POST.get("adress"),
                vehicle_maintenance=request.POST.get("vehicle_maintenance"),
                vehicle_tire=request.POST.get("vehicle_tire"),
                vehicle_insurance=request.POST.get("vehicle_insurance"),
                vehicle_license=request.POST.get("vehicle_license"),
                vehicle_inspection=request.POST.get("vehicle_inspection"),
            )
            success_message = "Araç başarıyla eklendi."
        except Exception as e:
            error_message = f"Hata oluştu: {str(e)}"

    return render(request, "arac_ekle.html", locals())


def arac_sil(request, pid):
    if not request.user.is_staff:
        return redirect("login")
    car = Vehicle.objects.get(id=pid)
    car.delete()
    return redirect("arac_goruntule")


def atama_ekle(request):
    error_message = ""
    success_message = ""

    if not request.user.is_staff:
        return redirect("login")

    if request.method == "POST":
        selected_driver_name = request.POST.get("name")
        car_plaka = request.POST.get("car_plaka")
        vehicle_inspection = request.POST.get("vehicle_inspection")
        adress = request.POST.get("adress")

        driver = Drıver.objects.filter(name=selected_driver_name).first()
        vehicle = Vehicle.objects.filter(car_plaka=car_plaka).first()

        if driver and vehicle:
            try:
                Atama.objects.create(
                    surucu=driver,
                    car_plaka=car_plaka,
                    vehicle_inspection=vehicle_inspection,
                    adress=adress,
                )
                success_message = "Atama başarıyla eklendi."
            except Exception as e:
                error_message = "Atama eklenirken bir hata oluştu: " + str(e)
        else:
            error_message = "Şoför veya araç bulunamadı."

    drivers = Drıver.objects.all()
    vehicles = Vehicle.objects.all()
    return render(
        request,
        "atama_ekle.html",
        {
            "driver": drivers,
            "vehicle": vehicles,
            "success_message": success_message,
            "error_message": error_message,
        },
    )


def atama_goruntule(request):
    if not request.user.is_staff:
        return redirect("login")
    a = Atama.objects.all()
    a = {"a": a}
    return render(request, "atama_goruntule.html", a)


def atama_sil(request, atama_id):
    if not request.user.is_staff:
        return redirect("login")

    atama = Atama.objects.get(id=atama_id)
    atama.delete()

    return redirect("atama_goruntule")


def puantaj_ekle(request):
    if not request.user.is_staff:
        return redirect("login")

    vehicles = Vehicle.objects.all()  # Tüm araçları al
    drivers = Drıver.objects.all()  # Tüm sürücüleri al
    success_message = ""
    error_message = ""

    if request.method == "POST":
        try:
            # Sürücü adını al
            driver_name = request.POST.get("surucu")
            # Sürücüyü adına göre bul
            driver = Drıver.objects.get(name=driver_name)

            # puanTable oluştururken sürücüyü doğru şekilde kullanın
            puanTable.objects.create(
                car_plaka=request.POST.get("car_plaka"),
                surucu=driver,  # Doğru sürücü modeli örneğini atayın
                date=request.POST.get("date"),
                devir_bakiye=request.POST.get("devir_bakiye"),
                borc_bakiye=request.POST.get("borc_bakiye"),
                alacak_bakiye=request.POST.get("alacak_bakiye"),
                toplam_bakiye=request.POST.get("toplam_bakiye"),
                adress=request.POST.get("adress"),
            )
            success_message = "Puantaj başarıyla eklendi."
        except Exception as e:
            error_message = f"Hata oluştu: {str(e)}"

    return render(
        request,
        "puanT_ekle.html",
        {
            "vehicles": vehicles,  # Araçları şablon dosyasına iletiliyor
            "success_message": success_message,
            "error_message": error_message,
            "drivers": drivers,  # Sürücüleri şablon dosyasına iletiliyor
        },
    )


def puantaj_goruntule(request):
    if not request.user.is_staff:
        return redirect("login")
    monthly_data = puanTable.calculate_monthly_data()
    puantajlar = puanTable.objects.all()
    p = puantajlar.count()
    context = {"puantajlar": puantajlar , "p" : p,'monthly_data': monthly_data}  # "p" değişkeni ekleniyor
    return render(request, "puanT_goruntule.html", context)

def puantaj_sil(request, puantaj_id):
    if not request.user.is_staff:
        return redirect("login")

    pauntaj = puanTable.objects.get(id=puantaj_id)
    pauntaj.delete()

    return redirect("puantaj_goruntule")

def grafik_view(request):
    # Veritabanından tüm puantajları al
    puantajlar = puanTable.objects.all()

    # Tarihler ve toplam bakiyeler için boş listeler oluştur
    dates = []
    totalBalances = []

    # Puantajlar üzerinde döngü yaparak tarihleri ve toplam bakiyeleri topla
    for puantaj in puantajlar:
        puantaj_date = puantaj.date.strftime('%Y-%m-%d')  # Tarihi uygun formata dönüştür
        if puantaj_date not in dates:
            dates.append(puantaj_date)
            totalBalances.append(puantaj.toplam_bakiye)
        else:
            index = dates.index(puantaj_date)
            totalBalances[index] += puantaj.toplam_bakiye

    # Grafik verilerini JSON formatına dönüştür
    chart_data = {
        'dates': dates,
        'totalBalances': totalBalances,
    }
    chart_data_json = json.dumps(chart_data)

    # Grafik verileriyle birlikte template'i render et
    return render(request, 'puanT_tablo.html', {'chart_data': chart_data_json})



def plaka_view(request):
    monthly_data = puanTable.calculate_monthly_data()
    return render(request, 'plaka_tablo.html', {'calculated_data': monthly_data})