.. sip:method-description::
    :status: todo
    :pysig: 44d48281574944fe2eb4a9b2393c0557
    :realsig: (QtMsgType,bool)
    :digest: 4888f62bfd2958d9f11695f44dcc2afb

Changes the message type *type* for the category to *enable*.

This method is meant for use only from inside a filter installed with installFilter(). For an overview on how to configure categories globally, see :ref:`qloggingcategory-configuring-categories`.

**Note:** ``QtFatalMsg`` cannot be changed; it will always remain ``true``.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLoggingCategory.isEnabled`.
