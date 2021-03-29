.. sip:method-description::
    :status: todo
    :pysig: 2b9057d9b4a06375acf76e6922f506e2
    :realsig: () const
    :digest: 3b060f229206cd1c3791732b9036aa72

If this :sip:ref:`~PyQt6.QtQml.QJSValue` is a :sip:ref:`~PyQt6.QtCore.QObject`, returns the :sip:ref:`~PyQt6.QtCore.QObject` pointer that the :sip:ref:`~PyQt6.QtQml.QJSValue` represents; otherwise, returns ``nullptr``.

If the :sip:ref:`~PyQt6.QtCore.QObject` that this :sip:ref:`~PyQt6.QtQml.QJSValue` wraps has been deleted, this function returns ``nullptr`` (i.e. it is possible for  to return ``nullptr`` even when :sip:ref:`~PyQt6.QtQml.QJSValue.isQObject` returns true).

.. seealso:: :sip:ref:`~PyQt6.QtQml.QJSValue.isQObject`.
