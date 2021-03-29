.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: 424f351ea3466ab7e348a831967a06aa

Creates a :sip:ref:`~PyQt6.QtCore.QUuid` object from the string *text*, which must be formatted as five hex fields separated by '-', e.g., "{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}" where each 'x' is a hex digit. The curly braces shown here are optional, but it is normal to include them. If the conversion fails, a null UUID is created. See :sip:ref:`~PyQt6.QtCore.QUuid.toString` for an explanation of how the five hex fields map to the public data members in :sip:ref:`~PyQt6.QtCore.QUuid`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUuid.toString`, :sip:ref:`~PyQt6.QtCore.QUuid`.
