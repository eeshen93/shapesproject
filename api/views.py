from urllib import response
from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Shape
from .serializers import ShapeSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import customuser
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from rest_framework.views import APIView

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	user1=request.user.email
	print (user1)
	api_urls = {
		'List':'/shape-list/',
		'Detail View':'/shape-detail/<str:pk>/',
		'Create':'/shape-create/',
		'Update':'/shape-update/<str:pk>/',
		'Delete':'/shape-delete/<str:pk>/',
		}

	return Response(api_urls)

class shapes_view(APIView):

	def get_queryset(self, request):
		user1=request.user
		shapes=Shape.objects.filter(user=user1.id)
		serializer=ShapeSerializer(shapes, many=True)
		return Response(serializer.data)


	def get(self,request):
		user1=request.user
		shapes=Shape.objects.filter(user=user1.id)
		serializer=ShapeSerializer(shapes, many=True)
		return Response(serializer.data)
		

	def post(self,request):
		
		user=request.user
		data={}
		if user.is_authenticated:
			data=request.data
			#print (data)
			try:
				data['side1']=float(data['side1'])
			except:
				pass
			try:
				data['side2']=float(data['side2'])
			except:
				pass
			try:
				data['side3']=float(data['side3'])
			except:
				pass
		

			data['user']=user.id
			

			if data['shape_type']=='square':
				data['area']=data['side1']**2
				data['perimeter']=data['side1']*4
				data['msg']='calculated'
				pass
			elif data['shape_type'] == 'rectangle':
				data['side2']=data['side2']
				## check for input mistakes ##
				if data['side2'] == data['side1']:
					
					#return Response({'error': 'This is a square, not a rectangle.'})
					data['area']=0
					data['perimeter']=0
					data['msg']='error: This is a square, not a rectangle.'

				else:
					
					data['area']=data['side1']*data['side2']
					data['perimeter']=(data['side1']*2)+(data['side2']*2)
					data['msg']='calculated'

		
			elif data['shape_type'] == 'diamond':
				data['side2']=data['side2']
				## check for input mistakes ##
				if 2*data['side1'] <= data['side2']:
					
					#return Response({'error': 'Make sure 2 × a > p'})
					data['area']=0
					data['perimeter']=0
					data['msg']='error: Make sure 2 × a > p'
				else:
					
					data['area']= 0.5 * data['side2'] * (((4*(data['side1']**2)) - data['side2']**2)**0.5)
					data['perimeter']=data['side1']*4
					data['msg']='calculated'

			elif data['shape_type'] == 'triangle':
				
				data['side2']=data['side2']
				data['side3']=data['side3']

				## check for input mistakes ##
				if data['side1']+data['side2']<=data['side3'] or data['side1']+data['side3']<=data['side2'] or data['side3']+data['side2']<=data['side1']:
					#return Response({'error': 'Not a triangle, sum of 2 sides must be greater than the 3rd side.'})
					data['area']=0
					data['perimeter']=0
					data['msg']='error: Not a triangle, sum of 2 sides must be greater than the 3rd side.'
				
				else:
					### area working for triangle ##
					p=data['side1']+data['side2']+data['side3']
					s=p/2
					data['area']=(s*(s-data['side1'])*(s-data['side2'])*(s-data['side3']))**0.5
					###
					data['perimeter']=p
					data['msg']='calculated'


			serializer=ShapeSerializer(data=data)
			if serializer.is_valid():
				serializer.save()
				

		return Response(serializer.data)

	def put(self, request,pk):
		user=request.user
		if user.is_authenticated:
			
			shape = Shape.objects.get(id=pk)
			data=request.data
			try:
				data['side1']=float(data['side1'])
			except:
				pass
			try:
				data['side2']=float(data['side2'])
			except:
				pass
			try:
				data['side3']=float(data['side3'])
			except:
				pass

			
			
			data['user']=user.id

			if data['shape_type']=='square':
				data['area']=data['side1']**2
				data['perimeter']=data['side1']*4
				data['msg']='calculated'
				pass

			elif data['shape_type'] == 'rectangle':
				data['side2']=data['side2']
				
				if data['side2'] == data['side1']: ## check for input mistakes ##
					#return Response({'error': 'This is a square, not a rectangle.'})
					data['area']=0
					data['perimeter']=0
					data['msg']='error: This is a square, not a rectangle.'

				else:
					data['area']=data['side1']*data['side2']
					data['perimeter']=(data['side1']*2)+(data['side2']*2)
					data['msg']='calculated'

		
			elif data['shape_type'] == 'diamond':
				data['side2']=data['side2']
				
				if 2*data['side1'] <= data['side2']: ## check for input mistakes ##
					#return Response({'error': 'Make sure 2 × a > p'})
					data['area']=0
					data['perimeter']=0
					data['msg']='error: Make sure 2 × a > p'

				else:
					data['area']= 0.5 * data['side2'] * (((4*(data['side1']**2)) - data['side2']**2)**0.5)
					data['perimeter']=data['side1']*4
					data['msg']='calculated'

			elif data['shape_type'] == 'triangle':

				data['side2']=data['side2']
				data['side3']=data['side3']

				if data['side1']+data['side2']<=data['side3'] or data['side1']+data['side3']<=data['side2'] or data['side3']+data['side2']<=data['side1']: ## check for input mistakes ##
					#return Response({'error': 'Not a triangle, sum of 2 sides must be greater than the 3rd side.'})
					data['area']=0
					data['perimeter']=0
					data['msg']='error: Not a triangle, sum of 2 sides must be greater than the 3rd side.'
				
				
				else:
					### area working for triangle ##
					p=data['side1']+data['side2']+data['side3']
					s=p/2
					data['area']=(s*(s-data['side1'])*(s-data['side2'])*(s-data['side3']))**0.5
					###
					data['perimeter']=p
					data['msg']='calculated'


			serializer=ShapeSerializer(instance=shape, data=data)
			if serializer.is_valid():
				serializer.save()

			return Response('Entry updated.')

	def delete(self, request,pk):
		shape = Shape.objects.get(id=pk)
		shape.delete()

		return Response('Entry deleted.')





