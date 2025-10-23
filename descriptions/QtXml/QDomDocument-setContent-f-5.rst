.. sip:method-description::
    :status: todo
    :pysig: d8b95f782433e872251a4af4f402d2fa
    :realsig: (QIODevice*,bool,QString*,int*,int*)
    :digest: 4ef11a604a7d9974b7747e083c807b05

Use the overload taking ParseOptions instead.

This function reads the XML document from the IO device *dev*, returning true if the content was successfully parsed; otherwise returns ``false``.

**Note:** This method will try to open *dev* in read-only mode if it is not already open. In that case, the caller is responsible for calling close. This will change in Qt 7, which will no longer open *dev*. Applications should therefore open the device themselves before calling :sip:ref:`~PyQt6.QtXml.QDomDocument.setContent`.
