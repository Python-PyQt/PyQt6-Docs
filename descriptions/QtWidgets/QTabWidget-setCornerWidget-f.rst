.. sip:method-description::
    :status: todo
    :pysig: de7db18542fd73eeb5a53a26f5ff2640
    :realsig: (QWidget*,Qt::Corner)
    :digest: 2b808835196088c6c8ac14053573067b

Sets the given *widget* to be shown in the specified *corner* of the tab widget. The geometry of the widget is determined based on the widget's :sip:ref:`~PyQt6.QtWidgets.QTabWidget.sizeHint` and the style().

Only the horizontal element of the *corner* will be used.

Passing ``nullptr`` shows no widget in the corner.

Any previously set corner widget is hidden.

All widgets set here will be deleted by the tab widget when it is destroyed unless you separately reparent the widget after setting some other corner widget (or ``nullptr``).

Note: Corner widgets are designed for :sip:ref:`~PyQt6.QtWidgets.QTabWidget.TabPosition.North` and :sip:ref:`~PyQt6.QtWidgets.QTabWidget.TabPosition.South` tab positions; other orientations are known to not work properly.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QTabWidget.cornerWidget`, :sip:ref:`~PyQt6.QtWidgets.QTabWidget.setTabPosition`.
