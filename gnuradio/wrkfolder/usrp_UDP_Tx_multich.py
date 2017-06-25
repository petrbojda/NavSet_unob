#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Usrp Udp Tx Multich
# Generated: Sun Jun 25 03:32:33 2017
##################################################

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import time


class usrp_UDP_Tx_multich(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Usrp Udp Tx Multich")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate_0 = samp_rate_0 = 2e6
        self.samp_rate = samp_rate = 32000
        self.gain = gain = 30
        self.freq = freq = 470e6

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(4),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(freq, 0)
        self.uhd_usrp_source_0.set_gain(gain, 0)
        self.uhd_usrp_source_0.set_antenna('TX/RX', 0)
        self.uhd_usrp_source_0.set_center_freq(0, 1)
        self.uhd_usrp_source_0.set_gain(0, 1)
        self.uhd_usrp_source_0.set_center_freq(0, 2)
        self.uhd_usrp_source_0.set_gain(0, 2)
        self.uhd_usrp_source_0.set_center_freq(0, 3)
        self.uhd_usrp_source_0.set_gain(0, 3)
        self.blocks_udp_sink_0_2 = blocks.udp_sink(gr.sizeof_gr_complex*1, '127.0.0.1', 12348, 1472, True)
        self.blocks_udp_sink_0_1 = blocks.udp_sink(gr.sizeof_gr_complex*1, '127.0.0.1', 12347, 1472, True)
        self.blocks_udp_sink_0_0 = blocks.udp_sink(gr.sizeof_gr_complex*1, '127.0.0.1', 12346, 1472, True)
        self.blocks_udp_sink_0 = blocks.udp_sink(gr.sizeof_gr_complex*1, '127.0.0.1', 12345, 1472, True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_udp_sink_0, 0))    
        self.connect((self.uhd_usrp_source_0, 1), (self.blocks_udp_sink_0_0, 0))    
        self.connect((self.uhd_usrp_source_0, 2), (self.blocks_udp_sink_0_1, 0))    
        self.connect((self.uhd_usrp_source_0, 3), (self.blocks_udp_sink_0_2, 0))    

    def get_samp_rate_0(self):
        return self.samp_rate_0

    def set_samp_rate_0(self, samp_rate_0):
        self.samp_rate_0 = samp_rate_0

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.uhd_usrp_source_0.set_gain(self.gain, 0)
        	

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.uhd_usrp_source_0.set_center_freq(self.freq, 0)


def main(top_block_cls=usrp_UDP_Tx_multich, options=None):

    tb = top_block_cls()
    tb.start()
    try:
        raw_input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
