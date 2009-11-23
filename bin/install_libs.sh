if [ ! -d 'lib/django' ]; then
  echo "--------------------------------------------------"
  echo "Installing Django 1.0,2"
  echo "--------------------------------------------------"

  svn checkout http://code.djangoproject.com/svn/django/tags/releases/1.0.2/django/ lib/django
fi

if [ ! -d 'lib/compress' ]; then
  echo "--------------------------------------------------"
  echo "Installing django-compress"
  echo "--------------------------------------------------"
  svn checkout http://django-compress.googlecode.com/svn/trunk/compress/ -r95 lib/compress
fi

if [ ! -d 'lib/dmigrations' ]; then
  echo "--------------------------------------------------"
  echo "Installing dmigrations"
  echo "--------------------------------------------------"
  svn checkout http://dmigrations.googlecode.com/svn/trunk/dmigrations/ -r22 lib/dmigrations
fi

if [ ! -d 'lib/django_extensions' ]; then
  echo "--------------------------------------------------"
  echo "Installing django-command-extensions"
  echo "--------------------------------------------------"
  svn checkout http://django-command-extensions.googlecode.com/svn/trunk/django_extensions/ -r187 lib/django_extensions
fi

if [ ! -d 'lib/timezones' ]; then
  echo "--------------------------------------------------"
  echo "Installing django-timezones"
  echo "--------------------------------------------------"
  svn checkout http://django-timezones.googlecode.com/svn/trunk/timezones/ -r45 lib/timezones
fi

if [ ! -d 'lib/pytz' ]; then
  echo "--------------------------------------------------"
  echo "Installing pytz-2009r"
  echo "--------------------------------------------------"

  cd lib
  wget http://pypi.python.org/packages/source/p/pytz/pytz-2009r.tar.bz2#md5=454be5c4b09ab879bb3a98be0b44f674
  tar -xjf pytz-2009r.tar.bz2
  mv pytz-2009r/pytz pytz

  rm -f pytz-2009r.tar.bz2
  rm -rf pytz-2009r
fi
