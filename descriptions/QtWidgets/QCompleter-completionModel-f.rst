.. sip:method-description::
    :status: todo
    :pysig: b1398307ea89da5fe868fb6740f9bc55
    :realsig: () const
    :digest: 72b0a0d8d9b6767ba2a986bb8d69425d

Returns the completion model. The completion model is a read-only list model that contains all the possible matches for the current completion prefix. The completion model is auto-updated to reflect the current completions.

**Note:** The return value of this function is defined to be an :sip:ref:`~PyQt6.QtCore.QAbstractItemModel` purely for generality. This actual kind of model returned is an instance of an :sip:ref:`~PyQt6.QtCore.QAbstractProxyModel` subclass.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QCompleter.completionPrefix`, :sip:ref:`~PyQt6.QtWidgets.QCompleter.model`.
