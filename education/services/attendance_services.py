from django.template.loader_tags import register

from education.models import Attendance



def get_attendance_by_order(total_order, pk, date):
    #attendance = Attendance.objects.filter(class__pk=pk, date=date)

    #dictionary ilk eleman 0 sa yoklama alınmadı, 2 eleman gelmeyen sayısı, 3. eleman gelen
    yoklama = {}
    gelen=0
    gelmeyen=0
    gelenArray=list()
    gelmeyenArray = list()
    kayitArray = list()

    for x in total_order:
        attendance = Attendance.objects.filter(class_object__pk=pk, date=date, lecture_order=x+1)

        if attendance.count() == 0:
           # yoklama[str(x+1) + "." + "ders"] = '0,0,0'
            gelenArray.append("0")
            gelmeyenArray.append("0")
            kayitArray.append("0")
        else:
            for att in attendance:
                if att.is_exist:
                    gelen = gelen + 1
                else:
                    gelmeyen = gelmeyen + 1

            gelenArray.append(str(gelen))
            gelmeyenArray.append(str(gelmeyen))
            kayitArray.append(str(attendance.count()))
            #yoklama[str(x + 1) + "." + "ders"] = str(attendance.count()) + "," + str(gelmeyen) + "," + str(gelen)

    yoklama['kayitSayisi'] = kayitArray
    yoklama['gelenSayisi'] = gelenArray
    yoklama['gelmeyenSayisi'] = gelmeyenArray

    return yoklama









