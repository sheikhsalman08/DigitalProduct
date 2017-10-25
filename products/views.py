#general 
from django.shortcuts import render
from django.views.generic import DetailView

#for download file
import os
from django.conf import settings
from django.http import HttpResponse
from django.utils.encoding import smart_str
from wsgiref.util import FileWrapper

from .models import Products
from django.shortcuts import redirect, HttpResponseRedirect
from django.contrib.auth.models import User

# Create your views here.

def home(request):
	pictures = Products.objects.filter(type="1")[:4]
	logo = Products.objects.filter(type="2")[:4]
	poster = Products.objects.filter(type="3")[:4]
	videos = Products.objects.filter(type="4")[:4]

	context = {
		'pictures':pictures,
		'logo': logo,
		'poster':poster,
		'videos':videos,
	}
	return render(request,'index.html',context)

def picture(request):
	pictures = Products.objects.filter(type="1")

	path = request.get_full_path()
	context = {
		'path':path,
		'pictures':pictures,
	}
	return render(request,'picture.html',context)

def logo(request):
	logo = Products.objects.filter(type="2")

	context = {
		'logo':logo,
	}
	return render(request,'logo.html',context)

def poster(request):
	poster = Products.objects.filter(type="3")

	context = {
		'poster':poster,
	}
	return render(request,'poster.html',context)

def videos(request):
	videos = Products.objects.filter(type="4")

	context = {
		'videos':videos,
	}
	return render(request,'video.html',context)


class ProductSinglePage(DetailView):
	model = Products
	template_name = "product.html"

	def get_context_data(self, **kwargs):
		context = super(ProductSinglePage, self).get_context_data(**kwargs)
		ThisId = self.kwargs['pk']
		product = Products.objects.get(id=ThisId)
		ThisType = product.type
		RelatedProducts = Products.objects.filter(type=ThisType).exclude(id=ThisId)[:4]
		ProductSize = product.image.size/1000
		ProductName = product.image.name
		print(ProductName)
		context = {
			'product' : product,
			'RelatedProducts':RelatedProducts,
			'ProductSize': ProductSize,
			'ProductName':ProductName,
			'ThisId': ThisId
		}

		return context


# def download_file(request, path):  
# 	response = HttpResponse('image/jpg/png/jpeg/pdf')
# 	# response['Content-Type']='image/png'
# 	response['Content-Disposition'] = "attachment; filename="+path

# 	# 	response['Content-Disposition'] = "attachment; filename='636721521.jpg'"
# 	response['X-Sendfile']= smart_str(os.path.join(settings.MEDIA_ROOT, path))
# 	return response

def download(request, image_id):
    img = Products.objects.get(id=image_id)
    wrapper    =  FileWrapper(open('{}/{}'.format(settings.MEDIA_ROOT, img.image.name),'r'))  # img.file returns full path to the image
    # content_type = mimetypes.guess_type(filename)[0]  # Use mimetypes to get file type
    # response['Content-Length']      = os.path.getsize(img.image)        
    response     = HttpResponse(wrapper,content_type='image/jpg')  
    response['Content-Disposition'] = "attachment; filename=%s" %  img.image
    return response