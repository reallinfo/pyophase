from datetime import date

from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase
from django.utils.translation import ugettext_lazy as _

from clothing.models import Settings, Type, Size, Color, Order
from ophasebase.models import Ophase
from staff.models import Person


class SettingsModelTests(TestCase):
    def test_settings_create(self):
        """Ensure creating of a settings object works"""
        self.assertEqual(Settings.objects.count(), 0)
        self.assertEqual(Settings.instance(), None)

        s = Settings.objects.create(clothing_ordering_enabled=True)

        self.assertEqual(Settings.objects.count(), 1)
        self.assertEqual(s.clothing_ordering_enabled, True)
        self.assertEqual(s, Settings.instance())

        s.clothing_ordering_enabled = False
        s.save()

        self.assertEqual(Settings.objects.count(), 1)
        self.assertEqual(s.clothing_ordering_enabled, False)
        self.assertEqual(s.__str__(), _('Clothing Einstellungen'))

    def test_settings_cannot_create_two_instances(self):
        """Ensure it is not possible to create a second instance"""
        self.assertEqual(Settings.objects.count(), 0)
        s = Settings.objects.create(clothing_ordering_enabled=True)
        self.assertEqual(Settings.objects.count(), 1)
        s2 = Settings(clothing_ordering_enabled=True)
        with self.assertRaises(ValidationError):
            s2.clean()


class TypeModelTests(TestCase):
    def test_type_create(self):
        """Ensure creating a type object works"""
        self.assertEqual(Type.objects.count(), 0)

        t = Type.objects.create(name="Testtyp", price=42)

        self.assertEqual(Type.objects.count(), 1)
        self.assertEqual(t.name, "Testtyp")
        self.assertEqual(t.price, 42)
        self.assertEqual(t.additional_only, False)

    def test_type_string_is_name(self):
        """Ensure the type objects's string representation is its name"""
        t = Type(name="Testtyp", price=42)
        self.assertEqual(t.__str__(), "Testtyp")

    def test_type_cannot_create_two_identical_types(self):
        """Ensure type names are unique"""
        t1 = Type.objects.create(name="T1", price=42)
        self.assertEqual(Type.objects.count(), 1)
        t2 = Type(name="T1", price=42)
        with self.assertRaises(IntegrityError):
            t2.save()


class SizeModelTests(TestCase):
    def test_size_create(self):
        """Ensure creating a size object works"""
        self.assertEqual(Size.objects.count(), 0)

        s = Size.objects.create(size="Testgröße")

        self.assertEqual(Size.objects.count(), 1)
        self.assertEqual(s.size, "Testgröße")

    def test_size_string_is_size(self):
        """Ensure the size objects's string representation is its size"""
        s = Size(size="Testgröße")
        self.assertEqual(s.__str__(), "Testgröße")

    def test_size_cannot_create_two_identical_types(self):
        """Ensure sizes are unique"""
        s1 = Size.objects.create(size="S1")
        self.assertEqual(Size.objects.count(), 1)
        s2 = Size(size="S1")
        with self.assertRaises(IntegrityError):
            s2.save()


class ColorModelTests(TestCase):
    def test_color_create(self):
        """Ensure creating a color object works"""
        self.assertEqual(Color.objects.count(), 0)

        c = Color.objects.create(name="Testfarbe")

        self.assertEqual(Color.objects.count(), 1)
        self.assertEqual(c.name, "Testfarbe")
        self.assertEqual(c.color_code, "#FFFFFF")

    def test_color_string_is_name(self):
        """Ensure the color objects's string representation is its name"""
        c = Color(name="Testfarbe")
        self.assertEqual(c.__str__(), "Testfarbe")

    def test_color_cannot_create_two_identical_types(self):
        """Ensure color names are unique"""
        c1 = Color.objects.create(name="C1")
        self.assertEqual(Color.objects.count(), 1)
        c2 = Color(name="C1")
        with self.assertRaises(IntegrityError):
            c2.save()


class OrderModelTest(TestCase):
    def setUp(self):
        self.ophase = Ophase.objects.create(
            start_date=date(2014, 4, 7), end_date=date(2014, 4, 11), is_active=True)
        self.person = Person.objects.create(ophase=self.ophase, prename="John", name="Doe", email="john@doe.net",
            phone="12345", matriculated_since="WS42", degree_course="Bsc", experience_ophase="nein", why_participate="Gründe")

    def test_order_create(self):
        """ Ensure creating an order object works"""
        self.assertEqual(Order.objects.count(), 0)

        t = Type.objects.create(name="Testtyp", price=42)
        s = Size.objects.create(size="Testgröße")
        c = Color.objects.create(name="Testfarbe")
        o = Order.objects.create(person=self.person, type=t, size=s, color=c, additional=False)

        self.assertEqual(Order.objects.count(), 1)