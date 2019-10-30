from django.db import models

# Each class is a model?


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # Important to add this method when dealing w/ interactive promopt
    def __str__(self):
        return self.question_text
    # Add custom date/time method

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
  # Relationship defined w/ Foreign Key
  # FK tells Django each key related to single Question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
