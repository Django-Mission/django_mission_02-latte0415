from asyncio.windows_events import NULL
from sre_constants import CATEGORY
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

# for basic mission
class Faq(models.Model):
    question = models.TextField(verbose_name='질문')
    CATEGORY_CHOICES = [
        ('General', '일반'),
        ('Account', '계정'),
        ('Etc', '기타'),
    ]
    category = models.CharField(
        verbose_name='카테고리',
        max_length=7,
        choices=CATEGORY_CHOICES,
        default='General',
    )
    answer = models.TextField(verbose_name='답변', null=True)
    created_at = models.DateTimeField(verbose_name='생성일시', auto_now_add=True)
    modified_at = models.DateTimeField(verbose_name='최종수정일시', auto_now_add=True)
    
    #writer = models.ForeignKey(to=User, related_name = 'faq_writer', on_delete=models.CASCADE)
    #final_writer = models.ForeignKey(to=User, related_name = 'faq_final_writer', on_delete=models.CASCADE)
    writer = models.ForeignKey(to=User, related_name = 'faq_writer', on_delete=models.CASCADE, null=True, blank=True)
    modifier = models.ForeignKey(to=User, related_name = 'faq_modifier', on_delete=models.CASCADE, null=True, blank=True)

# for advanced mission
class Inquiry(models.Model):
    title = models.TextField(verbose_name='제목')
    CATEGORY_CHOICES = [
        ('General', '일반'),
        ('Account', '계정'),
        ('Etc', '기타'),
    ]
    category = models.CharField(
        verbose_name='카테고리',
        max_length=7,
        choices=CATEGORY_CHOICES,
        default='General',
    )
    e_mail = models.EmailField(verbose_name='이메일', blank = True)
    e_mail_check = models.BooleanField(verbose_name='이메일수신동의')
    phone_number = models.CharField(verbose_name='전화번호', max_length=12, blank = True)
    phone_number_check = models.BooleanField(verbose_name='이메일수신동의')
    content = models.TextField(verbose_name='내용')
    image = models.ImageField(verbose_name='이미지', null=True, blank=True)

    #writer = models.ForeignKey(to=User, related_name = 'inquiry_writer', on_delete=models.CASCADE)
    writer = models.ForeignKey(to=User, related_name = 'inquiry_writer', on_delete=models.CASCADE, null=True, blank=True)

# for advanced mission
class Answer(models.Model):
    content = models.TextField(verbose_name='답변내용')
    from_inquiry = models.ForeignKey(to='Inquiry', on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='생성일시', auto_now_add=True)
    modified_at = models.DateTimeField(verbose_name='최종수정일시', auto_now_add=True)
    
    #writer = models.ForeignKey(to=User, related_name = 'answer_writer', on_delete=models.CASCADE)
    #modifier = models.ForeignKey(to=User, related_name = 'answer_modifier', on_delete=models.CASCADE)
    writer = models.ForeignKey(to=User, related_name = 'answer_writer', on_delete=models.CASCADE, null=True, blank=True)
    modifier = models.ForeignKey(to=User, related_name = 'answer_modifier', on_delete=models.CASCADE, null=True, blank=True)
