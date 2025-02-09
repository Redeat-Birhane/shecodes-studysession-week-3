from django.contrib import admin # type: ignore
from .models import Author, Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price')  # Show these fields in the list view
    search_fields = ('title',)  # Enable searching by title
    list_filter = ('author',)  # Add filter for author

    actions = ['apply_discount']

    def apply_discount(self, request, queryset):
        for book in queryset:
            book.price *= 0.9  # Apply a 10% discount
            book.save()
        self.message_user(request, "Discount applied to selected books.")

    apply_discount.short_description = "Apply 10% discount"

class BookInline(admin.TabularInline):  # Inline editing of books inside Author
    model = Book
    extra = 1  # Show 1 empty form by default

class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInline]  # Show books under Author in the admin panel

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
