.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: ff095684f10eb5c042b215ed08ea85f0

If *enable* is true, enables caching of file information. If *enable* is false caching is disabled.

When caching is enabled, :sip:ref:`~PyQt6.QtCore.QFileInfo` reads the file information from the file system the first time it's needed, but generally not later.

Caching is enabled by default.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.refresh`, :sip:ref:`~PyQt6.QtCore.QFileInfo.caching`.
