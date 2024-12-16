.. sip:method-description::
    :status: todo
    :pysig: d409847c33b4369753f8b837c22758e9
    :realsig: ()
    :digest: a5a4732202ccca49db39f512ab5793da

Returns the fallback search paths for icons.

The fallback search paths are consulted for standalone icon files if the :sip:ref:`~PyQt6.QtGui.QIcon.themeName` or :sip:ref:`~PyQt6.QtGui.QIcon.fallbackThemeName` do not provide results for an icon lookup.

If not set, the fallback search paths will be defined by the platform.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QIcon.setFallbackSearchPaths`, :sip:ref:`~PyQt6.QtGui.QIcon.themeSearchPaths`.
