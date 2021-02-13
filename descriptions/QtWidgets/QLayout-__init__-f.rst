.. sip:method-description::
    :status: todo
    :pysig: a73944383ffd572ba8b60debc3383262
    :realsig: (QWidget*)
    :digest: a68fdb3d8016acb901fb5b62a86fce6e

Constructs a new top-level :sip:ref:`~PyQt6.QtWidgets.QLayout`, with parent *parent*.

The layout is set directly as the top-level layout for *parent*. There can be only one top-level layout for a widget. It is returned by :sip:ref:`~PyQt6.QtWidgets.QWidget.layout`.

If *parent* is ``nullptr``, then you must insert this layout into another layout, or set it as a widget's layout using :sip:ref:`~PyQt6.QtWidgets.QWidget.setLayout`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.setLayout`.
