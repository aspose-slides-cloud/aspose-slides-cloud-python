from slides_configuration import *
from asposeslidescloud.models.slide_properties import SlideProperties

slide_properties = SlideProperties()
slide_properties.scale_type = 'DoNotScale'
slide_properties.size_type = 'OnScreen'

response = slides_api.set_slide_properties("test.pptx", slide_properties)
print(response)