## Templates

1. Create **templates** directory in App 
2. Update **view**  to use template

## Shortcut: render()
???? 


The template system uses dot-lookup syntax to access variable attributes. In the example of {{ question.question_text }}, first Django does a dictionary lookup on the object question. Failing that, it tries an attribute lookup – which works, in this case. If attribute lookup had failed, it would’ve tried a list-index lookup.

Method-calling happens in the {% for %} loop: question.choice_set.all is interpreted as the Python code question.choice_set.all(), which returns an iterable of Choice objects and is suitable for use in the {% for %} tag.