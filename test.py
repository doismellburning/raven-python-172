from unittest import TestCase
from raven.utils.serializer import transform

class DemoTestCase(TestCase):
    def test_handles_gettext_lazy(self):
        import pickle
        from django.utils.functional import lazy

        def fake_gettext(to_translate):
            return u'Igpay Atinlay'

        fake_gettext_lazy = lazy(fake_gettext, str)

        self.assertEquals(
            pickle.loads(pickle.dumps(
                    transform(fake_gettext_lazy("something")))),
            u'Igpay Atinlay')

