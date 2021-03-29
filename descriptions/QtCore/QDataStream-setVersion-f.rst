.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: fa74920fe2fd052af891e1d44e267dd7

Sets the version number of the data serialization format to *v*, a value of the :sip:ref:`~PyQt6.QtCore.QDataStream.Version.Version` enum.

You don't *have* to set a version if you are using the current version of Qt, but for your own custom binary formats we recommend that you do; see :ref:`qdatastream-versioning` in the Detailed Description.

To accommodate new functionality, the datastream serialization format of some Qt classes has changed in some versions of Qt. If you want to read data that was created by an earlier version of Qt, or write data that can be read by a program that was compiled with an earlier version of Qt, use this function to modify the serialization format used by :sip:ref:`~PyQt6.QtCore.QDataStream`.

The :sip:ref:`~PyQt6.QtCore.QDataStream.Version.Version` enum provides symbolic constants for the different versions of Qt. For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qdatastream.py
    :lines: 129-130

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDataStream.version`, :sip:ref:`~PyQt6.QtCore.QDataStream.Version.Version`.
