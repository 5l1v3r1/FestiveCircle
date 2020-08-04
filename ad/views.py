from django.shortcuts import render, redirect
from django.contrib.gis.geoip2 import GeoIP2
from django.contrib import messages
from django.utils import timezone
from user import views as users_views
from .models import *
from django.http import HttpResponseRedirect


def adv_search(request):
    if request.method == 'POST':
       return render(request,'ad/advanced_search.html')
    else:
        return render(request,'ad/advanced_search.html')


def main(request):

    g = GeoIP2()
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
        print("XFWD: ", ip_address)
    elif request.META.get('REMOTE_ADDR'):
        ip_address = request.META.get('REMOTE_ADDR')
        print("RMT: ", ip_address)
    
    if ip_address == '127.0.0.1':
        city = 'Lahore'
    else:
        city = g.city(ip_address)['city']
        if not city:
            city = 'Lahore'

    featured_details = Detail.objects.filter(featured=True)
    featured_details_images   = {}
    featured_details_paarize  = {}

    for detail in featured_details:
        featured_details_images[detail.id] = images.objects.filter(detail_id=detail).first()
        obj = VenuePrice.objects.filter(venue_id = Venue.objects.get(detail_id = detail.id)).first()
        featured_details_paarize[detail.id] = str(obj.per_guest)
    

    locs = Location.objects.filter(city='Lahore')[:8]
    loc_based_details = {}
    loc_based_images = {}
    loc_based_prices = {}
    
    for loc in locs:
        loc_based_details[Detail.objects.get(loction_id=loc).id] = Detail.objects.get(loction_id=loc)
        loc_based_images[Detail.objects.get(loction_id=loc).id] = images.objects.filter(detail_id=
                 Detail.objects.get(loction_id=loc).id).first()
        obj = VenuePrice.objects.get(venue_id = Venue.objects.get(detail_id = Detail.objects.get(loction_id=loc).id))
        loc_based_prices[Detail.objects.get(loction_id=loc).id] = str(obj.per_guest)
    



    context = {
        'featured_details' : featured_details,
        'featured_details_images': featured_details_images,
        'featured_details_paarize': featured_details_paarize,
        'loc_based_details': loc_based_details,
        'loc_based_images': loc_based_images,
        'loc_based_prices' : loc_based_prices,
        'location' : city,
    }

    if request.method == 'POST':
        category = request.POST.get('category')
        city =request.POST.get('city')
        price =request.POST.get('price')
        if not price:
            min_price = '0'
            max_price = '0'
        else:
            p = price.split("-")
            min_price = p[0]
            max_price = p[1]

        return redirect(search, category, city, min_price, max_price)

    else:
        return render(request,"ad/main.html", context)

