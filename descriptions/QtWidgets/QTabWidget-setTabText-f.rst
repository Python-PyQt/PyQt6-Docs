.. sip:method-description::
    :status: todo
    :pysig: d4d85079d3c184e4c59bdc73add11325
    :realsig: (int,const QString&)
    :digest: e081bd3ac03485acfbe5f4b7351dc245

Defines a new *label* for the page at position *index*'s tab.

If the provided text contains an ampersand character ('&'), a shortcut is automatically created for it. The character that follows the '&' will be used as the shortcut key. Any previous shortcut will be overwritten, or cleared if no shortcut is defined by the text. See the QShortcut documentation for details (to display an actual ampersand, use '&&').

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QTabWidget.tabText`.
