from django.db import models
import uuid
import random
from accounts.models import User
from core.models import Category,SubCategory


class Question(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    category=models.ForeignKey(SubCategory,on_delete=models.SET_NULL,blank=True,null=True,related_name="fk_category",verbose_name="Category")
    question=models.TextField(max_length=5000)
    mark=models.IntegerField(default=5)
    active=models.BooleanField(default=True,verbose_name="status")
    created_at=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    updated_at=models.DateTimeField(auto_now=True,verbose_name='Update date')

    def __str__(self) -> str:
        return self.question

    def get_answer(self):
        answer_objs=list(Answer.objects.filter(question=self))
        random.shuffle(answer_objs)
        data=[]
        for answer_obj in answer_objs:
            data.append({
                'answer':answer_obj.answer,
                'is_correct':answer_obj.is_correct
            })
        return data
    

class Answer(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    question=models.ForeignKey(Question,on_delete=models.SET_NULL,blank=True,null=True,related_name="fk_question")
    answer=models.CharField(max_length=500)
    is_correct=models.BooleanField(default=False)
    active=models.BooleanField(default=True,verbose_name="status")
    created_at=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    updated_at=models.DateTimeField(auto_now=True,verbose_name='Update date')

    def __str__(self) -> str:
        return self.answer
    