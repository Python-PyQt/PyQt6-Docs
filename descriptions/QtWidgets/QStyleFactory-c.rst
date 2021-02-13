.. sip:class-description::
    :status: todo
    :brief: Creates QStyle objects
    :digest: 84f99eda2ca74d1ec9d6c8c372286e7f

The :sip:ref:`~PyQt6.QtWidgets.QStyleFactory` class creates :sip:ref:`~PyQt6.QtWidgets.QStyle` objects.

The :sip:ref:`~PyQt6.QtWidgets.QStyle` class is an abstract base class that encapsulates the look and feel of a GUI. :sip:ref:`~PyQt6.QtWidgets.QStyleFactory` creates a :sip:ref:`~PyQt6.QtWidgets.QStyle` object using the :sip:ref:`~PyQt6.QtWidgets.QStyleFactory.create` function and a key identifying the style. The styles are either built-in or dynamically loaded from a style plugin (see QStylePlugin).

The valid keys can be retrieved using the :sip:ref:`~PyQt6.QtWidgets.QStyleFactory.keys` function. Typically they include "windows" and "fusion". Depending on the platform, "windowsvista" and "macos" may be available. Note that keys are case insensitive.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QStyle`.
