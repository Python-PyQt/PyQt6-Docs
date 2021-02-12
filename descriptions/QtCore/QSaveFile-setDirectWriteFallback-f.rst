.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: dbe8d25a4a6853e93fc3f4f7b0bdda9f

Allows writing over the existing file if necessary.

:sip:ref:`~PyQt6.QtCore.QSaveFile` creates a temporary file in the same directory as the final file and atomically renames it. However this is not possible if the directory permissions do not allow creating new files. In order to preserve atomicity guarantees, :sip:ref:`~PyQt6.QtCore.QSaveFile.open` fails when it cannot create the temporary file.

In order to allow users to edit files with write permissions in a directory with restricted permissions, call  with *enabled* set to true, and the following calls to :sip:ref:`~PyQt6.QtCore.QSaveFile.open` will fallback to opening the existing file directly and writing into it, without the use of a temporary file. This does not have atomicity guarantees, i.e. an application crash or for instance a power failure could lead to a partially-written file on disk. It also means :sip:ref:`~PyQt6.QtCore.QSaveFile.cancelWriting` has no effect, in such a case.

Typically, to save documents edited by the user, call (true), and to save application internal files (configuration files, data files, ...), keep the default setting which ensures atomicity.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSaveFile.directWriteFallback`.
