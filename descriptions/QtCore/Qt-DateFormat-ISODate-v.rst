.. sip:enum-member-description::
    :status: todo
    :value: 1
    :digest: 33ef4dc6f764c19e19ed6b6be90c5cfa

`ISO 8601 <https://doc.qt.io/qt-6/http://www.iso.org/iso/catalogue_detail?csnumber=40874>`_ extended format, as for ``ISODateWithMs``, but omitting the milliseconds (``.zzz``) part when converting to a string. There is no difference when reading from a string: if a fractional part is present on the last time field, either format will accept it.
