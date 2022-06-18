.. sip:class-description::
    :status: todo
    :brief: Contains platform specific hints and settings
    :digest: fa06833c8f2d2571d38cfe5b7b4de969

The :sip:ref:`~PyQt6.QtGui.QStyleHints` class contains platform specific hints and settings.

An object of this class, obtained from :sip:ref:`~PyQt6.QtGui.QGuiApplication`, provides access to certain global user interface parameters of the current platform.

Access to most settings is read only. The platform itself usually provides the user with ways to tune these parameters. Authors of custom user interface components should read relevant settings to allow the components to exhibit the same behavior and feel as other components.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QGuiApplication.styleHints`.
