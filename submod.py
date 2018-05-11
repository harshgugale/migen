from migen import *
	
class adder(Module):
	def __init__ (self,n):
		self.a = a = Signal(n)
		self.b = b = Signal(n)
		self.c = c = Signal(n+1)

		self.comb += c.eq(a+b)

class top(Module):
	def __init__ (self,n):
		self.inp1 = inp1 = Signal(n)
		self.inp2 = inp2 = Signal(n)
		self.val = val = Signal(n+1)

		add_mod1 = adder(n)
		add_mod2 = adder(n+1)
		
		self.submodules+=add_mod1
		self.submodules+=add_mod2

		self.res = add_mod2.c
		self.comb+=[add_mod1.a.eq(inp1),add_mod1.b.eq(inp2),add_mod2.a.eq(add_mod1.c),add_mod2.b.eq(val)]

def testbench(dut):
	yield dut.inp1.eq(4)
	yield dut.inp2.eq(5)
	yield dut.val.eq(4)
	yield
	print("{}".format((yield dut.res)))



dut = top(8)
run_simulation(dut,testbench(dut),vcd_name = "add_three_no")
