from django.shortcuts import render
from django.http import HttpResponse
import random
import string
# Create your views here.

#def home(request):
    #return HttpResponse("WELCOME!")

#def home(request):
#    return render(request, 'blog1/home.html', {'testvar' : 'WELCOME!'})

def length(request):
    return render(request, 'generate/length.html')

def password(request):

    len_var = request.GET['len_var']

    try:
        brackets = request.GET['brackets']
    except:
        brackets = None
    try:
        special_characters = request.GET['special_characters']
    except:
        special_characters = None

    gen_pass = ''
    #comment = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ()[]{}!"#$%&:;?@_\'*+,-./=<>\\^`|~'

    base_string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    bracket_string = '()[]{}'
    special_string = '!#$%&:;?@_'


    for y in range(int(len_var)):
        '''if brackets == "True" :
            x = random.randint(0, 67)
            gen_pass += (base_string + bracket_string)[x]
    
        if special_characters == "True":
            x = random.randint(0, 71)
            gen_pass += (base_string + special_string)[x]'''

        if brackets == "True" or special_characters == "True" :
            if brackets == None:
                x = random.randint(0, 61)
                y = random.randint(62, 71)
                gen_pass = gen_pass + (base_string + special_string)[x] + (base_string + special_string)[y]
                if len(gen_pass) > int(len_var):
                    gen_pass = gen_pass[0:int(len_var)]

            if special_characters == None:
                x = random.randint(0, 61)
                y = random.randint(62, 67)
                gen_pass = gen_pass +(base_string + bracket_string)[x]+ (base_string + bracket_string)[y]
                if len(gen_pass) > int(len_var):
                    gen_pass = gen_pass[0:int(len_var)]

        ls = list(gen_pass)
        random.shuffle(ls)
        gen_pass = ''.join(ls)

        if brackets == "True" and special_characters == "True" :
            x = random.randint(0, 61)
            y = random.randint(62, 71)
            z = random.randint(72, 77)
            gen_pass = gen_pass + (base_string + special_string + bracket_string)[x] + (base_string + special_string + bracket_string)[y] + (base_string + special_string + bracket_string)[z]
            if len(gen_pass) > int(len_var):
                gen_pass = gen_pass[0:int(len_var)]

            ls = list(gen_pass)
            random.shuffle(ls)
            gen_pass = ''.join(ls)    

        if brackets == None and special_characters == None:
            x = random.randint(0, 61)
            gen_pass += (base_string)[x]

    return render(request, 'generate/pass.html', {'len_var':len_var, 'gen_pass':gen_pass})
