# Rec.Inf.
Proyecto Final

Traceback (most recent call last):
  File "main.py", line 14, in <module>
    main()
  File "main.py", line 11, in main
    database.insertBLOB(stemmed)
  File "/home/ivanvillanueva/Documents/Rec.Inf./base de documentos/BaseDeDatos.py", line 31, in insertBLOB
    file = self.convertToBinaryData(testfile)
  File "/home/ivanvillanueva/Documents/Rec.Inf./base de documentos/BaseDeDatos.py", line 18, in convertToBinaryData
    with open(filename, 'rb') as file:
TypeError: expected str, bytes or os.PathLike object, not NoneType
