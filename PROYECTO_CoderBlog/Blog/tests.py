from django.test import TestCase
from django.test import TestCase, SimpleTestCase
from .models import Articulo, User,ImagenArticulo

# Create your tests here.

class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

class ArticuloTests(TestCase):
    @classmethod
    def setUpTestData(self):
        self.imagen = ImagenArticulo.objects.create(nombre="zzzz", imagen = None)
        self.user = User.objects.create(first_name ="aaaaa", email = "aaaaaa@gmail.com", password = "aaaa1234")
        self.articulo = Articulo.objects.create(titulo = "titulo", subtitulo = "subtitulo", texto = "textotextotexto", fecha = "1111-11-11", autor = self.user, imagen= self.imagen)
    
    def test_model_content(self):

        response = self.client.get("/pages/")

        expected = [
            {
                "titulo": self.articulo.titulo,
                "subtitulo": self.articulo.subtitulo,
                "texto": self.articulo.texto,
                "fecha": self.articulo.fecha,
                "autor": self.articulo.autor.id,
                "imagen": self.articulo.imagen.id,
            }
        ]
        self.assertEqual(response.status_code , 200)
        self.assertEqual(Articulo.objects.count(),1)
        

class ArticuloPost(TestCase):
    @classmethod
    def setUpTestData(self):
        self.imagen1 = ImagenArticulo.objects.create(nombre="zzzdbfdbz", imagen = None)
        self.user1 = User.objects.create(first_name ="aaajsryjhaa", email = "aaasrgaaa@gmail.com", password = "aaaasergse1234", username = "dfgdfsgfds")
        self.articulo1 = Articulo.objects.create(titulo = "titughsedlo", subtitulo = "subtedthgsedgitulo", texto = "textotextdegsdeotexto", fecha = "2011-11-11", autor = self.user1, imagen= self.imagen1)
     
        self.imagen2 = ImagenArticulo.objects.create(nombre="fdfdfhf", imagen = None)
        self.user2 = User.objects.create(first_name ="bbbbb", email = "aaafffa@gmail.com", password = "aadgthdaa1234")
        self.articulo2 = Articulo.objects.create(titulo = "titulsgfso", subtitulo = "subtsfgsfitulo", texto = "textotsfgsfgextotexto", fecha = "1311-11-11", autor = self.user2, imagen= self.imagen2)


    def test_delete_article(self):
        
        self.articulo1.delete()
        self.assertEqual(Articulo.objects.count(),1)