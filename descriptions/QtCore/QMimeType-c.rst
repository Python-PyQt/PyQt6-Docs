.. sip:class-description::
    :status: todo
    :brief: Describes types of file or data, represented by a MIME type string
    :digest: 6e6779ad3c66e316fc2a4c13b47f687b

The :sip:ref:`~PyQt6.QtCore.QMimeType` class describes types of file or data, represented by a MIME type string.

For instance a file named "readme.txt" has the MIME type "text/plain". The MIME type can be determined from the file name, or from the file contents, or from both. MIME type determination can also be done on buffers of data not coming from files.

Determining the MIME type of a file can be useful to make sure your application supports it. It is also useful in file-manager-like applications or widgets, in order to display an appropriate :sip:ref:`~PyQt6.QtCore.QMimeType.iconName` for the file, or even the descriptive :sip:ref:`~PyQt6.QtCore.QMimeType.comment` in detailed views.

To check if a file has the expected MIME type, you should use :sip:ref:`~PyQt6.QtCore.QMimeType.inherits` rather than a simple string comparison based on the :sip:ref:`~PyQt6.QtCore.QMimeType.name`. This is because MIME types can inherit from each other: for instance a C source file is a specific type of plain text file, so text/x-csrc inherits text/plain.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMimeDatabase`, `MIME Type Browser Example <https://doc.qt.io/qt-6/qtcore-mimetypes-mimetypebrowser-example.html>`_.
