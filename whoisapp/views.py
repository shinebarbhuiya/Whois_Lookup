from django.shortcuts import redirect, render
import requests
import json
import tldextract
from django.http import HttpResponse

# Create your views here.
def Redirect_Page(request):
    return render(request, 'error.html')
    # return HttpResponse('Oppps! No such shit exist.')

def MainApp(request):

    url = "https://whois-3n3hiq001-shinebarbhuiya.vercel.app/"
    # url = input("Enter the domain : ")

    domain = request.GET.get('domain', 'facebook.com')
    # domain = 'edmground.com'

    # domain = 'https://ownthecart.com'
    domain_extract = tldextract.extract(domain)
    domain = domain_extract.registered_domain
    # print(domain)

    sent_json = {      
    "domain": domain
    }

    r = requests.post(url, headers= {"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"}, json= sent_json)

    not_found = r.text.strip()

    if not_found == 'Domain is not found.':
        return Redirect_Page(request)
    else:

        data = r.json()

        registant_name = data['registrant'].get('name', 'No Name')
        registant_street = data['registrant'].get('street', 'No Data')
        registant_city= data['registrant'].get('city', 'No Data')
        registant_state = data['registrant'].get('province', 'No Data')
        registant_postal = data['registrant'].get('postal_code', 'No Data')
        registant_country= data['registrant'].get('country', 'No Data')
        registant_phone = data['registrant'].get('phone', 'No Data')
        registant_email= data['registrant'].get('email', 'No Data')

        domain_ = data['domain'].get('domain', 'No Data')        
        domain_name = data['domain'].get('name', 'No Data')      
        extension = data['domain'].get('extension', 'No Data')           
        whois_server = data['domain'].get('whois_server', 'No Data')              
        server_names = data['domain'].get('name_servers', 'No Data')              
        date_created = data['domain'].get('created_date', 'No Data')              
        date_update = data['domain'].get('updated_date', 'No Data')              
        date_expired = data['domain'].get('expiration_date', 'No Data')                 

        registrar_name = data['registrar'].get('name', 'No Data')       
        registrar_phone = data['registrar'].get('phone', 'No Data')          
        registrar_email = data['registrar'].get('email', 'No Data')          
        registrar_url = data['registrar'].get('referral_url', 'No Data')                 

        if len(registant_email) > 25:
            registant_email = "hiddenemail@email.com"

        if len(registrar_email) > 25:
            registrar_email = "hiddenemail@email.com"
        

        payload= {
                'domain' : domain_ ,
                'domain_name' :  domain_name,
                'extension' : extension,
                'whois_server' : whois_server,
                'server_names' : server_names,
                'date_created' : date_created,
                'date_update' : date_update,
                'date_expired' : date_expired,

                'registrar_name' : registrar_name,
                'registrar_phone' : registrar_phone,
                'registrar_email' : registrar_email,
                'registrar_url' : registrar_url,

                'registrant_name' : registant_name,
                'registrant_street' : registant_street,
                'registrant_city' : registant_city,
                 'registrant_state' : registant_state,
                'registrant_postal' : registant_postal,
                'registrant_country' : registant_country,
                'registrant_phone' : registant_phone,
                'registrant_email' : registant_email,    
                
        }
  
    context = { 'data' : payload} 
    return render(request, 'index.html'  , context )




