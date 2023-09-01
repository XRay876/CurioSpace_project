from django.shortcuts import get_object_or_404, redirect, render
from datetime import date

from django.urls import reverse

from .models import *
from .forms import SaveCommentForm, fill_TODO_form, System_form, Modules_form, Products_form, ArchLayout_form, ProductsVeh_form, ProductsVnedr_form, Resources_form

from django.contrib import messages
import json
import logging

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse

from django.views.generic import TemplateView

from django.db.models import IntegerField
from django.db.models.functions import Cast

from django.contrib.sessions.models import Session




def index(request):
    selected_table = request.GET.get('table', 'fill_TODO')
    if selected_table == 'fill_TODO':
        table_data = fill_TODO.objects.annotate(uid_int=Cast('uid', IntegerField())).order_by('uid_int')
    elif selected_table == 'System':
        table_data = System.objects.all()
    elif selected_table == 'Modules':
        table_data = Modules.objects.annotate(uModulesID_int=Cast('uModulesID', IntegerField())).order_by('uModulesID_int')
    elif selected_table == 'Products':
        table_data = Products.objects.order_by('uID')
    elif selected_table == 'ArchLayout':
        table_data = ArchLayout.objects.annotate(uArchID_int=Cast('uArchID', IntegerField())).order_by('uArchID_int')
    elif selected_table == 'ProductsVeh':
        table_data = ProductsVeh.objects.annotate(uVehID_int=Cast('uVehID', IntegerField())).order_by('uVehID_int')
    elif selected_table == 'ProductsVnedr':
        table_data = ProductsVnedr.objects.order_by('uVnedrID')
    elif selected_table == 'Resources':
        table_data = Resources.objects.all()
    else:
        # Обработка других вариантов таблицы, если необходимо
        table_data = None
    
    context = {
        'selected_table': selected_table,
        'table_data': table_data,
        
        
    }

    return render(request, 'main/index.html', context)
        

def about(request):
    fill_TODO_form_instance = None
    system_form_instance = None
    modules_form_instance = None
    products_form_instance = None
    arch_layout_form_instance = None
    products_veh_form_instance = None
    products_vnedr_form_instance = None
    resources_form_instance = None
    resources_form_errors = None

    form_success = False

    selected_table = None

    if request.method == 'POST':
        selected_table = request.POST['table']

        if selected_table == 'fill_TODO':
            fill_TODO_form_instance = fill_TODO_form(request.POST)
            if fill_TODO_form_instance.is_valid():
                fill_TODO_instance = fill_TODO_form_instance.save(commit=False)
                fill_TODO_instance.save()
                form_success = True
            else:
                fill_TODO_form_errors = fill_TODO_form_instance.errors
        elif selected_table == 'System':
            system_form_instance = System_form(request.POST)
            if system_form_instance.is_valid():
                system_instance = system_form_instance.save(commit=False)
                system_instance.save()
                form_success = True
            else:
                system_form_errors = system_form_instance.errors
        elif selected_table == 'Modules':
            modules_form_instance = Modules_form(request.POST)
            if modules_form_instance.is_valid():
                modules_instance = modules_form_instance.save(commit=False)
                modules_instance.save()
                form_success = True
            else:
                modules_form_errors = modules_form_instance.errors
        elif selected_table == 'Products':
            products_form_instance = Products_form(request.POST)
            if products_form_instance.is_valid():
                products_instance = products_form_instance.save(commit=False)
                products_instance.save()
                form_success = True
            else:
                products_form_errors = products_form_instance.errors
        elif selected_table == 'ArchLayout':
            arch_layout_form_instance = ArchLayout_form(request.POST)
            if arch_layout_form_instance.is_valid():
                arch_layout_instance = arch_layout_form_instance.save(commit=False)
                arch_layout_instance.save()
                form_success = True
            else:
                arch_layout_form_errors = arch_layout_form_instance.errors
        elif selected_table == 'ProductsVeh':
            products_veh_form_instance = ProductsVeh_form(request.POST)
            if products_veh_form_instance.is_valid():
                products_veh_instance = products_veh_form_instance.save(commit=False)
                products_veh_instance.save()
                form_success = True
            else:
                products_veh_form_errors = products_veh_form_instance.errors
        elif selected_table == 'ProductsVnedr':
            products_vnedr_form_instance = ProductsVnedr_form(request.POST)
            if products_vnedr_form_instance.is_valid():
                products_vnedr_instance = products_vnedr_form_instance.save(commit=False)
                products_vnedr_instance.save()
                form_success = True
            else:
                products_vnedr_form_errors = products_vnedr_form_instance.errors
        elif selected_table == 'Resources':
            resources_form_instance = Resources_form(request.POST)
            if resources_form_instance.is_valid():
                resources_instance = resources_form_instance.save(commit=False)
                resources_instance.save()
                form_success = True
            else:
                resources_form_errors = resources_form_instance.errors

    else:
        fill_TODO_form_instance = fill_TODO_form()
        system_form_instance = System_form()
        modules_form_instance = Modules_form()
        products_form_instance = Products_form()
        arch_layout_form_instance = ArchLayout_form()
        products_veh_form_instance = ProductsVeh_form()
        products_vnedr_form_instance = ProductsVnedr_form()
        resources_form_instance = Resources_form()

    context = {
        'fill_TODO_form': fill_TODO_form_instance,
        'fill_TODO_form_errors': fill_TODO_form_errors if 'fill_TODO_form_errors' in locals() else None,
        'system_form': system_form_instance,
        'system_form_errors': system_form_errors if 'system_form_errors' in locals() else None,
        'modules_form': modules_form_instance,
        'modules_form_errors': modules_form_errors if 'modules_form_errors' in locals() else None,
        'products_form': products_form_instance,
        'products_form_errors': products_form_errors if 'products_form_errors' in locals() else None,
        'arch_layout_form': arch_layout_form_instance,
        'arch_layout_form_errors': arch_layout_form_errors if 'arch_layout_form_errors' in locals() else None,
        'products_veh_form': products_veh_form_instance,
        'products_veh_form_errors': products_veh_form_errors if 'products_veh_form_errors' in locals() else None,
        'products_vnedr_form': products_vnedr_form_instance,
        'products_vnedr_form_errors': products_vnedr_form_errors if 'products_vnedr_form_errors' in locals() else None,
        'resources_form': resources_form_instance,
        'resources_form_errors': resources_form_errors if 'resources_form_errors' in locals() else None,
        'selected_table': selected_table,
        'form_success' : form_success
    }

    return render(request, 'main/about.html', context)





