from django.shortcuts import render, redirect
import openai,os
from dotenv import load_dotenv
from .models import Article,Livre,Category,Auteur
import base64
from io import BytesIO
from PIL import Image
import requests
import media
openai.api_key = "sk-proj-s1No2TLxSsEe551UWafLT3BlbkFJnXcsmsvf1pGbUSC32U1k"



def detail(request, id_livre):
    livre = Livre.objects.get(id=id_livre)
    category = livre.category
    livres_en_relation = Livre.objects.filter(category=category).order_by('title')[:5]
    return render(request, 'detail.html', {"livre": livre, "ler": livres_en_relation})

def my_view(request):
    result = ''  
    categories = Category.objects.all().order_by()
    auteurs = Auteur.objects.all().order_by()
    user_input = '' 
    if request.method == 'POST':
        user_input1 = request.POST.get('user_input2')
        user_input2 = request.POST.get('user_input3')
        user_input3 = request.POST.get('user_input1')
        auteur_id = request.POST.get('auteeurs')  
        category_id = request.POST.get('category')
        category_id = request.POST.get('category')  
        if category_id:
            category_id=Category.objects.get(naid=category_id) 
            category_id = Category.objects.get(id=category_id)
        else:
            category_id=Category(name=user_input3)
            category_id.save()
        if auteur_id:
            auteur_id = Auteur.objects.get(id=auteur_id)
        else:
            auteur_id=Auteur(name=user_input2)
            auteur_id.save()
        
        result = user_input1 
        
        user_input = "Resume livre intitulé " + result

        model = "gpt-3.5-turbo"
        temperature = 0.7

        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "user", "content": user_input}
            ],
            temperature=temperature
        )

        response = response.choices[0].message.content
        desc = response
        prompt = "livre qui a une page de couverture" + result
        n = 1
        size = "256x256"
        response = openai.Image.create(
            prompt=prompt,
            n=n,
            size=size
        )

        image_url = response["data"][0]["url"]
        response = requests.get(image_url)
        image_data = response.content
        
        filename = 'media/' + result + '.png'

        with open(filename, 'wb') as f:
            f.write(image_data)


        limage = result+'.png'  # Update the image field with the file path
        

        livre = Livre.objects.create(title=result, category =category_id, auteur=auteur_id, desc=desc, image=limage)
        livre.save()

    

    

    return render(request, 'my_view.html', {"result": result,"categories":categories,"auteurs":auteurs})


def detail2(request):
    livre = Livre.objects.all()
    if request.method == 'POST':
        user_input1 = request.POST.get('user_input1')
        if user_input1 != "" and user_input1 is not None:
            livre = Livre.objects.filter(title__icontains=user_input1)
            return render(request, "noslivres.html", {"liste_livres": livre})  # <--- Use redirect instead of render
    return render(request, "detail2.html")




def noslivres(request):
    liste_livres = Livre.objects.all().order_by("-title")
    context = {"liste_livres": liste_livres}
    livre = Livre.objects.all()
    if request.method == 'POST':
        user_input1 = request.POST.get('user_input1')
        if user_input1 != "" and user_input1 is not None:
            livre = Livre.objects.filter(title__icontains=user_input1)
            return render(request, "noslivres.html", {"liste_livres": livre})
    return render(request, "noslivres.html", context)
 
def auteur(request):
    auteur= Auteur.objects.all().order_by('-name')
    livre = Livre.objects.all()
    if request.method == 'POST':
        user_input1 = request.POST.get('user_input1')
        if user_input1 != "" and user_input1 is not None:
            livre = Livre.objects.filter(title__icontains=user_input1)
            return render(request, "noslivres.html", {"liste_livres": livre})
    context = {"liste_auteurs": auteur}
    return render(request, "nosauteurs.html", context)


def noslivresauteur(request,auteur_id):
    listelivre=Livre.objects.filter(auteur_id=auteur_id)
    livre = Livre.objects.all()
    if request.method == 'POST':
        user_input1 = request.POST.get('user_input1')
        if user_input1 != "" and user_input1 is not None:
            livre = Livre.objects.filter(title__icontains=user_input1)
            return render(request, "noslivres.html", {"liste_livres": livre})
    context = {"liste_livres": listelivre}
    return render(request, "noslivres.html", context)


def nosauteurs(request):
    liste_auteurs = Auteur.objects.all().order_by("?")
    livre = Livre.objects.all()
    if request.method == 'POST':
        user_input1 = request.POST.get('user_input1')
        if user_input1 != "" and user_input1 is not None:
            livre = Livre.objects.filter(title__icontains=user_input1)
            return render(request, "noslivres.html", {"liste_livres": livre})
    context = {"liste_auteurs": liste_auteurs}
    return render(request, "nosauteurs.html", context)

def auteurslivres(request, auteur):
    auteur = Auteur.objects.get(name=auteur)
    livre = Livre.objects.all()
    if request.method == 'POST':
        user_input1 = request.POST.get('user_input1')
        if user_input1 != "" and user_input1 is not None:
            livre = Livre.objects.filter(title__icontains=user_input1)
            return render(request, "noslivres.html", {"liste_livres": livre})
    liste_livres = Livre.objects.filter(auteur=auteur)
    context = {"liste_livres": liste_livres}
    return render(request, "noslivres.html", context)

def genre(request):
    category = Category.objects.all().order_by('?')
    livre = Livre.objects.all()
    if request.method == 'POST':
        user_input1 = request.POST.get('user_input1')
        if user_input1 != "" and user_input1 is not None:
            livre = Livre.objects.filter(title__icontains=user_input1)
            return render(request, "noslivres.html", {"liste_livres": livre})
    return render(request ,"genre.html",{"category":category})

def genre_category(request, category):
    category = Category.objects.get(name=category)
    livre = Livre.objects.all()
    if request.method == 'POST':
        user_input1 = request.POST.get('user_input1')
        if user_input1 != "" and user_input1 is not None:
            livre = Livre.objects.filter(title__icontains=user_input1)
            return render(request, "noslivres.html", {"liste_livres": livre})
    liste_livres = Livre.objects.filter(category=category)
    context = {"liste_livres": liste_livres}
    return render(request, "noslivres.html", context)