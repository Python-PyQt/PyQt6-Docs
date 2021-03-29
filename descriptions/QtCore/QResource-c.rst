.. sip:class-description::
    :status: todo
    :brief: Interface for reading directly from resources
    :digest: 1664dd118ab09051c52d0a723d5afd40

The :sip:ref:`~PyQt6.QtCore.QResource` class provides an interface for reading directly from resources.

:sip:ref:`~PyQt6.QtCore.QResource` is an object that represents a set of data (and possibly children) relating to a single resource entity. :sip:ref:`~PyQt6.QtCore.QResource` gives direct access to the bytes in their raw format. In this way direct access allows reading data without buffer copying or indirection. Indirection is often useful when interacting with the resource entity as if it is a file, this can be achieved with :sip:ref:`~PyQt6.QtCore.QFile`. The data and children behind a :sip:ref:`~PyQt6.QtCore.QResource` are normally compiled into an application/library, but it is also possible to load a resource at runtime. When loaded at run time the resource file will be loaded as one big set of data and then given out in pieces via references into the resource tree.

A :sip:ref:`~PyQt6.QtCore.QResource` can either be loaded with an absolute path, either treated as a file system rooted with a ``/`` character, or in resource notation rooted with a ``:`` character. A relative resource can also be opened which will be found in the list of paths returned by :sip:ref:`~PyQt6.QtCore.QDir.searchPaths`.

A :sip:ref:`~PyQt6.QtCore.QResource` that is representing a file will have data backing it, this data can possibly be compressed, in which case :sip:ref:`~PyQt6.QtCore.qUncompress` must be used to access the real data; this happens implicitly when accessed through a :sip:ref:`~PyQt6.QtCore.QFile`. A :sip:ref:`~PyQt6.QtCore.QResource` that is representing a directory will have only children and no data.

.. _qresource-dynamic-resource-loading:

Dynamic Resource Loading
------------------------

A resource can be left out of an application's binary and loaded when it is needed at run-time by using the :sip:ref:`~PyQt6.QtCore.QResource.registerResource` function. The resource file passed into :sip:ref:`~PyQt6.QtCore.QResource.registerResource` must be a binary resource as created by rcc. Further information about binary resources can be found in `The Qt Resource System <https://doc.qt.io/qt-6/resources.html>`_ documentation.

This can often be useful when loading a large set of application icons that may change based on a setting, or that can be edited by a user and later recreated. The resource is immediately loaded into memory, either as a result of a single file read operation, or as a memory mapped file.

This approach can prove to be a significant performance gain as only a single file will be loaded, and pieces of data will be given out via the path requested in :sip:ref:`~PyQt6.QtCore.QResource.setFileName`.

The :sip:ref:`~PyQt6.QtCore.QResource.unregisterResource` function removes a reference to a particular file. If there are :sip:ref:`~PyQt6.QtCore.QResource` objects that currently reference resources related to the unregistered file, they will continue to be valid but the resource file itself will be removed from the resource roots, and thus no further :sip:ref:`~PyQt6.QtCore.QResource` can be created pointing into this resource data. The resource itself will be unmapped from memory when the last :sip:ref:`~PyQt6.QtCore.QResource` that points to it is destroyed.

.. seealso:: `The Qt Resource System <https://doc.qt.io/qt-6/resources.html>`_, :sip:ref:`~PyQt6.QtCore.QFile`, :sip:ref:`~PyQt6.QtCore.QDir`, :sip:ref:`~PyQt6.QtCore.QFileInfo`.
