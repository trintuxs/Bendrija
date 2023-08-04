from datetime import date

from django.core.mail import send_mail
from django.shortcuts import render


from administracija.models import Kaupiamsis_Inasas, Islaidos
from gyventojas.models import Butas

# Create your views here.
def kaupiamasis_inasas(request):
    # Calculate the total amount for each owner (butas)
    owners = Butas.objects.all()
    for owner in owners:
        kaupiamasis_inasas = Kaupiamsis_Inasas.objects.filter(owner=owner)
        total_amount = sum(inasas.amount for inasas in kaupiamasis_inasas)
        owner.total_amount = total_amount if total_amount else 0

    payment_details = []
    for owner in owners:
        kaupiamasis_inasas = Kaupiamsis_Inasas.objects.filter(owner=owner)
        total_amount = sum(inasas.amount for inasas in kaupiamasis_inasas)
        payment_amount = total_amount * 0.12  # mokestis uz kv 1=0.12centu
        payment_details.append({'owner': owner, 'payment_amount': payment_amount})
        # Send email to owner about payment
        subject = 'Mokėjimas už kaupiamąjį įnašą'
        message = f"Sveiki,\n\nPrašome apmokėti sumą {payment_amount} už kaupiamąjį įnašą.\n\nPagarbiai,"
        from_email = 'ilgoji4bendrija@gmail.com'  # El. pašto adresas, nuo kurio siunčiama žinutė
        recipient_list = [owner.flat_nr.owner.email]  # El. pašto adresas, į kurį siunčiama žinutė
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

    # Calculate the total amount for all owners combined
    all_kaupiamasis_inasas = Kaupiamsis_Inasas.objects.all()
    total_sum = sum(inasas.amount for inasas in all_kaupiamasis_inasas)

    # Get the expenses for the current month
    current_month = date.today().month
    current_month_expenses = Islaidos.objects.filter(date__month=current_month)

    total_current_month_expenses = sum(expense.repairs_cost for expense in current_month_expenses)

    # Calculate the remaining total after subtracting the current month expenses
    remaining_total = total_sum - total_current_month_expenses

    context = {
        'owners': owners,
        'total_sum': total_sum if total_sum else 0,
        'current_month_expenses': current_month_expenses,
        'total_current_month_expenses': total_current_month_expenses,
        'remaining_total': remaining_total,
        'payment_details': payment_details,
    }
    return render(request, 'kaupiamasis_inasas.html', context)