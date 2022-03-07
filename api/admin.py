from django.contrib import admin
from .models import Media, Room, Vehicle, Reservation


class RoomAdmin(admin.ModelAdmin):
    fields = ('title', 'price')


class VehicleAdmin(admin.ModelAdmin):
    fields = ('name', 'price')


class MediaAdmin(admin.ModelAdmin):
    fields = ('file_name', 'url')


class ReservationAdmin(admin.ModelAdmin):
    fields = ('total', 'created_at')


admin.site.register(Room, RoomAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Reservation, ReservationAdmin)
# Register your models here.
