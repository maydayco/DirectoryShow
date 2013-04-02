# Create your views here.
import paramiko
from time import gmtime, strftime
from django.shortcuts import render_to_response
from django.http import HttpResponse
def home(request):
    content = {
            'machine' : 'Test Machine 1',
            'address' : '54.244.114.170',
            'date' : strftime("%Y-%m-%d %H:%M:%S", gmtime()), 
            'body' : 'Welcome!',
            }
    return render_to_response('index.html', content)

def show(request):
    str = get()
    html = ''
    for i in str:
         html += '<br/>' + i
    html += '<br/>'
    return HttpResponse(html)

def get(): 
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('tm2', username='test', password='liu123456')
    stdin, stdout, stderr = ssh.exec_command('find /home -maxdepth 3 -printf \'%p\t%s\n\'')
    str = stdout.readlines()
    ssh.close()
    return str
