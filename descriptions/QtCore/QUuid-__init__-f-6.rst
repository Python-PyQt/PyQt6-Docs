.. sip:method-description::
    :status: todo
    :pysig: 547000f13f2e7a3400a249c3cc6ac740
    :realsig: (QAnyStringView)
    :digest: d415ce254215bc6801e9d8c492e00679

Creates a :sip:ref:`~PyQt6.QtCore.QUuid` object from the string *text*, which must be formatted as five hex fields separated by '-', e.g., "{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}" where each 'x' is a hex digit. The curly braces shown here are optional, but it is normal to include them. If the conversion fails, a null UUID is created. See :sip:ref:`~PyQt6.QtCore.QUuid.toString` for an explanation of how the five hex fields map to the public data members in :sip:ref:`~PyQt6.QtCore.QUuid`.

**Note:** In Qt versions prior to 6.3, this constructor was an overload set consisting of QString, :sip:ref:`~PyQt6.QtCore.QByteArray` and ``const char\*`` instead of one constructor taking QAnyStringView.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUuid.toString`, :sip:ref:`~PyQt6.QtCore.QUuid`.
