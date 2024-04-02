
from .models import  puanTable

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