def post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            title = request.POST.get('venue_title')
            category = request.POST.get('category')
            city = request.POST.get('city')
            area = request.POST.get('area')
            address = request.POST.get('address')
            description = request.POST.get('description')

            location = Location.objects.create(city=city, area=area, street=address) 
            detail = Detail.objects.create(title=title, loction_id=location, featured=True, 
            description=description, rating=0, views=0, status='Active', expiryDate=timezone.now() + timezone.timedelta(days=30))
            
            print(title) 
            print(category)
            print(city)
            print(area)
            print(description)

            for image in request.FILES.getlist('images'):
                images.objects.create(title=title, detail_id=detail, image=image)
                print(str(image)+' '+str(image.size))
            
            print("Services: ")
            decoration_price = None
            decoration = None
            if request.POST.get('decoration') == 'Decoration':
                decoration = True
                decoration_price = request.POST.get('decoration_price')
            print(str(decoration)+" "+str(decoration_price))

            wifi = None
            wifi_price = None
            if request.POST.get('wifi') == 'WiFi':
                wifi = True
                wifi_price = request.POST.get('wifi_price')
            print(str(wifi)+' '+str(wifi_price))

            valet_parking_price = None
            valet_parking = None
            if request.POST.get('valet_parking') == 'Valet Parking':
                valet_parking = True
                valet_parking_price = request.POST.get('valet_parking_price')
            print(str(valet_parking)+' '+str(valet_parking_price))

            outside_catering_price = None
            outside_catering = None
            if request.POST.get('outside_catering') == 'Outside Catering':
                outside_catering = True
                outside_catering_price = request.POST.get('outside_catering_price')
            print(str(outside_catering)+' '+str(outside_catering_price))

            heater_price = None
            heater = None
            if request.POST.get('heater') == 'Heater':
                heater = True
                heater_price = request.POST.get('heater_price')
            print(str(heater)+' '+str(heater_price))

            air_conditioner_price = None
            air_conditioner = None
            if request.POST.get('air_conditioner') == 'Air Conditioner':
                air_conditioner = True
                air_conditioner_price = request.POST.get('air_conditioner_price')
            print(str(air_conditioner)+' '+str(air_conditioner_price))

            dj_system_price = None
            dj_system = None
            if request.POST.get('dj_system') == 'DJ System':
                dj_system = True
                dj_system_price = request.POST.get('dj_system_price')
            print(str(dj_system)+' '+str(dj_system_price))

            bridal_room_price = None
            bridal_room = None
            if request.POST.get('bridal_room') == 'Bridal Room':
                bridal_room = True
                bridal_room_price = request.POST.get('bridal_room_price')
            print(str(bridal_room)+' '+str(bridal_room_price))
            
            generator_price = None
            generator = None
            if request.POST.get('generator') == 'Generator':
                generator = True
                generator_price = request.POST.get('generator_price')
            print(str(generator)+' '+str(generator_price))

            outside_dj_price = None
            outside_dj = None
            if request.POST.get('outside_dj') == 'Outside DJ':
                outside_dj = True
                outside_dj_price = request.POST.get('outside_dj_price')
            print(str(outside_dj)+' '+str(outside_dj_price))

            outside_decoration_price = None
            outside_decoration = None
            if request.POST.get('outside_decoration') == 'Outside Decoration':
                outside_decoration = True
                outside_decoration_price = request.POST.get('outside_decoration_price')
            print(str(outside_decoration)+' '+str(outside_decoration_price))

            bridal_makeup_price = None
            bridal_makeup = None
            if request.POST.get('bridal_makeup') == 'Bridal Makeup':
                bridal_makeup = True
                bridal_makeup_price = request.POST.get('bridal_makeup_price')
            print(str(bridal_makeup)+' '+str(bridal_makeup_price))
            
            sitting_capacity = request.POST.get('sitting_capacity')
            parking_capacity = request.POST.get('parking_capacity')
            
            venue = Venue.objects.create(author=request.user, detail_id=detail, sitting_capacity=sitting_capacity, 
                category=category, parking_capacity=parking_capacity,  air_conditioner=air_conditioner, heater=heater, dj_system=dj_system,
                wifi=wifi, bridal_room=bridal_room, valet_parking=valet_parking, decoration=decoration, generator=generator,
                outside_catering=outside_catering, outside_dj=outside_dj, outside_decoration=outside_decoration)
            
            per_head_price = request.POST.get('per_head_price')
            VenuePrice.objects.create(venue_id=venue, per_guest=per_head_price, wifi=wifi_price, heater=heater_price, 
                 dj_system=dj_system_price, decoration=decoration_price, bridal_room= bridal_room_price, valet_parking=valet_parking_price,
                 outside_catering=outside_catering_price, air_conditioner=air_conditioner_price, 
                 generator=generator_price, outside_dj=outside_dj_price, outside_decoration=outside_decoration_price,
                 bridal_makeup=bridal_makeup_price)
            
            leng = request.POST.get('menu')
            leng= int(leng)+1
            if request.POST:
                i = 1
                for index in range(i,leng):
                    print(index)
                    dish_title =""
                    dish_description =""
                    price =""
                    flag=0
                    if 'menu_title_'+str(index) in request.POST:
                        menu_title= request.POST['menu_title_'+str(index)]
                        flag = 1
                    if 'menu_description_'+str(index) in request.POST:
                        menu_description= request.POST['menu_description_'+str(index)]
                        flag = 1
                    if 'menu_price_'+str(index)  in request.POST:
                        menu_price= request.POST['menu_price_'+str(index)]         
                        flag = 1

                    if flag == 1: 
                        Dish_Menu.objects.create(venue_id=venue, title=menu_title, description=menu_description, price=menu_price) 
            return None

        else:
            return render(request,'ad/post.html')
    else:
        messages.error(request, 
            "You have to login first to post an Ad.",
            extra_tags="message")
        return render(request,'user/login.html')



