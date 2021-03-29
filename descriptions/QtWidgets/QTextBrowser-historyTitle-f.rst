.. sip:method-description::
    :status: todo
    :pysig: d4d85079d3c184e4c59bdc73add11325
    :realsig: (int) const
    :digest: 339f5d8b0e46259892b8ebfb12aceab1

Returns the documentTitle() of the HistoryItem.

+----------+--------------------------------------------------------------+
| Input    | Return                                                       |
+==========+==============================================================+
| *i* < 0  | :sip:ref:`~PyQt6.QtWidgets.QTextBrowser.backward` history    |
+----------+--------------------------------------------------------------+
| *i* == 0 | current, see :sip:ref:`~PyQt6.QtWidgets.QTextBrowser.source` |
+----------+--------------------------------------------------------------+
| *i* > 0  | :sip:ref:`~PyQt6.QtWidgets.QTextBrowser.forward` history     |
+----------+--------------------------------------------------------------+

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_widgets_qtextbrowser.py
    :lines: 54-55
