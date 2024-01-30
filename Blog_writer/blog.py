import os
import openai
from AI_Blog_Writer import settings
import requests
import json

openai.api_key = settings.OPENAI_API_KEY
URL = "https://api.openai.com/v1/chat/completions"

def generateBlogTopics(prompt):
    BlogIdeas = {
      'model' : 'gpt-3.5-turbo',
      'messages': [{'role': 'user' , 'content': f"Generate blog topics on: {prompt}. \n \n"}],
      'temperature' : 1.0 ,
      'top_p': 1.0,
      'n': 1 ,
      'stream': False,
      'presence_penalty' : 0,
      'frequency_penalty' : 0
    }
    headers = {
      'Content-Type' : 'application/json' ,
      'Authorization' : f"Bearer {openai.api_key}"}

    response = requests.post(URL,headers = headers,json = BlogIdeas)
    reply = response.json()['choices'][0]['message']['content']
    # reply = json.loads(reply)
    return reply

def generateBlogContent(prompt):
    BlogContent = {
      'model' : 'gpt-3.5-turbo',
      'messages': [{'role': 'user' , 'content': f"Expand the blog title in to high level blog sections: {prompt} \n\n- Introduction:"}],
      'temperature' : 1.0 ,
      'top_p': 1.0,
      'n': 1 ,
      'stream': False,
      'presence_penalty' : 0,
      'frequency_penalty' : 0
    }
    headers = {
      'Content-Type' : 'application/json' ,
      'Authorization' : f"Bearer {openai.api_key}"}

    response = requests.post(URL,headers = headers,json = BlogContent)
    reply = response.json()['choices'][0]['message']['content']
    return reply

def blogSectionExpander(prompt):
    BlogSection = {
      'model' : 'gpt-3.5-turbo',
      'messages': [{'role': 'user' , 'content': f"Expand the blog section in to a detailed professional , witty and clever explanation.\n\n {prompt}"}],
      'temperature' : 1.0 ,
      'top_p': 1.0,
      'n': 1 ,
      'stream': False,
      'presence_penalty' : 0,
      'frequency_penalty' : 0
    }
    headers = {
      'Content-Type' : 'application/json' ,
      'Authorization' : f"Bearer {openai.api_key}"}

    response = requests.post(URL,headers = headers,json = BlogSection)
    reply = response.json()['choices'][0]['message']['content']
    return reply