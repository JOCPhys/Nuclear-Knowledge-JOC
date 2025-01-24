# filepath: /workspace/Nuclear-Knowledge-JOC/blog/templatetags/category_urls.py
from django import template
from django.urls import reverse

register = template.Library()

CATEGORY_URLS = {
    'nuclear_facilities': 'nuclear_facilities',
    'nuclear_fuel_waste': 'nuclear_fuel_waste',
    'nuclear_defence': 'nuclear_defence',
    'nuclear_power_space': 'nuclear_power_space',
    'fact_or_fiction': 'fact_or_fiction',
    'educational_resources': 'educational_resources',
}

@register.simple_tag
def category_url(category):
    return reverse(CATEGORY_URLS.get(category, 'landing_page'))