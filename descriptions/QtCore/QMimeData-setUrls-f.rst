.. sip:method-description::
    :status: todo
    :pysig: 459251bb2973b2a4da8428d1f5914624
    :realsig: (const QList<QUrl>&)
    :digest: d2e72f5765a324ef7d209b5004acefa2

Sets the URLs stored in the MIME data object to those specified by *urls*.

URLs correspond to the MIME type ``text/uri-list``.

Since Qt 5.0,  also exports the urls as plain text, if :sip:ref:`~PyQt6.QtCore.QMimeData.setText` was not called before, to make it possible to drop them into any lineedit and text editor.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMimeData.urls`, :sip:ref:`~PyQt6.QtCore.QMimeData.hasUrls`, :sip:ref:`~PyQt6.QtCore.QMimeData.setData`.
