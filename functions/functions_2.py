import html
def make_element(name, value, **attrs):
    # here attrs acts as a dictionary and the individual keys and values can be accessed
    # concating the keys and vals with equals
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
    name=name,
    attrs=attr_str,
    value=html.escape(value))
    return element
# Example
# Creates '<item size="large" quantity="6">Albatross</item>'
print(make_element('item', 'Albatross', size='large', quantity=6))
# Creates '<p>&lt;spam&gt;</p>'
print(make_element('p', '<spam>'))