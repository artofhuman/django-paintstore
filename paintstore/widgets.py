from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe


class ColorPickerWidget(forms.TextInput):
    class Media:
        css = {
            "all": ("paintstore/css/colorpicker.css",)
        }
        
        js  = (
            "https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.js", 
            "paintstore/colorpicker.js",
        )

    input_type = 'colorpicker'

    def render(self, name, value, attrs=None):
        script = u"""<script type='text/javascript'>
                        $(document).ready(function(){
                            $('#%s').ColorPicker({
                                onSubmit: function(hsb, hex, rgb, el, parent) {
                                    $(el).val('#' + hex);
                                    $(el).ColorPickerHide();
                                }
                            }).bind('keyup', function(){
                                $(this).ColorPickerSetColor(this.value.replace('#', ''));
                            });
                        });
                    </script>
                    """ % ("id_%s" % name,)

        super_render = super(ColorPickerWidget, self).render(name, value, attrs)
        return mark_safe(u"%s%s" % (super_render, script))