def display(request, id):

    featured_details = Detail.objects.filter(featured=True)
    featured_details_images   = {}
    featured_details_paarize  = {}
    
    
    for detail in featured_details:
        featured_details_images[detail.id] = images.objects.filter(detail_id=detail).first()
        featured_details_paarize[detail.id] = str(Dish_Menu.objects.get(venue_id = Venue.objects.get(detail_id = detail.id)))

    detail = Detail.objects.get(id=id)
    image = images.objects.filter(detail_id=id)
    venue = Venue.objects.get(detail_id=id)
    venuePrice = VenuePrice.objects.get(venue_id=venue)
    dishMenu = Dish_Menu.objects.get(venue_id=venue)
    C = contact.objects.get(detail_id=detail) 
    phoneNo = C.phone
    context = {
       'details':detail,
       'images':image,
       'venues':venue,
       'venuePrices':venuePrice,
       'dishMenus':dishMenu,
       'phoneNo':phoneNo,
       'featured_details':featured_details,
       'featured_details_images':featured_details_images,
       'featured_details_paarize':featured_details_paarize,
    }
    return render(request,"ad/display.html", context)

def search(request, category, city,  min_price, max_price):
    venuePrice = VenuePrice.objects.filter(per_guest__lte=max_price)
    vPrice = venuePrice.filter(per_guest__gte=min_price)
    search_details_images = {}
    search_details_price = {}
    dic = {}     
    if category == 'None':
        if city == 'None':
            if max_price == '0' and min_price == '0':
                detail = Detail.objects.all()
                for deta in detail:
                    dic[deta.id] = deta
                for detail in dic:   
                    search_details_images[detail] = images.objects.filter(detail_id=detail).first()
                    search_details_price[detail] = str(Dish_Menu.objects.filter(venue_id = Venue.objects.get(detail_id = detail)).first())
                context = {
                    'det' : dic,
                    'search_details_images': search_details_images,
                    'search_details_price' : search_details_price

                }
                return render(request,"ad/search.html",context)
            else:
                for ven in vPrice:
                    dic[ven.venue_id.detail_id.id] = Detail.objects.get(id=ven.venue_id.detail_id.id)

                for detail in dic:   
                    search_details_images[detail] = images.objects.filter(detail_id=detail).first()
                    search_details_price[detail] = str(Dish_Menu.objects.filter(venue_id = Venue.objects.get(detail_id = detail)).first())
                context = {
                    'det' : dic,
                    'search_details_images': search_details_images,
                    'search_details_price' : search_details_price

                }
                return render(request,"ad/search.html",context)  
        else:
            if max_price == '0' and min_price == '0':
                location = Location.objects.filter(city=city)
                for loc in location:
                   dic[loc.id] = Detail.objects.get(loction_id=loc.id)
                for detail in dic:   
                    search_details_images[detail] = images.objects.filter(detail_id=detail).first()
                    search_details_price[detail] = str(Dish_Menu.objects.filter(venue_id = Venue.objects.get(detail_id = detail)).first())
                context = {
                    'det' : dic,
                    'search_details_images': search_details_images,
                    'search_details_price' : search_details_price

                }
                return render(request,"ad/search.html",context)
            else:
                for ven in vPrice:
                    dic[ven.venue_id.detail_id.id] = Detail.objects.get(id=ven.venue_id.detail_id.id)
                for detail in dic:   
                    search_details_images[detail] = images.objects.filter(detail_id=detail).first()
                    search_details_price[detail] = str(Dish_Menu.objects.filter(venue_id = Venue.objects.get(detail_id = detail)).first())
                context = {
                    'det' : dic,
                    'search_details_images': search_details_images,
                    'search_details_price' : search_details_price

                }
                return render(request,"ad/search.html",context)
    else:    
        if city == 'None':
            if max_price == '0' and min_price == '0':
                venue = Venue.objects.filter(category=category)
                for ven in venue:
                    dic[ven.detail_id.id] = Detail.objects.get(id=ven.detail_id.id)
                for detail in dic:   
                    search_details_images[detail] = images.objects.filter(detail_id=detail).first()
                    search_details_price[detail] = str(Dish_Menu.objects.filter(venue_id = Venue.objects.get(detail_id = detail)).first())
                context = {
                    'det' : dic,
                    'search_details_images': search_details_images,
                    'search_details_price' : search_details_price

                }
                return render(request,"ad/search.html",context)
            else:
                for ven in vPrice:
                    dic[ven.venue_id.detail_id.id] = Detail.objects.get(id=ven.venue_id.detail_id.id)
                for detail in dic:   
                    search_details_images[detail] = images.objects.filter(detail_id=detail).first()
                    search_details_price[detail] = str(Dish_Menu.objects.filter(venue_id = Venue.objects.get(detail_id = detail)).first())
                context = {
                    'det' : dic,
                    'search_details_images': search_details_images,
                    'search_details_price' : search_details_price

                }
                return render(request,"ad/search.html",context)  
        else:
            if max_price == '0' and min_price == '0':
                location = Location.objects.filter(city=city)
                for loc in location:
                    detail = Detail.objects.get(loction_id=loc.id)
                    venue = Venue.objects.get(detail_id=detail.id)
                    if venue.category == category:
                        dic[venue.detail_id.id] = Detail.objects.get(id=venue.detail_id.id)
                for detail in dic:   
                    search_details_images[detail] = images.objects.filter(detail_id=detail).first()
                    search_details_price[detail] = str(Dish_Menu.objects.filter(venue_id = Venue.objects.get(detail_id = detail)).first())
                context = {
                    'det' : dic,
                    'search_details_images': search_details_images,
                    'search_details_price' : search_details_price

                }
                return render(request,"ad/search.html",context)
            else:
                for ven in vPrice:
                    dic[ven.venue_id.detail_id.id] = Detail.objects.get(id=ven.venue_id.detail_id.id)
                for detail in dic:   
                    search_details_images[detail] = images.objects.filter(detail_id=detail).first()
                    search_details_price[detail] = str(Dish_Menu.objects.filter(venue_id = Venue.objects.get(detail_id = detail)).first())
                context = {
                    'det' : dic,
                    'search_details_images': search_details_images,
                    'search_details_price' : search_details_price

                }
                return render(request,"ad/search.html",context)


