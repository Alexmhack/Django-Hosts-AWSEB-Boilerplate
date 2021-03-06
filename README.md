# Django-Hosts-AWSEB-Boilerplate
Using Django backend with django-hosts and deploying using AWS ElasticBeanstalk

What **django-hosts** does is allows you to use subdomains in your django website for example
a seperate subdomain for the app *help* like *help.example.com* or *blog.example.com*. You can have as many subdomains as your apps in your django project.

Follow the steps from this [repo](https://github.com/Alexmhack/Django-ElasticBeanstalk-Boilerplate) for launching elastic beanstalk environemnt inside a VPC. After finishing those steps continue from below.

I am uinsg [pipenv](https://docs.pipenv.org/en/latest/) for my virtualenv you are free to use of your choice, active pipenv virtualenv
by running `pipenv shell`.

1. Install [django-hosts](https://django-hosts.readthedocs.io/en/latest/) in your virtualenv
	`pip install django-hosts`

2. You can directly get the sample code for a running django-hosts enabled django project from this
	[repo](https://github.com/Alexmhack/Hosts-Django)
	Or just follow the steps below to install django-hosts in your django project.

3. Now follow the installation steps stated out [here](https://django-hosts.readthedocs.io/en/latest/#installation).

4. Create a **hostsconf** folder in your project folder containing **settings.py** file. Add three
	files in this folder namely,
	1. **__init__.py**
	2. **urls.py**
	3. **views.py**

5. Your files should have these pieces of code in it,
	1. For [urls.py](https://github.com/Alexmhack/Hosts-Django/blob/master/project/hostsconf/urls.py)
	2. For [views.py](https://github.com/Alexmhack/Hosts-Django/blob/master/project/hostsconf/views.py)

	*Click on the raw button and copy paste the code.*

6. Now create a **hosts.py** file alongside the **settings.py** file with this [piece](https://github.com/Alexmhack/Hosts-Django/blob/master/project/hosts.py) of code.

	For further explanation of what's happening inside these files you visit the official [docs](https://django-hosts.readthedocs.io/en/latest/)

7. Assuming you have your elastic beanstalk environment ready, if not follow these [steps](https://github.com/Alexmhack/Django-ElasticBeanstalk-Boilerplate). Run `eb status` and copy paste
	the whole `CNAME: xxxxxxxxxxx` in your 	`ALLOWED_HOSTS` settings.

8. Create additional apps for the project by running
	`python manage.py startapp blog`
	`python manage.py startapp help`
	Add these to the `INSTALLED_APPS`

9. Run `eb config` if not to change the `WSGIPath` to our `boilerplate/settings.py` file.

10. Add some templates and use the django-hosts template tags like the templates in this repo.
	**To use the urls don't forget to add `PARENT_HOST` setting as explained [here](https://django-hosts.readthedocs.io/en/latest/templatetags.html#fully-qualified-domain-names-fqdn)**

11. Run eb deploy and test out the site, if you have your domain available, attach it to your environment and enjoy the use of subdomains with your domain.

**NOTE:** I have tested this project in my local machine by editing the **etc/hosts** folder and 
pointing my localhost to `djapp.com`. You can do the same with the elastic beanstalk env url by adding the subdomains to the `ALLOWED_HOSTS` appended by the subdomain for example `blog.elastic_benstalk_url.com`
