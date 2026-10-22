from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    'january':'Eat no meat for the entire month',
    'february': "Walk for at least 20 minutes everyday!",
    'march': "Learn Django for at least 20 minutes everyday!",
    'april':'Eat no banku for the entire month',
    'may': "Run for at least 20 minutes everyday!",
    'june': "Learn R for at least 20 minutes everyday!",
    'july':'Eat no fufu for the entire month',
    'august': "Exercise for at least 20 minutes everyday!",
    'september': "Learn Calculus for at least 20 minutes everyday!",
    'october': 'Eat no jollof for the entire month',
    'november': "Sleep for at least 20 minutes everyday!",
    'december': None,
}

# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months" : months,
    })
               

    # response_data = """
    #     <ul>
    #         <li><a href="/challenges/january"></a>January</li>
    #     </ul>

    # """


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound('<h1>Invalid month</h1>')
    
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # build path with prefix '/challenge'
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text":challenge_text,
            "month_name":month
            })
    except:
        raise Http404()
    
# def show_challenge_list(request):
#     challenge_month = list(monthly_challenges.keys())
#     challenge_values = list(monthly_challenges.values())
#     response_data = ''
#     for i in range(12):
#         # response_data = f"\n{response_data}{challenge_month[i]} - {challenge_values[i]}\n"
#         response_data = "<a>" + response_data + challenge_month[i].title() + " - " + challenge_values[i].title() + "</a>" + "<br>"
#     return HttpResponse(response_data)



# f"<ol>{challenge_month[i]} - {challenge_values[i]}</ol>"
