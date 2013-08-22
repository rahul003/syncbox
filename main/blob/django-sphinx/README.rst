This is a layer that functions much like the Django ORM does except it works on top of the Sphinx (http://www.sphinxsearch.com) full-text search engine.

Please Note: You will need to create your own sphinx indexes and install sphinx on your server to use this app.

*There will no longer be release packages available. Please use SVN to checkout the latest trunk version, as it should always be stable and current.*

Installation
------------

To install the latest stable version::

	sudo easy_install django-sphinx

To install the latest development version (updated quite often)::

	git clone git://github.com/dcramer/django-sphinx.git  
	cd django-sphinx
	sudo python setup.py install

*Note:* You will need to install the `sphinxapi.py` package into your Python Path or use one of the included versions. To use the included version, you must specify the following in your `settings.py` file::

	# Sphinx 0.9.9
	SPHINX_API_VERSION = 0x116

	# Sphinx 0.9.8
	SPHINX_API_VERSION = 0x113

	# Sphinx 0.9.7
	SPHINX_API_VERSION = 0x107

Usage
-----

The following is some example usage::

	from djangosphinx.models import SphinxSearch
	
	class MyModel(models.Model):
	    search = SphinxSearch() # optional: defaults to db_table
	    # If your index name does not match MyModel._meta.db_table
	    # Note: You can only generate automatic configurations from the ./manage.py script
	    # if your index name matches.
	    search = SphinxSearch('index_name')

	    # Or maybe we want to be more.. specific
	    searchdelta = SphinxSearch(
	        index='index_name delta_name',
	        weights={
	            'name': 100,
	            'description': 10,
	            'tags': 80,
	        },
	        mode='SPH_MATCH_ALL',
	        rankmode='SPH_RANK_NONE',
	    )

	queryset = MyModel.search.query('query')
	results1 = queryset.order_by('@weight', '@id', 'my_attribute')
	results2 = queryset.filter(my_attribute=5)
	results3 = queryset.filter(my_other_attribute=[5, 3,4])
	results4 = queryset.exclude(my_attribute=5)[0:10]
	results5 = queryset.count()

	# as of 2.0 you can now access an attribute to get the weight and similar arguments
	for result in results1:
	    print result, result._sphinx
	# you can also access a similar set of meta data on the queryset itself (once it's been sliced or executed in any way)
	print results1._sphinx


Some additional methods:
* count()
* extra() (passed to the queryset)
* all() (does nothing)
* select_related() (passed to the queryset)
* group_by(field, field, field)
* set_options(index='', weights={}, weights=[], mode='SPH_MODE_*', rankmode='SPH_MATCH_*')

The django-sphinx layer also supports some basic querying over multiple indexes. To use this you first need to understand the rules of a UNION. Your indexes must contain exactly the same fields. These fields must also include a `content_type` selection which should be the content_type id associated with that table (model).

You can then do something like this::

	from djangosphinx.models import SphinxSearch
	
	SphinxSearch('index1 index2 index3').query('hello')

This will return a list of all matches, ordered by weight, from all indexes. This performs one SQL query per index with matches in it, as Django's ORM does not support SQL UNION.

Config Generation
-----------------

django-sphinx now includes a tool to create sample configuration for your models. It will generate both a source, and index configuration for a model class. You will still need to manually tweak the output, and insert it into your configuration, but it should aid in initial setup.

To use it::

	from djangosphinx.utils import *

	from myproject.myapp.models import MyModel

	output = generate_config_for_model(MyModel)

	print output

If you have multiple models which you wish to use the UNION searching::

	model_classes = (ModelOne, ModelTwoWhichResemblesModelOne)

	output = generate_config_for_models(model_classes)

You can also now output configuration from the command line::

	./manage.py generate_sphinx_config <appname>

This will loop through all models in <appname> and attempt to find any with a SphinxSearch instance that is using the default index name (db_table).

Using the Config Generator
--------------------------

*New in 2.2*

django-sphinx now includes a simply python script to generate a config using your default template renderer. By default, we mean that if `coffin` is included in your INSTALLED_APPS, it uses it, otherwise it uses Django.

Two variables directly relate to the config generation:

	# The base path for sphinx files. Sub directories will include data, log, and run.
	SPHINX_ROOT = '/var/sphinx-search/'
	
	# Optional, defaults to 'conf/sphinx.html'. This should be configuration template.
	# See the included templates/sphinx.conf for an example.
	SPHINX_CONFIG_TEMPLATE = 'conf/sphinx.html'

Once done, your config can be passed via any sphinx command like so:

	# Index your stuff
	DJANGO_SETTINGS_MODULE=myproject.settings indexer --config /path/to/djangosphinx/config.py --all --rotate
	
	# Start the daemon
	DJANGO_SETTINGS_MODULE=myproject.settings searchd --config /path/to/djangosphinx/config.py
	
	# Query the daemon
	DJANGO_SETTINGS_MODULE=myproject.settings search --config /path/to/djangosphinx/config.py my query
	
	# Kill the daemon
	kill -9 $(cat /var/sphinx-search/run/searchd.pid)

For now, we recommend you setup some basic bash aliases or scripts to deal with this. This is just the first step in embedded config generation, so stay tuned!

* Note: Make sure your PYTHON_PATH is setup properly!

Using Sphinx in Admin
---------------------

Sphinx includes it's own ModelAdmin class to allow you to use it with Django's built-in admin app.

To use it, see the following example::

	from djangosphinx.admin import SphinxModelAdmin
	
	class MyAdmin(SphinxModelAdmin):
		index = 'my_index_name' # defaults to Model._meta.db_table
		weights = {'field': 100}

Limitations? You know it.

- Only shows your max sphinx results (defaults to 1000)
- Filters currently don't work.
- This is a huge hack, so it may or may not continue working when Django updates.

Frequent Questions
------------------

*How do I run multiple copies of Sphinx using django-sphinx?*

The easiest way is to just run a different SPHINX_PORT setting in your settings.py. If you are using the above config generation, just modify the PORT, and start up the daemon

Resources
---------

* http://groups.google.com/group/django-sphinx
* http://www.davidcramer.net/code/65/setting-up-django-with-sphinx.html