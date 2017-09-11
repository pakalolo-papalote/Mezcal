import hashlib
import re, math
import numpy as np
from collections import namedtuple

class Shot:
	r, g, b = 255, 255, 255
	rgb = [ 255, 255, 255 ]
	h, s, v = 0, 0, 100
	hsv = [ 0, 0, 100 ]
	hex =  "#ffffff"
	updating = False

	def __init__( self, rgb=None, hsv=None, hex=None ):
		if type( rgb ) is tuple:
			if [ 255>=val>=0 for val in rgb ] == [True,True,True]:
				self.rgb = [ rgb[0], rgb[1], rgb[2] ]
			else: default = True
		elif type(hsv) is tuple:
			if 360>=hsv[0]>=0 and 100>= hsv[1]>=0 and 100>= hsv[2]>=0:
				self.hsv =  [ hsv[0], hsv[1], hsv[2] ]
			else: default = True
		elif type(hex) is str:
			regex = re.compile( r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', re.IGNORECASE )
			if regex.match( hex ):
				self.hex = hex
			else: default = True
		else: default = True
		if default is True:
			self.hex = "#ffffff"
		self.update()

	def __setattr__( self, name, value ):
		object.__setattr__( self, name, value )
		if name is not "last":
			if self.updating is not True and name is not "updating":
				self.last = name
				self.updating = True
				self.update()

	def update( self ):
		if self.last is "rgb":

			self.r = self.rgb[0]
			self.g = self.rgb[1]
			self.b = self.rgb[2]
			self.update_from_rgb()
		elif self.last is "r" or self.last is "g" or self.last is "b":
			self.rgb = [ self.r, self.g, self.b ]
			self.update_from_rgb()
		elif self.last is "hsv":
			self.h = self.hsv[0]
			self.s = self.hsv[1]
			self.v = self.hsv[2]
			self.update_from_hsv()
		elif self.last is "h" or self.last is "s" or self.last is "v":
			self.hsv = [ self.h, self.s, self.v ]
			self.update_from_hsv()
		elif self.last is "hex":
			self.update_from_hex()
		else: pass
		self.updating = False

	def update_from_hsv(self):
		rgb_clr = self.hsv2rgb( tuple( self.hsv )  )
		self.rgb = list( [ float( val * 255 ) for val in rgb_clr ] )
		self.r = self.rgb[0]
		self.g = self.rgb[1]
		self.b = self.rgb[2]
		self.hex = self.rgb2hex( rgb_clr )

	def update_from_rgb( self ):
		rgb_clr = [ float(val / 255) for val in self.rgb ]
		hsv_clr = self.rgb2hsv( tuple( rgb_clr[:3] ) )
		self.hsv = list( [np.round( hsv_clr[0] ), np.round( hsv_clr[1] ), np.round( hsv_clr[2] )] )
		self.h = self.hsv[0]
		self.s = self.hsv[1]
		self.v = self.hsv[2]
		self.hex = self.rgb2hex( rgb_clr )

	def update_from_hex( self ):
		rgb_clr = self.hex2rgb( str( self.hex ) )
		self.rgb = list( [ float( val * 255 ) for val in rgb_clr ] )
		self.r = self.rgb[0]
		self.g = self.rgb[1]
		self.b = self.rgb[2]
		hsv_clr = self.rgb2hsv( rgb_clr )
		self.hsv = list( [ np.round( hsv_clr[0]  ), np.round( hsv_clr[1] ), np.round( hsv_clr[2] )] )
		self.h = self.hsv[0]
		self.s = self.hsv[1]
		self.v = self.hsv[2]

	def rgb2hex( self, rgb, force_long=True):
		FLOAT_ERROR = 0.0000005
		hx = '#' + ''.join(["%02x" % int(c*255 + 0.5 - FLOAT_ERROR) for c in rgb])
		if force_long == False and \
			hx[1] == hx[2] and \
			hx[3] == hx[4] and \
			hx[5] == hx[6]:
			return '#' + hx[1] + hx[3] + hx[5]
		return hx

	def hex2rgb( self, str_rgb):
		try:
			rgb = str_rgb[1:]
			if len(rgb) == 6: r, g, b = rgb[0:2], rgb[2:4], rgb[4:6]
			elif len(rgb) == 3: r, g, b = rgb[0] * 2, rgb[1] * 2, rgb[2] * 2
			else: raise ValueError()
		except: raise ValueError("Invalid value %r provided for rgb color." % str_rgb)
		return tuple([float(int(v, 16)) / 255 for v in (r, g, b)])
		# From: http://code.activestate.com/recipes/576919-python-rgb-and-hsv-conversion/

	def rgb2hsv( self,  rgb ):
		r, g, b = rgb[0], rgb[1], rgb[2]
		mx = max(r, g, b)
		mn = min(r, g, b)
		df = mx-mn
		if mx == mn: h = 0
		elif mx == r:
			h = (60 * ((g-b)/df) + 360) % 360
		elif mx == g: h = (60 * ((b-r)/df) + 120) % 360
		elif mx == b: h = (60 * ((r-g)/df) + 240) % 360
		if mx == 0: s = 0
		else: s = df/mx
		v = mx
		hsv = (h, s*100, v*100)
		return hsv

	def hsv2rgb( self, hsv):
		h = float(hsv[0])
		s = float(hsv[1]/100)
		v = float(hsv[2]/100)
		h60 = h / 60.0
		h60f = math.floor(h60)
		hi = int(h60f) % 6
		f = h60 - h60f
		p = v * (1 - s)
		q = v * (1 - f * s)
		t = v * (1 - (1 - f) * s)
		r, g, b = 0, 0, 0
		if hi == 0: r, g, b = v, t, p
		elif hi == 1: r, g, b = q, v, p
		elif hi == 2: r, g, b = p, v, t
		elif hi == 3: r, g, b = p, q, v
		elif hi == 4: r, g, b = t, p, v
		elif hi == 5: r, g, b = v, p, q
		rgb = (float(r), float(g), float(b ))
		return rgb

	hex2hsv = lambda x: self.rgb2hsv(self.hex2rgb(x))

class Bottle:
	complimentary = [ Shot(), Shot() ]
	split_compliments = [ Shot(), Shot(), Shot() ]
	triads = [ Shot(), Shot(), Shot() ]
	tetrads = [ Shot(), Shot(), Shot(), Shot() ]
	analogous = [ Shot(), Shot(), Shot() ]
	monochromatic = [ Shot(), Shot(), Shot() ]
	hex_scheme = None
	rgb_scheme =  None
	hsv_scheme = None

	def __init__( self, hex=None, rgb=None, hsv=None ):
		self.generating = False
		self.rumHex( hex, rgb, hsv )

	def __getattribute__( self, name ):
		if name is "hex_scheme" or name is "rgb_scheme" or name is "hsv_scheme":
			if self.generating is False:
				self.generating = True
				object.__setattr__(self, name, {"complimentary": [], "split_compliments": [],"triads": [], "tetrads": [],"analogous": [], "monochromatic": [] } )
				self.get_scheme( name )
		return object.__getattribute__(self, name)
		object.__setattr__( self, name, None )

	def __setattr__( self, name, value ):
		if name is "hex":
			self.rumHex( hex=value )
		elif name is "rgb":
			self.rumHex( rgb=value )
		elif name is "hsv":
			self.rumHex( hsv=value )
		else:
			object.__setattr__( self, name, value )

	def rumHex( self, hex=None, rgb=None, hsv=None ):
		if hex is not None:
			self.complimentary[0].hex = hex
		elif rgb is not None:
			self.complimentary[0].rgb = rgb
		elif hsv is not None:
			self.complimentary[0].hsv = hsv
		else: pass

		for scheme in [self.complimentary, self.triads, self.tetrads, self.analogous, self.monochromatic, self.split_compliments]:
			for shot in scheme:
				shot.hsv = self.complimentary[0].hsv

		self.complimentary[1].h = ( self.complimentary[0].h + 360 / 2 ) % 360
		self.complimentary[1].update()

		offset = 360 / 15
		self.split_compliments[1].h = ( self.complimentary[0].h + 360 / 2 - offset ) % 360
		self.split_compliments[2].h = ( self.complimentary[0].h + 360 / 2 + offset ) % 360

		offset = 360 / 3
		self.triads[1].h = ( self.complimentary[0].h + offset ) % 360
		self.triads[2].h = ( self.complimentary[0].h - offset ) % 360

		offset = 360 / 4
		self.tetrads[1].h = ( self.complimentary[0].h + offset )  % 360
		self.tetrads[2].h = ( self.complimentary[0].h + ( 2 * offset ) ) % 360
		self.tetrads[3].h =  ( self.complimentary[0].h + ( 3 * offset ) )  % 360

		offset = 360 / 12
		self.analogous[1].h =  ( self.complimentary[0].h - offset ) % 360
		self.analogous[2].h = ( self.complimentary[0].h + offset ) % 360

		if self.monochromatic[0].s < ( 100 / 10 ):
			self.monochromatic[1].s = ( self.complimentary[0].s + 100 / 3 ) % 100
			self.monochromatic[2].s = ( self.complimentary[0].s + 2 * 100 / 3 ) % 100
		else:
			self.monochromatic[2].v = ( self.complimentary[0].v + 100 / 3 ) % 100
			self.monochromatic[1].v = ( self.complimentary[0].v + 2 * 100 / 3 ) % 100

	def get_scheme( self, name ):
		if name is "hex_scheme":
			self.hex_scheme['complimentary'] = [ shot.hex for shot in self.complimentary ]
			self.hex_scheme['split_compliments'] = [ shot.hex for shot in self.split_compliments ]
			self.hex_scheme['triads'] = [ shot.hex for shot in self.triads ]
			self.hex_scheme['tetrads'] = [ shot.hex for shot in self.tetrads ]
			self.hex_scheme['analogous'] = [ shot.hex for shot in self.analogous ]
			self.hex_scheme['monochromatic'] = [ shot.hex for shot in self.monochromatic ]
		elif name is "rgb_scheme":
			self.rgb_scheme['complimentary'] = [ tuple( np.round(shot.rgb ) ) for shot in self.complimentary ]
			self.rgb_scheme['split_compliments'] = [ tuple( np.round(shot.rgb ) ) for shot in self.split_compliments ]
			self.rgb_scheme['triads'] = [ tuple( np.round(shot.rgb ) ) for shot in self.triads ]
			self.rgb_scheme['tetrads'] = [ tuple( np.round(shot.rgb ) ) for shot in self.tetrads ]
			self.rgb_scheme['analogous'] = [ tuple( np.round(shot.rgb ) ) for shot in self.analogous ]
			self.rgb_scheme['monochromatic'] = [ tuple( np.round(shot.rgb ) ) for shot in self.monochromatic ]
		elif name is "hsv_scheme":
			self.hsv_scheme['complimentary'] = [ tuple( np.round( shot.hsv ) ) for shot in self.complimentary ]
			self.hsv_scheme['split_compliments'] = [ tuple( np.round( shot.hsv ) ) for shot in self.split_compliments ]
			self.hsv_scheme['triads'] = [ tuple( np.round( shot.hsv ) ) for shot in self.triads ]
			self.hsv_scheme['tetrads'] = [ tuple( np.round( shot.hsv ) ) for shot in self.tetrads ]
			self.hsv_scheme['analogous'] = [ tuple( np.round( shot.hsv ) ) for shot in self.analogous ]
			self.hsv_scheme['monochromatic'] = [ tuple( np.round( shot.hsv ) ) for shot in self.monochromatic ]
		else: pass
		self.generating = False

if __name__ == "__main__":
	mw=Bottle( )
	mw.hex = "#0066cc"
	print("---------------")
	print( mw.hex_scheme )
	print("---------------")
	mw.rgb = ( 100, 200, 100 )
	print("---------------")
	print( mw.hsv_scheme )
	print("---------------")
	mw.hsv = ( 360, 100, 40 )
	print("---------------")
	print( mw.rgb_scheme )
