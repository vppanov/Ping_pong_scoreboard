import os
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql


class BlobDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(BlobDelegate, self).initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignCenter

    def displayText(self, value, locale):
        if isinstance(value, QtCore.QByteArray):
            value = value.data().decode()
        return super(BlobDelegate, self).displayText(value, locale)


def createConnection():
    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "stats.db")
    db.setDatabaseName(file)
    if not db.open():
        QtWidgets.QMessageBox.critical(
            None,
            QtWidgets.qApp.tr("Cannot open database"),
            QtWidgets.qApp.tr(
                "Unable to establish a database connection.\n"
                "This example needs SQLite support. Please read "
                "the Qt SQL driver documentation for information "
                "how to build it.\n\n"
                "Click Cancel to exit."
            ),
            QtWidgets.QMessageBox.Cancel)
        return False
    return True


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    if not createConnection():
        sys.exit(-1)
    w = QtWidgets.QTableView()

    w.setFont(QtGui.QFont('Arial', 18))
    w.horizontalHeader().setStretchLastSection(False)
    w.horizontalHeader().setFixedHeight(40)
    w.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
    # w.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
    w.setWordWrap(True)
    delegate = BlobDelegate(w)
    w.setItemDelegateForColumn(4, delegate)
    model = QtSql.QSqlQueryModel()
    model.setQuery("SELECT * FROM Singles_statistics")
    w.setModel(model)
    w.resize(1024, 600)
    delegate = BlobDelegate(w)
    w.setItemDelegate(delegate)
    w.show()
    sys.exit(app.exec_())
