.. sip:method-description::
    :status: todo
    :pysig: 2959872364c7b497ae5baab9d50a0314
    :realsig: ()
    :digest: 6a3989c77eafedb197a9d1cb866bafd5

Returns the search paths for icon themes.

The default value will depend on the platform:

On X11, the search path will use the XDG_DATA_DIRS environment variable if available.

By default all platforms will have the resource directory ``:\icons`` as a fallback. You can use "rcc -project" to generate a resource file from your icon theme.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QIcon.setThemeSearchPaths`, :sip:ref:`~PyQt6.QtGui.QIcon.fromTheme`, :sip:ref:`~PyQt6.QtGui.QIcon.setThemeName`.
