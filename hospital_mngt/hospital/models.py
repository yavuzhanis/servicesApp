from django.db import models
import datetime
from django.utils import timezone


class Vehicle(models.Model):
    vehicle_model = models.IntegerField(null=True)
    vehicle_inspection = models.DateField()
    car_plaka = models.CharField(max_length=40)
    adress = models.TextField(max_length=200)
    vehicle_maintenance = models.DateField(default=datetime.date.today)
    vehicle_tire = models.DateField(default=datetime.date.today)
    car_battery = models.BooleanField(default=False)
    vehicle_insurance = models.DateField(default=datetime.date.today)
    vehicle_license = models.BooleanField(default=False)
    carArventoNumber = models.IntegerField(null=True)

    def __str__(self):
        return self.car_plaka


class Drıver(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=40)
    mobile = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Admın(models.Model):
    admin = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True)
    driver = models.ForeignKey(Drıver, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    mobile = models.IntegerField(null=True)
    vehicle_model = models.CharField(max_length=50)
    vehicle_inspection = models.DateField(null=True)
    car_plaka = models.CharField(max_length=40)
    vehicle_maintenance = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.Vehicle.car_plaka + "  " + self.Drıver.name


class Atama(models.Model):
    surucu = models.ForeignKey(Drıver, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True)
    car_plaka = models.CharField(max_length=40)
    vehicle_inspection = models.DateField(default=datetime.date.today)
    adress = models.TextField(max_length=200, null=True)

    def __str__(self):
        return f"Atama: {self.surucu.name} - {self.vehicle.car_plaka}"


class puanTable(models.Model):
    car_plaka = models.CharField(max_length=40)
    surucu = models.ForeignKey(Drıver, on_delete=models.CASCADE)
    adress = models.TextField(max_length=200)
    date = models.DateField(default=timezone.now)
    devir_bakiye = models.IntegerField()
    borc_bakiye = models.IntegerField()
    alacak_bakiye = models.IntegerField()
    toplam_bakiye = models.IntegerField()
    daily_data = models.JSONField(default=list)


    @staticmethod
    def calculate_monthly_data():
            #! Örnek: Günlük verilerden aylık veri hesapla
            monthly_data = {}  #! {Arac_plakası: {"Ay": "AylıkToplamServis", ...}}

            # Günlük verileri al
            daily_data = puanTable.objects.all()

            for data in daily_data:
                #! Her bir günlük veriyi işle
                car_plaka = data.car_plaka
                date = data.date
                month_year = date.strftime("%Y-%m")  # Ay ve yılı al
                #! Toplam servis sayısını güncelle
                monthly_data.setdefault(car_plaka, {}).setdefault(month_year, 0)
                monthly_data[car_plaka][month_year] += 1

            return monthly_data



class Plate(models.Model):
    plate_number = models.CharField(max_length=40, unique=True)
    vehicle = models.ForeignKey(
        "Vehicle", on_delete=models.CASCADE, related_name="plates"
    )
    driver = models.ForeignKey(
        "Drıver", on_delete=models.CASCADE, related_name="plates"
    )

    def __str__(self):
        return self.plate_number
