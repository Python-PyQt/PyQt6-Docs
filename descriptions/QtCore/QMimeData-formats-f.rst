.. sip:method-description::
    :status: todo
    :pysig: a34fd3e57af0cc79ef189995220041c2
    :realsig: () const
    :digest: ee88ce7904ec9e20fd04ae7fbb380927

Returns a list of formats supported by the object. This is a list of MIME types for which the object can return suitable data. The formats in the list are in a priority order.

For the most common types of data, you can call the higher-level functions :sip:ref:`~PyQt6.QtCore.QMimeData.hasText`, :sip:ref:`~PyQt6.QtCore.QMimeData.hasHtml`, :sip:ref:`~PyQt6.QtCore.QMimeData.hasUrls`, :sip:ref:`~PyQt6.QtCore.QMimeData.hasImage`, and :sip:ref:`~PyQt6.QtCore.QMimeData.hasColor` instead.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMimeData.hasFormat`, :sip:ref:`~PyQt6.QtCore.QMimeData.setData`, :sip:ref:`~PyQt6.QtCore.QMimeData.data`.
