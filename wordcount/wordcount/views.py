from django.http import HttpResponse
from django.shortcuts import render
import operator

# def home(request):
#     return render(request, "home.html", {'hithere':'This is me'})

# def eggs(request):
#     return HttpResponse("<h1>Eggs are great!<h1>")

def home(request):
    return render(request, "home.html")

def count(request):
    fulltext = request.GET["fulltext"]
    print(fulltext)
    wordlist = fulltext.split()
    print(wordlist)

    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    # return render(request, "count.html", {"fulltext":fulltext, "count":len(wordlist), "worddictionary":worddictionary})
    # return render(request, "count.html", {"fulltext":fulltext, "count":len(wordlist), "worddictionary":worddictionary.items()}) #items() making list
    return render(request, "count.html", {"fulltext":fulltext, "count":len(wordlist), "sortedwords":sortedwords}) 

