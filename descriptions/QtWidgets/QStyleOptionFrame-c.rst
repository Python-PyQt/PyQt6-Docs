.. sip:class-description::
    :status: todo
    :brief: Used to describe the parameters for drawing a frame
    :digest: 9db69e979d2aa2869cf3bd0fb66356a1

The :sip:ref:`~PyQt6.QtWidgets.QStyleOptionFrame` class is used to describe the parameters for drawing a frame.

:sip:ref:`~PyQt6.QtWidgets.QStyleOptionFrame` is used for drawing several built-in Qt widgets, including :sip:ref:`~PyQt6.QtWidgets.QFrame`, :sip:ref:`~PyQt6.QtWidgets.QGroupBox`, :sip:ref:`~PyQt6.QtWidgets.QLineEdit`, and :sip:ref:`~PyQt6.QtWidgets.QMenu`.

For performance reasons, there are few member functions and the access to the member variables is direct (i.e., using the ``.`` or ``->`` operator). This makes the structures straightforward to use and emphasizes that these are simply parameters used by the style functions.

An instance of the :sip:ref:`~PyQt6.QtWidgets.QStyleOptionFrame` class has type SO_Frame and version 3.

The type is used internally by :sip:ref:`~PyQt6.QtWidgets.QStyleOption`, its subclasses, and qstyleoption_cast() to determine the type of style option. In general you do not need to worry about this unless you want to create your own :sip:ref:`~PyQt6.QtWidgets.QStyleOption` subclass and your own styles. The version is used by :sip:ref:`~PyQt6.QtWidgets.QStyleOption` subclasses to implement extensions without breaking compatibility. If you use qstyleoption_cast(), you normally do not need to check it.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QStyleOption`.
