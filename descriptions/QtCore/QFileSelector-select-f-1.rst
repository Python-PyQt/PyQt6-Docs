.. sip:method-description::
    :status: todo
    :pysig: 85614b66e1780877cf0b12760bffaa85
    :realsig: (const QUrl&) const
    :digest: 02d39d68e18a6f94207f785b635718d6

This is a convenience version of select operating on :sip:ref:`~PyQt6.QtCore.QUrl` objects. If the scheme is not file or qrc, *filePath* is returned immediately. Otherwise selection is applied to the path of *filePath* and a :sip:ref:`~PyQt6.QtCore.QUrl` is returned with the selected path and other :sip:ref:`~PyQt6.QtCore.QUrl` parts the same as *filePath*.

See the class overview for the selection algorithm.
