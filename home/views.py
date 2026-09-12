# Django views are Python functions or classes that receive web requests and return web responses. 
# They contain the logic to process HTTP requests and generate appropriate HTTP responses, 
# in the form of HTML content to be rendered in the user’s web browser


# By default, the views file imports this func, which is used to render templates and return an HTTP response
from django.shortcuts import render

# takes in one param; the HTTP  request received by the server
def index(request):
    template_data = {} # store data that will be passed from view functions to templates
    template_data['title'] = 'Movies Store' #  used to define the browser tab title
    return render(request, 
                'home/index.html', {
                'template_data': template_data})

def about(request):
    template_data = {}
    template_data['title'] = 'About'
    return render(request, 
                'home/about.html',
                {'template_data': template_data}) 
