vlib work                                            
vmap work work

#vlog *.v
vlog block1.v
vlog block2.v
vlog noblock1.v
vlog noblock2.v
vlog testbench.v

vsim work.testbench

#add wave *
add wave -radix  unsigned sim:/testbench/*

run 500 ns