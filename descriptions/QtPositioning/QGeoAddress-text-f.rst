.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 45eb467b6578d458b30e3667d6af389c

Returns the address as a single formatted string. It is the recommended string to use to display the address to the user. It typically takes the format of an address as found on an envelope, but this is not always necessarily the case.

The address text is either automatically generated or explicitly assigned. This can be determined by checking :sip:ref:`~PyQt6.QtPositioning.QGeoAddress.isTextGenerated`.

If an empty string is provided to :sip:ref:`~PyQt6.QtPositioning.QGeoAddress.setText`, then :sip:ref:`~PyQt6.QtPositioning.QGeoAddress.isTextGenerated` will be set to ``true`` and  will return a string which is locally formatted according to :sip:ref:`~PyQt6.QtPositioning.QGeoAddress.countryCode` and based on the elements of the address such as street, city and so on. Because the text string is generated from the address elements, a sequence of calls such as , :sip:ref:`~PyQt6.QtPositioning.QGeoAddress.setStreet`,  may return different strings for each invocation of .

If a non-empty string is provided to :sip:ref:`~PyQt6.QtPositioning.QGeoAddress.setText`, then :sip:ref:`~PyQt6.QtPositioning.QGeoAddress.isTextGenerated` will be set to ``false`` and  will always return the explicitly assigned string. Calls to modify other elements such as :sip:ref:`~PyQt6.QtPositioning.QGeoAddress.setStreet`, :sip:ref:`~PyQt6.QtPositioning.QGeoAddress.setCity` and so on will not affect the resultant string from .

.. seealso:: :sip:ref:`~PyQt6.QtPositioning.QGeoAddress.setText`.
