from django.shortcuts import render
from Blog_writer import blog

# Create your views here.
def home(request):
    blogIdeas = blogSection = blogExpander = ""
    if request.method == 'POST':
        # idea = request.POST['blogTopic']
        # section = request.POST.get('blogSection')
        # expander = request.POST.get('blogExpander')
        # blogIdeas = blog.generateBlogTopics(idea)
        # blogIdeas = blogIdeas.replace('\n', '<br>')
        # blogSection = blog.generateBlogContent(section)
        # blogSection = blogSection.replace('\n', '<br>')
        # blogExpander = blog.blogSectionExpander(expander)
        # blogExpander = blogExpander.replace('\n', '<br>')
        if 'form1' in request.POST:
            prompt = request.POST['blogTopic']
            blogIdeas = blog.generateBlogTopics(prompt)
            blogIdeas = blogIdeas.replace('\n', '<br>')

        if 'form2' in request.POST:
            prompt = request.POST['blogSection']
            blogSection = blog.generateBlogContent(prompt)
            blogSection = blogSection.replace('\n', '<br>')

        if 'form3' in request.POST:
            prompt = request.POST['blogExpander']
            blogExpander = blog.blogSectionExpander(prompt)
            blogExpander = blogExpander.replace('\n', '<br>')

    content = {'blogIdeas' : blogIdeas,'blogSection' : blogSection , 'blogExpander' : blogExpander}
    return render(request, 'home.html', content)  # Correct indentation here
 # Adjust indentation for the return statement outside the if block