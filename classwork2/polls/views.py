from django.http import HttpResponse


def index(request):
    return HttpResponse("This is a bad request. Use one of the other routes")
def system(request):
    return HttpResponse("My favorite OS is Windows")
def language(request):
    return HttpResponse("My favorite language is JavaScript")
def ide(request):
    return HttpResponse("My favorite IDE is currently IntelliJ")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def sum(request, number1, number2):
    return HttpResponse(("The sum of ", number1, " and ", number2, ' is ', (number2+number1)))
def name(request, name1):
    return HttpResponse(("Hello ", name1))
def timestwo(request, number1):
    return HttpResponse(("The product times 2 is: ", (number1*2)))
def loop(request, number1):
    for x in range(0, number1):
        print(x)
        x+=9
    return HttpResponse(("The sum of all numbers is: ", x))
