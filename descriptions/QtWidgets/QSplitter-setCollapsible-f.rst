.. sip:method-description::
    :status: todo
    :pysig: 47bc384ef78158df7bdc68df0f06aef9
    :realsig: (int,bool)
    :digest: 9841f74e1e9af44f4b8c549b2a317038

Sets whether the child widget at *index* is collapsible to *collapse*.

By default, children are collapsible, meaning that the user can resize them down to size 0, even if they have a non-zero minimumSize() or :sip:ref:`~PyQt6.QtWidgets.QSplitter.minimumSizeHint`. This behavior can be changed on a per-widget basis by calling this function, or globally for all the widgets in the splitter by setting the :sip:ref:`~PyQt6.QtWidgets.QSplitter.childrenCollapsible` property.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QSplitter.isCollapsible`, :sip:ref:`~PyQt6.QtWidgets.QSplitter.childrenCollapsible`.
