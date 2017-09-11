
from PyQt5.QtCore import ( QObject, pyqtSignal, pyqtSlot )
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QColorDialog
from Mezcal.Barrel import Bottle
from Ui_MezcalPicker import Ui_MezcalPicker

class Message( Bottle, Ui_MezcalPicker ):
	picked_colour = pyqtSignal( QColor )
	ts = QColor(100,20,30)
	theme_color = pyqtSignal( QColor )
	picked_type = pyqtSignal( str )
	sig_analogous1 = pyqtSignal( str )
	sig_analogous2 = pyqtSignal( str )
	sig_analogous3 = pyqtSignal( str )
	sig_compliments1 = pyqtSignal( str )
	sig_compliments2 = pyqtSignal( str )
	sig_mono1 = pyqtSignal( str )
	sig_mono2 = pyqtSignal( str )
	sig_mono3 = pyqtSignal( str )
	sig_scompliments1 = pyqtSignal( str )
	sig_scompliments2 = pyqtSignal( str )
	sig_scompliments3 = pyqtSignal( str )
	sig_tetrad1 = pyqtSignal( str )
	sig_tetrad2 = pyqtSignal( str )
	sig_tetrad3 = pyqtSignal( str )
	sig_tetrad4 = pyqtSignal( str )
	sig_triad1 = pyqtSignal( str )
	sig_triad2 = pyqtSignal( str )
	sig_triad3 = pyqtSignal( str )
	picked_style = pyqtSignal(str)

	@pyqtSlot()
	def pick_theme( self ):
		color = QColorDialog.getColor( self.ts )
		if color.isValid():
			style = lambda x: "background-color: rgb( %s, %s, %s );" % ( int(x[0]), int(x[1]), int(x[2]) )
			self.picked_colour.emit(color)
			self.push_rum_color.setStyleSheet( style( (color.red(), color.green(), color.blue( ) )  ) )
			self.theme_color.emit( color )

	@pyqtSlot( str )
	def convert_style( self, color ):
		rgb = color.replace( "background-color: rgb(", "" ).replace( ");","" ).split( "," )
		qcolor = QColor(int(rgb[0]), int(rgb[1]),int(rgb[2]))
		self.ts = qcolor
		self.picked_colour.emit( qcolor )

	@pyqtSlot( QColor )
	def set_theme( self, colour ):
		style = lambda x: "background-color: rgb( %s, %s, %s );" % ( int(x[0]), int(x[1]), int(x[2]) )
		self.rgb = ( colour.red(), colour.green(), colour.blue() )
		self.sig_analogous1.emit( style( self.analogous[0].rgb  ) )
		self.sig_analogous2.emit( style( self.analogous[1].rgb  ) )
		self.sig_analogous3.emit( style( self.analogous[2].rgb  ) )
		self.sig_compliments1.emit( style( self.complimentary[0].rgb ) )
		self.sig_compliments2.emit( style(self.complimentary[1].rgb  ) )
		self.sig_scompliments1.emit( style(self.split_compliments[0].rgb  ) )
		self.sig_scompliments2.emit( style(self.split_compliments[1].rgb  ) )
		self.sig_scompliments3.emit( style( self.split_compliments[2].rgb ) )
		self.sig_mono1.emit( style( self.monochromatic[0].rgb ) )
		self.sig_mono2.emit( style(self.monochromatic[1].rgb  ) )
		self.sig_mono3.emit( style( self.monochromatic[2].rgb ) )
		self.sig_triad1.emit( style( self.triads[0].rgb ) )
		self.sig_triad2.emit( style( self.triads[1].rgb  ) )
		self.sig_triad3.emit( style( self.triads[2].rgb ) )
		self.sig_tetrad1.emit( style( self.tetrads[0].rgb ) )
		self.sig_tetrad2.emit( style( self.tetrads[1].rgb ) )
		self.sig_tetrad3.emit( style( self.tetrads[2].rgb ) )
		self.sig_tetrad4.emit( style( self.tetrads[3].rgb ) )
		print( self.hex_scheme )

	@pyqtSlot()
	def set_scompliments1( self ):
		self.picked_type.emit(  self.push_scompliment1.text() )
		self.picked_style.emit(  self.scompliment1.styleSheet() )
	@pyqtSlot()
	def set_analogous3( self ):
		self.picked_type.emit(  self.push_analogous3.text() )
		self.picked_style.emit(  self.analogous3.styleSheet() )
	@pyqtSlot()
	def set_analogous1( self ):
		self.picked_type.emit(  self.push_analogous1.text() )
		self.picked_style.emit(  self.analogous1.styleSheet() )
	@pyqtSlot()
	def set_analogous2( self ):
		self.picked_type.emit(  self.push_analogous2.text() )
		self.picked_style.emit(  self.analogous2.styleSheet() )
	@pyqtSlot()
	def set_compliments2( self ):
		self.picked_type.emit(  self.push_compliment2.text() )
		self.picked_style.emit(  self.compliment2.styleSheet() )
	@pyqtSlot()
	def set_monochrome2( self ):
		self.picked_type.emit(  self.push_monochrome2.text() )
		self.picked_style.emit(  self.monochrome2.styleSheet() )
	@pyqtSlot()
	def set_monochrome3( self ):
		self.picked_type.emit(  self.push_monochrome3.text() )
		self.picked_style.emit(  self.monochrome3.styleSheet() )
	@pyqtSlot()
	def set_scompliments2( self ):
		self.picked_type.emit(  self.push_scompliment2.text() )
		self.picked_style.emit(  self.scompliment2.styleSheet() )
	@pyqtSlot()
	def set_scompliments3( self ):
		self.picked_type.emit(  self.push_scompliment3.text() )
		self.picked_style.emit(  self.scompliment3.styleSheet() )
	@pyqtSlot()
	def set_tetrad1( self ):
		self.picked_type.emit(  self.push_tetrad1.text() )
		self.picked_style.emit(  self.tetrad1.styleSheet() )
	@pyqtSlot()
	def set_tetrad2( self ):
		self.picked_type.emit(  self.push_tetrad2.text() )
		self.picked_style.emit(  self.tetrad2.styleSheet() )
	@pyqtSlot()
	def set_tetrad3( self ):
		self.picked_type.emit(  self.push_tetrad3.text() )
		self.picked_style.emit(  self.tetrad3.styleSheet() )
	@pyqtSlot()
	def set_triad1( self ):
		self.picked_type.emit(  self.push_triad1.text() )
		self.picked_style.emit(  self.triad1.styleSheet() )
	@pyqtSlot()
	def set_triad2( self ):
		self.picked_type.emit(  self.push_triad2.text() )
		self.picked_style.emit(  self.triad2.styleSheet() )
	@pyqtSlot()
	def set_tetrad3( self ):
		self.picked_type.emit(  self.push_triad3.text() )
		self.picked_style.emit(  self.triad3.styleSheet() )
	@pyqtSlot()
	def set_monochrome1( self ):
		self.picked_type.emit(  self.push_monochrome1.text() )
		self.picked_style.emit(  self.monochrome1.styleSheet() )
	@pyqtSlot()
	def set_tetrad4( self ):
		self.picked_type.emit(  self.push_tetrad4.text() )
		self.picked_style.emit(  self.tetrad4.styleSheet() )


