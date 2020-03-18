function Transistor(rb,rc,re,vbb,vcc,b) 
	local ib = (vbb-0.7)/rb
	print(ib)
	local ic = b*ib
	print(ic)
	local ie = (b+1)*ib
	print(ie)
	local vce = vcc - ic*rc-ie*re 
	return 'Q is ('.. vce ..','.. ic ..')'..'\n(v_max '..vcc..', i_max '.. vcc/(re+rc)..')'
end
print(Transistor(1e3,2e3,200,1,10,100))