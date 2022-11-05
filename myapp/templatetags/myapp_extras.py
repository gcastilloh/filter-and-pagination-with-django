from django import template

register = template.Library()

@register.simple_tag
def my_url(value, field_name, urlencode=None):
    url = f'?{field_name}={value}'
    if urlencode:
        
        # main url: page=2&name=&gender=Female&age=8
        # querystring = ['page=2','name=', 'gender=Female','age=8']
        # filtered_querystring = ['name=', 'gender=Female','age=8']
        # encoded_querystring = 'name=&gendre=Female&age=8'
        # url = {?page=2}&{name=&gendre=Female&age=8}

        querystring = urlencode.split('&')
        filtered_querystring = filter(lambda p: p.split('=')[0]!=field_name,querystring)
        encoded_querystring = '&'.join(filtered_querystring)
        url = f'{url}&{encoded_querystring}'
    return url