def diagram(request):
    deviation_colors = {
        'Не определен': 'White',
        '<резерв>': 'LightBlue',
        'Не эксплуатируется': 'LightBlue',
        'На паузе': 'White',
        'Эксплуатируется/Завершен': 'LightGreen'
    }

    products = Products.objects.all()
    resources = Resources.objects.all()

    data = []
    for product in products:
        try:
            manager = resources.filter(uResID=product.uRP).first()

            deviation_product = ''
            if product.uStopTime:
                deviation_product = (product.uStopTime - date.today()).days

            organization = product.uComponentA
            if 'IMS4 old' in organization:
                organization = 'IMS4 old'
            elif 'IMS3' in organization:
                organization = 'IMS3'
            elif 'IMS4 new' in organization:
                organization = 'IMS4 new'
            elif 'ПП' in organization:
                organization = 'ПП'
            else:
                organization = ''

            products_veh = ProductsVeh.objects.filter(uVehProductID=product.uID)
            products_data = []

            for veh in products_veh:
                deviation_veh = None
                if veh.uVehDate:
                    deviation_veh = (veh.uVehDate - date.today()).days

                deviation_color_veh = ''
                if deviation_veh is not None:
                    if veh.uVehClosed == True:
                        deviation_color_veh = 'Green'
                    elif deviation_veh < 0:
                        deviation_color_veh = 'Red'
                    elif deviation_veh >= 0:
                        deviation_color_veh = 'Blue'

                products_data.append({
                    'product': veh.uVehID + '. ' + veh.uVehType + ' ' + veh.uVehDescription,
                    'deadline_veh': veh.uVehDate,
                    'deviation_veh': deviation_veh,
                    'deviation_color_veh': deviation_color_veh,
                    'deviation_product': deviation_product,
                })

            data.append({
                'organization': organization,
                'componentA': product.uConstruction + '. ' + product.uComponentA,
                'procedure': product.uID + '. ' + product.uName,
                'products': products_data,
                'deadline_product': product.uStopTime if product.uStopTime else '',
                'deviation_product': deviation_product,
                'deviation_color': deviation_colors.get(product.uStatus, 'White'),
                'manager': product.uRP if product else ''
            })
        except Exception as e:
            data.append({
                'organization': None,
                'componentA': None,
                'procedure': None,
                'products': [],
                'deadline_product': None,
                'deviation_product': None,
                'deviation_color': 'White',
                'manager': None
            })

    data = sorted(data, key=lambda item: (item['organization'], item['componentA'], item['procedure'], item['manager']))            

    return render(request, 'main/diagram.html', {'data': data})



def save_comment(request):

    form_success = False
    if request.method == 'POST':
        try:            
            form = SaveCommentForm(request.POST)
            if form.is_valid():
                form.save()
                form_success = True
                request.session['form_success'] = form_success
                return redirect(request.META['HTTP_REFERER'])
            else:
                form_success = False
                request.session['form_success'] = form_success

                return JsonResponse({'error': 'Ошибка валидации формы.'}, status=400)
        except Exception as e:
            logging.exception('Ошибка при сохранении комментария:')
            form_success = False
            request.session['form_success'] = form_success
            return JsonResponse({'error': 'Произошла внутренняя ошибка сервера'}, status=500)
    else:
        form_success = False
        request.session['form_success'] = form_success
        return HttpResponse('Invalid request method.')
    
    

