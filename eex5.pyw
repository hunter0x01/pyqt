from PyQt5 import QtCore, QtGui, QtWidgets


class PartsList(QtWidgets.QListView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGridSize(QtCore.QSize(108, 80))
        self.setViewMode(QtWidgets.QListView.IconMode)
        self.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self._model = LibraryModel(self)
        self.setModel(self._model)
        path = QtCore.QStandardPaths.writableLocation(
            QtCore.QStandardPaths.PicturesLocation
        )
        d = QtCore.QDir(path)
        formats = [
            "*.{}".format(fm.data().decode())
            for fm in QtGui.QImageReader.supportedImageFormats()
        ]
        for info in d.entryInfoList(formats, QtCore.QDir.Files):
            part = self.__getPartItem(info.filePath())
            self._model.appendRow(part)

    def __getPartItem(self, name):
        part = QtGui.QStandardItem()
        pixmap = QtGui.QPixmap(name)
        part.setData(pixmap, QtCore.Qt.DecorationRole)
        part.setText(name)
        part.setEditable(False)
        return part


class LibraryModel(QtGui.QStandardItemModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setColumnCount(1)

    def mimeTypes(self):
        return super().mimeTypes() + ["part/name"]

    def mimeData(self, indexes):
        data = super().mimeData(indexes)
        encoded = QtCore.QByteArray()
        stream = QtCore.QDataStream(encoded, QtCore.QIODevice.WriteOnly)
        for ix in indexes:
            stream << ix.data(QtCore.Qt.DecorationRole)
        data.setData("part/name", encoded)
        return data


class SchematicView(QtWidgets.QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        scene = QtWidgets.QGraphicsScene(self)
        self.setScene(scene)
        self.setSceneRect(0, 0, 1, 1)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat("part/name"):
            event.acceptProposedAction()

    def dragMoveEvent(self, event):
        if event.mimeData().hasFormat("part/name"):
            event.acceptProposedAction()

    def dropEvent(self, event):
        sp = self.mapToScene(event.pos())
        fmt = "part/name"
        data = event.mimeData()
        if data.hasFormat(fmt):
            encoded = data.data(fmt)
            stream = QtCore.QDataStream(encoded, QtCore.QIODevice.ReadOnly)
            pixmap = QtGui.QPixmap()
            while not stream.atEnd():
                stream >> pixmap
                pixmap_item = self.scene().addPixmap(pixmap)
                pixmap_item.setPos(sp)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    hlay = QtWidgets.QHBoxLayout(w)
    pl = PartsList()
    sv = SchematicView()
    hlay.addWidget(pl)
    hlay.addWidget(sv)
    w.resize(640, 480)
    w.show()
    sys.exit(app.exec_())