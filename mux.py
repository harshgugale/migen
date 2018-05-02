from migen import *

class mux(Module):
		
	def __init__ (self,selb):
		self.out = out = Signal()
		self.sel = sel = Signal(selb)
		self.inp = inp = Signal(2**selb)
		
		for j in range(2**selb):
			self.comb += If(sel == j,out.eq(inp[selb]))
			
	
def testbench(dut):
	yield dut.inp.eq(5)
	for i in range(8):
		yield dut.sel.eq(i)
		print("Sel {} out {}".format(i,(yield dut.out)))

dut = mux(3)
run_simulation(dut,testbench(dut))
