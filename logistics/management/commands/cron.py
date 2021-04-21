# coding=utf-8
from django.core.management.base import BaseCommand
from core.models import Subscription
from datetime import date


class Command(BaseCommand):
    help = 'Executes all the stuff that needs to be maintained daily'

    def handle(self, *args, **options):

        # Deactivate all ended subscriptions
        for s in Subscription.objects.filter(active=True, end_date__lte=date.today()).iterator():
            s.active = False
            # NOTE: after saving, a signal will be triggered to add deactivation contactproducthistory entries
            s.save()

        for s in Subscription.objects.filter(active=True, type__in='NG'):
            # Do something with the people that owes us money.
            pass
