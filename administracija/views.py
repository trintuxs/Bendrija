from django.shortcuts import render
from administracija.models import Kaupiamsis_Inasas, Expenses
from gyventojas.models import Flat


#Visu butu savininkai
def kaupiamasis_inasas(request):
    owners = Flat.objects.all()
    payment_details = []

    for owner in owners:
        total_amount = Kaupiamsis_Inasas.calculate_total_amount(owner)
        owner.total_amount = total_amount

        # Apskaiciuojame ir siunčiame pranešimą tik jei yra Kaupiamasis Inasas šiam savininkui
        kaupiamasis_inasas = Kaupiamsis_Inasas.objects.filter(owner=owner).first()
        if kaupiamasis_inasas:
            payment_amount = kaupiamasis_inasas.calculate_payment_amount()
            payment_details.append({'owner': owner, 'payment_amount': payment_amount})
            kaupiamasis_inasas.send_payment_email()

    # Gauname visų inasų bendrą sumą
    total_sum = Kaupiamsis_Inasas.calculate_total_sum()

    # Skaiciuojama šio mėnesio išlaidų suma (jei tai susiję su kitu kodu)
    total_current_month_expenses = Expenses.calculate_total_current_month_expenses()

    # Likutis po šio mėnesio išlaidų
    remaining_total = total_sum - total_current_month_expenses

    context = {
        'owners': owners,
        'total_sum': total_sum,
        'total_current_month_expenses': total_current_month_expenses,
        'remaining_total': remaining_total,
        'payment_details': payment_details,
    }
    return render(request, 'kaupiamasis_inasas.html', context)