def edit(request, id):

    detail = Detail.objects.get(id=id)
    image = images.objects.filter(detail_id=id)
    venue = Venue.objects.get(detail_id=id)
    venuePrice = VenuePrice.objects.get(venue_id=venue)
    dishMenu = Dish_Menu.objects.filter(venue_id=venue)
    context = {
       'details':detail,
       'images':image,
       'venues':venue,
       'prices':venuePrice,
       'menus':dishMenu,
    }
    print(venue.decoration)
    print(venue.wifi)
    print(venue.valet_parking)
    print(venue.outside_catering)
    print(venue.heater)
    print(venue.air_conditioner)
    print(venue.dj_system)
    print(venue.bridal_room)
    print(venue.generator)
    print(venue.outside_dj)
    print(venue.outside_decoration)
    print(venue.bridal_makeup)

    if request.method == 'POST':
        post_title =request.POST.get('post_title')
        city =request.POST.get('city')
        area =request.POST.get('area')
        street =request.POST.get('street')
        post_description =request.POST.get('post_description')

        guest_price =request.POST.get('guest_price')
        heater_price =request.POST.get('heater_price')
        dj_system_price =request.POST.get('dj_system_price')
        decoration_price =request.POST.get('decoration_price')
        wiFi_price =request.POST.get('wiFi_price')
        BridalRoom_price =request.POST.get('BridalRoom_price')

        dish_title =request.POST.get('dish_title')
        dish_description =request.POST.get('dish_description')
        price =request.POST.get('price')
        sitting_capacity =request.POST.get('sitting_capacity')
        parking_capacity =request.POST.get('parking_capacity')

        name =request.POST.get('name')
        phone =request.POST.get('phone')

        decoration =request.POST.get('decoration')
        if decoration == 'on':
            decoration = True
        else:
            decoration = False

        wifi =request.POST.get('wifi')
        if wifi == 'on':
            wifi = True
        else:
            wifi = False

        valet_parking =request.POST.get('valet_parking')
        if valet_parking == 'on':
            valet_parking = True
        else:
            valet_parking = False

        heater =request.POST.get('heater')
        if heater == 'on':
            heater = True
        else:
            heater = False

        ac =request.POST.get('ac')
        if ac == 'on':
            ac = True
        else:
            ac = False

        dj_system =request.POST.get('dj_system')
        if dj_system == 'on':
            dj_system = True
        else:
            dj_system = False

        bridal_room =request.POST.get('bridal_room')
        if bridal_room == 'on':
            bridal_room = True
        else:
            bridal_room = False

        generator =request.POST.get('generator')
        if generator == 'on':
            generator = True
        else:
            generator = False

        outside_dj =request.POST.get('outside_dj')
        if outside_dj == 'on':
            outside_dj = True
        else:
            outside_dj = False

        outside_decoration =request.POST.get('outside_decoration')
        if outside_decoration == 'on':
            outside_decoration = True
        else:
            outside_decoration = False

        outside_catering =request.POST.get('outside_catering')
        if outside_catering == 'on':
            outside_catering = True
        else:
            outside_catering = False
        category = request.POST.get('category')
     
        Detail.objects.filter(id=id).update(title=post_title,description=post_description)  
        Location.objects.filter(id=Detail.objects.get(id=id).loction_id.id).update(city=city, area=area, street=street)

        for img in request.FILES.getlist('images'):
            images.objects.create(title=post_title, detail_id=Detail.objects.get(id=id),image=img)
            ig = images.objects.filter(detail_id=Detail.objects.get(id=id)).first()
            ig.delete()
        
        contact.objects.filter(detail_id=Detail.objects.get(id=id)).update(name=name, phone=phone)

        Venue.objects.filter(detail_id=id).update(sitting_capacity=sitting_capacity,category=category,
        parking_capacity=parking_capacity,air_conditioner=ac,heater=heater,dj_system=dj_system,wifi=wifi,
        bridal_room=bridal_room,valet_parking=valet_parking,decoration=decoration,generator=generator,
        outside_catering=outside_catering,outside_dj=outside_dj,outside_decoration=outside_decoration)

        VenuePrice.objects.filter(venue_id=venue).update(per_guest=guest_price, wiFi=wiFi_price, heater=heater_price, 
        dj_system=dj_system_price, decoration=decoration_price, BridalRoom= BridalRoom_price)


        leng = Dish_Menu.objects.filter(venue_id=venue).count()
        leng= int(leng)+1
        if request.POST:
            i = 1
            Dish_Menu.objects.filter(venue_id=venue).delete()
            for index in range(i,leng):
                dish_title =""
                dish_description =""
                price =""
                flag=0
                
                if 'dish_title'+str(index) in request.POST:
                    dish_title= request.POST['dish_title'+str(index)]
                    flag = 1
                if 'dish_description'+str(index) in request.POST:
                    dish_description= request.POST['dish_description'+str(index)]
                    flag = 1
                if 'price'+str(index)  in request.POST:
                    price= request.POST['price'+str(index)]         
                    flag = 1
                if flag == 1: 
                    Dish_Menu.objects.create(title=dish_title,venue_id=venue,description=dish_description,price=price)
                


        return redirect('/')

    else:
        return render(request,"ad/edit.html", context)

