# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class Academy(http.Controller):
    
    @http.route(['/academy/teacher_form'], type='http', auth="user", website=True)
    def teacher_form(self, **post):
        return request.render('academy.create_teacher',{})
	
    
    @http.route(['/academy/form/submit'], type='http', auth="user", website=True)
    def teacher_form_submit(self, **post):
        teacher = request.env['academy.teachers'].create({
            'name': post.get('name'),
			'lastname': post.get('lastname'),
			'birth_day': post.get('birth_day'),
			'card_number': post.get('card_number'),
			'birthplace' : post.get('birthplace')
        })
      
        return request.render("academy.teacher_form_success",{
            'teacher': teacher,
        })		
	
	#To the browser
    @http.route('/academy/hello/', auth='public')
    def welcome(self, **kw):
        return "Hello, world1111"

    #Templates
    @http.route('/academy/teachers/', auth='public')
    def getteachers(self, **kw):
        return http.request.render('academy.home', {
            'teachers': ["Diana Padilla", "Jody Caroll", "Lester Vaughn"],
        })
    #Storing data in Odoo
    @http.route('/academy/academy/', auth='public')
    def index(self, **kw):
        Teachers = http.request.env['academy.teachers']
        return http.request.render('academy.data', {
            'teachers': Teachers.search([])
        })

    # Website support just add the  flag  website=True  
    @http.route('/academy/data/', auth='user',website=True)
    def getdata(self, **kw):
        Teachers = http.request.env['academy.teachers']
        return http.request.render('academy.index', {
            'teachers': Teachers.search([]),
        })
    # URLs and routing
    @http.route('/academy/<name>/', auth='public', website=True)
    def teacher(self, name):
        return '<h1>{}</h1>'.format(name)

    @http.route('/academy/<int:id>/', auth='public', website=True)
    def teacher1(self, id):
        return '<h1>{} ({})</h1>'.format(id, type(id).__name__)









#    @http.route('/academy/<name>/', auth='public',website=True)
#    def teacher(self, name):
#        return '<h1>{}</h1>'.format(name)
#    @http.route('/academy/<int:id>/', auth='public', website=True)
#    def teacher(self, id):
 #       return '<h1>{} ({})</h1>'.format(id, type(id).__name__)

   # Website support
    @http.route('/academy/<model("academy.teachers"):teacher>/', auth='public', website=True)
    def teacher(self, teacher):
        return http.request.render('academy.biography', {
            'person': teacher
        })



#     @http.route('/academy/academy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('academy.listing', {
#             'root': '/academy/academy',
#             'objects': http.request.env['academy.academy'].search([]),
#         })

#     @http.route('/academy/academy/objects/<model("academy.academy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('academy.object', {
#             'object': obj
#         })
