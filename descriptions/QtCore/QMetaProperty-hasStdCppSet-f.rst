.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 09978ecc02fc77c14f6f90e08f981b23

Returns ``true`` if the property has a C++ setter function that follows Qt's standard "name" / "setName" pattern. Designer and uic query  in order to avoid expensive :sip:ref:`~PyQt6.QtCore.QObject.setProperty` calls. All properties in Qt [should] follow this pattern.
