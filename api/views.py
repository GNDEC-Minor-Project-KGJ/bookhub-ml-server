from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import BookSerializer
from .models import Book

import pandas as pd
import pickle

# Vectorizing
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import RegexpTokenizer
import re
import string
import random

# For recommendation
from sklearn.metrics.pairwise import cosine_similarity
from gensim.models import Word2Vec
from gensim.models.phrases import Phrases, Phraser
from matplotlib import pyplot
from gensim.models import KeyedVectors

# Create your views here.
books = pickle.load(open('C:/Users/Konark Lohat/OneDrive/Desktop/Bookhub-backend/books_api/api/cached_db/books.pkl', 'rb'))
cosine_similarity = pickle.load(open('C:/Users/Konark Lohat/OneDrive/Desktop/Bookhub-backend/books_api/api/cached_db/cosine_similarity.pkl', 'rb'))


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/book-list/',
        'Detail View': '/book-detail/<str:pk>/',
        'Create': '/book-create/',
        'Update': '/book-update/<str:pk>/',
        'Delete': '/book-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def ShowAll(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ShowOne(request, id):
    book = Book.objects.get(id=id)
    serializer = BookSerializer(book, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def Create(request):
    print(request.data)
    serializer = BookSerializer(data=request.data)
    print("This is serialize - ", serializer)

    if serializer.is_valid():
        print("******************************")
        serializer.save()
        
    

    return Response(serializer.data)


@api_view(['POST'])
def Update(request, titile):
    book = Book.objects.get(id=title)
    serializer = BookSerializer(instance=book, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def Delete(request, title):
    book = Book.objects.get(id=title)
    book.delete()

    return Response('Item successfully deleted!')


@api_view(['GET'])
def recommend_by_title(request, genre, title):
    
    data = books.loc[books['genre'] == genre]  
    data.reset_index(level = 0, inplace = True) 
  
    # Convert the index into series
    indices = pd.Series(data.index, index = data['title'])
    
    #Converting the book description into vectors and used bigram
    tf = TfidfVectorizer(analyzer='word', ngram_range=(2, 2), min_df = 1, stop_words='english')
    tfidf_matrix = tf.fit_transform(data['title'])
    
    # Calculating the similarity measures based on Cosine Similarity
    sg = cosine_similarity(tfidf_matrix, tfidf_matrix)
    
    # Get the index corresponding to original_title
    idx = indices[title]
    
    # Get the pairwsie similarity scores 
    sig = list(enumerate(sg[idx]))
    
    # Sort the books
    sig = sorted(sig, key=lambda x: x[1], reverse=True)
    
    # Scores of the 5 most similar books 
    sig = sig[1:6]
    
    # Book indicies
    movie_indices = [i[0] for i in sig]
   
    # Top 5 book recommendation
    rec = data[['title', 'url', 'author', 'word_count']].iloc[movie_indices]
    
    res = []
    for i in rec['title']:
        # print("THIS IS -- ", i)
        bookData = Book.objects.get(title=i)
        serializer = BookSerializer(bookData, many=False)
        res.append(serializer.data)
    
    # It reads the top 5 recommend
    return Response(res)


@api_view(['GET'])
def recommend_by_desc(request, genre, title):
    # Matching the genre with the dataset and reset the index
    data = books.loc[books['genre'] == genre]  
    data.reset_index(level = 0, inplace = True) 
  
    # Convert the index into series
    indices = pd.Series(data.index, index = data['title'])
    
    #Converting the book description into vectors and used bigram
    tf = TfidfVectorizer(analyzer='word', ngram_range=(2, 2), min_df = 1, stop_words='english')
    tfidf_matrix = tf.fit_transform(data['cleaned_desc'])
    
    # Calculating the similarity measures based on Cosine Similarity
    sg = cosine_similarity(tfidf_matrix, tfidf_matrix)
    
    # Get the index corresponding to original_title
    idx = indices[title]
    
    # Get the pairwsie similarity scores
    sig = list(enumerate(sg[idx]))
    
    # Sort the books
    sig = sorted(sig, key=lambda x: x[1], reverse=True)
    
    # Scores of the 5 most similar books 
    sig = sig[1:6]
    
    # Book indicies
    movie_indices = [i[0] for i in sig]
   
    # Top 5 book recommendation
    rec = data[['title']].iloc[movie_indices]
    
    res = []
    for i in rec['title']:
        # print("THIS IS -- ", i)
        bookData = Book.objects.get(title=i)
        serializer = BookSerializer(bookData, many=False)
        res.append(serializer.data)
    
    # It reads the top 5 recommend
    print(res)
    return Response(res)

@api_view(['GET'])
def top_rated(request):
    books = Book.objects.all().order_by('-rating')[:4]
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def longest(request):
    books = Book.objects.all().order_by('-word_count')[:4]
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)
