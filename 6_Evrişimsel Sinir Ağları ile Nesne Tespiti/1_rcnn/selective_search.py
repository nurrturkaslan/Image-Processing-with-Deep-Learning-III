"""
Seçmeli Arama Yöntemi:

Seçmeli arama, süper piksel algoritması kullanarak bir görseli aşırı bölümlere ayırma yöntemidir.

Süper piksel, ortak özellikleri(piksel yoğunluğu gibi)
paylaşan bir piksel grubu olarak tanımlanabilir.

Seçmeli arama, beş temel benzerlik ölçüsüne dayalı olarak süper pikselleri hiyerarşik bir şekilde birleştirir.

Renk benzerliği
doku benzerliği
boyut benzerliği
şekil benzerliği
Yukarıda benzerliklerin doğrusal kombinasyonu

seçmeli arama, sınıf etiketleri değil bölgeler oluşturur. Oluşturulan
bu bölgeler sonrasında sınıflandırıcıya girdi olarak verilecektir.




"""
import cv2
import random

image = cv2.imread("pyramid.jpg")
image = cv2.resize(image, dsize = (600,600))
cv2.imshow("image",image)

# ilklendir ss
ss = cv2.ximgproc.segmentation.createSelectiveSearchSegmentation()
ss.setBaseImage(image)
ss.switchToSelectiveSearchQuality()

print("start")
rects = ss.process()

output = image.copy()

for (x,y,w,h) in rects[:50]:
    color = [random.randint(0,255) for j in range(0,3)]
    cv2.rectangle(output, (x,y),(x+w,y+h),color,2)
    
cv2.imshow("output",output)