def report(request):

    
    surnames = Products.objects.values_list('uRP', flat=True).distinct()
    

    products = Products.objects.all()

    selected_surname = request.GET.get('surname', '')
    if selected_surname != '':
        products = products.filter(uRP=selected_surname)
    # print(selected_surname)

    data = []
    for product in products:
        try:
            products_veh = ProductsVeh.objects.filter(uVehProductID=product.uID)
            products_data = []

            for veh in products_veh:
                
                last_comment = ReportCommentsNew.objects.filter(uProductIDReport=product.uID, uVehIDReport=veh.uVehID).order_by('-date').first()
                last_comment_date = last_comment.date if last_comment else None
                last_comment_text = last_comment.text if last_comment else None

                

                products_data.append({
                    'product_id' : veh.id,
                    'product': veh.uVehID,
                    'last_comment_date': last_comment_date,
                    'last_comment_text': last_comment_text,
                })

            
            main_product_last_comment = ReportCommentsNew.objects.filter(uProductIDReport=product.uID, uVehIDReport='').order_by('-date').first()
            main_product_last_comment_date = main_product_last_comment.date if main_product_last_comment else None
            main_product_last_comment_text = main_product_last_comment.text if main_product_last_comment else None

            

            data.append({
                'procedure_id' : product.id,
                'procedure': product.uID,
                'products': products_data,
                'last_comment_date': main_product_last_comment_date,
                'last_comment_text': main_product_last_comment_text,
                
            })
        except Exception as e:
            data.append({  
                'procedure': None,
                'products': [],
            })

    form_success = request.session.get('form_success', False)

    if form_success:
        del request.session['form_success']

    return render(request, 'main/report.html', {'data': data, 'form_success': form_success, 'surnames' : surnames, 'selected_surname': selected_surname})


def comment_history(request):
    procedure = request.GET.get('procedure')
    veh = request.GET.get('veh')

    # Fetch the comment history for the selected procedure and veh
    comments = ReportCommentsNew.objects.filter(
        uProductIDReport=procedure,
        uVehIDReport=veh
    ).order_by('-date')

    # Prepare the comment data to be sent as JSON response
    comment_data = []
    for comment in comments:
        comment_data.append({
            'date': comment.date.strftime('%d-%m-%Y %H:%M'),  # Format date as a string
            'text': comment.text,
        })

    return JsonResponse(comment_data, safe=False)
    
    



def delete_item(request, table, item_id):
    if table == 'fill_TODO':
        item = fill_TODO.objects.get(id=item_id)
    elif table == 'System':
        item = System.objects.get(id=item_id)
    elif table == 'Modules':
        item = Modules.objects.get(id=item_id)
    elif table == 'Products':
        item = Products.objects.get(id=item_id)
    elif table == 'ArchLayout':
        item = ArchLayout.objects.get(id=item_id)
    elif table == 'ProductsVeh':
        item = ProductsVeh.objects.get(id=item_id)
    elif table == 'ProductsVnedr':
        item = ProductsVnedr.objects.get(id=item_id)
    elif table == 'Resources':
        item = Resources.objects.get(id=item_id)
    else:
        return JsonResponse({'message': 'Ошибка'}, status=400)

    item.delete()
    return redirect(request.META['HTTP_REFERER'])



def edit_item(request, table, item_id):
    if table == 'fill_TODO':
        model = fill_TODO
        form_class = fill_TODO_form
    elif table == 'System':
        model = System
        form_class = System_form
    elif table == 'Modules':
        model = Modules
        form_class = Modules_form
    elif table == 'Products':
        model = Products
        form_class = Products_form
    elif table == 'ArchLayout':
        model = ArchLayout
        form_class = ArchLayout_form
    elif table == 'ProductsVeh':
        model = ProductsVeh
        form_class = ProductsVeh_form
    elif table == 'ProductsVnedr':
        model = ProductsVnedr
        form_class = ProductsVnedr_form
    elif table == 'Resources':
        model = Resources
        form_class = Resources_form


    post = get_object_or_404(model, id=item_id)
    if request.method == "POST":
        form = form_class(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect(reverse('home') + '?table=' + table)
    else:
        form = form_class(instance=post)
    
    context = {
        'edit_form': form,
        'selected_table': table,
        'item_id': item_id,
    }
    
    return render(request, 'main/edit_item.html', context)



def edit_comment(request, item_id, class_veh_or_not):
    if class_veh_or_not == 'YES':
        post = get_object_or_404(Products, id=item_id)
        form = Products_form(request.POST, instance=post)
    elif class_veh_or_not == 'NO':
        post = get_object_or_404(ProductsVeh, id=item_id)
        form = ProductsVeh_form(request.POST, instance=post)
        
    if request.method == "POST":
        

        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect(reverse('report'))
    else:
        if class_veh_or_not == 'YES':
            form = Products_form(instance=post)
        elif class_veh_or_not == 'NO':
            form = ProductsVeh_form(instance=post)
        
    
    context = {
        'edit_comment_form': form,
        'item_id': item_id,
    }
    
    return render(request, 'main/edit_comment.html', context)