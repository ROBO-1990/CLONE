from django.contrib import admin
from .models import FirstAidGuide, FirstAidVideo, Quiz, QuizQuestion, QuizAnswer, Badge, UserBadge


class QuizAnswerInline(admin.TabularInline):
    model = QuizAnswer
    extra = 2
    fields = ['answer_text', 'is_correct', 'order']


class QuizQuestionInline(admin.TabularInline):
    model = QuizQuestion
    extra = 1
    fields = ['question_text', 'order']
    show_change_link = True


@admin.register(FirstAidGuide)
class FirstAidGuideAdmin(admin.ModelAdmin):
    list_display = ['title', 'urgency_type', 'created_at']
    list_filter = ['urgency_type', 'created_at']
    search_fields = ['title', 'content']


@admin.register(FirstAidVideo)
class FirstAidVideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'guide', 'duration', 'created_at']
    list_filter = ['guide', 'created_at']
    search_fields = ['title', 'description']


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['title', 'guide', 'created_at']
    list_filter = ['guide', 'created_at']
    search_fields = ['title', 'description']
    inlines = [QuizQuestionInline]


@admin.register(QuizQuestion)
class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'quiz', 'order']
    list_filter = ['quiz']
    search_fields = ['question_text']
    inlines = [QuizAnswerInline]
    ordering = ['quiz', 'order']


@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    list_display = ['name', 'level', 'required_score', 'quiz']
    list_filter = ['level']
    search_fields = ['name', 'description']


@admin.register(UserBadge)
class UserBadgeAdmin(admin.ModelAdmin):
    list_display = ['user', 'badge', 'earned_at', 'quiz_score']
    list_filter = ['badge', 'earned_at']
    search_fields = ['user__username', 'badge__name']
    date_hierarchy = 'earned_at'
