.. sip:method-description::
    :status: todo
    :pysig: f68a9646b4b9824d6ee155882d0b2050
    :realsig: (const QString&,int)
    :digest: c121c5849d28d00e81bd4b947aef6a2b

Adds *prefix* to the current group and starts writing an array of size *size*. If *size* is -1 (the default), it is automatically determined based on the indexes of the entries written.

If you have many occurrences of a certain set of keys, you can use arrays to make your life easier. For example, let's suppose that you want to save a variable-length list of user names and passwords. You could then write:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qsettings.py
    :lines: 181-195

The generated keys will have the form

* ``logins/size``

* ``logins/1/userName``

* ``logins/1/password``

* ``logins/2/userName``

* ``logins/2/password``

* ``logins/3/userName``

* ``logins/3/password``

* ...

To read back an array, use :sip:ref:`~PyQt6.QtCore.QSettings.beginReadArray`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSettings.beginReadArray`, :sip:ref:`~PyQt6.QtCore.QSettings.endArray`, :sip:ref:`~PyQt6.QtCore.QSettings.setArrayIndex`.
