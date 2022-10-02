.. sip:method-description::
    :status: todo
    :pysig: 77fc5b9585221742f56bbf6c51142efc
    :realsig: (QAnyStringView)
    :digest: 208a6ad5665c9c553ad9a88fd61fec8a

Creates a :sip:ref:`~PyQt6.QtCore.QUuid` object from the string *string*, which must be formatted as five hex fields separated by '-', e.g., "{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}" where each 'x' is a hex digit. The curly braces shown here are optional, but it is normal to include them. If the conversion fails, a null UUID is returned. See :sip:ref:`~PyQt6.QtCore.QUuid.toString` for an explanation of how the five hex fields map to the public data members in :sip:ref:`~PyQt6.QtCore.QUuid`.

**Note:** In Qt versions prior to 6.3, this function was an overload set consisting of QStringView and QLatin1StringView instead of one function taking QAnyStringView.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUuid.toString`, :sip:ref:`~PyQt6.QtCore.QUuid`.