def ads(request):
    ads_details_images = {}
    details = {}
    venue = Venue.objects.filter(author=request.user)
    for ven in venue:
        details[ven.detail_id.id] = Detail.objects.get(id=ven.detail_id.id)

    for det in details:   
        ads_details_images[det] = images.objects.filter(detail_id=det).first()

    context = {
        'record':details,
        'ads_details_images': ads_details_images,
    }
    return render(request,'ad/ads.html',context)

def delete(request, id):
    try:
        detail = Detail.objects.get(id=id)
        loc = Location.objects.get(id=detail.loction_id.id)
    except:
        messages.error(request, "There was an error deleting your ad")
        return HttpResponseRedirect('/user/my-ads/')            
    if request.method == 'POST':
        loc.delete()
        messages.success(request, "Your ad has been deleted")
        return HttpResponseRedirect('/user/my-ads/')
    return render(request,'ad/delete.html')


def deactivate(request, id):
    try:
        detail = Detail.objects.get(id=id)
        loc = Location.objects.get(id=detail.loction_id.id)
    except:
        messages.error(request, "There was an error deactivating your ad")
        return HttpResponseRedirect('/user/my-ads/')   
    if request.method == 'POST':
        detail.status = "Deactive"
        detail.save()
        messages.success(request, "Your ad has been deactivated")
        return HttpResponseRedirect('/user/my-ads/')
    return render(request,'ad/deactivate.html')

def activate(request, id):
    try:
        detail = Detail.objects.get(id=id)
        loc = Location.objects.get(id=detail.loction_id.id)
    except:
        messages.error(request, "There was an error deactivating your ad")
        return HttpResponseRedirect('/user/my-ads/')
    if request.method == 'POST':
        detail.status = "Active"
        detail.save()
        messages.success(request, "Your ad has been activated")
        return HttpResponseRedirect('/user/my-ads/')
    return render(request,'ad/activate.html')