from django.http import HttpResponse
from django.template import loader

from detail.models import Cattegory


# Create your views here.
def home(request):
    list_species = []
    get_all_cattegory = Cattegory.objects.all()

    for cattegory in get_all_cattegory:
        species = cattegory.species
        list_species.append(species)

    template = loader.get_template('index.html')
    context = {'list_species': list_species}

    return HttpResponse(template.render(context, request))
