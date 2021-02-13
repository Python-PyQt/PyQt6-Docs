.. sip:method-description::
    :status: todo
    :pysig: 3c5f8db1f89588f513ecfd6f79323aae
    :realsig: (int) const
    :digest: a36848490a3bee5581eef6834b542662

Returns the url of the HistoryItem.

+----------+--------------------------------------------------------------+
| Input    | Return                                                       |
+==========+==============================================================+
| *i* < 0  | :sip:ref:`~PyQt6.QtWidgets.QTextBrowser.backward` history    |
+----------+--------------------------------------------------------------+
| *i* == 0 | current, see :sip:ref:`~PyQt6.QtWidgets.QTextBrowser.source` |
+----------+--------------------------------------------------------------+
| *i* > 0  | :sip:ref:`~PyQt6.QtWidgets.QTextBrowser.forward` history     |
+----------+--------------------------------------------------------------+
