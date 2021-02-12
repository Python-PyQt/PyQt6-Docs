.. sip:method-description::
    :status: todo
    :pysig: a5704e7d57089c440a7d83c72d987b9e
    :realsig: (const QByteArray&)
    :digest: 716bd63d6aecfd92c4bd403f7a96fdc2

Creates a :sip:ref:`~PyQt6.QtCore.QUuid` object from the :sip:ref:`~PyQt6.QtCore.QByteArray` *text*, which must be formatted as five hex fields separated by '-', e.g., "{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}" where each 'x' is a hex digit. The curly braces shown here are optional, but it is normal to include them. If the conversion fails, a null UUID is created. See :sip:ref:`~PyQt6.QtCore.QUuid.toByteArray` for an explanation of how the five hex fields map to the public data members in :sip:ref:`~PyQt6.QtCore.QUuid`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUuid.toByteArray`, :sip:ref:`~PyQt6.QtCore.QUuid`.
