.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: de644eb61fd6663265de516e56388946

Returns the tag associated with this method.

Tags are special macros recognized by ``moc`` that make it possible to add extra information about a method.

Tag information can be added in the following way in the function declaration:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qmetaobject.py
    :lines: 153-160

and the information can be accessed by using:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qmetaobject.py
    :lines: 164-169

For the moment, ``moc`` will extract and record all tags, but it will not handle any of them specially. You can use the tags to annotate your methods differently, and treat them according to the specific needs of your application.

**Note:** Since Qt 5.0, ``moc`` expands preprocessor macros, so it is necessary to surround the definition with ``#ifndef`` ``Q_MOC_RUN``, as shown in the example above. This was not required in Qt 4. The code as shown above works with Qt 4 too.
