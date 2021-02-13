.. sip:method-description::
    :status: todo
    :pysig: 927028349b02da8582fd4fa260a22820
    :realsig: (const QWidget*)
    :digest: 7083ade78ad498061c2c706fc9db9a0c

If a *widget* is passed, the default palette for the widget's class is returned. This may or may not be the application palette. In most cases there is no special palette for certain types of widgets, but one notable exception is the popup menu under Windows, if the user has defined a special background color for menus in the display settings.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QApplication.setPalette`, :sip:ref:`~PyQt6.QtWidgets.QWidget.palette`.
