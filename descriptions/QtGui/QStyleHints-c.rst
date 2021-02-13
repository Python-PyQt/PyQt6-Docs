.. sip:class-description::
    :status: todo
    :brief: Contains platform specific hints and settings
    :digest: 810b91ea4acd461161e6802c1aa7bbb5

The :sip:ref:`~PyQt6.QtGui.QStyleHints` class contains platform specific hints and settings.

An object of this class, obtained from :sip:ref:`~PyQt6.QtGui.QGuiApplication`, provides access to certain global user interface parameters of the current platform.

Access is read only; typically the platform itself provides the user a way to tune these parameters.

Access to these parameters are useful when implementing custom user interface components, in that they allow the components to exhibit the same behaviour and feel as other components.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QGuiApplication.styleHints`.