@api_view(['GET',])
def api_shapes(request):
	user1=request.user
	shapes=Shape.objects.filter(user=user1.id)
	serializer=ShapeSerializer(shapes, many=True)

	return Response(serializer.data)
	

@api_view(['POST',])
def api_create_shape(request):
	user=request.user
	data={}
	if user.is_authenticated:
		data=request.data
		#print (data)
		try:
			data['side1']=float(data['side1'])
		except:
			pass
		try:
			data['side2']=float(data['side2'])
		except:
			pass
		try:
			data['side3']=float(data['side3'])
		except:
			pass
	

		data['user']=user.id
		

		if data['shape_type']=='square':
			data['area']=data['side1']**2
			data['perimeter']=data['side1']*4
			data['msg']='calculated'
			pass
		elif data['shape_type'] == 'rectangle':
			data['side2']=data['side2']
			## check for input mistakes ##
			if data['side2'] == data['side1']:
				
				#return Response({'error': 'This is a square, not a rectangle.'})
				data['area']=0
				data['perimeter']=0
				data['msg']='error: This is a square, not a rectangle.'

			else:
				
				data['area']=data['side1']*data['side2']
				data['perimeter']=(data['side1']*2)+(data['side2']*2)
				data['msg']='calculated'

	
		elif data['shape_type'] == 'diamond':
			data['side2']=data['side2']
			## check for input mistakes ##
			if 2*data['side1'] <= data['side2']:
				
				#return Response({'error': 'Make sure 2 × a > p'})
				data['area']=0
				data['perimeter']=0
				data['msg']='error: Make sure 2 × a > p'
			else:
				
				data['area']= 0.5 * data['side2'] * (((4*(data['side1']**2)) - data['side2']**2)**0.5)
				data['perimeter']=data['side1']*4
				data['msg']='calculated'

		elif data['shape_type'] == 'triangle':
			
			data['side2']=data['side2']
			data['side3']=data['side3']

			## check for input mistakes ##
			if data['side1']+data['side2']<=data['side3'] or data['side1']+data['side3']<=data['side2'] or data['side3']+data['side2']<=data['side1']:
				#return Response({'error': 'Not a triangle, sum of 2 sides must be greater than the 3rd side.'})
				data['area']=0
				data['perimeter']=0
				data['msg']='error: Not a triangle, sum of 2 sides must be greater than the 3rd side.'
			
			else:
				### area working for triangle ##
				p=data['side1']+data['side2']+data['side3']
				s=p/2
				data['area']=(s*(s-data['side1'])*(s-data['side2'])*(s-data['side3']))**0.5
				###
				data['perimeter']=p
				data['msg']='calculated'


		serializer=ShapeSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			

	return Response(serializer.data)

