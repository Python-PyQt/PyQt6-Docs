.. sip:enum-member-description::
    :status: todo
    :value: 25
    :digest: 2bdafb5a1a6af3323fe9c75a5a055cad

Enables compression of certain frequent events. On the X11 windowing system, the default value is true, which means that :sip:ref:`~PyQt6.QtCore.QEvent.Type.MouseMove`, :sip:ref:`~PyQt6.QtCore.QEvent.Type.TouchUpdate`, and changes in window size and position will be combined whenever they occur more frequently than the application handles them, so that they don't accumulate and overwhelm the application later. On Windows 8 and above the default value is also true, but it only applies to touch events. Mouse and window events remain unaffected by this flag. On other platforms, the default is false. (In the future, the compression feature may be implemented across platforms.) You can test the attribute to see whether compression is enabled. If your application needs to handle all events with no compression, you can unset this attribute. Notice that input events from tablet devices will not be compressed. See  if you want these to be compressed as well. This value was added in Qt 5.7.
