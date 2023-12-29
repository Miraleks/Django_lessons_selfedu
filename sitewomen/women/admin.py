from django.contrib import admin, messages

from women.models import Women, Category


class MarriedFilter(admin.SimpleListFilter):
    title = ' Семейный статус'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('married', 'Замужем'),
            ('single', 'Не замужем'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'married':
            return queryset.filter(husband__isnull=False)
        if self.value() == 'single':
            return queryset.filter(husband__isnull=True)
        return queryset


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'content', 'cat', 'husband', 'tags']
    # exclude = ['tags', 'is_published']
    readonly_fields = ['slug', ]
    filter_horizontal = ['tags', ]
    list_display = (
        # 'id',
        'title',
        'date_created',
        'is_published',
        'cat',
        'brief_info'

    )
    list_display_links = (
        # 'id',
        'title',
    )
    ordering = (
        'date_created',
        'title',
    )
    list_editable = ('is_published',)
    list_per_page = 10
    actions = ['set_published', 'set_draft', ]
    search_fields = ['title', 'cat__name']
    list_filter = [MarriedFilter, 'cat__name', 'is_published']

    @admin.display(description='Краткое описание', ordering='content')
    def brief_info(self, women: Women):
        return f'Описание {len(women.content)} символов.'

    @admin.action(description='Опубликовать записи')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Women.Status.PUBLISHED)
        self.message_user(request, f'Изменено {count} записей.')

    @admin.action(description='Снять записи с публикации')
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Women.Status.DRAFT)
        self.message_user(request, f'{count} записей снято с публикации.', messages.WARNING)


# admin.site.register(Women, WomenAdmin) # заменено на декоратор

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )

    list_display_links = (
        'id',
        'name',
    )
