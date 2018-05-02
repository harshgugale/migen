from migen import *
from migen.fhdl import verilog

class mux(Module):
		
	def __init__ (self,selb):
		self.out = out = Signal()
		self.sel = sel = Signal(selb)
		self.inp = inp = Signal(2**selb)
		
		for j in range(2**selb):
			self.comb += If(sel == j,out.eq(inp[j]))	
	
def testbench(dut,selb):
 	yield dut.inp.eq(0b00000001)
 	for i in range(2**selb):
 		yield dut.sel.eq(i)
 		print("Sel {} out {}".format(i,(yield dut.out)))
 		yield
		
dut = mux(3)
run_simulation(dut,testbench(dut,3))
#print(verilog.convert(dut,{dut.inp,dut.out,dut.sel}))
