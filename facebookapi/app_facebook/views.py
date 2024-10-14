""" import facebook
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from decouple import config  # Importer config pour lire les variables depuis .env

class FacebookPostsView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            # Récupérer le jeton d'accès et l'ID de la page depuis le fichier .env
            access_token = config('FACEBOOK_ACCESS_TOKEN')
            page_id = config('PAGE_ID')
            
            # Initialiser l'API Graph avec le jeton d'accès
            graph = facebook.GraphAPI(access_token)
            
            # Récupérer les posts de la page spécifiée
            posts = graph.get_connections(page_id, 'posts')
            
            # Retourner les posts récupérés avec un statut HTTP 200 (OK)
            return Response(posts, status=status.HTTP_200_OK)
        except facebook.GraphAPIError as e:
            # En cas d'erreur, renvoyer une réponse avec le message d'erreur et un statut HTTP 400 (Bad Request)
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
 """
""" 
import facebook
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from decouple import config  # Importer config pour lire les variables depuis .env

class FacebookPostsView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            # Récupérer le jeton d'accès et l'ID de la page depuis le fichier .env
            access_token = config('FACEBOOK_ACCESS_TOKEN')
            page_id = config('PAGE_ID')
            
            # Initialiser l'API Graph avec le jeton d'accès
            graph = facebook.GraphAPI(access_token)
            
            # Définir les champs que vous voulez récupérer (ajoutez description, attachments, etc.)
            fields = 'created_time,message,attachments{media,description,url}'
            
            # Récupérer les posts de la page spécifiée avec les champs supplémentaires
            posts = graph.get_connections(page_id, 'posts', fields=fields)
            
            # Retourner les posts récupérés avec un statut HTTP 200 (OK)
            return Response(posts, status=status.HTTP_200_OK)
        except facebook.GraphAPIError as e:
            # En cas d'erreur, renvoyer une réponse avec le message d'erreur et un statut HTTP 400 (Bad Request)
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST) """
import facebook
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from decouple import config  # Importer config pour lire les variables depuis .env

class FacebookPostsView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            # Récupérer le jeton d'accès et l'ID de la page depuis le fichier .env
            access_token = config('FACEBOOK_ACCESS_TOKEN')
            page_id = config('PAGE_ID')
            
            # Initialiser l'API Graph avec le jeton d'accès
            graph = facebook.GraphAPI(access_token)
            
            # Définir les champs et ajouter la limite (pagination)
            fields = 'created_time,message,attachments{media,description,url}'
            limit = 3  # Limite de posts par page

            # Récupérer le curseur après la page actuelle si fourni
            after_cursor = request.query_params.get('after', None)
            if after_cursor:
                posts = graph.get_connections(page_id, 'posts', fields=fields, limit=limit, after=after_cursor)
            else:
                posts = graph.get_connections(page_id, 'posts', fields=fields, limit=limit)
            
            # Retourner les posts récupérés avec pagination
            return Response(posts, status=status.HTTP_200_OK)
        except facebook.GraphAPIError as e:
            # En cas d'erreur, renvoyer une réponse avec le message d'erreur et un statut HTTP 400 (Bad Request)
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
