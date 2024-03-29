from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Quiz(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_number = models.IntegerField(default=1)  # Add a default value for question_number
    text = models.TextField()
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.question_number}. {self.text}"  # Return question number along with text

@receiver(post_save, sender=Question)
def update_question_number(sender, instance, created, **kwargs):
    if created:
        last_question = Question.objects.filter(quiz=instance.quiz).order_by('-question_number').first()
        if last_question:
            instance.question_number = last_question.question_number + 1
        else:
            instance.question_number = 1
        instance.save()

