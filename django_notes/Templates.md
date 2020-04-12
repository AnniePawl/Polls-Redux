# Templates

Templates are Django's way of generating HTML dynamically.They contain the static parts of desired HTML output as well as some special syntax describing how dynamic content will be inserted. Templates define the look and feel of a site and provide "holes" for child templates.

1. Create **templates** directory in your app
2. Update **view** to use template

## Example Template

**mysite/news/templates/news/year_archive.html**

```html
{% extends "base.html" %} {% block title %}Articles for {{ year }}{% endblock %}
{% block content %}
<h1>Articles for {{ year }}</h1>

{% for article in article_list %}
<p>{{ article.headline }}</p>
<p>By {{ article.reporter.full_name }}</p>
<p>Published {{ article.pub_date|date:"F j, Y" }}</p>
{% endfor %} {% endblock %}
```

Method-calling happens in the {% for %} loop: question.choice_set.all is interpreted as the Python code question.choice_set.all(), which returns an iterable of Choice objects and is suitable for use in the {% for %} tag.
