from django.shortcuts import render
import openai,os
from dotenv import load_dotenv
from .models import Article,Livre,Category
from django.views.decorators.csrf import csrf_exempt 
load_dotenv()

api_key = os.getenv("OPENAI_KEY", None)
def detail(request,id_livre):
    livre=Livre.objects.get(id=id_livre) 
    category=livre.category
    livres_en_relation = Livre.objects.filter(category=category).order_by('title')[:5]
    openai.api_key = "sk-proj-HuMbWINvafQ96sv9jLUsT3BlbkFJESwv7qk0dYz6SJFieRb4"

# Define the user's input (e.g. a question)
    user_input = "Summarize the book titled" +livre.title

# Define the model and parameters for the response
    model = "gpt-3.5-turbo"
    temperature = 0.7

# Create a chat completion request
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "user", "content": user_input}
        ],
        temperature=temperature
    )

# Print the response
    response=(response.choices[0].message.content)
    livre.desc=response
    return render(request,'detail.html',{"livre":livre,"ler":livres_en_relation,"response":response})

def chatbot(request):
    chatbot_response = ""  # Initialize with an empty string

    if api_key is not None and request.method == 'POST':
        openai.api_key = api_key
        user_input = request.POST.get('user_input')
        prompt = user_input

        response = openai.Completion.create(
            engine='gpt-3.5-turbo-instruct',
            prompt=prompt,
            max_tokens=256,
            temperature=0.5,
        )
        print(response)

        chatbot_response = response.choices[0].message
        print(chatbot_response)

        return render(request, 'main.html', {"response": chatbot_response})
    return render(request, 'chatbot.html')


def home(request):
    list_articles=Article.objects.all()
    context={"liste_articles":list_articles}
    return render(request,"index.html",context )

def detail3(request,id_livre):
    livre=Livre.objects.get(id=id_livre) 
    category=livre.category
    livres_en_relation = Livre.objects.filter(category=category).order_by('title')[:5]
    return render(request,'detail.html',{"livre":livre,"ler":livres_en_relation})

def detail2(request):
    return render(request,"detail2.html")

def noslivres(request):
    liste_livres = Livre.objects.all().order_by("?")
    context = {"liste_livres": liste_livres}
    return render(request, "noslivres.html", context)


def noslivresalphabetique(request):
    liste_livres = Livre.objects.all().order_by('-category_id')
    context = {"liste_livres": liste_livres}
    return render(request, "noslivres.html", context)

def genre(request):
    return render(request ,"genre.html")

def genre_category(request, category):
    category = Category.objects.get(name=category)
    liste_livres = Livre.objects.filter(category=category)
    context = {"liste_livres": liste_livres}
    return render(request, "noslivres.html", context)