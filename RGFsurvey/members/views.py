from django.http import HttpResponse
from django.template import loader
from api.models import Tree

def members(request):
  template = loader.get_template('test.html')
  return HttpResponse(template.render())
  
def detailes(request, id):
  tree = Tree.objects.get(Tree_id=id)
  # mymember = Member.objects.get(id=id)
  template = loader.get_template('viewsDatiles.html')
  context = {
    'tree': tree,
  }
  return HttpResponse(template.render(context, request))
