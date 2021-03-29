.. sip:method-description::
    :status: todo
    :pysig: f6a258d8f3ee5206d682d799316314b1
    :realsig: (bool)
    :digest: e5c6d7cf411e0358520801bdf87d4227

Finds a new widget to give the keyboard focus to, as appropriate for Tab and Shift+Tab, and returns ``true`` if it can find a new widget, or false if it cannot. If *next* is true, this function searches forward; if *next* is false, it searches backward.

You can reimplement this function in a subclass of :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` to provide fine-grained control over how tab focus passes inside your scene. The default implementation is based on the tab focus chain defined by :sip:ref:`~PyQt6.QtWidgets.QGraphicsWidget.setTabOrder`.
