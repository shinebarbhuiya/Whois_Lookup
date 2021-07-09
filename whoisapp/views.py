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

    url = "https://whois-api.vercel.app"
    # url = input("Enter the domain : ")

    domain = request.GET.get('domain', 'ownthecart.com')
    # domain = 'edmground.com'

    # domain = 'https://ownthecart.com'
    domain_extract = tldextract.extract(domain)
    domain = domain_extract.registered_domain
    print(domain)

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



        payload= {
                'domain' : data['domain']['domain'],
                'domain_name' : data['domain']['name'],
                'extension' : data['domain']['extension'],
                'whois_server' : data['domain']['whois_server'],
                'server_names' : data['domain']['name_servers'],
                'date_created' : data['domain']['created_date'],
                'date_update' : data['domain']['updated_date'],
                'date_expired' : data['domain']['expiration_date'],

                'registrar_name' : data['registrar']['name'],
                'registrar_phone' : data['registrar']['phone'],
                'registrar_email' : data['registrar']['email'],
                'registrar_url' : data['registrar']['referral_url'],

                'registrant_name' : registant_name,
                'registrant_street' : registant_street,
                'registrant_city' : registant_city,
                 'registrant_state' : registant_state,
                'registrant_postal' : registant_postal,
                'registrant_country' : registant_country,
                'registrant_phone' : registant_phone,
                'registrant_email' : registant_email,

                # 'registrant_name' : data['registrant']['name'],
                # 'registrant_street' : data['registrant']['street'],
                # 'registrant_city' : data['registrant']['city'],
                #  'registrant_state' : data['registrant']['province'],
                # 'registrant_postal' : data['registrant']['postal_code'],
                # 'registrant_country' : data['registrant']['country'],
                # 'registrant_phone' : data['registrant']['phone'],
                # 'registrant_email' : data['registrant']['email'],

                
        }

        
        print(registant_state)



    
        
        

               

        

        # if registrant_state:
        #     payload['registrant_state'] = data['registrant']['province']
        # else:
        #     payload['registrant_state'] = "No Results"


    # print(data)
    # name = data['domain']['name']
    # print(name)
        



    
    context = { 'data' : payload} 
    return render(request, 'index.html'  , context )




