from django.shortcuts import render

def gst(request):
    if request.method == 'POST':
        price = float(request.POST.get('price', 0))
        gst = float(request.POST.get('gst', 0))
        
        gst_amount = price * (gst / 100)
        total_bill = price + gst_amount
        
        context = {
            'price': price,
            'gst': gst,
            'gst_amount': gst_amount,
            'total_bill': total_bill
        }
        
        return render(request, 'result.html', context)
    
    return render(request, 'index.html')