@api_view(['DELETE',])
def api_delete_shape(request,pk):
	shape = Shape.objects.get(id=pk)
	shape.delete()

	return Response('Entry deleted.')

@api_view(['POST',])
def api_update_shape(request,pk):
	user=request.user
	if user.is_authenticated:
		
		shape = Shape.objects.get(id=pk)
		data=request.data
		try:
			data['side1']=float(data['side1'])
		except:
			pass
		try:
			data['side2']=float(data['side2'])
		except:
			pass
		try:
			data['side3']=float(data['side3'])
		except:
			pass

		
		
		data['user']=user.id

		if data['shape_type']=='square':
			data['area']=data['side1']**2
			data['perimeter']=data['side1']*4
			data['msg']='calculated'
			pass

		elif data['shape_type'] == 'rectangle':
			data['side2']=data['side2']
			
			if data['side2'] == data['side1']: ## check for input mistakes ##
				#return Response({'error': 'This is a square, not a rectangle.'})
				data['area']=0
				data['perimeter']=0
				data['msg']='error: This is a square, not a rectangle.'

			else:
				data['area']=data['side1']*data['side2']
				data['perimeter']=(data['side1']*2)+(data['side2']*2)
				data['msg']='calculated'

	
		elif data['shape_type'] == 'diamond':
			data['side2']=data['side2']
			
			if 2*data['side1'] <= data['side2']: ## check for input mistakes ##
				#return Response({'error': 'Make sure 2 × a > p'})
				data['area']=0
				data['perimeter']=0
				data['msg']='error: Make sure 2 × a > p'

			else:
				data['area']= 0.5 * data['side2'] * (((4*(data['side1']**2)) - data['side2']**2)**0.5)
				data['perimeter']=data['side1']*4
				data['msg']='calculated'

		elif data['shape_type'] == 'triangle':

			data['side2']=data['side2']
			data['side3']=data['side3']

			if data['side1']+data['side2']<=data['side3'] or data['side1']+data['side3']<=data['side2'] or data['side3']+data['side2']<=data['side1']: ## check for input mistakes ##
				#return Response({'error': 'Not a triangle, sum of 2 sides must be greater than the 3rd side.'})
				data['area']=0
				data['perimeter']=0
				data['msg']='error: Not a triangle, sum of 2 sides must be greater than the 3rd side.'
			
			
			else:
				### area working for triangle ##
				p=data['side1']+data['side2']+data['side3']
				s=p/2
				data['area']=(s*(s-data['side1'])*(s-data['side2'])*(s-data['side3']))**0.5
				###
				data['perimeter']=p
				data['msg']='calculated'


		serializer=ShapeSerializer(instance=shape, data=data)
		if serializer.is_valid():
			serializer.save()

		return Response('Entry updated.')