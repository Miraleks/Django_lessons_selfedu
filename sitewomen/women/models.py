from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

from transliterate import translit, get_available_language_codes


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Women.Status.PUBLISHED)


class Women(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(max_length=255,
                             verbose_name='Заголовок')
    slug = models.SlugField(max_length=255,
                            unique=True,
                            db_index=True,
                            verbose_name='Slug')
    content = models.TextField(blank=True,
                               verbose_name='Текст статьи')
    date_created = models.DateTimeField(auto_now_add=True,
                                        verbose_name='Дата создания')
    date_update = models.DateTimeField(auto_now=True,
                                       verbose_name='Дата последнего изменения')
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.DRAFT,
                                       verbose_name='Состояние')
    cat = models.ForeignKey('Category',
                            on_delete=models.PROTECT,
                            related_name='posts',
                            verbose_name='Категория')
    tags = models.ManyToManyField('TagPost',
                                  blank=True,
                                  related_name='tags',
                                  verbose_name='Тэги')
    husband = models.OneToOneField('Husband',
                                   on_delete=models.SET_NULL,
                                   null=True, blank=True,
                                   related_name='wumen',
                                   verbose_name='Муж')

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Відомі жінки"
        verbose_name_plural = "Відомі жінки"

        ordering = ['-date_created']  # порядок сортировки '-' - в обратном порядке
        indexes = [
            models.Index(fields=['-date_created'])
        ]

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(translit(str(self.title), reversed=True))
        super().save(*args, **kwargs)


class Husband(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(null=True)
    m_count = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


class TagPost(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})
