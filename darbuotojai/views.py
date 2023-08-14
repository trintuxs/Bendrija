from django.db.models import Sum
from django.shortcuts import render

from darbuotojai.models import Staff


# Darbuotoju sarasas
# Staff list
# Staff total wages count
# Darbuotoju atliginimu bendra suma

def staff_list(request):
    staff = Staff.objects.all()
    total_wage = Staff.objects.aggregate(total_wage=Sum('wage'))['total_wage']
    context = {'staff': staff, 'total_wage': total_wage}
    return render(request, 'staff_list.html', context)
