#!/usr/bin/env python
from PyQt5.QtCore import ( QObject, pyqtSignal, pyqtSlot )
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QWidget
from Bottle import Message

class SampleWidget( QWidget, Message  ):
	def __init__( self, parent=None ):
		super( SampleWidget, self ).__init__( parent )
		Message.__init__(self)
		self.setupUi( self )
		self.requiredFields = [ 'Name', 'Title', 'ExpHex' ]
		self.theme_color.emit( QColor(102,0,212) )
		self.rgb = (102,0,212)
		picker = lambda x: print( ( x.red(), x.green(), x.blue() ) )
		self.picked_style.connect( self.convert_style )
		self.picked_type.connect( print )
		self.picked_colour.connect( picker )
		self.theme_color.connect( picker )

if __name__ == "__main__":
    import sys
    app = QApplication( sys.argv )
    guinness = SampleWidget( )
    guinness.show( )
    sys.exit( app.exec_( ) )
