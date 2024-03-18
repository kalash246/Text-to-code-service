from django.shortcuts import render
from django.http import JsonResponse
from .oai_queries import get_completion

def query_view(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        lang = request.POST.get('lang')
        cleaningFn = request.POST.get('cleaningFn')
        add_lang = language_view(lang)
        add_cleaningFn = cleaning_function_view(cleaningFn)
        new_prompt = add_lang + prompt + add_cleaningFn
        print("Final Prompt before hit: ----> "+new_prompt)
        response = get_completion(new_prompt)
        return JsonResponse({'response': response})
    return render(request, 'query.html')

def language_view(lang):
    return "Create a " + lang + " function. "

def cleaning_function_view(cleaningFn):
    if cleaningFn == "columnHooks":
        return "The function takes the parameter `values` which is expected to be a two-dimensional array where each inner array contains a value at position 1 and an index at position 2."
    else:
	    return "The function takes the first parameter `row` which refers to an object that includes column keys paired with their corresponding values for a given row, and it takes the second argument `rowIndex` which is the Index of the current iteration."
